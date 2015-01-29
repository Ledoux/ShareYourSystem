/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

data 

*/

InstancesDictObject={}
ReactVarsDictObject={}

InstanceClass = function(_UpdateDictObject)
{
    //Define
    var LocalInstance=this

    //update
    _.extend(LocalInstance,_UpdateDictObject)

    //Debug
    /*
    console.log(
        'InstanceClass init l 22 \n',
        'LocalInstance is \n',
        LocalInstance
    )
    */

    //
    LocalInstance.ChildInstancesDictsObject={}

}

InstanceClass.prototype.globalify=function()
{

    //Define
    var LocalInstance=this

    //Debug
    /*
    console.log(
        'globalify l 135 \n',
    )
    */

    //Put in the InstancesDictObject Dict 
    InstancesDictObject[
        LocalInstance.getData('NameStr')
    ]=LocalInstance

    //
    /*
    if(ReactVarsDictObject[
        LocalInstance.Abstraction.CollectionStr
    ]==undefined)
    {
        //init
        ReactVarsDictObject[
            LocalInstance.Abstraction.CollectionStr
        ]=new ReactVar()
    }
    */
}

InstanceClass.prototype.findParent = function()
{
    //Define
    var LocalInstance=this

    //Debug
    /*
    console.log(
        'instance findParent l 76 \n',
        'LocalInstance is \n',
        LocalInstance
    )
    */

    //First look at an already possible ParentIdStr given
    if (LocalInstance.ParentIdStr!=undefined)
    {
        //get
        LocalInstance.ParentInstance=InstancesDictObject[LocalInstance.ParentIdStr]

    }
    else if(LocalInstance.Abstraction.ParentAbstraction!=undefined)
    {

        //Debug
        /*
        console.log(
            'abstraction added parent find l 194\n',
            'LocalInstance.ParentNameStr is \n',
            LocalInstance.ParentNameStr,
            '\n',
            'LocalInstance.Abstraction.ParentAbstraction is \n',
            LocalInstance.Abstraction.ParentAbstraction,
            '\n',
            //'LocalInstance.Abstraction.ParentAbstraction.Collection.find().fetch() is \n',
            //LocalInstance.Abstraction.ParentAbstraction.Collection.find().fetch()
        )
        */

        //find
        var ParentFind=LocalInstance.Abstraction.ParentAbstraction.Collection.find(
                {
                    'NameStr':LocalInstance.ParentNameStr
                }
            )

        //Debug
        /*
        console.log(
            'abstraction added parent find l 201\n',
            'ParentFind.fetch() is \n',
            ParentFind.fetch()
        )
        */

        var ParentObjectsArray=ParentFind.fetch()

        if(_.size(ParentObjectsArray)==1)
        {
            //get
            LocalInstance.ParentInstance=InstancesDictObject[
                    ParentObjectsArray[0]._id
                ]
        }
    }

    //LocalInstance.Abstraction.InstancesDictObject[LocalInstance.PathStr]=LocalInstance

    //Debug
    /*
    console.log(
        'abstraction findParent l 128 \n',
        'LocalInstance.NameStr is \n',
        LocalInstance.NameStr,
        '\n',
        'LocalInstance.ParentInstance is \n',
        LocalInstance.ParentInstance
    )
    */
}

InstanceClass.prototype.findChildren = function()
{
    //Define
    var LocalInstance=this

    //Debug
    /*
    console.log(
        'instance findChildren l 136 \n',
        'LocalInstance is \n',
        LocalInstance
    )  
    */

    //map
    _.map(
        LocalInstance.Abstraction.ChildAbstractionsArray,
        function(__ChildAbstraction)
        {

            //Debug
            /*
            console.log(
                'instance l 630\n',
                'LocalInstance.Abstraction is \n',
                LocalInstance.Abstraction,
                '\n',
                '\n',
                '__ChildAbstraction is \n',
                __ChildAbstraction,
                '\n',
                'LocalInstance.NameStr is \n',
                LocalInstance.NameStr
            )
            */

            //set
            /*
            if(LocalInstance.ChildInstancesDictsObject[
                __ChildAbstraction.CollectionStr
            ]==undefined)
            {
                LocalInstance.ChildInstancesDictsObject[
                    __ChildAbstraction.CollectionStr
                ]={}
            }
            */

            //find
            var Find=__ChildAbstraction.Collection.find(
                {
                    'ParentNameStr':LocalInstance.NameStr
                }
            )

            //Debug
            /*
            console.log(
                'instance in findChildren l 191\n',
                'Find.fetch() is \n',
                Find.fetch()
            )
            */

            //Define
            var PossibleChildObjectsArray=Find.fetch()

            //filter the ones that have already a parent 
            var PossibleAbandonnedChildObjectsArray=_.filter(
                    PossibleChildObjectsArray,
                    function(__PossibleChildObject)
                    {

                        //Check
                        if(__PossibleChildObject.ParentIdStr==LocalInstance._id)
                        {
                            return true
                        }
                        else if (__PossibleChildObject.ParentIdStr==undefined || __PossibleChildObject.ParentIdStr == "")
                        {
                            if(__PossibleChildObject.ParentInstance==undefined)
                            {
                                return true
                            }
                        }

                        //return false either
                        return false
                    }
            )

            //Debug
            /*
            console.log(
                'instance in findChildren map l 191\n',
                'LocalInstance.NameStr is \n',
                LocalInstance.NameStr,
                '\n',
                'PossibleAbandonnedChildObjectsArray is \n',
                PossibleAbandonnedChildObjectsArray
            )
            */

            //objectify the possible childs in order to remove the redundant children with the same NameStr
            var ChildObjectsDictObject=_.object(
                _.map(
                    PossibleAbandonnedChildObjectsArray,
                    function(__PossibleAbandonnedChildObject)
                    {
                        return [
                                    __PossibleAbandonnedChildObject.NameStr,
                                    __PossibleAbandonnedChildObject
                                ]
                    }
                )
            )


            //Debug
            console.log(
                'instance in findChildren map l 235\n',
                'LocalInstance.NameStr is \n',
                LocalInstance.NameStr,
                '\n',
                'ChildObjectsDictObject is \n',
                ChildObjectsDictObject
            )

            //set the child instances and also the ParentIdStr        
            LocalInstance.ChildInstancesDictsObject[
                    __ChildAbstraction.CollectionStr
                ]=_.object(
                    _.map(
                        ChildObjectsDictObject,
                        function(__ChildObject,__ChildNameStr)
                        {
                            //Debug
                            /*
                            console.log(
                                'instance map child l 673 \n',
                                'we get the child instance'
                            )
                            */

                            //get the ChildInstance
                            var ChildInstance=InstancesDictObject[__ChildObject._id]

                            //Debug
                            console.log(
                                'instance findChildren map child l 300 \n',
                                'LocalInstance.NameStr is \n',
                                LocalInstance.NameStr,
                                '\n',
                                'ChildInstance is \n',
                                ChildInstance,
                                '\n',
                                'we are going to update with the ParentIdStr'
                            )

                            //update
                            ChildInstance.Abstraction.Collection.update(
                                {
                                    _id:__ChildObject._id
                                },
                                {
                                    $set:{
                                        'ParentIdStr':LocalInstance._id
                                    }
                                }
                            )

                            //return
                            return [__ChildNameStr,ChildInstance]
                        }
                )
            )


        }
    )

    //Debug
    /*
    console.log(
        'abstraction findChildren l 302 \n',
        'LocalInstance.NameStr is \n',
        LocalInstance.NameStr,
        '\n',
        'LocalInstance.ChildInstancesDictsObject is \n',
        LocalInstance.ChildInstancesDictsObject
    )
    */
}


/*
InstanceClass.prototype.setChildInstancesDictsObject = function(_FindDictObject)
{
    //Define
    var LocalInstance=this

    

    //map
    _.map(
        LocalInstance.Abstraction.ChildAbstractionsArray,
        function(__ChildAbstraction)
        {
            //Debug
            console.log(
                'instance l 630\n',
                'LocalInstance.Abstraction is \n',
                LocalInstance.Abstraction,
                '\n',
                '\n',
                '__ChildAbstraction is \n',
                __ChildAbstraction,
                '\n',
                'LocalInstance.NameStr is \n',
                LocalInstance.NameStr
            )
            
            //set
            LocalInstance.ChildInstancesDictsObject[
                __ChildAbstraction.CollectionStr
            ]={}

            //find
            var Find=__ChildAbstraction.Collection.find(
                //{
                //    'ParentNameStr':LocalInstance.NameStr
                //}
                _FindDictObject
            )

            //Debug
            console.log(
                'instance in child map l 657\n',
                'Find.fetch() is \n',
                Find.fetch()
            )

            //Define
            var ChildObjectsArray=Find.fetch()

            //map
            LocalInstance.ChildInstancesDictsObject[
                __ChildAbstraction.CollectionStr
            ]=_.map(
                    ChildObjectsArray,
                    function(__ChildObject)
                    {
                        //Debug
                        console.log(
                            'instance map child l 673 \n',
                            'we get the child instance'
                        )

                        //get the ChildInstance
                        var ChildInstance=InstancesDictObject[__ChildObject._id]

                        //return
                        return ChildInstance
                    }
            )
        }
    )
}
*/

InstanceClass.prototype.setChildren=function()
{
    //Define
    var LocalInstance=this

    //map
    _.map(
            LocalInstance.ChildInstancesDictsObject,
            function(__ChildInstancesDict)
            {

                _.map(
                    __ChildInstancesDict,
                    function(__ChildInstance)
                    {
                        __ChildInstance.Abstraction.Collection.update(
                            {
                                _id:__ChildInstance._id
                            },
                            {
                                $set:{
                                    'ParentId':LocalInstance._id
                                }
                            }

                        )
                    }
                )
            }
        )
   

}


