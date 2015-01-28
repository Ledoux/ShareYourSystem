/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

subscribe

*/

//Debug
/*
console.log(
	'subscribe l 14 \n',
	'_.keys(CollectionsDictObject) is \n',
	_.keys(CollectionsDictObject)
)
*/

//map subscribe
_.map(
  _.keys(CollectionsDictObject),
  function(__CollectionStr)
  {
    Meteor.subscribe(__CollectionStr[0].toLowerCase()+__CollectionStr.slice(1))
  }
)

