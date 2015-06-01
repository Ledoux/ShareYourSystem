
/*/ */

/*/ */
var SYS, exports;

SYS = {};

if (typeof window !== "undefined") {

  /*
  	console.log(
  		"We are client side"
  	)
   */
  SYS.SideStr = "client";
  exports = {};
  SYS.run = function(_BackFunction, _KeyStr, _PathStr) {

    /*
    		require(
    			[__PathStr],
    			->
    				#first extend
    				SYS[__KeyStr]=exports
    
    				#call
    				_BackFunction()
    		)
     */
    console.log(["_BackFunction is \n", _BackFunction, "_KeyStr is \n", _KeyStr, "_PathStr is \n", _PathStr]);
    return $.getScript(_PathStr, function() {

      /*
      				console.log(
      					[
      						"l.67 Coffeelogy\n"
      						"Call back \n",
      						"__BackFunction is \n"
      						__BackFunction,
      						"__KeyStr is \n"
      						__KeyStr,
      						"__PathStr is \n"
      						__PathStr,
      					]
      				)
       */
      SYS[_KeyStr] = eval(_KeyStr);
      return _BackFunction();
    });
  };
} else {

  /*
  	console.log(
  		"We are server side"
  	)
   */
  SYS._ = require("underscore");
  SYS.SideStr = "server";
  SYS.run = function(_BackFunction, _KeyStr, _PathStr) {

    /*
    		console.log(
    			[
    				"_BackFunction is \n"
    				_BackFunction,
    				"_KeyStr is \n"
    				_KeyStr,
    				"_PathStr is \n"
    				_PathStr,
    			]
    		)
     */
    var ModuleObject;
    ModuleObject = require(_PathStr);

    /*
    		console.log(
    			"ModuleObject is \n",
    			ModuleObject
    		)
     */
    SYS[_KeyStr] = ModuleObject;
    return _BackFunction();
  };
}

exports.SYS = SYS;

console.log("************************\n", "Welcome to Coffeelogy \n", "We are " + SYS.SideStr + " side ! \n");
