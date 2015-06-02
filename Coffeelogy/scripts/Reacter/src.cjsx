
window.addEventListener "load",
	->
		#console
		console.log('ready for coffee-react ?')

		#require #NB it is important to call it as Reat and not react
		React = require('react')

		#test
		console.log React

		#create
		Hello = React.createClass 
			render: -> <div>Hello {this.props.name}</div>

		#test
		console.log document.getElementById("example")

		#render
		React.render(<Hello name="John" />, document.getElementById("example"));