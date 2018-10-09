(function () {
    "use strict";

    var modules = [
        'ngAnimate',
        'ui.router',
    ];

    angular.module('blog', modules);
})();
(function () {
    "use strict";

    angular.module('blog')
        .controller('mainCtrl', ['$scope', '$window', 'apiHelper', Ctrl]);

    function Ctrl($scope, $window, apiHelper) {
        $scope.name = "Photon";
        $scope.user = {};
        $scope.errors = {};
        $scope.authorizedUser = false;
        $scope.token = "";

        var get = function () {
            apiHelper.currentUser().then(onSuccess).catch(onError);

            function onSuccess(response) {
                if (response) {
                    $scope.authorizedUser = true;
                }
            }

            function onError(response) {
                if (response) {
                    $scope.authorizedUser = false;
                }
            }
        }
        get();

        $scope.loginFormSubmit = function () {
            if (!_.isEmpty($scope.user)) {
                apiHelper.login($scope.user).then(onSuccess).catch(onError);
            } else {
                $scope.errors.loginError = "Unable to log in with provided credentials.";
            }
            function onSuccess(response) {
                if (response) {
                    $window.location.reload();
                }
            }

            function onError(response) {
                $scope.errors.loginError = response.data.non_field_errors[0];
            }
        }
    }
})();
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
(function () {
    "use strict";

    angular.module('blog')
    .factory('apiHelper', function ($http) {
        var localhost = "http://localhost:8000/";
        var routes = {
            "login"                        :  localhost + "api/v1/rest-auth/login/",
            "logout"                       :  localhost + "api/v1/rest-auth/logout/",
            "password_reset"               :  localhost + "api/v1/rest-auth/password/reset/",
            "password_reset_confirm"       :  localhost + "api/v1/rest-auth/password/reset/confirm/",
            "user"                         :  localhost + "api/v1/rest-auth/user/",
            "password_change"              :  localhost + "api/v1/rest-auth/password/change/",
            "users"                        :  localhost + "api/v1/users/",
            "posts"                        :  localhost + "api/v1/posts/",
            "current_user"                 :  localhost + "api/v1/current-user/",
        }
        return  {
            login: (data) => $http.post(routes.login, data), 
            logout: () => $http.get(routes.logout), 
            passwordReset: () => $http.get(routes.password_reset), 
            passwordResetConfirm: () => $http.get(routes.password_reset_confirm), 
            user: () => $http.get(routes.user), 
            passwordChange: () => $http.get(routes.password_change), 
            users: () => $http.get(routes.users), 
            posts: () => $http.get(routes.posts), 
            currentUser: () => $http.get(routes.current_user), 
        }
    })
})();

