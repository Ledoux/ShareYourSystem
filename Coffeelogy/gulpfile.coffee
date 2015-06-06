###

  Import modules

###

path = require('path')
gulp = require('gulp')
gutil = require('gulp-util')
sass = require('gulp-sass')
watchify = require('watchify')
lodash = require('lodash')
browserify = require('browserify')
source = require('vinyl-source-stream')
transform = require('vinyl-transform')
cjsx = require('gulp-cjsx')
coffee = require('gulp-coffee')
coffeeify = require('coffeeify')
cjsxfy = require('coffee-reactify')
connect = require('gulp-connect')
uglify = require('gulp-uglify')
concat = require('gulp-concat')
importCss = require('gulp-import-css')
minifyCSS = require('gulp-minify-css')
ngAnnotate = require('gulp-ng-annotate')
prefix = require('gulp-autoprefixer')
concat = require('gulp-concat')
_ = require('lodash')
# HACK: for some reason plugins like ngAnnotate & uglify require streamify
#streamify = require('gulp-streamify')
rename = require('gulp-rename')

###

  define the environment

###

isProd = gutil.env.type == 'prod'

###

  define the vendor

###

#set

dev_vendorLibs = [
	{name: 'lodash', js: 'node_modules/lodash/lodash.js'}
]

#dev_vendorLibs = [
#	{ require: 'node_modules/lodash/lodash.js', expose: 'lodash'}
#]


###

  Say where to watch and to write

###


#sources
cssSources = ['styles/*.css']
sassSources = ['styles/*.scss']
htmlSources = ['**/*.html']
scriptSources = [
					'scripts/**/*.cjsx',
					'scripts/**/*.coffee',
					'scripts/**/*.js'
				]

MainObject = {
				entries : ['./scripts/main.js'],
				extensions: ['.js', '.coffee', '.cjsx']
			}

###

  Define change tasks

###

gulp.task 'log',
	-> 
		gutil.log '== My First Task =='


gulp.task 'copy',
	-> 
		gulp.src('index.html')
		.pipe(gulp.dest,assetsDir)

gulp.task 'sass',
	->
		gulp.src sassSources
		.pipe(sass(style: 'expanded'))
		.on('error', gutil.log)
		.pipe(gulp.dest 'assets')
		.pipe(connect.reload())

gulp.task 'css', 
	->
		gulp.src cssSources
    	.pipe(importCss())
    	.pipe(gulp.dest('assets'))
    	.pipe(connect.reload())


cjsxDir = null
findPath = (file, t) ->
	cjsxDir = file.path
	console.log(cssDir);

gulp.task 'cjsx', 
	->
		gulp.src(scriptSources)
    	.pipe( tap( findPath ) )
    	.pipe(cjsx({bare: true}).on('error', gutil.log))
    	.pipe(gulp.dest(cjsxDir));

gulp.task 'html',
	->
		gulp.src(htmlSources)
		.pipe(connect.reload())

gulp.task 'coffeeGulp',
	->
		gulp.src(['gulpfile.coffee'])
		.pipe coffee({bare: true}).on('error', gutil.log)
	    .pipe gulp.dest ""



#vendor treatment

###
gulp.task 'dev_vendor_bundle',
	->
		browserify(
  				["./assets/empty.js"],
  				{
  					#debug: false,
  					#extensions: ['.js', '.coffee', '.cjsx']
  				}
  		)
  		.on('prebundle', (bundle) -> 
  			vendorLibs.forEach(external) ->
  				if external.expose?
  					bundle.require(external.require, expose: external.expose)
  				else
  					bundle.require(external.require)
  		)
  		.bundle()
  		.pipe(source('dev_vendor.js'))
  		.pipe(gulp.dest("assets"))
###

#define the require way to build vendor lib
brequire = (pathname) ->

	#Debug
	console.log('pathname is '+pathname)

	#set
	#filename = pathname.split('/').slice(-2,-1)[0]
	filename = pathname.split('/').slice(-1)[0]

	#Debug
	console.log('filename is '+filename)

	#return
	return browserify(pathname)
			.require(filename, { expose: pathname})
			.bundle();

gulp.task 'dev_vendor_bundle',
	->

		#collect
		[js, css, assets] = for type in ['js', 'css', 'assets']
			files = _.filter(_.pluck(dev_vendorLibs, type))
			files = _.map(files, (t) -> if _.isArray(t) then t else [t])
			_.reduce(files, (t, acc) -> t.concat(acc))

		#Check
		if js!=undefined and js.length>0

			#set
			browserified = transform(brequire)

			#return
			return gulp.src(js)
				.pipe(if isProd then ngAnnotate() else gutil.noop())
				.pipe(if isProd then uglify() else gutil.noop())
			    .pipe(browserified)
			    .pipe(concat('dev_vendor.js'))
			    .pipe(gulp.dest('assets'));

		#Check
		if css!=undefined and css.length>0
			gulp.src(css)
			.pipe(prefix("last 2 versions", "> 1%"))
			.pipe(if isProd then minifyCSS() else gutil.noop())
			.pipe(concat('dev_vendor.css'))
			.pipe(gulp.dest('assets'))


gulp.task 'iframe_vendor_bundle', 
	->
		browserify [
						'./node_modules/react/react.js',
						'./node_modules/lodash/lodash.js'
					]
		.bundle()
        .pipe(source('iframe_vendor.js'))
	    .pipe(gulp.dest('assets'))

#main treatment

gulp.task 'main_bundle', 
	->

		#convert locally to js



		#MainBrowserify = browserify MainObject
		MainBrowserify = browserify lodash.assign({}, watchify.args, MainObject)
		MainWatchify = watchify MainBrowserify
		.transform(cjsxfy)
		#.transform(coffeeify)
		#.exclude('react')
		.bundle()
        .pipe(source('buffer.js'))
	    .pipe(gulp.dest('assets'))
	    .pipe(connect.reload())
	    

gulp.task 'main_min',
	->
		gulp.src(['assets/buffer.js'])
		.pipe(uglify()) 
		.pipe(concat('main.min.js'))
		.pipe(gulp.dest('assets'))
		.pipe(connect.reload())

#all treatment

###

  Define watch connect

###

gulp.task 'watch',
	->
		gulp.watch(cssSources, ['css'])
		#gulp.watch ["gulpfile.coffee"], ['coffeeGulp']
		gulp.watch(scriptSources, [
									'main_bundle',
									#'cjsx'
								])
		#gulp.watch coffeeSources, ['coffee']
		#gulp.watch [outputVendorPath], ['vendor_min']
		#gulp.watch ['./assets/buffer.js'], ['main_min']
		#gulp.watch sassSources, ['sass'] 
		gulp.watch(htmlSources, ['html'])


gulp.task 'connect', 	
	->
		connect.server root: '.',livereload: true

###

  Define global tasks

###

gulp.task 'default',
	[
		'dev_vendor_bundle',
		#'iframe_vendor_bundle',
		'html', 
		#'cjsx',
		'main_bundle',
		#'main_min',
		#'sass', 
		'css',
		'connect', 
		'watch'
	]