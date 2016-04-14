/**
 * Created by shahar on 14/04/16.
 */
angular.module('dashboard', [])
    .controller('main', ['$scope', '$timeout', '$http', function ($scope, $timeout, $http) {
        $scope.teams = [];
        $scope.users = [];

        $scope.update = function () {
            $http({
                method: 'GET',
                url: '/api/getTeams'
            }).then(function successCallback(response) {
                $scope.teams = response.data;
            }, function errorCallback(response) {
            });
            $http({
                method: 'GET',
                url: '/api/getUsers'
            }).then(function successCallback(response) {
                $scope.users = response.data;
            }, function errorCallback(response) {
            });
            $timeout($scope.update,1000);
        };

        $scope.update();
    }]);