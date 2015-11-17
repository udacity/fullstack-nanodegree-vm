'use strict';

define([], function() {
    return [function() {
        return {
            restrict: 'AE',
            replace: true,
            transclude: true,
            scope: {
                init: '&',
                item: '=',
                current_url: '@',
                showButton: '@',
                prefix: '@',
                image: '@'
            },
            templateUrl: 'static/js/directives/templates/_show_item.html',
            controller: 'ItemController',
            link: function postLink(scope, element, attrs) {
                scope.init();
            }
        }
    }];
});
