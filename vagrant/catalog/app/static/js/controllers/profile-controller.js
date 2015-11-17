'use strict';

define(['LoadDataService', 'DataBroadcastService'], function(LoadDataService, DataBroadcastService) {
  return ['$scope', '$timeout', 'LoadDataService', 'DataBroadcastService',
    function($scope, $timeout, LoadDataService, DataBroadcastService) {
      $scope.isLoggedIn = false;
      $scope.picture = undefined;

      $scope.init = function() {
        var status = DataBroadcastService.login_status.get
        $scope.isLoggedIn = (status.id !== undefined);
        $scope.picture = status.picture !== undefined ? status.picture : undefined;
      }

      $scope.$on('broadcastLoginStatusChange', function() {
        $scope.login_status = DataBroadcastService.login_status.get;
      });

      $scope.$watch('login_status', function(new_value, old_value) {
        if ((new_value !== undefined) && (new_value !== {}) && (new_value !== old_value)) {
          $scope.isLoggedIn = (new_value.id !== undefined);
          $scope.picture = new_value.picture !== undefined ? new_value.picture : undefined;
        }
      }, true);

    }
  ];
});
