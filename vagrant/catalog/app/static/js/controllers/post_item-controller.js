'use strict';

define(['LoadDataService'], function(LoadDataService) {
  return ['$scope', '$rootScope', '$uibModal', 'LoadDataService',
    function($scope, $rootScope, $uibModal, LoadDataService) {
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

      $scope.prefix = "static/";
      $scope.postItem = function(_item) {
        var modalInstance = $uibModal.open({
          templateUrl: 'static/js/directives/templates/_post_item.html',
          controller: 'PostModalController',
          resolve: {
            item: function() {
              return _item || {};
            },
            data: function() {
              return {
                title: (_item === undefined) ? '' : _item.title,
                description: (_item === undefined) ? '' : _item.description,
                header: (_item === undefined) ? 'Add new item' : ['Edit ', _item.title].join(""),
                image_id: (_item === undefined) ? undefined : _item.image_id,
                selectedCategory: (_item === undefined) ? 'Soccer' : _item.category_id,
                categories: function(){
                  return LoadDataService.loadData(self.category_url).then(
                    function(response){return response.data.categories;},
                    function(error){return [];}
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
