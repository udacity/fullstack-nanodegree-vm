'use strict';

define(['PostDataService', 'DataBroadcastService'], function(PostDataService, DataBroadcastService) {
  return ['PostDataService', 'DataBroadcastService', 'GooglePlus', '$scope', function(PostDataService, DataBroadcastService, GooglePlus, $scope) {
    $scope.isDisabled = false;
    $scope.login_status = undefined;
    $scope.goggle_url = "http://localhost:8000/gconnect/?_csrf_token={{ csrf_token() }}";
    $scope.google_status = undefined;

    $scope.init = function() {
      $scope.isDisabled = false;
    };

    $scope.logToGoogle = function() {
      //load login status from credentials
      GooglePlus.login().then(function(authResult) {
        // GooglePlus.getUser().then(function(user) {
        //   console.log(user);
        // });
        $scope.google_status = authResult
        console.log(authResult);

        GooglePlus.getUser().then(function(user) {
          console.log(user);
        });
      }, function(err) {
        console.log(err);
      });
    };

    $scope.logToFacebook = function() {
      //load login status from credentials
    };

    $scope.logToTwitter = function() {
      //load login status from credentials
    };

    $scope.$on('broadcastLoginStatusChange', function() {
      $scope.login_status = DataBroadcastService.login_status.get;
    });

    $scope.$watch('login_status', function(new_value, old_value) {
      if (new_value != old_value) {
        $scope.isDisabled = (new_value !== undefined && new_value.id != undefined);
      }
    }, true);

    $scope.$watch('google_status', function(new_value, old_value) {
      if ((new_value != undefined) && (new_value !== {}) && (new_value !== '') && (new_value != old_value)) {
        PostDataService.login($scope.goggle_url, {}).then(
          function(response) {
            DataBroadcastService.login_status.set = response;
          }
        );
      }
    });

  }];
});
