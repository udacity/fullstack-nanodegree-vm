'use strict';

define([], function() {
    return ['$http', '$q', function($http, $q) {
        var service = {}

        service.loadCategories = function() {
            var request = $http({
                method: 'get',
                url: 'http://localhost:8000/category/json',
                params: {
                    action: 'get'
                }
            });
            return request.then(handleSuccess, handleError);
        }

        service.loadData = function(url) {
            var request = $http({
                method: 'get',
                url: url,
                params: {
                    action: 'get'
                }
            });
            return request.then(handleSuccess, handleError);
        }

        var handleSuccess = function(response) {
            //Creating a deferred object
            var deferred = $q.defer();

            deferred.resolve(response);
            return deferred.promise;
        }

        var handleError = function(response){
            //Creating a deferred object
            var deferred = $q.defer();

            deferred.reject("An error occured while fetching items");
            return deferred.promise;
        }

        return service;
    }];
});
