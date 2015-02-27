'use strict';


// Declare app level module which depends on filters, and services
angular.module('characters', ['djangular', 'ui.router', 'djangular.csrf',
	'characters.filters', 'characters.services', 'characters.directives', 'characters.controllers'])
	.config(['$stateProvider','DjangoProperties', '$urlRouterProvider',
	function($stateProvider, DjangoProperties, $urlRouterProvider, UserListCtrl) {

	$urlRouterProvider.otherwise("/users");

  // Now set up the states
	  $stateProvider
	    .state('users', {
	      url: "/users",
	      templateUrl: DjangoProperties.STATIC_URL + "partials/users.html"
	    })
	    .state('users.list', {
	      url: "/list",
	      templateUrl: DjangoProperties.STATIC_URL +  "partials/users.list.html",
	      controller: 'UserListCtrl'
	    })
	    .state('users.detail', {
	      url: "/detail/{userID:int}",
	      templateUrl: DjangoProperties.STATIC_URL +  "partials/users.detail.html",
	      controller: 'UserDetailCtrl'
	    })
	    .state('mages', {
	      url: "/mages",
	      templateUrl: DjangoProperties.STATIC_URL + "partials/mages.html"
	    })
	    .state('mages.list', {
	      url: "/list",
	      templateUrl: DjangoProperties.STATIC_URL + "partials/mages.list.html",
	      controller: 'MageCtrl'
	    })
	    .state('mages.detail', {
		     url: "/detail/{mageID:int}",
		     views:{
		      	"": {
		      		templateUrl: DjangoProperties.STATIC_URL +  "partials/mages.detail.html",
	      			controller: 'MageCtrl',
		      	},
		      	"characteristics@mages.detail": {
		      		templateUrl:  DjangoProperties.STATIC_URL + "common_partials/characteristics.html"
		      	}, 
		      	"attributes@mages.detail": {
		      		templateUrl: DjangoProperties.STATIC_URL +  "common_partials/attributes.html"
		      	}, 
		  		"skills@mages.detail": {
		  			templateUrl: DjangoProperties.STATIC_URL +  "common_partials/skills.html"
		  		}, 
		  		"spells@mages.detail": {
		  			templateUrl: DjangoProperties.STATIC_URL + "partials/spells.html"
		  		}, 
		  	}
	    });
	  }]);
