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