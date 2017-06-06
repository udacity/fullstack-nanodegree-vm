requirejs.config({
  baseUrl: "/static",
  paths: {
    'jquery': "vendors/jquery/dist/jquery",
    'angular': "vendors/angular/angular",
    'angular-route': "vendors/angular-route/angular-route",
    'angular-resource': "vendors/angular-resource/angular-resource",
    'lodash': "vendors/lodash/lodash",
    'bootbox': "vendors/bootbox.js/bootbox",
    'ngBootbox': "vendors/ngBootbox/ngBootbox",
    'twitter': "vendors/bootstrap/dist/js/bootstrap.min",
    'ui_bootstrap': "vendors/angular-bootstrap/ui-bootstrap-tpls",
    'ngAnimate': "vendors/ngAnimate/js/angular-animate.min",
    'ngModal': "vendors/ngModal/dist/ng-modal",
    'bootstrapSelect': "vendors/bootstrap-select/dist/js/bootstrap-select",
    'googleplus': "vendors/angular-google-plus/dist/angular-google-plus",
    'googlePlusSignin': "vendors/angular-directive.g-signin/google-plus-signin",
    'Facebook': "vendors/angular-easyfb/src/angular-easyfb",
    app: "js/app",
    SignoutController: "js/controllers/signout-controller",
    SignoutDirective: "js/directives/signout-directive",
    SigninController: "js/controllers/signin-controller",
    SigninDirective: "js/directives/signin-directive",
    LoadDataService: "js/services/load_data-service",
    DataBroadcastService: "js/services/data_broadcast-service",
    PostDataService: "js/services/post_data-service",
    SessionInjector: "js/services/session_injector-service",
    AuthenticationService: "js/services/authentication-service",
    CategoriesController: "js/controllers/categories-controller",
    ItemsController: "js/controllers/items-controller",
    ItemController: "js/controllers/item-controller",
    AddNewItemController: "js/controllers/add_new_item-controller",
    DeleteItemController: "js/controllers/delete_item-controller",
    PostItemController: "js/controllers/post_item-controller",
    PostModalController: "js/controllers/post_modal-controller",
    ProfileController: "js/controllers/profile-controller",
    CategoryPanelDirective: "js/directives/category_panel-directive",
    ItemsPanelDirective: "js/directives/items_panel-directive",
    ItemDirective: "js/directives/item-directive",
    PostItemDirective: "js/directives/post_item-directive",
    AddNewItemDirective: "js/directives/add_new_item-directive",
    ProfileDirective: "js/directives/profile-directive"
  },
  shim: {
    jquery: {
      exports: '$'
    },
    lodash: {
      exports: '_'
    },
    ngResource: {
      deps: ['angular'],
      exports: 'angular'
    },
    'angular-route': {
      deps: ['angular'],
      exports: 'angular'
    },
    angular: {
      exports: 'angular'
    },
    'twitter': {
      deps: [
        'jquery'
      ]
    },
    'bootstrapSelect': {
      exports: 'bootstrapSelect'
    },
    ngModal: {
      exports: 'ngModal'
    },
    Facebook: {
      deps: [
        'angular'
      ],
      exports: 'ezfb'
    },
    'ngBootbox': {
      deps: [
        'jquery',
        'angular',
        'twitter',
        'bootbox'
      ]
    },
    'bootbox': {
      deps: [
        'angular'
      ],
      exports: 'bootbox'
    },
    'ngAnimate': {
      deps: [
        'jquery',
        'angular'
      ],
      exports: 'ngAnimate'
    },
    'ui_bootstrap': {
      deps: [
        'angular',
        'ngAnimate'
      ]
    },
    'googleplus': {
      deps: [
        'angular'
      ]
    },
    'googlePlusSignin': {
      deps: [
        'angular'
      ]
    }
  },

});

require(['app'],
  function(app) {
    app.init();
  },
  function(error) {
    console.log('Custom ERROR handler', error);
    var failedId = error.requireModules && error.requireModules[0];
    console.log(failedId);
    console.log(error.message);
  });
