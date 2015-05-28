phonecatApp = angular.module "phonecatApp", []

phonecatApp.controller "PhoneListCtrl", 
		($scope)->
			$scope.phones = [
				name: "Nexus S",
				snippet: "Fast just got faster with Nexus S.",
				name: "Motorola XOOM™ with Wi-Fi",
				snippet: "The Next, Next Generation tablet.",
				name: "MOTOROLA XOOM™",
				snippet: "The Next, Next Generation tablet."
			]

console.log(
			{name:3, surname:{name:4,surname: 'u'}}
		)
