###/#################/#
# Define a require 
# server or client side working
###/###

#init
SYS = {}

#Check
if typeof window!="undefined"

	#debug
	###
	console.log(
		"We are client side"
	)
	###

	#set
	SYS.SideStr = "client"

	#set
	exports = {}

	#alias
	run = (_ScriptStr,_BackFunction) ->
		require(
			[_ScriptStr],
			->
				#first extend
				_.extend(SYS,exports)

				#call
				_BackFunction()
		)

	

else

	#debug
	###
	console.log(
		"We are server side"
	)
	###

	#require
	SYS._ = require("underscore")

	#set
	SYS.SideStr = "server"

	run = (_ScriptStr,_BackFunction) ->
		
		#require
		ModuleObject = require(_ScriptStr)

		#debug
		###
		console.log(
			"ModuleObject is \n",
			ModuleObject
		)
		###

		#extend
		SYS._.extend(SYS,ModuleObject)

		#back call like...
		_BackFunction()

#debug
console.log(
	"************************\n"
	"Welcome to Coffeelogy \n",
	"We are " + SYS.SideStr + " side ! \n",
	#"require function is ",
	#require
)

#require
run(
	"./Teamer/src.js",
	->
		console.log(
			"HHHH\n",
			SYS.TeamerClass
		)
)
