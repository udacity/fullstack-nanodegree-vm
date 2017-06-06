'use strict';

define(['LoadDataService', 'DataBroadcastService'], function(LoadDataService, DataBroadcastService) {
  return ['$scope', '$uibModal', 'LoadDataService', 'DataBroadcastService',
    function($scope, $uibModal, LoadDataService, DataBroadcastService) {
      var self = this;
      $scope.items = [];
      $scope.url = "http://localhost:8000/items/json";
      $scope.current_url = "";
      $scope.category = "All Items";
      $scope.category_url = "http://localhost:8000/category/json";
      $scope.use_current_user = false;
      $scope.login_user = undefined;
      $scope.user_id = undefined;

      $scope.init = function() {
        $scope.use_current_user = false;
        $scope.login_user = 'You are not logged in!'
        $scope.category_id = DataBroadcastService.category_id.get;
        $scope.current_url = $scope.url;
        $scope.user_id = undefined;
        LoadDataService.loadData($scope.url)
          .then(
            function(response) {
              $scope.items = response.data.items;
            });
      }

      $scope.$on('reloadData', function() {
        LoadDataService.loadData($scope.url)
          .then(
            function(response) {
              $scope.items = response.data.items;
            });
      })

      $scope.$on('broadcastCategoryChange', function() {
        $scope.category_id = DataBroadcastService.category_id.get;
      });

      $scope.$watch('category_id', function(new_value, old_value) {
        if (new_value !== null && new_value != old_value) {
          if (new_value === undefined) {
            $scope.current_url = $scope.url;
          } else {
            $scope.current_url = [$scope.url, "/category_id=", new_value].join("");
          }
          LoadDataService.loadData($scope.current_url)
            .then(
              function(response) {
                $scope.items = response.data.items;
              }
            );
        }
      }, true);

      $scope.$on('broadcastCategoryNameChange', function() {
        $scope.category = DataBroadcastService.category_name.get;
      });

      $scope.$watch('category', function(new_value, old_value) {
        if (new_value !== null && new_value != old_value) {
          if (new_value === undefined) {
            $scope.category = "All Items";
          } else {
            $scope.category = new_value;
          }
        }
      }, true);

      $scope.$on('broadcastUseCurrentUser', function() {
        $scope.use_current_user = DataBroadcastService.use_current_user.get;
      });

      $scope.$watch('use_current_user', function(new_value, old_value) {
        if (new_value !== undefined && new_value != old_value) {
          if (new_value) {
            if ($scope.user_id !== undefined) {
              $scope.current_url = [$scope.url, "/user_id=", $scope.user_id].join("");
              LoadDataService.loadData($scope.current_url)
                .then(
                  function(response) {
                    $scope.items = response.data.items;
                  }
                );
            } else {
              $scope.items = [];
            }
          }
        }
      }, true);

      $scope.$on('broadcastLoginStatusChange', function() {
        $scope.login_status = DataBroadcastService.login_status.get;
      });

      $scope.$watch('login_status', function(new_value, old_value) {
        if (new_value != old_value) {
          $scope.login_user = (new_value !== undefined && new_value.id != undefined) ? new_value.name : 'You are not logged in!';
          $scope.user_id = new_value.id !== undefined ? new_value.id : undefined;
        }
      }, true);
    }
  ];
});
