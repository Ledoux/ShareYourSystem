###
	Manager Class
###

#debug
console.log(
	"import Manager \n"
)

#require
Teamer = require('../Teamer/src.js')

#define
class ManagerClass extends Teamer.TeamerClass
  	
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

#Check
if GLOBAL.SideStr == 'server'

	#export
	exports.ManagerClass = ManagerClass