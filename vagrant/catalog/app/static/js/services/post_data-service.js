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
      var request = $http({
        method: 'put',
        url: url,
        data: data,
        headers: {
          'Content-Type': 'application/json'
        },
        params: {
          action: 'put'
        }
      });
      return request.then(handleSuccess, handleError);
    }

    service.addNewItem = function(url, data) {
      // var request = $http({
      //   method: 'post',
      //   url: url,
      //   headers: {
      //     'Content-Type': undefined
      //   },
      //   params: {
      //     action: 'post'
      //   }
      // });
      // return request.then(handleSuccess, handleError);
    }

    service.login = function(url, data) {
      // return this.post(url, data);
      return this.post(url, data, 'application/octet-stream; charset=utf-8', 'post');
        // return this.post(url, data, 'application/json; charset=utf-8');
    }

    service.post = function(url, data, content_type, method) {
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
