require.config({
    paths: {
        'angular': '../../bower_components/angular/angular.min',
        'jquery': '../../bower_components/jquery/dist/jquery.min',
        'twbs': '../../bower_components/bootstrap/dist/js/bootstrap.min',
        'bootbox': '../../bower_components/bootbox/bootbox',
        'ngBootbox': '../../ngBootbox'
    },
    shim: {
        'angular': {
            exports: 'angular'
        },
        'twbs': {
            deps: [
                'jquery'
            ]
        },
        'bootbox': {
            deps: [
                'jquery',
                'twbs'
            ]
        },
        'ngBootbox': {
            deps: [
                'jquery',
                'angular',
                'twbs',
                'bootbox'
            ]
        }
    }
});

require(['angular', 'app'], function (angular, app) {
    angular.bootstrap(document, ['app']);
});