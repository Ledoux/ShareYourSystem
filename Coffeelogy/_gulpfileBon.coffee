###

  Import modules

###

gulp = require 'gulp'
gutil = require 'gulp-util'
sass = require 'gulp-sass'
browserify = require 'browserify'
source = require 'vinyl-source-stream'
#reactify = require 'reactify'
#transform = require 'vinyl-transform'
cjsx = require 'gulp-cjsx'
coffee = require 'gulp-coffee'
coffeeify = require 'coffeeify'
connect = require 'gulp-connect'
uglify = require 'gulp-uglify'
concat = require 'gulp-concat'
notify = require('gulp-notify')

###

  Handle error 

###

handleErrors = () ->
    notify.onError({
        title: 'Compile error'
        message: '<%= error.message %>'
    }).apply(this, Array.prototype.slice.call(arguments))
    this.emit('end')


###

  Say where to watch and to write

###

inputDir = 'scripts'
outputTransformDir = 'transforms'
outputFinalDir = 'assets'
outputRequireFile = 'main_require.js'
outputFinalFile = 'main.js'
outputRequirePath = outputFinalDir+'/'+outputRequireFile

cjsxSources = [inputDir+'/*.cjsx']
coffeeSources = [inputDir+'/*.coffee']
jsSources = [outputTransformDir+'/*.js']
sassSources = ['styles/*.scss']
htmlSources = ['**/*.html']

###

  Define specific tasks

###

gulp.task 'log',
	-> 
		gutil.log '== My First Task =='


gulp.task 'copy',
	-> 
		gulp.src 'index.html'
		.pipe gulp.dest outputFinalDir

gulp.task 'sass',
	->
		gulp.src sassSources
		.pipe sass(style: 'expanded')
		.on 'error', gutil.log
		.pipe gulp.dest outputFinalDir
		.pipe connect.reload()

gulp.task 'cjsx',
	->
		gulp.src cjsxSources
    	.pipe cjsx({bare: true}).on('error', gutil.log)
    	.pipe gulp.dest outputTransformDir

gulp.task 'coffeeGulp',
	->
		gulp.src ['gulpfile.coffee']
		.pipe coffee({bare: true}).on('error', gutil.log)
	    .pipe gulp.dest ""

gulp.task 'coffee',
	->
		gulp.src coffeeSources
		.pipe coffee({bare: true}).on('error', gutil.log)
	    .pipe gulp.dest outputTransformDir

gulp.task 'js',
	->
		gulp.src jsSources
		.pipe uglify() 
		.pipe concat outputRequireFile
		.pipe gulp.dest outputFinalDir
		#.pipe connect.reload()
			
gulp.task 'watch',
	->
		gulp.watch cjsxSources, ['cjsx']
		#gulp.watch coffeeSources, ['coffee']
		gulp.watch ["gulpfile.coffee"], ['coffeeGulp']
		gulp.watch jsSources, ['js']
		gulp.watch [outputRequirePath], ['browserify']
		gulp.watch sassSources, ['sass'] 
		gulp.watch htmlSources, ['html'] 

gulp.task 'browserify', 
	->
		browserify outputRequirePath
		.bundle()
        .pipe source outputFinalFile
	    .pipe gulp.dest outputFinalDir
	    .pipe connect.reload()	

gulp.task 'connect', 	
	->
		connect.server root: '.',livereload: true

gulp.task 'html',
	->
		gulp.src htmlSources
		.pipe connect.reload() 

###

  Define global tasks

###

gulp.task 'default',
	[
		'html', 
		'cjsx',
		#'coffee', 
		'js', 
		'browserify', 
		'sass', 
		'connect', 
		'watch'
	]