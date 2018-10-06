const gulp = require('gulp');
const sass = require('gulp-sass');
const concat = require('gulp-concat');

gulp.task('default', ['css', 'js', 'librarycss', 'libraryjs']);

// Modifying Bootstrap and Materialize
gulp.task('css', function () {
    gulp.src('src/app/sass/**/*.scss')
        .pipe(concat('main.css'))
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('src/static'))
});

var librarycss = [
    "node_modules/font-awesome/css/font-awesome.css"
];

// Library CSS 
gulp.task('librarycss', function () {
    gulp.src(librarycss)
        .pipe(concat('library.css'))
        .pipe(gulp.dest('src/static'))    
});

// Javascript
gulp.task('js', function() {
    gulp.src('src/app/**/*.js')
        .pipe(concat('main.js'))
        .pipe(gulp.dest('src/static'))
});

var libraryjs = [
    'node_modules/jquery/dist/jquery.js',
    'node_modules/popper.js/dist/umd/popper.js',
    'node_modules/bootstrap/dist/js/bootstrap.js',
    'node_modules/angular/angular.js',
    'node_modules/angular-animate/angular-animate.js',
    'node_modules/angular-ui-router/release/angular-ui-router.min.js',
];

// Library Javascript
gulp.task('libraryjs', function () {
    gulp.src(libraryjs)
        .pipe(concat('library.js'))
        .pipe(gulp.dest('src/static'))
});

gulp.task('watch', ['css', 'js'], function() {
    gulp.watch('src/app/sass/**/*.scss', ['css']);
    gulp.watch('src/app/**/*.js', ['js']);
})