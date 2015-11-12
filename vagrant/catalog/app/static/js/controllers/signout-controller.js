'use strict';

define(['LoadDataService', 'DataBroadcastService'], function(LoadDataService, DataBroadcastService) {
  return ['LoadDataService', 'DataBroadcastService', '$scope', function(LoadDataService, DataBroadcastService, $scope) {
    $scope.isDisabled = true;
    $scope.logout_url = "http://localhost:8000/logout";

    $scope.init = function() {
      $scope.isDisabled = true;
    };

    $scope.logout = function() {
      LoadDataService.loadData($scope.logout_url)
        .then(
          function(response) {
            DataBroadcastService.login_status.set = response;
          });
    };

    $scope.$on('broadcastLoginStatusChange', function() {
      $scope.login_status = DataBroadcastService.login_status.get;
    });

    $scope.$watch('login_status', function(new_value, old_value) {
      if (new_value != old_value) {
        $scope.isDisabled = (new_value === undefined || new_value.id === undefined);
      }
    }, true);

  }];
});
