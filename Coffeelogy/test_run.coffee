
if typeof window=='undefined'
	SYS = require("Coffeelogy.js").SYS

SYS.run ->
			#Debug
			console.log(
				SYS.React
			)

			#
			Hello = SYS.createClass 
				render: ->
					React.createElement("div", null, """
\t\t\t\t\t\tSALUT
""")
		,
		"React",
		"bower_components/react/react.min.js"
