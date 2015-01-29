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

    ////////////////////////////////
    //update`
    ////////////////////////////////

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

    //init
    LocalInstance.ChildInstancesDictsObject={}

    //check
    if(LocalInstance.GrandParentNameStrsArray==undefined)
    {
        //init
        LocalInstance.GrandParentNameStrsArray=[]
    }

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

    //Define
    var ParentObject=null

    //First look at an already possible ParentIdStr given
    if (LocalInstance.ParentIdStr!=undefined)
    {
        //Debug
        /*
        console.log(
            'instance l 94\n',
            'LocalInstance.ParentIdStr is \n',
            LocalInstance.ParentIdStr,
            '\n',
            'LocalInstance.NameStr is \n',
            LocalInstance.NameStr,
            '\n',
            'LocalInstance.ParentNameStr is \n',
            LocalInstance.ParentNameStr,
            '\n'
        )
        */

        //findOne
        ParentObject=LocalInstance.Abstraction.ParentAbstraction.Collection.findOne(
            {
                _id:LocalInstance.ParentIdStr
            }
        )

        //Debug
        /*
        console.log(
            'instance l 121\n',
            'ParentObject is \n',
            ParentObject
        )
        */
    }

    if(LocalInstance.ParentInstance==undefined && LocalInstance.Abstraction.ParentAbstraction!=undefined)
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
            'LocalInstance.NameStr is \n',
            LocalInstance.NameStr,
            '\n',
            'ParentFind.fetch() is \n',
            ParentFind.fetch()
        )
        */

        //Define
        var PossibleParentObjectsArray=ParentFind.fetch()

        //Check
        if(_.size(PossibleParentObjectsArray)>1)
        {
            //Debug
            /*
            console.log(
                'instance findParent l 161 \n',
                'LocalInstance.NameStr is \n',
                LocalInstance.NameStr,
                '\n',
                'it is not sufficient to find a parent'
            )
            */

            //Check
            if(LocalInstance.GrandParentNameStrsArray!=undefined)
            {

                //Debug
                /*
                console.log(
                    'instance findParent l 177 \n',
                    'LocalInstance.NameStr is \n',
                    LocalInstance.NameStr,
                    '\n',
                    'LocalInstance.GrandParentNameStrsArray is \n',
                    LocalInstance.GrandParentNameStrsArray
                )
                */

                //filter
                var FilterArray=_.filter(
                    PossibleParentObjectsArray,
                    function(__PossibleParentObject)
                    {

                        //get
                        var PossibleParentInstance=InstancesDictObject[__PossibleParentObject._id]

                        //Debug
                        /*
                        console.log(
                            'instance grand parent for l 197\n',
                            '__PossibleParentObject is \n',
                            __PossibleParentObject,
                            '\n',
                            'PossibleParentInstance.GrandParentNameStrsArray is \n',
                            PossibleParentInstance.GrandParentNameStrsArray
                        )
                        */

                        //map
                        return _.all(
                                    _.map(
                                        _.range(
                                            _.size(
                                                LocalInstance.GrandParentNameStrsArray
                                            )
                                        ),
                                        function(__Int)
                                        {
                                            return LocalInstance.GrandParentNameStrsArray[__Int
                                            ]==PossibleParentInstance.GrandParentNameStrsArray[__Int]
                                        }
                                    )
                                )
                    }
                )
    
                //Debug
                /*
                console.log(
                    'instance findParent l 177 \n',
                    'LocalInstance.NameStr is \n',
                    LocalInstance.NameStr,
                    '\n',
                    'FilterArray is \n',
                    FilterArray
                )
                */

                //Check
                if(_.size(FilterArray)==1)
                {
                    ParentObject=FilterArray[0]
                }
            }

        }
        else if(_.size(PossibleParentObjectsArray)==1)
        {
            ParentObject=PossibleParentObjectsArray[0]
        }
    }


    //Check
    if(ParentObject!=null)
    {

        //Debug
        /*
        console.log(
            'instance findParent l 276 \n',
            'LocalInstance.NameStr is \n',
            LocalInstance.NameStr,
            '\n',
            'Ok we find one unique parent'
        )
        */
        
        ////////////////////////////////////////////
        //update at this level
        ////////////////////////////////////////////

        //get
        LocalInstance.ParentInstance=InstancesDictObject[
                ParentObject._id
            ]

        //set
        LocalInstance.GrandParentNameStrsArray=_.union(
            [LocalInstance.ParentInstance.NameStr],
            LocalInstance.ParentInstance.GrandParentNameStrsArray
        )

        //Debug
        /*
        console.log(
            'We give directly the ParentIdStr to the data'
        )
        */

        //update the ParentIdStr
        LocalInstance.Abstraction.Collection.update(
            {_id:LocalInstance._id},
            {
                $set:{
                        'ParentIdStr':LocalInstance.ParentInstance._id
                    }
            }
        )

        ////////////////////////////////////////////
        //update at the level of the parent
        ////////////////////////////////////////////

        //Define
        var UpdateDictObject={}
        UpdateDictObject[
            'ChildIdStrsDictsObject.'+LocalInstance.Abstraction.CollectionStr+'.'+LocalInstance.NameStr
        ]=LocalInstance._id

        //update
        LocalInstance.ParentInstance.Abstraction.Collection.update(
            {
                _id:LocalInstance.ParentInstance._id
            },
            {
                $set:UpdateDictObject
            }
        )
    }

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
            /*
            console.log(
                'instance in findChildren map l 305\n',
                'LocalInstance.NameStr is \n',
                LocalInstance.NameStr,
                '\n',
                'ChildObjectsDictObject is \n',
                ChildObjectsDictObject
            )
            */

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
                            /*
                            console.log(
                                'instance findChildren map child l 336 \n',
                                'LocalInstance.NameStr is \n',
                                LocalInstance.NameStr,
                                '\n',
                                'ChildInstance is \n',
                                ChildInstance,
                                '\n',
                                'we are going to update with the ParentIdStr'
                            )
                            */

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




