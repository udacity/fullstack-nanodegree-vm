'use strict';

define(['PostDataService', 'DataBroadcastService', 'AuthenticationService'], function(PostDataService, DataBroadcastService, AuthenticationService) {
  return ['PostDataService', 'DataBroadcastService', 'AuthenticationService', 'GooglePlus', '$scope', 'ezfb', '$window', '$location', '$q', function(PostDataService, DataBroadcastService, AuthenticationService, GooglePlus, $scope, ezfb, $window, $location, $q) {
    $scope.isDisabled = false;
    $scope.login_status = undefined;
    $scope.goggle_url = "http://localhost:8000/glogin";
    $scope.facebook_url = "http://localhost:8000/flogin";

    $scope.init = function() {
      $scope.isDisabled = false;
    };

    $scope.$on('event:google-plus-signin-success', function(event, authResult) {
      PostDataService.login(AuthenticationService.auth_url($scope.goggle_url), authResult['code']).then(
        function(response) {
          DataBroadcastService.login_status.set = response.data;
        }
      );
    });

    // Below is buggy code for later
    ezfb.Event.subscribe('auth.statusChange', function(authResult) {
      updateFacebook(authResult);
    });


    $scope.logToFacebook = function() {
      ezfb.login(null, {
        scope: 'email,user_likes'
      });
    };

    $scope.$on('broadcastLoginStatusChange', function() {
      $scope.login_status = DataBroadcastService.login_status.get;
    });

    $scope.$watch('login_status', function(new_value, old_value) {
      if ((new_value !== undefined) && (new_value !== {}) && (new_value !== old_value)) {
        $scope.isDisabled = (new_value.id !== undefined);
      }
    }, true);

    var updateFacebook = function(authResult) {
      ezfb.getLoginStatus().then(function(res) {
          return ezfb.api('/me?fields=id,name,email,picture');
        })
        .then(function(information) {
          var result = $.extend(authResult, information);
          if (result['status'] === 'connected') {
            try {
              FB.setAccessToken(result['authResponse']['accessToken'])
            } catch (err) {}
            PostDataService.login(AuthenticationService.auth_url($scope.facebook_url), result).then(
              function(response) {
                DataBroadcastService.login_status.set = response.data;
              }
            );
          }
        });
    }

  }];
});
