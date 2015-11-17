'use strict';

define(['LoadDataService', 'DataBroadcastService'], function(LoadDataService, DataBroadcastService) {
  return ['$scope', '$timeout', 'LoadDataService', 'DataBroadcastService',
    function($scope, $timeout, LoadDataService, DataBroadcastService) {
      $scope.prefix = 'static/';
      $scope.showButton = false;
      $scope.login_status = undefined;
      $scope.url = "http://localhost:8000/image/json/";

      $scope.init = function() {
        $scope.login_status = undefined;
        var url = [$scope.url, "id=", $scope.item.image_id].join("");
        var current_id = DataBroadcastService.login_status.get.id
        $scope.showButton = (current_id !== undefined && current_id === $scope.item.user_id);
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
          var current_id = new_value.id
          $scope.showButton = (current_id !== undefined && current_id === $scope.item.user_id);
        }
      }, true);

    }
  ];
});
