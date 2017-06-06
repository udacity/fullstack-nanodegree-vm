'use strict';

define(['PostDataService', 'AuthenticationService'], function(PostDataService, AuthenticationService) {
  return ['$scope', 'PostDataService', 'AuthenticationService',
    function($scope, PostDataService, AuthenticationService) {
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
                self.service.deleteItem(AuthenticationService.auth_url([self.url, item.id].join("")))
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
