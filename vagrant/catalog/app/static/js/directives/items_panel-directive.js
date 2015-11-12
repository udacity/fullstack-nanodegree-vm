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
                items: '=',
                category_id: '=',
                category: '@',
                use_current_user: '@',
                login_user: '@',
                login_status: '@'
            },
            templateUrl: 'static/js/directives/templates/_show_items.html',
            controller: 'ItemsController',
            link: function(scope) {
                scope.init();
            }
        }
    }];
});
