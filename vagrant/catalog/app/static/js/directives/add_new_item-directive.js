'use strict';

define([], function() {
  return [function() {
    return {
      restrict: 'AE',
      replace: true,
      transclude: true,
      scope: {
        init: '&',
        addNewItem: '&',
        category: '=',
        isDisabled: '='
      },
      templateUrl: 'static/js/directives/templates/_add_item.html',
      controller: 'AddNewItemController',
      link: function postLink(scope, element, attrs) {
        scope.init();
      }
    }
  }];
});
