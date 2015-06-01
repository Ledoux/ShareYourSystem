
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
coffeelint = require('gulp-coffeelint')
uglify = require('gulp-uglify')
minifyCSS = require('gulp-minify-css')
_ = require('lodash')

# HACK: for some reason plugins like ngAnnotate & uglify require streamify
streamify = require('gulp-streamify')

cacheify = require('cacheify')
coffeeify = require('coffeeify')
level = require('level')
db = level('./.gulp-cache')
notify = require('gulp-notify')

handleErrors = () ->
    notify.onError({
        title: 'Compile error'
        message: '<%= error.message %>'
    }).apply(this, Array.prototype.slice.call(arguments))

    this.emit('end')

#SOURCES

libDashboardSources = {
    coffeeWatch: ['app/columbus/columbus/**/*.coffee']
    js: ['app/columbus/dist/*.js']
    templates: ['app/columbus/columbus/**/*.html']
    assets: ['app/columbus/columbus/styles/**/*.{eot,svg,ttf,woff}']
    stylesLoadPaths: ['app/columbus']
    stylesWatch: ['app/columbus/columbus/styles/**/*']
}

sources = {
    coffee: ['app/scripts/main.coffee']
    coffeeWatch: ['app/scripts/**/*.coffee'].concat(libDashboardSources.coffeeWatch)
    templates: ['app/scripts/**/*.html']
    styles: ['app/styles/main.scss']
    stylesLoadPaths: ['app/styles'].concat(libDashboardSources.stylesLoadPaths)
    stylesWatch: ['app/styles/**/*'].concat(libDashboardSources.stylesWatch)
    assets: {
        html: ['app/*.html']
        icon: ['app/*.ico']
        images: ['app/images/**/*.{ico,svg,png,jpg}']
    }
    assetsWatch: ['app/*.html', 'app/images/**/*.{ico,svg,png}']
}
# sources.assetsWatch = _.reduce(_.values(sources.assets), (item, acc) -> acc.concat(item))

explorationServerLibs = [
    'app/vendor/coffee-script.js',
    'app/vendor/sass.min.js'
]

vendorLibs = [


    {name: 'modernizr', js: 'bower_components/modernizr/modernizr.js'},
    {name: 'jquery', js: 'bower_components/jquery/jquery.js'},
    {
        name: 'angular'
        js: [
            'bower_components/angular/angular.js',
            'bower_components/angular-route/angular-route.js'
        ]
    },
    {
        name: 'explorationServer'
        js: 'bower_components/ngstorage/ngStorage.js'
    },
    {
        name: 'dat.gui'
        js: 'app/vendor/dat.gui.js'
    },
    {name: 'animate.css', css: 'bower_components/animate.css/animate.css'},
    {
        name: 'ng-json-explorer'
        css: 'app/vendor/ng-json-explorer/gd-ui-jsonexplorer.css'
        js: 'app/vendor/ng-json-explorer/gd-ui-jsonexplorer.js'
    },
    {
        name: 'Columbus dependencies',
        js: 'app/columbus/dist/columbusDependencies.js'
        css: 'app/columbus/dist/columbusDependencies.css'
    },
    {name: 'sweetalert', css: 'bower_components/sweetalert/lib/sweet-alert.css',
    js: 'bower_components/sweetalert/lib/sweet-alert.js'},

    {
        name: 'CalHeatMap'
        js: 'app/vendor/cal-heatmap/cal-heatmap.js'
        css: 'app/vendor/cal-heatmap/cal-heatmap.css'

    }
]

#ENVIRONMENT

isProd = gutil.env.type == 'prod'

#TASKS

gulp.task 'lint', () ->
    gulp.src(['app/scripts/**/*.coffee'])
        .pipe(coffeelint())
        .pipe(coffeelint.reporter())


publish = (folder) ->
    awspublish = require('gulp-awspublish')
    parallelize = require('concurrent-transform')
    fs = require('fs')

    fs.readFile(process.env.HOME + '/.s3cfg', 'utf-8', (err, data) ->
        if err
            console.log err
            return

        keys = {}
        for line in data.split('\n')
            splitIdx = line.indexOf('=')
            if splitIdx >= 0
                fieldName = line[0..splitIdx - 1].trim().toLowerCase()
                value = line[splitIdx + 1..].trim()
                if fieldName.length > 0
                    keys[fieldName] = value

        auth = {
            accessKeyId: keys['access_key']
            secretAccessKey: keys['secret_key']
            params: {
                Bucket: 'private-snips-net'
            }
        }


        publisher = awspublish.create(auth)
        force = gutil.env.force == 'true'

        bucketPath = (path) ->
            path.dirname = "Traces/#{folder}/" + path.dirname
            return path

        gulp.src(['dist/**/*'])
            .pipe(rename(bucketPath))
            .pipe(awspublish.gzip())
            .pipe(parallelize(publisher.publish({
                'Content-Encoding': 'gzip'
                'x-amz-acl': 'private' # Make it private because we only want to access it through private.snips.net
                }, {force: force}), 10))
            .pipe(awspublish.reporter())
    )

gulp.task 'publish-develop', () ->
    if not isProd
        throw new Error('ERROR: you can only use publish in production mode, use `gulp --type prod publish`')
    publish('researchVisualization-develop')


gulp.task 'publish-master', () ->
    if not isProd
        throw new Error('ERROR: you can only use publish in production mode, use `gulp --type prod publish`')
    publish('researchVisualization-master')


gulp.task 'dashboard-templates', () ->
    gulp.src(libDashboardSources.templates)
        .pipe(gulp.dest('dist/columbus/scripts'))


gulp.task 'dashboard-styles-assets', () ->
    gulp.src(libDashboardSources.assets)
        .pipe(gulp.dest('dist/styles'))


gulp.task 'vendor', () ->
    [js, css, assets] = for type in ['js', 'css', 'assets']
        files = _.filter(_.pluck(vendorLibs, type))
        files = _.map(files, (t) -> if _.isArray(t) then t else [t])
        _.reduce(files, (t, acc) -> t.concat(acc))

    gulp.src(js)
        .pipe(if isProd then ngAnnotate() else gutil.noop())
        .pipe(if isProd then uglify() else gutil.noop())
        .pipe(concat('vendor.js'))
        .pipe(gulp.dest('dist/scripts'))

    gulp.src(css)
        .pipe(prefix("last 2 versions", "> 1%"))
        .pipe(if isProd then minifyCSS() else gutil.noop())
        .pipe(concat('vendor.css'))
        .pipe(gulp.dest('dist/styles'))


gulp.task 'explorationServerVendor', () ->
    # Specific to the exploration server, to remove after we create a standalone exploration
    # NOTE: it is also used in the lightweight exploration page
    gulp.src(explorationServerLibs)
        .pipe(concat('explorationServerVendor.js'))
        .pipe(gulp.dest('dist/scripts'))


gulp.task 'scripts', () ->
    transform = if isProd then coffeeify else cacheify(coffeeify, db)

    bundler = browserify({
            entries: ['./scripts/main.coffee']
            debug: not isProd,
            basedir: './app', # if we do not use this, it tries to include modules in `node_modules` which can create conflicts
            paths: ['./columbus/'],
            extensions: ['.js', '.coffee'],
            ignoreMissing: true
        })
        .transform(transform)

    return bundler
        .bundle()
        .on('error', handleErrors)
        .on('error', gutil.log)
        .on('error', gutil.beep)
        .pipe(source('main.js'))
        .pipe(if isProd then streamify(ngAnnotate()) else gutil.noop())
        .pipe(if isProd then streamify(uglify()) else gutil.noop())
        .pipe(gulp.dest('dist/scripts'))
        .pipe(notify('Finished compiling scripts'))

gulp.task 'styles', () ->
    return sass(sources.styles, {loadPath: sources.stylesLoadPaths})
        .on('error', handleErrors)
        .on('error', gutil.log)
        .pipe(prefix("last 2 versions", "> 1%"))
        .on('error', handleErrors)
        .on('error', gutil.log)
        .on('error', gutil.beep)
        .pipe(if isProd then minifyCSS() else gutil.noop())
        .pipe(gulp.dest('dist/styles'))
        .pipe(notify('Finished compiling styles'))


gulp.task 'app-assets', () ->
    assets = sources.assets
    es.concat(
        gulp.src(assets.html).pipe(gulp.dest('dist/')),
        gulp.src(assets.icon).pipe(gulp.dest('dist/')),
        gulp.src(assets.images).pipe(gulp.dest('dist/images')),
    )


gulp.task 'app-templates', () ->
    gulp.src(sources.templates)
        .pipe(gulp.dest('dist/scripts'))


gulp.task 'watch', () ->
    gulp.watch sources.coffeeWatch, ['scripts']
    gulp.watch libDashboardSources.js, ['vendor']
    gulp.watch libDashboardSources.templates, ['dashboard-templates']
    gulp.watch libDashboardSources.assets, ['dashboard-styles-assets']
    gulp.watch sources.templates, ['app-templates']
    gulp.watch sources.stylesWatch, ['styles']
    gulp.watch sources.assetsWatch, ['app-assets']
