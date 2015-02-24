'use strict';

/* Services */


// Demonstrate how to register services
// In this case it is a simple value service.
angular.module('characters.services', [])
  .factory('Users', ['$http', function($http){
    return{
      get: function(callback){
          $http.get('api/users').success(function(data) {
          // prepare data here
          callback(data);
          console.log(data)
        });
      }
    };
  }]);
