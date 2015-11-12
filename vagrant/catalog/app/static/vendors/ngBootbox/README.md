ngBootbox
=========

AngularJS wrapper for Bootbox.js. Bootbox.js allowes you to easily make use of Twitter Bootstrap modals for javascript alerts, confirms and prompts. ngBootbox includes three directives, one for each of alert, confirm and prompt.

Current version
===============

### Version 0.1.2

Installation
=========

Bower
-----
    bower install --save ngBootbox
    
npm
---
    npm install --save ngbootbox

Development mode
----------------
    <head>
        <script src="bower_components/jquery/dist/jquery.js"></script>
        <script src="bower_components/angular/angular.js"></script>
        <script src="bower_components/bootstrap/dist/js/bootstrap.js"></script>
        <script src="bower_components/bootbox/bootbox.js"></script>
        <script src="bower_components/ngBootbox/dist/ngBootbox.js"></script>
    </head>

Production mode
---------------
    <head>
        <script src="bower_components/jquery/dist/jquery.min.js"></script>
        <script src="bower_components/angular/angular.min.js"></script>
        <script src="bower_components/bootstrap/dist/js/bootstrap.min.js"></script>
        <script src="bower_components/bootbox/bootbox.js"></script>
        <script src="bower_components/ngBootbox/dist/ngBootbox.min.js"></script>
    </head>

Initialize module
-----------------
    angular.module('yourApp', ['ngBootbox']);

Minification
------------

ngBootbox is minification safe, so to minify your own development files, use [Gulp](http://gulpjs.com/) or [Grunt](http://gruntjs.com/) with [ngAnnotate](https://github.com/olov/ng-annotate) ([gulp-ng-annotate](https://www.npmjs.org/package/gulp-ng-annotate/) or [grunt-ng-annotate](https://www.npmjs.org/package/grunt-ng-annotate)).

Demo
====

Visit this page for a working [demo](http://eriktufvesson.github.io/ngbootbox/ "ngBootbox").

Directives
==========

ng-bootbox-alert
----------------

    <button class="btn btn-default" ng-bootbox-alert="Alert message!">
        Alert
    </button>

ng-bootbox-confirm
------------------

    <button class="btn btn-lg btn-primary" ng-bootbox-confirm="Are you sure you want to confirm this?"
            ng-bootbox-confirm-action="confirmCallbackMethod(attr1, attr2)" ng-bootbox-confirm-action-cancel="confirmCallbackCancel(attr1, attr2)">
        Confirm
    </button>

ng-bootbox-prompt
-----------------

    <button class="btn btn-lg btn-primary" ng-bootbox-prompt="Please type in your name"
            ng-bootbox-prompt-action="promptCallback(result)" ng-bootbox-prompt-action-cancel="promptCallbackCancelled(result)">
        Prompt
    </button>

ng-bootbox-custom-dialog
------------------------

    <button class="btn btn-lg btn-primary"
            ng-bootbox-title="A cool title!"
            ng-bootbox-custom-dialog="Some custom text"
            ng-bootbox-buttons="customDialogButtons"
            ng-bootbox-class-name="some-class">
        Custom dialog
    </button>

    <script>
        $scope.customDialogButtons = {
            warning: {
                label: "Warning!",
                className: "btn-warning",
                callback: function() { $scope.addAction('Warning', false); }
            },
            success: {
                label: "Success!",
                className: "btn-success",
                callback: function() { $scope.addAction('Success!', true) }
            },
            danger: {
                label: "Danger!",
                className: "btn-danger",
                callback: function() { $scope.addAction('Danger!', false) }
            },
            main: {
                label: "Click ME!",
                className: "btn-primary",
                callback: function() { $scope.addAction('Main...!', true) }
            }
        };
        </script>

Custom dialog with HTML Template
--------------------------------

    <button class="btn btn-lg btn-primary"
            ng-bootbox-title="A cool title!"
            ng-bootbox-custom-dialog
            ng-bootbox-custom-dialog-template="custom-dialog.tpl.html"
            ng-bootbox-buttons="customDialogButtons">
        Custom dialog with template
    </button>

Custom dialog options
---------------------

An options object can also be used to configure a custom dialog. A full list of available options can be found in the official Bootbox.js [documentation](http://bootboxjs.com/documentation.html).

    <button class="btn btn-lg btn-success"
            ng-bootbox-custom-dialog
            ng-bootbox-options="customDialogOptions">
        Custom dialog options
    </button>

    <script>
        $scope.customDialogOptions = {
            message: 'This is a message!',
            title: 'The best title!',
            onEscape: function() {
              $log.info('Escape was pressed');
            },
            show: true,
            backdrop: false,
            closeButton: true,
            animate: true,
            className: 'test-class',
            buttons: {
                warning: {
                    label: "Cancel",
                    className: "btn-warning",
                    callback: function() { ... }
                },
                success: {
                    label: "Ok",
                    className: "btn-success",
                    callback: function() { ... }
                }
            }
        };
    </script>

$ngBootbox service
==================

The $ngBootbox service can be used to utilize bootbox.js from within your angular code.

Usage
-----
Inject the **$ngBootbox** service in your own angular controller, service, directive, etc.

    angular.module('yourApp')
        .controller('yourCtrl', function($ngBootbox) { ... });


Methods
-------

### $ngBootbox.alert(msg)

Returns a promise that is resolved when the dialog is closed.

**Example**

    $ngBootbox.alert('An important message!')
        .then(function() {
            console.log('Alert closed');
        });


### $ngBootbox.confirm(msg)

Returns a promise that is resolved when if confirmed and rejected if dismissed.

**Example**

    $ngBootbox.confirm('A question?')
        .then(function() {
            console.log('Confirmed!');
        }, function() {
            console.log('Confirm dismissed!');
        });

### $ngBootbox.prompt(msg)

Returns a promise that is resolved when submitted and rejected if dismissed.

**Example**

    $ngBootbox.prompt('Enter something')
        .then(function(result) {
            console.log('Prompt returned: ' + result);
        }, function() {
            console.log('Prompt dismissed!');
        });

### $ngBootbox.customDialog(options)

**Example**

    var options = {
            message: 'This is a message!',
            title: 'The title!',
            className: 'test-class',
            buttons: {
                 warning: {
                     label: "Cancel",
                     className: "btn-warning",
                     callback: function() { ... }
                 },
                 success: {
                     label: "Ok",
                     className: "btn-success",
                     callback: function() { ... }
                 }
            }
        };

    $ngBootbox.customDialog(options);

A full list of available options can be found in the official Bootbox.js [documentation](http://bootboxjs.com/documentation.html).

### Update

**New in 0.0.4:** There is now support for specifying a HTML template also when using the $ngBootbox service for displaying custom dialogs.

    $scope.customDialogOptions = {
    templateUrl: 'custom-dialog.tpl.html',
         title: 'The title!',
         buttons: $scope.customDialogButtons
    };

When doing this, the message property will be overwritten by the content of the HTML template.


### $ngBootbox.setDefaults(options)

Used to set default values for all your Bootbox alerts, confirms, prompts and dialogs.

**Example**

    $ngBootbox.setDefaults({
        animate: false,
        backdrop: false
    });

A full list of available options can be found in the official Bootbox.js [documentation](http://bootboxjs.com/documentation.html).

### $ngBootbox.hideAll()

Hide all currently active bootbox dialogs.

**Example**

    $ngBootbox.hideAll();

### $ngBootbox.addLocale(String name, object values)

Allows the user to add a custom translation for each of the built-in command buttons. The values object should be in this format:

    {
        OK : '',
        CANCEL : '',
        CONFIRM : ''
    }

### $ngBootbox.removeLocale(String name)

Allows the user to remove a locale from the available locale settings.

### $ngBootbox.setLocale(String name)

Allows the user to select a locale rather than using setDefaults("locale", ...).
