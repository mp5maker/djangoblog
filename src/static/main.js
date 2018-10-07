(function () {
    "use strict";

    var modules = [
        'ngAnimate',
        'ui.router',
    ];

    angular.module('blog', modules);
})();
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
(function() {
    "use strict";
    
    angular.module('blog')
    .controller('mainCtrl', function($scope){
        $scope.name = "Photon"
    });
})();