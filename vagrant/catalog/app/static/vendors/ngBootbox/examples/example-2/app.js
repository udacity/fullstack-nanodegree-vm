define([
    'angular',
    'bootbox',
    'ngBootbox'
], function (angular, bootbox) {
    'use strict';

    var app = angular.module('app', [
        'ngBootbox'
    ]);

    app.controller('TestCtrl', function ($scope, $log, $ngBootbox) {

        $scope.actions = [];

        $scope.addAction = function (type, msg) {
            console.log(type + ': ' + msg);
            $scope.actions.push({
                msg: type + ': ' + msg
            });
        };

    });

    return app;
});
