'use strict';

define([], function() {
  return [function() {
    return {
      restrict: 'AE',
      replace: true,
      transclude: true,
      scope: {
        init: '&',
        logout: '&',
        provider: '@',
        google_url: '@',
        facebook_url: '@',
        isDisabled: '@'
      },
      templateUrl: 'static/js/directives/templates/_signout.html',
      controller: 'SignoutController',
      link: function postLink(scope, element, attrs) {
        scope.init();
      }
    }
  }];
});
