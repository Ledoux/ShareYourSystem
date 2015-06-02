###

  Import modules

###

gulp = require 'gulp'
gutil = require 'gulp-util'
sass = require 'gulp-sass'
watchify = require 'watchify'
lodash = require 'lodash'
browserify = require 'browserify'
source = require 'vinyl-source-stream'
cjsx = require 'gulp-cjsx'
coffee = require 'gulp-coffee'
coffeeify = require 'coffeeify'
cjsxfy = require 'coffee-reactify'
connect = require 'gulp-connect'
uglify = require 'gulp-uglify'
concat = require 'gulp-concat'
importCss = require 'gulp-import-css'

###

  Say where to watch and to write

###

#sources
cssSources = ['styles/*.css']
sassSources = ['styles/*.scss']
htmlSources = ['**/*.html']
scriptsSources = [
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
		gulp.src 'index.html'
		.pipe gulp.dest assetsDir

gulp.task 'sass',
	->
		gulp.src sassSources
		.pipe sass(style: 'expanded')
		.on 'error', gutil.log
		.pipe gulp.dest 'assets'
		.pipe connect.reload()

gulp.task 'css', 
	->
		gulp.src cssSources
    	.pipe importCss()
    	.pipe gulp.dest 'assets'
    	.pipe connect.reload()

gulp.task 'html',
	->
		gulp.src htmlSources
		.pipe connect.reload() 

gulp.task 'coffeeGulp',
	->
		gulp.src ['gulpfile.coffee']
		.pipe coffee({bare: true}).on('error', gutil.log)
	    .pipe gulp.dest ""

#vendor treatment

gulp.task 'vendor_min',
	->
		gulp.src outputVendorPath
		.pipe uglify() 
		.pipe concat 'vendor.min.js'
		.pipe gulp.dest 'assets'
			
gulp.task 'vendor_bundle', 
	->
		browserify [
						'./node_modules/react/react.js',
						'./node_modules/lodash/lodash.js'
					]
		.bundle()
        .pipe source 'vendor.js'
	    .pipe gulp.dest 'assets'

#main treatment

gulp.task 'main_bundle', 
	->
		#MainBrowserify = browserify MainObject
		
		MainBrowserify = browserify lodash.assign({}, watchify.args, MainObject)
		MainWatchify = watchify MainBrowserify

		.transform(cjsxfy)
		#.transform(coffeeify)
		#.exclude('react')
		.bundle()
        .pipe source 'buffer.js'
	    .pipe gulp.dest 'assets'
	    .pipe connect.reload()
	    

gulp.task 'main_min',
	->
		gulp.src ['assets/buffer.js']
		.pipe uglify() 
		.pipe concat 'main.min.js'
		.pipe gulp.dest 'assets'
		.pipe connect.reload()

#all treatment

###

  Define watch connect

###

gulp.task 'watch',
	->
		gulp.watch cssSources, ['css']
		#gulp.watch ["gulpfile.coffee"], ['coffeeGulp','cjsx']
		gulp.watch scriptsSources, ['main_bundle']
		#gulp.watch coffeeSources, ['coffee']
		#gulp.watch [outputVendorPath], ['vendor_min']
		#gulp.watch ['./assets/buffer.js'], ['main_min']
		#gulp.watch sassSources, ['sass'] 
		gulp.watch htmlSources, ['html'] 


gulp.task 'connect', 	
	->
		connect.server root: '.',livereload: true

###

  Define global tasks

###

gulp.task 'default',
	[
		#'vendor_bundle',
		#'vendor_min',
		'html', 
		'main_bundle',
		#'main_min',
		#'sass', 
		'css',
		'connect', 
		'watch'
	]