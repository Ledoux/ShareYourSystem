###
	Manager Class
###

#require
Teamer = require('../Teamer/Teamer.js')

#define
class exports.ManagerClass extends Teamer.TeamerClass
  	
  	#constructor:
	ManagementObject = {}
	ManagedParentVariable = null

	manage:(ManagingKeyStr,ManagingValueVariable)=>

		#Debug
		console.log(
			[
				'ManagingKeyStr is '+ManagingKeyStr
				'ManagingValueVariable is '+ManagingValueVariable
			]
		)

		ManagingValueVariable.ManagedParentVariable = this

		#update
		ManagementObject[ManagingKeyStr]=ManagingValueVariable 

		#Debug
		console.log(
			ManagementObject
		)

		#return
		return this

