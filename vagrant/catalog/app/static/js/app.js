define([
    'angular',
    'jquery',
    'twitter',
    'ngModal',
    'ngAnimate',
    'ui_bootstrap',
    'bootstrapSelect',
    'bootbox',
    'ngBootbox',
    'googleplus',
    'googlePlusSignin',
    'Facebook',
    'LoadDataService',
    'DataBroadcastService',
    'PostDataService',
    'SessionInjector',
    'AuthenticationService',
    'SigninController',
    'SignoutController',
    'SigninDirective',
    'SignoutDirective',
    'CategoriesController',
    'ItemsController',
    'ItemController',
    'DeleteItemController',
    'PostItemController',
    'PostModalController',
    'AddNewItemController',
    'ProfileController',
    'CategoryPanelDirective',
    'ItemsPanelDirective',
    'ItemDirective',
    'PostItemDirective',
    'AddNewItemDirective',
    'ProfileDirective'
  ],
  function(angular,
    jquery,
    twitter,
    ngModal,
    ngAnimate,
    ui_bootstrap,
    bootstrapSelect,
    bootbox,
    ngBootbox,
    googleplus,
    googlePlusSignin,
    Facebook,
    LoadDataService,
    DataBroadcastService,
    PostDataService,
    SessionInjector,
    AuthenticationService,
    SigninController,
    SignoutController,
    SigninDirective,
    SignoutDirective,
    CategoriesController,
    ItemsController,
    ItemController,
    DeleteItemController,
    PostItemController,
    PostModalController,
    AddNewItemController,
    ProfileController,
    CategoryPanelDirective,
    ItemsPanelDirective,
    ItemDirective,
    PostItemDirective,
    AddNewItemDirective,
    ProfileDirective) {
    'use strict';

    var app = angular.module('CatalogApp', ['ui.bootstrap', 'googleplus','directive.g+signin', 'ezfb']);

    app.factory('LoadDataService', LoadDataService);
    app.factory('DataBroadcastService', DataBroadcastService);
    app.factory('PostDataService', PostDataService);
    app.factory('SessionInjector', SessionInjector);
    app.factory('AuthenticationService', AuthenticationService);
    app.controller('SigninController', SigninController);
    app.controller('SignoutController', SignoutController);
    app.controller('CategoriesController', CategoriesController);
    app.controller('ItemsController', ItemsController);
    app.controller('ItemController', ItemController);
    app.controller('DeleteItemController', DeleteItemController);
    app.controller('PostItemController', PostItemController);
    app.controller('PostModalController', PostModalController);
    app.controller('AddNewItemController', AddNewItemController);
    app.controller('ProfileController', ProfileController);
    app.directive('signin', SigninDirective);
    app.directive('signout', SignoutDirective);
    app.directive('categorypanel', CategoryPanelDirective);
    app.directive('itemspanel', ItemsPanelDirective);
    app.directive('showitem', ItemDirective);
    app.directive('postitem', PostItemDirective);
    app.directive('additem', AddNewItemDirective);
    app.directive('profile', ProfileDirective)

    app.config(['GooglePlusProvider', function(GooglePlusProvider) {
      GooglePlusProvider.init({
        clientId: '600120679756-8md2l1b36ha6qa349u2uvhl1nrejs8k9.apps.googleusercontent.com',
        // apiKey: 'Ev4gloAsQynGg0Puo3nlmY_r'
        apiKey: 'AIzaSyA3UC3p1jK-zxHUktNBlI46RU1aWXXMez8',
        scope: 'https://www.googleapis.com/auth/plus.login https://www.googleapis.com/auth/userinfo.email',
      });
    }]);

    app.config(['$httpProvider', function($httpProvider) {
      $httpProvider.interceptors.push('SessionInjector');
    }]);

    app.config(['ezfbProvider', function(ezfbProvider) {
      ezfbProvider.setInitParams(
        {
          appId: '521603404683305',
          version: 'v2.5',
          xfbml: true,
        });
    }]);


    app.init = function() {
      angular.bootstrap(document, ['CatalogApp']);
    };

    return app;
  });
