
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
			Install interface
		###

		#get
		editorTextArea = document.getElementById('editor') 
		resultFrame = document.getElementById('result')

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
		jsScript = "function myScript(){return 100;};\nmyScript()\n"

		###
		#require
		#fs = require('browserify-fs')
		fs = require('brfs')

		#Debug
		console.log "fs is "+fs
		#console.log "fs.readFileSync is "+ fs.readFileSync

		#read
		cjsxScript = fs.readFileSync(
						'../Reacter/src.cjsx'
					)
		###
		
		#set
		cjsxScript="->\n"
		cjsxScript+="\t#console\n"
		cjsxScript+="\tconsole.log('ready for coffee-react ?')\n"
		cjsxScript+="\n\t#require #NB it is important to call it as Reat and not react\n"
		cjsxScript+="\tReact = require('react')\n"
		cjsxScript+="\n\t#test\n"
		cjsxScript+="\tconsole.log React\n"
		cjsxScript+="\n\t#create"
		cjsxScript+="\tHello = React.createClass\n "
		cjsxScript+="\t\t render: -> <div>Hello {this.props.name}</div>\n"
		cjsxScript+="\n\t#test\n"
		cjsxScript+="\tconsole.log document.getElementById('example')\n"
		cjsxScript+="\n\t#render\n"
		cjsxScript+="\tReact.render(<Hello name='John' />, document.getElementById('example'));\n"
		cjsxScript+="\n\t#put some value already\n"
		cjsxScript+="\tscriptCodeMirror.setValue(jsScript)"

		#Debug
		console.log("cjsxScript is "+cjsxScript)

		#set
		scriptCodeMirror.setValue(cjsxScript)

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
			console.log "scriptStr is : \n'" + scriptStr + "' " 

			#eval
			stdOutStr = String(eval(editorTextArea.value))

			#Debug
			console.log "stdOutStr is :\n' " + stdOutStr + "' "

			#get
			sourceStr = base64.encode(stdOutStr)

			#Debug
			#console.log("sourceStr is "+sourceStr)

			#set
			resultFrame.src = "data:text/html;charset=utf-8;base64," + sourceStr

		#Debug
		#console.log "run is "+run

		#run
		run()

		#console
		#console.log "runButton is ",runButton

		#set
		runButton.addEventListener("click",run)

