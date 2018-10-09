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

