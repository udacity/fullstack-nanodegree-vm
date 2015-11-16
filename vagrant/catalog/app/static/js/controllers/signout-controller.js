'use strict';

define(['PostDataService', 'DataBroadcastService', 'AuthenticationService'], function(PostDataService, DataBroadcastService, AuthenticationService) {
  return ['PostDataService', 'DataBroadcastService', 'AuthenticationService', '$scope', function(PostDataService, DataBroadcastService,AuthenticationService, $scope) {
    $scope.isDisabled = true;
    $scope.log_type = undefined;

    $scope.google_url = "http://localhost:8000/glogout";
    $scope.facebook_url = "http://localhost:8000/flogout";

    $scope.init = function() {
      $scope.isDisabled = true;
    };

    $scope.logout = function() {
      var url = undefined;
      if ($scope.log_type == 'google') {
        url = $scope.google_url;
      } else if ($scope.log_type == 'facebook') {
        url = $scope.facebook_url;
      }
      if (url !== undefined) {
        PostDataService.logout(AuthenticationService.auth_url(url))
          .then(
            function(response) {
              DataBroadcastService.login_status.set = response;
            });
      }
    };

    $scope.$on('broadcastLoginStatusChange', function() {
      $scope.login_status = DataBroadcastService.login_status.get;
    });

    $scope.$watch('login_status', function(new_value, old_value) {
      if ((new_value !== undefined) && (new_value !== {}) && (new_value !== old_value)) {
        $scope.isDisabled = (new_value.id === undefined);
        $scope.log_type = new_value.type;
      }
    }, true);

  }];
});
