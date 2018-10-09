(function() {
    "use strict";

    angular.module('blog')
    .directive('blogFooter', Ctrl);

    function Ctrl() {
        return {
            restrict: "E",
            templateUrl: "/static/layouts/blog-footer.html"
        }
    }
})();