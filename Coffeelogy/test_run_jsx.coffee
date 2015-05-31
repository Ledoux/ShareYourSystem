
if typeof window=='undefined'
	SYS = require("./Coffeelogy.js").SYS

SYS.run ->
			#Debug
			console.log(
				SYS.React
			)

			#
			Hello = SYS.createClass 
				render: ->
					<div>
						SALUT
					</div>
		,
		"React",
		"./bower_components/react/react.min.js"
