(function() {
    "use strict";

    angular.module('blog')
    .directive('blogHeader', Ctrl);

    function Ctrl() {
        return {
            restrict: "E",
            templateUrl: "/static/layouts/blog-header.html"
        }
    }
})(); 