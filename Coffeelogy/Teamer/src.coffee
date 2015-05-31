###
	Teamer Class
###

#Check
if typeof window == "undefined"
	SideStr = "server"
else
	SideStr = "client"

#debug
console.log(
	"import Teamer \n",
	"Side is "+SideStr
)

#define
class exports.TeamerClass
  	
  	#constructor:
	TeamObject = {}
	TeamedParentVariable = null

	team:(TeamingKeyStr,TeamingValueVariable)=>

		#Debug
		console.log(
			[
				'TeamingKeyStr is '+TeamingKeyStr
				'TeamingValueVariable is '+TeamingValueVariable
			]
		)

		TeamingValueVariable.TeamedParentVariable = this

		#update
		TeamObject[TeamingKeyStr]=TeamingValueVariable 

		#Debug
		console.log(
			TeamObject
		)

		#return
		return this

