angular-google-plus
==================

[![Build Status](http://img.shields.io/travis/mrzmyr/angular-google-plus.svg?style=flat)](https://travis-ci.org/mrzmyr/angular-google-plus) [![npm version](https://badge.fury.io/js/angular-google-plus.svg)](http://badge.fury.io/js/angular-google-plus) [![Bower version](https://badge.fury.io/bo/angular-google-plus.svg)](http://badge.fury.io/bo/angular-google-plus)

> A angular module which handles the login with the Google+ API

#### Demo

Try [this demo](http://plnkr.co/edit/jvHVtNedJoPcqRKg8OLz?p=preview). _Remind that there is no `API Key` and `Client ID` inserted_

#### Install

Install the angular module with bower or npm.

```
$ bower install angular-google-plus
```

```
$ npm install angular-google-plus
```

#### Usage

```js
var app = angular.module('app', ['googleplus']);

app.config(['GooglePlusProvider', function(GooglePlusProvider) {
     GooglePlusProvider.init({
        clientId: 'YOUR_CLIENT_ID',
        apiKey: 'YOUR_API_KEY'
     });
}]);

app.controller('AuthCtrl', ['$scope', 'GooglePlus', function ($scope, GooglePlus) {
    $scope.login = function () {
        GooglePlus.login().then(function (authResult) {
            console.log(authResult);

            GooglePlus.getUser().then(function (user) {
                console.log(user);
            });
        }, function (err) {
            console.log(err);
        });
    };
}]);
```

#### Credits

- Insperation from [jakemmarsh's gist](https://gist.github.com/jakemmarsh/5809963)
