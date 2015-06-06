(function e(t,n,r){
	function s(o,u){
		if(!n[o]){
			if(!t[o]){
				var a=typeof require=="function"&&require;
				if(!u&&a)return a(o,!0);
				if(i)return i(o,!0);
				var f=new Error("Cannot find module '"+o+"'");
				throw f.code="MODULE_NOT_FOUND",f}
				var l=n[o]={exports:{}};
				t[o][0].call(l.exports,
					function(e){var n=t[o][1][e];return s(n?n:e)},
					l,l.exports,e,t,n,r)}
				return n[o].exports}
				var i=typeof require=="function"&&require;
				for(var o=0;o<r.length;o++)s(r[o]);return s})
(
	{1:[function(require,module,exports){
//
console.log('Hey in b')
},{}],2:[function(require,module,exports){
//
console.log('Hey in a')

},{}],3:[function(require,module,exports){

//start
require('./a/a.js')
require('./b/b.js')

},{"./a/a.js":1,"./b/b.js":2}]},{},[3])

//# sourceMappingURL=data:application/json;charset:utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi4uLy4uLy4uLy4uLy4uLy4uL3Vzci9sb2NhbC9saWIvbm9kZV9tb2R1bGVzL2Jyb3dzZXJpZnkvbm9kZV9tb2R1bGVzL2Jyb3dzZXItcGFjay9fcHJlbHVkZS5qcyIsImEvYS5qcyIsImIvYi5qcyIsIm1haW4uanMiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7QUNBQTtBQUNBOztBQ0RBO0FBQ0E7QUFDQTtBQUNBOztBQ0hBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EiLCJmaWxlIjoiZ2VuZXJhdGVkLmpzIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXNDb250ZW50IjpbIihmdW5jdGlvbiBlKHQsbixyKXtmdW5jdGlvbiBzKG8sdSl7aWYoIW5bb10pe2lmKCF0W29dKXt2YXIgYT10eXBlb2YgcmVxdWlyZT09XCJmdW5jdGlvblwiJiZyZXF1aXJlO2lmKCF1JiZhKXJldHVybiBhKG8sITApO2lmKGkpcmV0dXJuIGkobywhMCk7dmFyIGY9bmV3IEVycm9yKFwiQ2Fubm90IGZpbmQgbW9kdWxlICdcIitvK1wiJ1wiKTt0aHJvdyBmLmNvZGU9XCJNT0RVTEVfTk9UX0ZPVU5EXCIsZn12YXIgbD1uW29dPXtleHBvcnRzOnt9fTt0W29dWzBdLmNhbGwobC5leHBvcnRzLGZ1bmN0aW9uKGUpe3ZhciBuPXRbb11bMV1bZV07cmV0dXJuIHMobj9uOmUpfSxsLGwuZXhwb3J0cyxlLHQsbixyKX1yZXR1cm4gbltvXS5leHBvcnRzfXZhciBpPXR5cGVvZiByZXF1aXJlPT1cImZ1bmN0aW9uXCImJnJlcXVpcmU7Zm9yKHZhciBvPTA7bzxyLmxlbmd0aDtvKyspcyhyW29dKTtyZXR1cm4gc30pIiwiLy9cbmNvbnNvbGUubG9nKCdIZXkgaW4gYicpIiwiLy9cbmNvbnNvbGUubG9nKCdIZXkgaW4gYScpXG5cbiIsIi8vc3RhcnRcbnJlcXVpcmUoJy4vYS9hLmpzJylcbnJlcXVpcmUoJy4vYi9iLmpzJylcblxuIl19
