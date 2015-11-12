'use strict';

define([], function() {
      return [function() {
          return {
            restrict: 'AE',
            replace: true,
            transclude: true,
            scope: {
              'loadCategories': '&modalLoadCategories',
              'loadImages': '&modalLoadImages',
              'item': '=',
              'category_url': '@',
              'selectedCategory': '=modalCategory',
              'categories': '=modalCategories',
              'images': '=modalImages',
              'selectedImage': '=modalImage',
              'header': '@',
              'title': '=',
              'description': '=',
              footer: '=modalFooter',
              'init': '&',
              changeCategory: '&modalChangeCategory',
              callbackbuttonleft: '&ngClickLeftButton',
              callbackbuttonright: '&ngClickRightButton',
              handler: '=lolo'
            },
            templateUrl: 'static/js/directives/templates/_post_item.html',
            controller: 'PostModalController',
            // controller: function($scope) {
            //   $scope.handler = $scope.item.id;
            //
            //   // $scope.selectedCategory = $scope.item.category_id || $scope.categories[0].id;
            //   // $scope.selectedImage = $scope.item.image_id || "";
            //   // $scope.loadImages($scope.selectedCategory);
            //   // $scope.loadCategories($scope.category_url);
            //   // $scope.init();
            // },
            link: function postLink(scope, element, attrs) {
              scope.$watch('selectedCategory', function(new_value, old_value) {
                  if (new_value !== "" && new_value !== undefined && (new_value != old_value)) {
                    scope.loadImages();
                    // scope.selectedImage = scope.images[0].id;
                  }
                }, true);
                // scope.loadImages();
                scope.init();
                // scope.loadCategories(scope.category_url);
                // scope.dialogStyle = {};
                // if (attrs.width)
                //   scope.dialogStyle.width = attrs.width;
                // if (attrs.height)
                //   scope.dialogStyle.height = attrs.height;
                // scope.hideModal = function() {
                //   scope.show = false;
                // };
              }
            }
          }];
      });
