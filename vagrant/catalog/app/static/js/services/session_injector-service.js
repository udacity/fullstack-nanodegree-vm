'use strict';

define([], function() {
  return ['$injector', '$q', function($injector, $q) {
    var sessionInjector = {
      request: function(config) {
        var _csrf_token = document.querySelector("meta[name='_csrf_token']").getAttribute('content');
        config.headers['x-csrf-token'] = _csrf_token;
        return config;
      }
    };
    return sessionInjector;
  }];
})
