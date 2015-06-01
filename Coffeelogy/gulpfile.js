
/*

  Import modules
 */
var browserify, cjsx, cjsxSources, coffee, coffeeSources, coffeeify, concat, connect, gulp, gutil, handleErrors, htmlSources, inputDir, jsSources, notify, outputEmptyFile, outputFinalDir, outputMainFile, outputMainRequireFile, outputRequirePath, outputTransformDir, outputVendorFile, sass, sassSources, source, uglify;

gulp = require('gulp');

gutil = require('gulp-util');

sass = require('gulp-sass');

browserify = require('browserify');

source = require('vinyl-source-stream');

cjsx = require('gulp-cjsx');

coffee = require('gulp-coffee');

coffeeify = require('coffeeify');

connect = require('gulp-connect');

uglify = require('gulp-uglify');

concat = require('gulp-concat');

notify = require('gulp-notify');


/*

  Handle error
 */

handleErrors = function() {
  notify.onError({
    title: 'Compile error',
    message: '<%= error.message %>'
  }).apply(this, Array.prototype.slice.call(arguments));
  return this.emit('end');
};


/*

  Say where to watch and to write
 */

inputDir = 'scripts';

outputTransformDir = 'transforms';

outputFinalDir = 'assets';

outputMainRequireFile = 'main_require.js';

outputMainFile = 'main.js';

outputEmptyFile = 'empty.js';

outputVendorFile = 'vendor.js';

outputRequirePath = outputFinalDir + '/' + outputMainRequireFile;

cjsxSources = [inputDir + '/*.cjsx'];

coffeeSources = [inputDir + '/*.coffee'];

jsSources = [outputTransformDir + '/*.js'];

sassSources = ['styles/*.scss'];

htmlSources = ['**/*.html'];


/*

  Define specific tasks
 */

gulp.task('log', function() {
  return gutil.log('== My First Task ==');
});

gulp.task('copy', function() {
  return gulp.src('index.html').pipe(gulp.dest(outputFinalDir));
});

gulp.task('sass', function() {
  return gulp.src(sassSources).pipe(sass({
    style: 'expanded'
  })).on('error', gutil.log).pipe(gulp.dest(outputFinalDir)).pipe(connect.reload());
});

gulp.task('cjsx', function() {
  return gulp.src(cjsxSources).pipe(cjsx({
    bare: true
  }).on('error', gutil.log)).pipe(gulp.dest(outputTransformDir));
});

gulp.task('coffeeGulp', function() {
  return gulp.src(['gulpfile.coffee']).pipe(coffee({
    bare: true
  }).on('error', gutil.log)).pipe(gulp.dest(""));
});

gulp.task('coffee', function() {
  return gulp.src(coffeeSources).pipe(coffee({
    bare: true
  }).on('error', gutil.log)).pipe(gulp.dest(outputTransformDir));
});

gulp.task('js', function() {
  return gulp.src(jsSources).pipe(uglify()).pipe(concat(outputMainRequireFile)).pipe(gulp.dest(outputFinalDir));
});

gulp.task('watch', function() {
  gulp.watch(cjsxSources, ['cjsx']);
  gulp.watch(["gulpfile.coffee"], ['coffeeGulp']);
  gulp.watch(jsSources, ['js']);
  gulp.watch([outputRequirePath], ['browserify']);
  gulp.watch(sassSources, ['sass']);
  return gulp.watch(htmlSources, ['html']);
});

gulp.task('vendor', function() {
  return browserify(outputEmptyFile).require('./node_modules/react/react.js').bundle().pipe(source(outputVendorFile)).pipe(gulp.dest(outputFinalDir)).pipe(connect.reload());
});

gulp.task('browserify', function() {
  return browserify(outputRequirePath).bundle().pipe(source(outputMainFile)).pipe(gulp.dest(outputFinalDir)).pipe(connect.reload());
});

gulp.task('connect', function() {
  return connect.server({
    root: '.',
    livereload: true
  });
});

gulp.task('html', function() {
  return gulp.src(htmlSources).pipe(connect.reload());
});


/*

  Define global tasks
 */

gulp.task('default', ['html', 'cjsx', 'js', 'vendor', 'browserify', 'sass', 'connect', 'watch']);
