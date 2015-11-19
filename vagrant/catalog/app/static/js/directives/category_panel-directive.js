'use strict';

define([], function() {
    return [function() {
        return {
            restrict: 'AE',
            replace: true,
            transclude: true,
            scope: {
                init: '&',
                changeCategoryID: '&',
                viewMyItems: '&',
                categories: '@',
                all_index: '@',
                my_index: '@',
                selected: '='
            },
            templateUrl: 'static/js/directives/templates/_show_categories.html',
            controller: 'CategoriesController',
            link: function postLink(scope, element, attrs) {
                scope.init();
            }
        }
    }];
});
