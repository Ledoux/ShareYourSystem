
gulp = require('gulp')
gutil = require('gulp-util')

browserify = require('browserify')
source = require('vinyl-source-stream')
sass = require('gulp-ruby-sass')
ngAnnotate = require('gulp-ng-annotate')
rename = require('gulp-rename')
concat = require('gulp-concat')
es = require('event-stream')
prefix = require('gulp-autoprefixer')
uglify = require('gulp-uglify')
minifyCSS = require('gulp-minify-css')
_ = require('lodash')

# HACK: for some reason plugins like ngAnnotate & uglify require streamify
streamify = require('gulp-streamify')

cacheify = require('cacheify')
coffeeify = require('coffeeify')
level = require('level')
db = level('./.gulp-cache')
notify = require("gulp-notify")

module.exports = exports = {}

#########################################################################
# ENVIRONMENT
#########################################################################

exports.isProd = isProd = gutil.env.type == 'prod'

#########################################################################
# CONFIG
#########################################################################

DEST_DIR = '../docker/build'

exports.destDirs = {
    'static': DEST_DIR + '/static',
    'templates': DEST_DIR + '/templates',
    'exploration': DEST_DIR + '/static/exploration'
}

exports.libDashboardSources = {
    coffeeWatch: ['app/exploration/columbus/columbus/**/*.coffee']
    js: ['app/exploration/columbus/dist/*.js']
    templates: ['app/exploration/columbus/columbus/**/*.html']
    assets: ['app/exploration/columbus/columbus/styles/**/*.{eot,svg,ttf,woff}']
    stylesLoadPaths: ['app/exploration/columbus']
    stylesWatch: ['app/exploration/columbus/columbus/styles/**/*']
}


#########################################################################
# UTILS
#########################################################################

exports.handleErrors = handleErrors = () ->
    notify.onError({
        title: 'Compile error'
        message: '<%= error.message %>'
    }).apply(this, Array.prototype.slice.call(arguments))
    this.emit('end')

#########################################################################
# TASKS
#########################################################################

exports.compileVendor = (vendorLibs, destDir, libName='vendor') ->
    [js, css, assets] = for type in ['js', 'css', 'assets']
        files = _.filter(_.pluck(vendorLibs, type))
        files = _.map(files, (t) -> if _.isArray(t) then t else [t])
        _.reduce(files, (t, acc) -> t.concat(acc))

    gulp.src(js)
        .pipe(if isProd then ngAnnotate() else gutil.noop())
        .pipe(if isProd then uglify() else gutil.noop())
        .pipe(concat(libName + '.js'))
        .pipe(gulp.dest(destDir + '/scripts'))

    gulp.src(css)
        .pipe(prefix("last 2 versions", "> 1%"))
        .pipe(if isProd then minifyCSS() else gutil.noop())
        .pipe(concat(libName + '.css'))
        .pipe(gulp.dest(destDir + '/styles'))

    # TODO: should also copy assets

exports.copyFiles = (files, destDir) ->
    gulp.src(files).pipe(gulp.dest(destDir))

exports.compileBrowserify = (entries, destDir, libName='main', browserifyOptions=null) ->
    browserifyOptions = _.defaults(browserifyOptions or {}, {
        entries: entries
        debug: not isProd
        extensions: ['.js', '.coffee']
        ignoreMissing: true
    })

    bundler = browserify(browserifyOptions)
        .transform(if isProd then coffeeify else cacheify(coffeeify, db))

    return bundler
        .bundle()
        .on('error', exports.handleErrors)
        .on('error', gutil.log)
        .on('error', gutil.beep)
        .pipe(source(libName + '.js'))
        .pipe(if isProd then streamify(ngAnnotate()) else gutil.noop())
        .pipe(if isProd then streamify(uglify()) else gutil.noop())
        .pipe(gulp.dest(destDir))
        .pipe(notify("Compiled scripts for #{destDir + '/' + libName}"))

exports.compileSass = (src, destDir, sassOptions=null) ->
    sassOptions = sassOptions or {}

    return sass(src, sassOptions)
        .pipe(notify(src))
        .pipe(notify(sassOptions))
        .on('error', handleErrors)
        .on('error', gutil.log)
        .pipe(prefix("last 2 versions", "> 1%"))
        .on('error', handleErrors)
        .on('error', gutil.log)
        .on('error', gutil.beep)
        .pipe(if isProd then minifyCSS() else gutil.noop())
        .pipe(gulp.dest(destDir))
        .pipe(notify("Compiled styles for #{destDir}"))
