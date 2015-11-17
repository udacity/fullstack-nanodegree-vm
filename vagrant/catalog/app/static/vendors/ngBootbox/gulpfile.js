var gulp = require('gulp');
var uglify = require('gulp-uglify');
var ngAnnotate = require('gulp-ng-annotate');
var rename = require('gulp-rename');
var connect = require('gulp-connect');
var livereload = require('gulp-livereload');
var open = require('gulp-open');
var jshint = require('gulp-jshint');

var paths = {
  scripts: [
    './ngBootbox.js',
    './examples/**/*.js',
    '!./examples/**/require.js'
  ]
};
var port = 8181;

gulp.task('default', ['dist']);

gulp.task('dist', function() {
  gulp.src('ngBootbox.js')
    .pipe(ngAnnotate())
    .pipe(gulp.dest('dist'))
    .pipe(uglify())
    .pipe(rename({ extname: '.min.js' }))
    .pipe(gulp.dest('dist'))
});

gulp.task('scripts', function() {
  gulp.src(paths.scripts)
    .pipe(jshint())
    .pipe(jshint.reporter('default'))
    .pipe(connect.reload());
})

gulp.task('webserver', function() {
  connect.server({
    port: port,
    livereload: true
  });
});

gulp.task('watch', function() {
  gulp.watch(paths.scripts, ['scripts']);
});

gulp.task('open', ['webserver'], function() {
  var options = {
    url: 'http://localhost:' + port + '/examples/index.html'
  };
  gulp.src('./examples/index.html')
    .pipe(open('', options));
});

gulp.task('serve', ['watch', 'open']);
