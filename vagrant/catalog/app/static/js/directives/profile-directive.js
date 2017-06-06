'use strict';

define([], function() {
    return [function() {
        return {
            restrict: 'AE',
            replace: true,
            transclude: true,
            scope: {
                init: '&',
                isLoggedIn: '@',
                picture: '@'
            },
            templateUrl: 'static/js/directives/templates/_profile.html',
            controller: 'ProfileController',
            link: function postLink(scope, element, attrs) {
                scope.init();
            }
        }
    }];
});
