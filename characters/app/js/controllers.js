'use strict';

/* Controllers */

angular.module('characters.controllers', []).
    controller('UserListCtrl', ['$scope', 'Users', function($scope, Users) {
        Users.get(function(data){
            $scope.users = data;
        });
    }])
    .controller('MageListCtrl', ['$scope', 'Mages', function($scope, Mages) {
        Mages.get(function(data){
            $scope.mages = data;
        });
    }
    ]);
