'use strict';

define(['PostDataService', 'DataBroadcastService'], function(PostDataService, DataBroadcastService) {
  return ['PostDataService', 'DataBroadcastService', 'GooglePlus', '$scope', function(PostDataService, DataBroadcastService, GooglePlus, $scope) {
    $scope.isDisabled = false;
    $scope.login_status = undefined;
    $scope.goggle_url = "http://localhost:8000/glogin?_csrf_token={{ csrf_token() }}";
    $scope.facebook_url = "http://localhost:8000/flogin?_csrf_token={{ csrf_token() }}";

    $scope.init = function() {
      $scope.isDisabled = false;
    };

    $scope.$on('event:google-plus-signin-success', function(event, authResult) {
      PostDataService.login($scope.goggle_url, authResult['code']).then(
        function(response) {
          DataBroadcastService.login_status.set = response.data;
        }
      );
    });
    $scope.$on('event:google-plus-signin-failure', function(event, authResult) {
      console.log(authResult);
    });

    $scope.logToFacebook = function() {
      //load login status from credentials
    };

    $scope.$on('broadcastLoginStatusChange', function() {
      $scope.login_status = DataBroadcastService.login_status.get;
    });

    $scope.$watch('login_status', function(new_value, old_value) {
      if ((new_value !== undefined) && (new_value !== {}) && (new_value !== old_value)) {
        $scope.isDisabled = (new_value.id !== undefined);
      }
    }, true);

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
