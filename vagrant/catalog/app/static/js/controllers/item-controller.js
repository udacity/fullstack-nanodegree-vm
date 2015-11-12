'use strict';

define(['LoadDataService'], function(LoadDataService) {
  return ['$scope', 'LoadDataService',
    function($scope, LoadDataService) {
      $scope.image = 'static/';
      $scope.url = "http://localhost:8000/image/json/";

      $scope.init = function() {
        $scope.isLoggedIn = true;
        var url = [$scope.url, "id=", $scope.item.image_id].join("");
        LoadDataService.loadData(url)
          .then(
            function(response) {
              $scope.image = [$scope.image, response.data.images[0].path].join("");
            });
      }

      $scope.$on('broadcastLoggedUserChange', function() {
        $scope.logged_user_id = DataBroadcastService.logged_user_id.get;
      });

      $scope.$watch('logged_user_id', function(new_value, old_value) {
        if (new_value != old_value) {
          if (new_value === undefined){
          $scope.isLoggedIn = false;
        }
        else{
          $scope.isLoggedIn = $scope.item.user_id === new_value;
        }
        }
      }, true);

    }
  ];
});
