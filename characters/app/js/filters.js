'use strict';

/* Filters */

angular.module('characters.filters', []).filter('classy', function() {
  return function(text) {
    return String(text).replace(/ /mg, "-");
  };
});
