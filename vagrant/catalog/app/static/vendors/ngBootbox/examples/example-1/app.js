/**
 * Created by Erik on 2014-05-30.
 */
angular.module('testApp', ['ngBootbox'])
  .controller('TestCtrl', function($scope, $log, $ngBootbox) {

      $scope.locales = ['bg_BG', 'br', 'cs', 'da', 'de', 'el', 'en', 'es', 'et', 'fa', 'fi', 'fr', 'he', 'hu', 'hr', 'id', 'it', 'ja', 'lt',
        'lv', 'nl', 'no', 'pl', 'pt', 'ru', 'sq', 'sv', 'th', 'tr', 'zh_CN', 'zh_TW'];
      $scope.selectedLocale = 'en';

      $ngBootbox.setDefaults({
          animate: false,
          backdrop: false,
          locale: $scope.selectedLocale
      });

      $scope.actions = [];

      $scope.addAction = function(type, msg) {
          console.log(type + ': ' + msg);
          $scope.actions.push({
              msg: type + ': ' + msg
          });
      };


      $scope.handleAlert = function() {
          $ngBootbox.alert('test1!')
            .then(function() {
                $log.log('Alert closed');
            });
      };

      $scope.handleConfirm = function() {
          $ngBootbox.confirm('test2!')
            .then(function() {
                $log.info('Confirmed!');
            }, function() {
                $log.log('Confirm dismissed!');
            });
      };

      $scope.handlePrompt = function() {
          $ngBootbox.prompt('test3!')
            .then(function(result) {
                $log.info('Prompt returned: ' + result);
            }, function() {
                $log.log('Prompt dismissed!');
            });
      };

      $scope.openCustomDialogWithService = function() {
        $ngBootbox.customDialog($scope.customDialogOptions);
      };

      $scope.customDialogOptions = {
          //message: 'This is a message!',
          templateUrl: 'custom-dialog.tpl.html',
          title: 'The best title!',
          onEscape: function() {
              $log.info('Escape was pressed');
          },
          show: true,
          backdrop: false,
          closeButton: true,
          animate: true,
          className: 'test-class',
          buttons: $scope.customDialogButtons,
          message: 'test'
      };

      $scope.customDialogButtons = {
          warning: {
              label: "Warning!",
              className: "btn-warning",
              callback: function() { $scope.addAction('Warning', false); }
          },
          success: {
              label: "Success!",
              className: "btn-success",
              callback: function() { $scope.addAction('Success!', true); }
          },
          danger: {
              label: "Danger!",
              className: "btn-danger",
              callback: function() { $scope.addAction('Danger!', false); }
          },
          main: {
              label: "Click ME!",
              className: "btn-primary",
              callback: function() { $scope.addAction('Main...!', true); }
          }
      };


      $scope.customConfirmButtons = {
          ok: {
              label: "Ok",
              className: "btn-primary",
              callback: function() { $scope.deleteBook(); }
          },
          cancel: {
              label: "Cancel",
              className: "btn-default"
          }
      };

      $scope.deleteBook = function() {
          $ngBootbox.alert('Book deleted!');
      };

      $scope.switchLanguage = function() {
          $ngBootbox.setLocale($scope.selectedLocale);
      };
  })
  .controller('CustomCtrl', function($scope, $log, $ngBootbox) {
      $scope.items = [
          { id: 1, name: 'Item 1' },
          { id: 2, name: 'Item 2' },
          { id: 3, name: 'Item 3' }
      ];

      $scope.buttonClick = function() {
          $ngBootbox.alert('The button was clicked!');
      };
  });
  /*.run(['$templateCache', function($templateCache) {
      $templateCache.put('custom-dialog.tpl.html',
        '<div ng-controller="CustomCtrl"><h1>This is a cached template!</h1><p>Some text...</p><h2>A list</h2><ul><li ng-repeat="item in items">{{item.name}}</li></ul><button class="btn btn-primary" ng-click="buttonClick()">A button</button></div>');
  }]);*/
