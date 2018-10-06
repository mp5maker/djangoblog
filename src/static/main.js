(function() {
    'use strict';

    var modules = [
        'ngAnimate',
        'ui.router'        
    ];

    angular.module('blog', modules);
})();
(function() {
    "use strict";
    
    angular.module('blog')
    .controller('mainCtrl', function($scope){
        $scope.name = "Photon"
    });
})();