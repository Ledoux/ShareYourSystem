console.log('ready');

window.addEventListener("load", function() {
  var Hello, React;
  console.log('ready');
  React = require('react');
  console.log(React);
  Hello = React.createClass({
    render: function() {
      return React.createElement("div", null, "Hello ", this.props.name);
    }
  });
  console.log(document.getElementById("example"));
  return React.render(React.createElement(Hello, {
    "name": "John"
  }), document.getElementById("example"));
});
