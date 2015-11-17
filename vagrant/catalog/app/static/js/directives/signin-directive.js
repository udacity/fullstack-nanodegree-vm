'use strict';

define([], function() {
    return [function() {
        return {
            restrict: 'AE',
            replace: true,
            transclude: true,
            scope: {
                init: '&',
                isDisabled: '@',
                login_status: '@',
                goggle_url: '@',
                facebook_url: '@'
            },
            templateUrl: 'static/js/directives/templates/_signin.html',
            controller: 'SigninController',
            link: function postLink(scope, element, attrs) {
              scope.init();
            }
        }
    }];
});
