
window.addEventListener "load",
	->
		#console
		console.log 'ready for coder ?'

		###
			Import CodeMirror
		###

		#require
		CodeMirror = require '../../node_modules/codemirror/lib/codemirror.js'
		$ = require 'jquery'

		#console
		console.log "CodeMirror is ",CodeMirror
		#console.log "$ is ",$

		###
			Install interface
		###

		#get
		editorTextArea = document.getElementById('editor') 
		resultFrame = document.getElementById('result')

		#Debug
		console.log "editorTextArea is ", editorTextArea

		#set
		scriptObject = {
			lineNumbers: true,
			value: "function myScript(){return 100;}\n",
			mode:  "javascript"
		}

		#instane
		#scriptCodeMirror = CodeMirror.fromTextArea(editorTextArea, scriptObject)
		scriptCodeMirror = CodeMirror editorTextArea, scriptObject

		#console
		console.log "scriptCodeMirror is ",scriptCodeMirror

		#get
		"runButton is "+runButton = document.getElementById 'run'

		#console
		console.log "runButton is ",runButton

		###
			Define submit
		###

		#define
		run = () ->
			scriptCodeMirror.save()
			resultFrame.src = "data:text/html;charset=utf-8;base64," + $.base64.encode(scriptCodeMirror.value)
