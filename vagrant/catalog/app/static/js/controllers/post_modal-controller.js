'use strict';

define(['LoadDataService', 'PostDataService'], function(LoadDataService, PostDataService) {
  return ['$scope', '$uibModalInstance', 'item', 'data', 'LoadDataService', 'PostDataService',
    function($scope, $uibModalInstance, item, data, LoadDataService, PostDataService) {
      $scope.image_url = "http://localhost:8000/image/json/";
      $scope.category_url = "http://localhost:8000/category/json";
      $scope.edit_url = "http://localhost:8000/item/edit/";
      $scope.add_new_url = "http://localhost:8000/item/add/";
      $scope.slideInterval = 0;
      $scope.noWrapSlides = true;
      // scope.images = [];
      $scope.item = item;
      $scope.data = data;
      $scope.categories = data.categories();
      $scope.selectedCategory = data.selectedCategory;
      $scope.footer = "All items must have a value or selection."


      $scope.loadImages = function() {
        if ($scope.selectedCategory !== "") {
          var url = [$scope.image_url, "category=", $scope.selectedCategory].join("");
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
        if ($scope.item === {}) {
          PostDataService.addNewItem($scope.add_new_url, update_item({})).then(
            function(response) {console.log(response)}
          );
        }
        else{
          var url = [$scope.edit_url, $scope.item.id,"/?_csrf_token={{ csrf_token() }}"].join("");
          PostDataService.editItem(url , update_item($scope.item)).then(
            function(response) {console.log(response)}
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
        var item = data
        item.category_id = $scope.selectedCategory.id;
        item.title = $scope.data.title;
        item.description = $scope.data.description;
        item.image_id = $scope.images.filter(function(item) {
          return item.active === true;
        })[0].id;

        return item;
      }


    }
  ];
});
