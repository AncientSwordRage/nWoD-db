'use strict';

/* Controllers */

angular.module('characters.controllers', []).
    controller('UserListCtrl', ['$scope', 'Users', function($scope, Users) {
        Users.get(function(data){
            $scope.users = data;
        });
    }
    ])
    .controller('MyCtrl2', [function() {

    }]);
