'use strict';

define(['LoadDataService', 'DataBroadcastService'], function(LoadDataService, DataBroadcastService) {
  return ['$scope', '$uibModal', 'LoadDataService', 'DataBroadcastService',
    function($scope, $uibModal, LoadDataService, DataBroadcastService) {
      var self = this;

      self.category_url = "http://localhost:8000/category/json";
      self.categories = [];
      self.loadCategories = function() {
        var url = category_url;
        LoadDataService.loadData(url)
          .then(
            function(response) {
              self.categories = response.data.categories;
            });
      }

      $scope.url = "http://localhost:8000/category/json";
      $scope.category = "All Items";
      $scope.categories = [];
      $scope.isDisabled = true;


      $scope.init = function() {
        $scope.isDisabled = (DataBroadcastService.login_status.get.id === undefined);
        LoadDataService.loadData($scope.url)
          .then(
            function(response) {
              $scope.categories = response.data.categories;
            });
      }

      $scope.$on('broadcastCategoryChange', function() {
        $scope.category_id = DataBroadcastService.category_id.get;
      });

      $scope.$watch('category_id', function(new_value, old_value) {
        if (new_value !== null && new_value != old_value) {
          if (new_value === undefined) {
            $scope.category = "All Items";
          } else {
            $scope.category = $scope.categories.filter(function(item) {
              return item.id === new_value;
            })[0].name;
          }
        }
      });

      $scope.$on('broadcastLoginStatusChange', function() {
        $scope.login_status = DataBroadcastService.login_status.get;
      });

      $scope.$watch('login_status', function(new_value, old_value) {
        if ((new_value !== undefined) && (new_value !== {}) && (new_value !== old_value)) {
          $scope.isDisabled = (new_value.id === undefined);
        }
      }, true);


      $scope.addNewItem = function(_item) {
        var category_id = $scope.category_id;
        var modalInstance = $uibModal.open({
          templateUrl: 'static/js/directives/templates/_post_item.html',
          controller: 'PostModalController',
          resolve: {
            item: function() {
              return {};
            },
            data: function() {
              return {
                title: '',
                description: '',
                header: 'Add new item',
                image_id: undefined,
                selectedCategory: category_id,
                categories: function() {
                  return LoadDataService.loadData(self.category_url).then(
                    function(response) {
                      return response.data.categories;
                    },
                    function(error) {
                      return [];
                    }
                  );
                }
              };
            }
          }
        });
      }

    }
  ];
});
