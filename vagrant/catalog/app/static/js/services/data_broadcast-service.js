'use strict';

define([], function() {
  return ['$http', '$q', '$rootScope', function($http, $q, $rootScope) {
    var service = {};
    var self = this;
    service.category_id = {
      id: null
    }
    Object.defineProperties(service.category_id, {
      "get": {
        get: function() {
          return this.id;
        }
      },
      "set": {
        set: function(id) {
          this.id = id;
          service.broadcastItem('broadcastCategoryChange');
        }
      }
    });

    service.category_name = {
      name: undefined
    }
    Object.defineProperties(service.category_name, {
      "get": {
        get: function() {
          return this.name;
        }
      },
      "set": {
        set: function(name) {
          this.name = name;
          service.broadcastItem('broadcastCategoryNameChange');
        }
      }
    });

    service.use_current_user = {
      status: false
    }
    Object.defineProperties(service.use_current_user, {
      "get": {
        get: function() {
          return this.status;
        }
      },
      "set": {
        set: function(status) {
          this.status = status;
          service.broadcastItem('broadcastUseCurrentUser');
        }
      }
    });

    service.logged_user_id = {
      id: undefined
    }
    Object.defineProperties(service.logged_user_id, {
      "get": {
        get: function() {
          return this.id;
        }
      },
      "set": {
        set: function(id) {
          this.id = id;
          service.broadcastItem('broadcastLoggedUserChange');
        }
      }
    });

    service.login_status = {
      id: undefined,
      name: undefined,
      provider: undefined,
      picture: undefined
    }
    Object.defineProperties(service.login_status, {
      "get": {
        get: function() {
          return this;
        }
      },
      "set": {
        set: function(data) {
          this.picture = (data == {} || data == undefined) ? undefined : data.picture;
          this.name = (data == {} || data == undefined) ? undefined : data.fullname;
          this.id = (data == {} || data == undefined) ? undefined : data.id;
          this.provider = (data == {} || data == undefined) ? undefined : data.provider;
          service.broadcastItem('broadcastLoginStatusChange');
        }
      }
    });

    service.broadcastItem = function(action) {
      $rootScope.$broadcast(action);
    };

    return service;
  }];
});
