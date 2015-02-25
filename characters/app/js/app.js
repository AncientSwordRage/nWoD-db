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
	    .state('mages', {
	      url: "/mages",
	      templateUrl: DjangoProperties.STATIC_URL + "partials/mages.html"
	    })
	    .state('mages.list', {
	      url: "/list",
	      templateUrl: DjangoProperties.STATIC_URL + "partials/mages.list.html",
	      controller: 'MageListCtrl'
	    })
	    });
	  }]);
