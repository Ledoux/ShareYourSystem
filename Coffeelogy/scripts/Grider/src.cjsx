
window.addEventListener "load",
	->
		#console
		console.log 'ready for coder ?'

		###
			Import CodeMirror
		###

		#require
		CodeMirror = require('codemirror')
		base64 = require('hi-base64')

		#console
		#console.log "CodeMirror is ",CodeMirror
		#console.log "base64 is ",base64

		###
			Install iframe
		###

		#result
		resultFrame = document.getElementById('result')

		#Debug
		console.log(["resultFrame is ",resultFrame])
		console.log resultFrame.contentDocument.head

		#append
		#resultFrame.contentDocument.head.innerHTML+='<script type="text/javascript" src="../../assets/iframe_vendor.js"></script>'
		#resultFrame.contentDocument.head.innerHTML+='<script type="text/javascript" src="../assets/iframe_test.js"></script>'
		
		#add the iframe_vendor
		#resultFrame.getElementById('head')
		#$("head").append('<script type="text/javascript" src="' + script + '"></script>');

		###
			Install editor
		###

		#get
		editorTextArea = document.getElementById('editor') 
		
		#Debug
		#console.log "editorTextArea is ", editorTextArea

		#set
		scriptObject = {
			lineNumbers: true,
			mode:  "javascript"
		}

		#instane
		scriptCodeMirror = CodeMirror.fromTextArea(editorTextArea, scriptObject)

		#set
		langStr = "js"
		#langStr = "coffee"
		#langStr = "cjsx"

		#init
		convertFunction = null

		#Check
		if langStr=="js"

			#console
			codeStr = "//Debug\n"
			codeStr +="console.log('ready for js ?')\n"
			codeStr +="\n//Define\n"
			codeStr +="function myFunc(){return 100;};\n"
			codeStr +="\n//test require\n"
			codeStr +="lodash=require('lodash')\n"
			codeStr +="\n//return\n"
			codeStr +="myFunc()\n"

			#alias
			convertFunction = eval

		else if langStr=="coffee"

			#console
			codeStr = "#Debug\n"
			codeStr +="console.log('ready for coffee ?')\n"
			codeStr +="\n#Define\n"
			codeStr +="myFunc= ()->return 100"
			codeStr +="\nreturn myFunc()"
			codeStr +="\n#test require\n"
			codeStr +="lodash = require 'lodash'\n"
			codeStr +="\n#Debug\n"
			codeStr +="console.log lodash\n"
			
			#require
			coffeeify = require('coffee-script')

			#set
			convertFunction = (string, options) -> 

				#Debug
				console.log("convert coffee, string is "+string)

				#get
				transformStr = coffeeify.compile(string)

				#Debug
				console.log('transformStr is : \n'+transformStr)

				#return 
				return eval(transformStr)

		else if langStr=="cjsx"

			#require
			cjsxfy = require('coffee-react-transform')
			coffeeify = require('coffee-script')

			#Debug
			console.log("cjsxfy is "+cjsxfy)

			#set
			convertFunction = (string, options) -> 

				#Debug
				console.log("convert cjsx, string is "+string)

				#get
				transformStr = coffeeify.compile(cjsxfy(string, options))

				#Debug
				console.log('transformStr is : \n'+transformStr)

				#return 
				return eval(transformStr)

			###
			#require
			#fs = require('browserify-fs')
			fs = require('brfs')

			#Debug
			console.log "fs is "+fs
			#console.log "fs.readFileSync is "+ fs.readFileSync

			#read
			codeStr = fs.readFileSync(
							'../Reacter/src.cjsx'
						)
			###
			
			#set
			codeStr = "#Debug\n"
			codeStr+= "console.log(\"ready for coffee-react ?\")\n"
			codeStr+="\n#require #NB it is important to call it as Reat and not react\n"
			codeStr+="React = require('react')\n"
			codeStr+="\n#test\n"
			codeStr+="console.log React\n"
			codeStr+="\n#create"
			codeStr+="Hello = React.createClass\n "
			codeStr+="\t render: -> <div>Hello {this.props.name}</div>\n"
			codeStr+="\n#test\n"
			codeStr+="console.log document.getElementById('example')\n"
			codeStr+="\n#render\n"
			codeStr+="React.render(<Hello name='John' />, document.getElementById('example'));\n"

			#Debug
			#console.log("codeStr is "+codeStr)

		#set
		scriptCodeMirror.setValue(codeStr)

		#console
		#console.log "In the editor :"+scriptCodeMirror.getValue()

		###
			Define submit
		###

		#get
		runButton = document.getElementById('run')

		#Debug
		#console.log("runButton is "+runButton)

		#define
		run = () ->

			#save
			scriptCodeMirror.save()

			#Debug
			scriptStr = editorTextArea.value

			#Debug
			#console.log "scriptStr is : \n'" + scriptStr + "' " 
			console.log "convertFunction is "+convertFunction

			#eval
			stdOutStr = String(convertFunction(editorTextArea.value))

			#Debug
			console.log("stdOutStr is :\n' " + stdOutStr + "' ")

			#get
			sourceStr = base64.encode(stdOutStr)

			#Debug
			#console.log("sourceStr is "+sourceStr)
			console.log resultFrame.contentDocument.body

			#set
			#resultFrame.src = "data:text/html;charset=utf-8;base64," + sourceStr
			resultFrame.contentDocument.body.innerHTML+="<br> >"+stdOutStr

		#Debug
		#console.log "run is "+run

		#run
		#run()

		#console
		#console.log "runButton is ",runButton

		#set
		runButton.addEventListener("click",run)

