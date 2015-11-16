'use strict';

define([], function() {
  return ['$http', '$q', function($http, $q) {
    var self = this;
    var service = {};

    service.auth_url = function(url) {
      // return [url, "?_csrf_token=", csrf_token()].join("");
      // return [url, "?_csrf_token={{ csrf_token() }}"].join("");
      return url;
    }

    var csrf_token = function() {
      return document.querySelector("meta[name='_csrf_token']").getAttribute('content');
    }

    var csrftoken = "{{ csrf_token() }}";

    return service;
  }];
});
