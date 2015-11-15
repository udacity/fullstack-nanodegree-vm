'use strict';

define([], function() {
  return ['$http', '$q', '$rootScope', function($http, $q, $rootScope) {
    var service = {};
    var self = this;

    service.deleteItem = function(url) {
      var request = $http({
        method: 'post',
        url: url,
        headers: {
          'Content-Type': undefined
        },
        params: {
          action: 'post'
        }
      });
      return request.then(handleSuccess, handleError);
    }

    service.editItem = function(url, data) {
      return this.post_data(url, data, 'application/json', 'put');
    }

    service.addNewItem = function(url, data) {
      return this.post_data(url, data, 'application/json', 'post');
    }

    service.logout = function(url) {
      return this.post(url, undefined, 'application/octet-stream; charset=utf-8', 'post', false);
    }

    service.login = function(url, data) {
      return this.post(url, data, 'application/octet-stream; charset=utf-8', 'post', false);
    }

    service.post_data = function(url, data, content_type, method) {
      var request = $http({
        method: method,
        url: url,
        data: data,
        headers: {
          'Content-Type': content_type
        },
        params: {
          action: method
        }
      });
      return request.then(handleSuccess, handleError);
    }

    service.post = function(url, data, content_type, method) {
      var request = $http({
        method: method,
        url: url,
        data: data,
        processData: false,
        headers: {
          'Content-Type': content_type
        },
        params: {
          action: method
        }
      });
      return request.then(handleSuccess, handleError);
    }


    var handleSuccess = function(response) {
      //Creating a deferred object
      var deferred = $q.defer();
      deferred.resolve(response);
      service.broadcastItem('reloadData');
      return deferred.promise;
    }

    var handleError = function(response) {
      //Creating a deferred object
      var deferred = $q.defer();

      deferred.reject("An error occured while fetching items");
      return deferred.promise;
    }


    service.broadcastItem = function(action) {
      $rootScope.$broadcast(action);
    };

    return service;
  }];
});
