
#import
Manager = require('./Manager.js')

#define
FirstManager = new Manager.ManagerClass()
  .manage("Child", new Manager.ManagerClass())

#console
console.log(FirstManager);
