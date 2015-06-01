var SYS;

if (typeof window === 'undefined') {
  SYS = require("./Coffeelogy.js").SYS;
}

SYS.run(function() {
  return console.log(SYS.React);
}, "React", "./bower_components/react/react.min.js");
