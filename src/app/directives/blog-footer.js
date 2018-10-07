(function() {
    "use strict";

    angular.module('blog')
    .directive('blogFooter', function() {
        return {
            restrict: "E",
            templateUrl: "/static/layouts/blog-footer.html"
        }
    })
})();