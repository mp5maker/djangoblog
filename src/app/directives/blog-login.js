(function() {
    "use strict";

    angular.module('blog')
    .directive('blogLogin', Ctrl);

    function Ctrl () {
        return {
            restrict: "E",
            templateUrl: "/static/layouts/blog-login.html"
        }
    }
})();