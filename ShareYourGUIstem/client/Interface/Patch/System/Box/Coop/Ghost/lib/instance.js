/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

data 

*/

InstancesDictObject={}

InstanceClass = function(_UpdateDictObject)
{
    //Define
    var LocalInstance=this

    //update
    _.extend(LocalInstance,_UpdateDictObject)

    //Set
    LocalInstance.NameStr=LocalInstance.Blaze.data[
                LocalInstance.Abstraction.TemplateKeyStr
            ]

    //Debug
    /*
    console.log(
        'InstanceClass init l 22 \n',
        'LocalInstance is \n',
        LocalInstance
    )
    */

    //datafy
    LocalInstance.datafy()
}

InstanceClass.prototype.familify = function()
{
    //Define
    var LocalInstance=this
    
    //Debug
    /*
    console.log(
            'init l 17',
            'We maybe find a parent \n',
            'LocalInstance.ParentTemplateStr is \n',
            LocalInstance.ParentTemplateStr,
            '\n',
            'LocalInstance.ParentCollectionStr is \n',
            LocalInstance.ParentCollectionStr
        )
    */

    //Check
    if (
        LocalInstance.Abstraction.ParentTemplateStr != undefined && LocalInstance.Abstraction.ParentTemplateStr != null)
    {

        //Debug
        /*
        console.log(
            'LocalInstance.Abstraction is \n',
            LocalInstance.Abstraction
        )
        */

        /*
        //Define
        var FindDict={}
        FindDict[
            LocalInstance.Abstraction.ParentAbstraction.TemplateKeyStr
        ]=LocalInstance.Blaze.data[
            'Parent'+LocalInstance.Abstraction.ParentAbstraction.TemplateKeyStr
        ]

        //Set a ParentObject
        LocalInstance.ParentObject=LocalInstance.Abstraction.ParentAbstraction.Collection.findOne(
            FindDict
        )
        */

        /*
        //Debug
        console.log(
            'init l 72 \n',
            'LocalInstance.ParentObject is \n',
            LocalInstance.ParentObject,
            '\n',
            'LocalInstance.ParentCollectionStr is \n',
            LocalInstance.ParentCollectionStr,
            '\n',
            'FindDict is \n',
            FindDict,
            'LocalInstance.Abstraction.TemplateStr is \n',
            LocalInstance.Abstraction.TemplateStr
        )
        */

        //Set a ParentInstance
        //LocalInstance.ParentInstance=Dict[
        //            LocalInstance.ParentCollectionStr
        //        ][LocalInstance.ParentObject._id]

        //set
        LocalInstance.ParentNameStr=LocalInstance.Blaze.data[
            'Parent'+LocalInstance.Abstraction.ParentAbstraction.TemplateKeyStr
        ]

        //set
        LocalInstance.ParentInstance=InstancesDictObject[LocalInstance.ParentNameStr]

        //childify the parent parent
        if(LocalInstance.ParentInstance!=undefined && LocalInstance.ParentInstance!=null)
        {
            if(LocalInstance.ParentInstance.ParentInstance!=undefined && LocalInstance.ParentInstance.ParentInstance!=null)
            {
                if(LocalInstance.ParentInstance.ParentInstance.HasChildBool==false)
                {
                    //Debug
                    console.log(
                        'instance l 121 \n'
                        'we can childify the parent parent here\n',
                        'LocalInstance.ParentInstance.ParentInstance.NameStr is \n',
                        LocalInstance.ParentInstance.ParentInstance.NameStr,
                        '\n',
                        'LocalInstance.NameStr is \n',
                        LocalInstance.NameStr
                    )

                    //childify
                    LocalInstance.ParentInstance.ParentInstance.childify()
                }
            }
        }

        //Debug
        /*
        console.log(
            'init l 290 \n',
            'LocalInstance.TemplateStr is \n',
            LocalInstance.TemplateStr,
            '\n',
            'LocalInstance.ParentInstance.ParentInstance is \n',
            LocalInstance.ParentInstance.ParentInstance,
            '\n',
            'OK we have made it childify'
        )
        */
    }

    //Set
    LocalInstance.HasParentBool = false
    LocalInstance.HasChildBool = false
}

InstanceClass.prototype.childify = function()
{
    //Define
    var LocalInstance=this

    //Debug
    /*
    console.log(
        'childify l 26 \n',
        'LocalInstance.TemplateStr is \n',
        LocalInstance.TemplateStr
    )
    */

    //map
    var ParentTemplateKeyStr='Parent'+LocalInstance.Abstraction.TemplateKeyStr

    //map
    LocalInstance.ChildObjectsArraysObject={}
    _.map(
            LocalInstance.Abstraction.ChildAbstractionsArray,
            function(__ChildAbstraction)
            {
                LocalInstance.ChildObjectsArraysObject[
                    __ChildAbstraction.CollectionStr
                ]={}
            }
        )
    LocalInstance.ChildInstancesArraysObject={}
    _.map(
            LocalInstance.Abstraction.ChildAbstractionsArray,
            function(__ChildAbstraction)
            {
                LocalInstance.ChildInstancesArraysObject[
                    __ChildAbstraction.CollectionStr
                ]={}
            }
        )

    //map
    _.map(
        LocalInstance.Abstraction.ChildAbstractionsArray,
        function(__ChildAbstraction)
        {

            //Define
            var FindDict={}
            FindDict[
                    ParentTemplateKeyStr
                ]=LocalInstance.Blaze.data[
                    LocalInstance.Abstraction.TemplateKeyStr
                ]
            
            //Debug
            /*
            console.log(
                'childify l 188 \n',
                'LocalInstance.NameStr \n',
                LocalInstance.NameStr,
                '\n',
                'FindDict is \n',
                FindDict,
                'LocalInstance.Blaze.data \n',
                LocalInstance.Blaze.data,
                '\n',
                'LocalInstance.Abstraction.TemplateKeyStr is \n',
                LocalInstance.Abstraction.TemplateKeyStr
            )
            */

            //Get the object
            LocalInstance.ChildObjectsArraysObject[
                __ChildAbstraction.CollectionStr
            ]=__ChildAbstraction.Collection.find(
                    FindDict
                ).fetch()

            //Debug
            /*
            console.log(
                'childify l 208 \n',
                'Ok it is fetched'
            )
            */

            //get the Instances
            LocalInstance.ChildInstancesArraysObject[
                __ChildAbstraction.CollectionStr
            ]=_.map(
                LocalInstance.ChildObjectsArraysObject[
                    __ChildAbstraction.CollectionStr
                ],
                function(__ChildObject)
                {
                    //Debug
                    console.log(
                            'childify l 257 \n',
                            '__ChildObject is \n',
                            __ChildObject,
                            '\n',
                            '_.keys(InstancesDictObject) is \n',
                            _.keys(InstancesDictObject),
                            '\n',
                            '__ChildAbstraction.TemplateKeyStr is \n',
                            __ChildAbstraction.TemplateKeyStr,
                            '__ChildObject[__ChildAbstraction.TemplateKeyStr] is \n',
                            __ChildObject[__ChildAbstraction.TemplateKeyStr]
                        )

                    //set
                    var ChildInstance=InstancesDictObject[
                            __ChildObject[
                               __ChildAbstraction.TemplateKeyStr
                            ]
                        ]

                    //Debug
                    console.log(
                        'childify l 278 \n',
                        'ChildInstance is \n',
                        ChildInstance
                    )

                    //return
                    return ChildInstance
                }
            )
        }
    )
    
    //Debug
    console.log(
        'childify l 266 \n',
        'LocalInstance.NameStr \n',
        LocalInstance.NameStr,
        '\n',
        'LocalInstance.ChildObjectsArraysObject is \n',
        LocalInstance.ChildObjectsArraysObject,
        '\n',
        'LocalInstance.ChildInstancesArraysObject is \n',
        LocalInstance.ChildInstancesArraysObject
    )

    //Debug
    /*
    console.log(
        'We are going to the parent parentify'
    )
    */

    //make it parentify
    //parentify(LocalInstance)

    //set to true
    LocalInstance.HasChildBool=true

    //Debug
    /*
    console.log(
        'end of childify l 100 \n',
        'LocalInstance.TemplateStr is \n',
        LocalInstance.TemplateStr
    )
    */
}

InstanceClass.prototype.parentify = function()
{

    //Define
    var LocalInstance=this

    //Debug
    /*
    console.log(
        'parentify l 147 \n',
        'LocalInstance.TemplateStr is \n',
        LocalInstance.TemplateStr
    )
    */

    //map
    _.map(            
        LocalInstance.ChildBlazesArraysObject,
        function(__ChildBlazesArray,__CollectionStr){

            //Debug
            /*
            console.log(
                'parentify l 159\n',
                ''
            )
            */

            //init
            var IndexInt=0

            //map
            _.map(
                __ChildBlazesArray,
                function(__ChildBlaze){

                    //Define
                    var LocalCollection=Meteor.Collection.get(__CollectionStr)

                    //Debug
                    /*
                    console.log(
                        'parentify l 143',
                        'LocalCollection is \n',
                        LocalCollection,
                        '\n',
                        'IndexInt is \n',
                        IndexInt
                    )  
                    */

                    //update
                    LocalCollection.update(
                        {
                            _id:__ChildBlaze.data._id
                        },
                        {
                            $set:
                            {
                                'ParentInt':IndexInt
                            }
                        }
                    )

                    //increment
                    IndexInt=IndexInt+1
                    
                }
            )

        }
    )

    //set
    LocalInstance.HasParentBool=true

    //Debug
    /*
    console.log(
        'End of the parentify l 170 \n',
        'LocalInstance.TemplateStr is \n',
        LocalInstance.TemplateStr
    )
    */
}

InstanceClass.prototype.defaultify = function()
{

    //Define
    var LocalInstance=this

    //Debug
    /*
    console.log(
            'init l 132',
            'LocalInstance.ParentObject is \n',
            LocalInstance.ParentObject,
            '\n',
            'Now we init default attributes'
        )
    */
    
    //map
    if (LocalInstance.Abstraction.DefaultObject == undefined || LocalInstance.Abstraction.DefaultObject == null)
    {
        LocalInstance.Abstraction.DefaultObject={}
    }
    LocalInstance.Abstraction.DefaultObject['ParentInt']=-1

    //Debug
    /*
    console.log(
        'init l 407',
        'LocalInstance.Abstraction.TemplateStr is \n',
        LocalInstance.Abstraction.TemplateStr,
        '\n',
        'LocalInstance.Abstraction.DefaultObject is \n',
        LocalInstance.Abstraction.DefaultObject
    )
    */

    //Check
    var UpdateBlazeKeyStrsList=_.filter(
        _.keys(LocalInstance.Abstraction.DefaultObject),
        function(__KeyStr){

            //Debug
            /*
            console.log(
                'init l 80 \n',
                '\n',
                '__KeyStr is \n',
                __KeyStr,
                '\n',
                'LocalInstance.Blaze.data[__KeyStr] is \n',
                LocalInstance.Blaze.data[
                __KeyStr]
            )
            */

            //return 
            return LocalInstance.Blaze.data[
                __KeyStr] === undefined || LocalInstance.Blaze.data[
                __KeyStr] === null
        }
    )

    //Debug
    /*
    console.log(
        'init.js l 439 \n',
        'UpdateBlazeKeyStrsList is \n',
        UpdateBlazeKeyStrsList
    )
    */

    //object
    var UpdatingBlaze=_.object(
                        _.map(
                            UpdateBlazeKeyStrsList,
                            function(__UpdateKeyStr){
                                return [
                                    __UpdateKeyStr,
                                    LocalInstance.Abstraction.DefaultObject[__UpdateKeyStr]
                                ]
                            }
                        )
                    )

    //Debug
    /*
    console.log(
        'init.js l 482 \n',
        'UpdatingBlaze is \n',
        UpdatingBlaze
    )
    */

    //update in the data
    _.extend(LocalInstance.Blaze.data,UpdatingBlaze)

    if (LocalInstance.CollectionStr != undefined && LocalInstance.CollectionStr != null)
    {

        //Debug
        /*
        console.log(
            'init l 542 \n',
            'LocalInstance.TemplateStr is \n',
            LocalInstance.TemplateStr,
            '\n',
            'LocalInstance.Blaze.data._id is \n',
            LocalInstance.Blaze.data._id,
            '\n',
            'Meteor.Collection.get(LocalInstance.CollectionStr).findOne({_id:LocalInstance.Blaze.data._id}) is \n',
            Meteor.Collection.get(
                LocalInstance.CollectionStr
            ).findOne(
                {_id:LocalInstance.Blaze.data._id}
            )
        )
        */

        //
        var QueryDict={}
        //QueryDict[LocalInstance.TemplateKeyStr]=LocalInstance.Blaze.data[LocalInstance.TemplateKeyStr]
        QueryDict={_id:LocalInstance.Blaze.data._id}

        //Debug 
        /*
        console.log(
            'init 532 \n',
            'QueryDict is \n',
            QueryDict
        )
        */

        //update in the db
        Meteor.Collection.get(
            LocalInstance.CollectionStr
        ).update(
            QueryDict,
            {
                //$set:{'o':3}
                $set:UpdatingBlaze
            }
        )

        //Debug
        /*
        console.log(
            'Ok we have updated \n',
            'Meteor.Collection.get(LocalInstance.CollectionStr).findOne({_id:LocalInstance.Blaze.data._id}) is \n',
            Meteor.Collection.get(LocalInstance.CollectionStr).findOne({_id:LocalInstance.Blaze.data._id})
        )
        */
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

    //Put in a global Dict 
    InstancesDictObject[
        LocalInstance.NameStr
    ]=LocalInstance
}

InstanceClass.prototype.datafy = function()
{

    //Define
    var LocalInstance=this

    //Point back
    LocalInstance.Blaze.Instance=this

    //familify
    LocalInstance.familify()
    
    //defaultify
    LocalInstance.defaultify()
    
    //globalify
    LocalInstance.globalify()
}


