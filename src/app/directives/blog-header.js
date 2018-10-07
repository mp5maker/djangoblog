(function() {
    "use strict";

    angular.module('blog')
    .directive('blogHeader', function() {
        return  {
            restrict: "E",
            templateUrl: "/static/layouts/blog-header.html"
        }
    });
})(); 