'use strict';

define(['PostDataService'], function(PostDataService) {
  return ['$scope', 'PostDataService',
    function($scope, PostDataService) {
      $scope.service = PostDataService;
      $scope.url = "http://localhost:8000/item/delete/";

      $scope.deleteItem = function(item) {
        dialog(item, this);
      }

      var dialog = function(item, self) {
        bootbox.dialog({
          message: "Are you sure you want to remove this item?",
          title: item.title,
          closeButton: false,
          buttons: {
            success: {
              label: "Yes",
              className: "btn-danger",
              callback: function(){
                self.service.deleteItem([self.url, item.id, "?_csrf_token={{ csrf_token() }}"].join(""))
                  .then(
                    function(response) {
                      // TODO Log to console
                    });
              }
            },
            danger: {
              label: "No!",
              className: "btn-danger",
              className: "btn-success",
              callback: function() {
                console.log('Cancel');
              }
            }
          }
        });
      }
    }
  ];
});
