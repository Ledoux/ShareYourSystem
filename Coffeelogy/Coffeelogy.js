// Generated by CoffeeScript 1.9.2

/*/ */

/*/ */
var SYS, exports, run;

SYS = {};

if (typeof window !== "undefined") {

  /*
  	console.log(
  		"We are client side"
  	)
   */
  SYS.SideStr = "client";
  exports = {};
  run = function(_ScriptStr, _BackFunction) {
    return require([_ScriptStr], function() {
      _.extend(SYS, exports);
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
  run = function(_ScriptStr, _BackFunction) {
    var ModuleObject;
    ModuleObject = require(_ScriptStr);

    /*
    		console.log(
    			"ModuleObject is \n",
    			ModuleObject
    		)
     */
    SYS._.extend(SYS, ModuleObject);
    return _BackFunction();
  };
}

console.log("************************\n", "Welcome to Coffeelogy \n", "We are " + SYS.SideStr + " side ! \n");

run("./Teamer/src.js", function() {
  return console.log("HHHH\n", SYS.TeamerClass);
});
