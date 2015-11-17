'use strict';

define(['LoadDataService', 'PostDataService', 'AuthenticationService'], function(LoadDataService, PostDataService, AuthenticationService) {
  return ['$scope', '$uibModalInstance', 'item', 'data', 'LoadDataService', 'PostDataService', 'AuthenticationService',
    function($scope, $uibModalInstance, item, data, LoadDataService, PostDataService, AuthenticationService) {
      $scope.image_url = "http://localhost:8000/images/json/";
      $scope.category_url = "http://localhost:8000/category/json";
      $scope.edit_url = "http://localhost:8000/item/edit/";
      $scope.add_new_url = "http://localhost:8000/item/new";
      $scope.slideInterval = 0;
      $scope.noWrapSlides = true;
      $scope.prefix = "static/";
      $scope.item = item;
      $scope.data = data;
      $scope.categories = data.categories();
      $scope.selectedCategory = data.selectedCategory;
      $scope.footer = "All items must have a value or selection."

      $scope.loadImages = function() {
        if ($scope.selectedCategory !== "") {
          var url = [$scope.image_url, "category_id=", $scope.selectedCategory].join("");
          LoadDataService.loadData(url)
            .then(
              function(response) {
                $scope.images = response.data.images;
                $scope.images = $scope.images.map(function(image) {
                  image.active = (image.id === $scope.data.image_id);
                  return image;
                });
              });
        }
      }

      $scope.cancel = function() {
        $uibModalInstance.dismiss('cancel');
      };

      $scope.changeCategory = function() {}

      $scope.save = function() {
        var self = this;
        if ($scope.item === {} || $scope.item.id === undefined) {
          PostDataService.addNewItem(AuthenticationService.auth_url($scope.add_new_url), update_item({})).then(
            function(response) {
              console.log(response)
            }
          );
        } else {
          var url = [$scope.edit_url, $scope.item.id].join("");
          PostDataService.editItem(AuthenticationService.auth_url(url), update_item($scope.item)).then(
            function(response) {
              console.log(response)
            }
          );
        }
        $uibModalInstance.close();
      };

      $scope.$watch('selectedCategory', function(new_value, old_value) {
        if (new_value !== "" && new_value !== undefined && (new_value != old_value || $scope.images === undefined)) {
          $scope.loadImages();
        }
      }, true);

      var update_item = function(data) {
        data.category_id = $scope.selectedCategory;
        data.title = $scope.data.title;
        data.description = $scope.data.description;
        data.image_id = $scope.images.filter(function(item) {
          return item.active === true;
        })[0].id;

        return data;
      }


    }
  ];
});
