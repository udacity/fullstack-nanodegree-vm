'use strict';

define(['PostDataService', 'DataBroadcastService', 'AuthenticationService'], function(PostDataService, DataBroadcastService, AuthenticationService) {
  return ['PostDataService', 'DataBroadcastService', 'AuthenticationService', '$scope', 'ezfb', '$window', '$location', '$q', function(PostDataService, DataBroadcastService, AuthenticationService, $scope, ezfb, $window, $location, $q) {
    $scope.isDisabled = true;
    $scope.provider = undefined;

    $scope.google_url = "http://localhost:8000/glogout";
    $scope.facebook_url = "http://localhost:8000/flogout";

    $scope.init = function() {
      $scope.isDisabled = true;
    };

    ezfb.Event.subscribe('auth.statusChange', function(authResult) {
      if (authResult.status !== 'connected' && $scope.provider === 'facebook') {
        PostDataService.logout(AuthenticationService.auth_url($scope.facebook_url))
          .then(
            function(response) {
              DataBroadcastService.login_status.set = response;
            });
      }
    });

    $scope.logout = function() {
      var url = undefined;
      if ($scope.provider === 'google') {
        PostDataService.logout(AuthenticationService.auth_url($scope.google_url))
          .then(
            function(response) {
              DataBroadcastService.login_status.set = response;
            });
      } else if ($scope.provider === 'facebook') {
        // ezfb.logout();
        try {
           ezfb.logout();
          // if (FB.getAccessToken() != null) {
          //   FB.logout(function(response) {
          //     // user is now logged out from facebook do your post request or just redirect
          //     // window.location.replace(href);
          //   });
          // } else {
          //   // user is not logged in with facebook, maybe with something else
          //   // window.location.replace(href);
          // }
        } catch (err) {
          console.log(err);
          // any errors just logout
          // window.location.replace(href);
        }
      }
    };

    $scope.$on('broadcastLoginStatusChange', function() {
      $scope.login_status = DataBroadcastService.login_status.get;
    });

    $scope.$watch('login_status', function(new_value, old_value) {
      if ((new_value !== undefined) && (new_value !== {}) && (new_value !== old_value)) {
        $scope.isDisabled = (new_value.id === undefined);
        $scope.provider = new_value.provider;
      }
    }, true);

  }];
});
