
#import
Teamer = require('./Teamer.js')

#define
FirstTeamer = new Teamer.TeamerClass()
  .team("Children", new Teamer.TeamerClass())

#console
console.log(FirstTeamer);
