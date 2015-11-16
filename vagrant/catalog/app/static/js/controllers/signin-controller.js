'use strict';

define(['PostDataService', 'DataBroadcastService', 'AuthenticationService'], function(PostDataService, DataBroadcastService, AuthenticationService) {
  return ['PostDataService', 'DataBroadcastService', 'AuthenticationService', 'GooglePlus', '$scope', 'Facebook', function(PostDataService, DataBroadcastService, AuthenticationService, GooglePlus, $scope, Facebook) {
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
    $scope.$on('event:google-plus-signin-failure', function(event, authResult) {
      console.log(authResult);
    });

    $scope.logToFacebook = function() {
      Facebook.login().then(function() {
        // console.log(authResult);
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

    $scope.$watch(
      function() {
        return Facebook.isReady();
      },
      function(newVal) {
        if (newVal)
          $scope.facebookReady = true;
      }
    );

    // $scope.$watch('google_status', function(new_value, old_value) {
    //   if ((new_value != undefined) && (new_value !== {}) && (new_value !== '') && (new_value != old_value)) {
    //     PostDataService.login($scope.goggle_url, new_value).then(
    //       function(response) {
    //         DataBroadcastService.login_status.set = response;
    //       }
    //     );
    //   }
    // });

  }];
});
