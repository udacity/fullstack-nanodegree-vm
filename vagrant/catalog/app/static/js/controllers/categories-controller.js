'use strict';

define(['LoadDataService', 'DataBroadcastService'], function(LoadDataService, DataBroadcastService) {
  return ['$scope', 'LoadDataService', 'DataBroadcastService',
    function($scope, LoadDataService, DataBroadcastService) {
      $scope.categories = [];
      $scope.items = [];
      $scope.url = "http://localhost:8000/category/json";
      $scope.selected = undefined;
      $scope.my_index = undefined;
      $scope.all_index = undefined;

      $scope.init = function() {
        LoadDataService.loadData($scope.url)
          .then(
            function(response) {
              $scope.categories = response.data.categories;

              $scope.all_index = $scope.categories.length;
              $scope.my_index = $scope.categories.length + 1;
              $scope.selected = $scope.all_index;
            });
      }

      $scope.changeCategoryID = function(category_id, index) {
        $scope.selected = index == undefined ? $scope.all_index : index;

        DataBroadcastService.category_id.set = category_id;
        DataBroadcastService.category_name.set = category_id === undefined ? undefined : $scope.categories.filter(function(item) {
          return item.id === category_id;
        })[0].name;
        DataBroadcastService.use_current_user.set = false;
      }

      $scope.viewMyItems = function() {
        $scope.selected = $scope.my_index;

        DataBroadcastService.category_name.set = 'My Items';
        DataBroadcastService.use_current_user.set = true;
      }
    }
  ];
});
