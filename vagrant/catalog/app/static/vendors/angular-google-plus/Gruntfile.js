module.exports = function(grunt) {
  'use strict';

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    jshint: {
      jshintrc: '.jshintrc',
      gruntfile: {
        src: 'Gruntfile.js'
      },
      source: {
        src: ['src/**/*.js', 'test/**/*.js']
      }
    },
    watch: {
      gruntfile: {
        files: '<%= jshint.gruntfile.src %>',
        tasks: ['jshint:gruntfile']
      },
      dist: {
        files: '<%= jshint.source.src %>',
        tasks: ['jshint', 'uglify:dist', 'uglify:src']
      }
    },
    uglify: {
      dist: {
        options: {
          banner: '/*! <%= pkg.name %> - v<%= pkg.version %> ' +
          '<%= grunt.template.today("yyyy-mm-dd") %> */\n'
        },
        files: {
          'dist/angular-google-plus.min.js': ['src/angular-google-plus.js']
        }
      },
      src: {
        options: {
          beautify: true,
          compress: false,
          preserveComments: 'all',
          banner: '/*! <%= pkg.name %> - v<%= pkg.version %> ' +
          '<%= grunt.template.today("yyyy-mm-dd") %> */\n'
        },
        files: {
          'dist/angular-google-plus.js': ['src/angular-google-plus.js']
        }
      }
    },
    karma: {
      unit: {
        configFile: 'karma.conf.js'
      },
      ci: {
        configFile: 'karma.conf.js',
        singleRun: true,
        browsers: ['PhantomJS']
      }
    }
  });

  // These plugins provide necessary tasks.
  grunt.loadNpmTasks('grunt-karma');
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-uglify');

  // Default task.
  grunt.registerTask('default', ['jshint', 'uglify:dist', 'uglify:src']);
};
