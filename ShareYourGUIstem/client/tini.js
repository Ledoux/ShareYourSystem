/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

tini

*/

//End to set up the abstractions
_.map(
    AbstractionsDictObject,
    function(__Abstraction)
    {
      //Debug
      /*
      console.log(
        'l 74 Interface',
        '__Abstraction is \n',
        __Abstraction
      )
      */
      
      //tini
      __Abstraction.tini()
    }
  )

Bars=new Mongo.Collection('bars')