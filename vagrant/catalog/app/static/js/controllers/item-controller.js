'use strict';

define(['LoadDataService', 'DataBroadcastService'], function(LoadDataService, DataBroadcastService) {
  return ['$scope', '$timeout', 'LoadDataService', 'DataBroadcastService',
    function($scope, $timeout, LoadDataService, DataBroadcastService) {
      $scope.prefix = 'static/';
      $scope.isLoggedIn = false;
      $scope.login_status = undefined;
      $scope.url = "http://localhost:8000/image/json/";

      $scope.init = function() {
        $scope.login_status = undefined;
        var url = [$scope.url, "id=", $scope.item.image_id].join("");
        $scope.isLoggedIn = (DataBroadcastService.login_status.get.id !== undefined);
        LoadDataService.loadData(url)
          .then(
            function(response) {
              $scope.image = response.data === undefined ? undefined : [$scope.prefix, response.data.path].join("");
            });
      }

      $scope.$on('broadcastLoginStatusChange', function() {
        $scope.login_status = DataBroadcastService.login_status.get;
      });

      $scope.$watch('login_status', function(new_value, old_value) {
        if ((new_value !== undefined) && (new_value !== {}) && (new_value !== old_value)) {
          $scope.isLoggedIn = (new_value.id !== undefined);
        }
      }, true);

    }
  ];
});
