console.log('ready')
window.addEventListener "load",
	->
		console.log('ready')

		React = require('react')

		console.log React

		Hello = React.createClass 
			render: -> <div>Hello {this.props.name}</div>


		console.log document.getElementById("example")


		React.render(<Hello name="John" />, document.getElementById("example"));

