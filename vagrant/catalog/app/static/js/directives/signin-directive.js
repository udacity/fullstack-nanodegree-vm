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
                logToGoogle: '&',
                goggle_url: '@',
                google_status: '@',
                logToFacebook: '&',
                logToTwitter: '&'
            },
            templateUrl: 'static/js/directives/templates/_signin.html',
            controller: 'SigninController',
            link: function postLink(scope, element, attrs) {
              scope.init();
            }
        }
    }];
});
