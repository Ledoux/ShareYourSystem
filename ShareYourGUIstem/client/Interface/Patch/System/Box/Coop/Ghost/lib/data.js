/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

data 

*/

DataClass = function(_UpdateDictObject)
{
    //Define
    var LocalData=this

    //update
    _.extend(LocalData,_UpdateDictObject)

    //Debug
    /*
    console.log(
        'DataClass init l 22 \n',
        'LocalData is \n',
        LocalData
    )
    */
}

DataClass.prototype.familify = function()
{
    //Define
    var LocalData=this
    
    //Debug
    /*
    console.log(
            'init l 17',
            'We maybe find a parent \n',
            'LocalData.ParentTemplateStr is \n',
            LocalData.ParentTemplateStr,
            '\n',
            'LocalData.ParentCollectionStr is \n',
            LocalData.ParentCollectionStr
        )
    */

    //Check
    if (LocalData.ParentTemplateStr != undefined && LocalData.ParentTemplateStr != null)
    {

        //Define
        var FindDict={}
        FindDict[
            LocalData.ParentTemplateStr+'Str'
        ]=LocalData.Blaze.data[
            LocalData.ParentTemplateKeyStr
        ]

        //Set a ParentCollection
        LocalData.ParentCollection=Meteor.Collection.get(
           LocalData.ParentCollectionStr
        )

        //Set a ParentObject
        LocalData.ParentObject=LocalData.ParentCollection.findOne(
            FindDict
        )

        //Debug
        /*
        console.log(
            'init l 72 \n',
            'LocalData.ParentObject is \n',
            LocalData.ParentObject,
            'BlazesDict is \n',
            BlazesDict,
            '\n',
            'LocalData.ParentCollectionStr is \n',
            LocalData.ParentCollectionStr,
            '\n',
            'BlazesDict[LocalData.ParentCollectionStr] is \n',
            BlazesDict[
                    LocalData.ParentCollectionStr
                ]
        )
        */

        //Set a ParentBlaze
        LocalData.ParentBlaze=BlazesDict[
                    LocalData.ParentCollectionStr
                ][LocalData.ParentObject._id]

        //childify the parent parent
        if(LocalData.ParentBlaze!=undefined && LocalData.ParentBlaze!=null)
        {
            if(LocalData.ParentBlaze.ParentBlaze!=undefined && LocalData.ParentBlaze.ParentBlaze!=null)
            {
                if(LocalData.ParentBlaze.ParentBlaze.HasChildBool==false)
                {
                    //childify(LocalData.ParentBlaze.ParentBlaze)
                }
            }
        }

        //Debug
        /*
        console.log(
            'init l 290 \n',
            'LocalData.TemplateStr is \n',
            LocalData.TemplateStr,
            '\n',
            'LocalData.ParentBlaze.ParentBlaze is \n',
            LocalData.ParentBlaze.ParentBlaze,
            '\n',
            'OK we have made it childify'
        )
        */
    }

    //Define at the children level
    LocalData.ChildCollectionStrsArray=LocalData.ChildCollectionStrsArray
    LocalData.ChildCollectionsArray=[]
    LocalData.ChildObjectsArraysObject={}
    LocalData.ChildBlazesArraysObject={}

    //Debug
    /*
    console.log(
            'init l 235',
            'Now we define maybe children',
            'LocalData.TemplateStr is \n',
            LocalData.TemplateStr,
            '\n',
            'LocalData.ChildCollectionStrsArray is \n',
            LocalData.ChildCollectionStrsArray
        )
    */

    //Check
    LocalData.HasParentBool = false
    LocalData.HasChildBool = false
}

DataClass.prototype.childify = function()
{
    //Define
    var LocalData=this

    //Debug
    /*
    console.log(
        'childify l 26 \n',
        'LocalData.TemplateStr is \n',
        LocalData.TemplateStr
    )
    */

    //map
    var ParentTemplateKeyStr='Parent'+LocalData.TemplateKeyStr
    _.map(
        LocalData.ChildCollectionStrsArray,
        function(__ChildCollectionStr)
        {
            //Define
            var LocalChildCollection=Meteor.Collection.get(
                __ChildCollectionStr
            )

            //Define
            var FindDict={}
            FindDict[ParentTemplateKeyStr]=LocalData.Blaze.data[LocalData.TemplateKeyStr]
            
            //Debug
            /*
            console.log(
                'childify l 46',
                'FindDict is \n',
                FindDict
            )
            */

            //Get the object
            LocalData.ChildObjectsArraysObject[
                __ChildCollectionStr
            ]=LocalChildCollection.find(
                    FindDict
                ).fetch()

            //get the Blazes
            LocalData.ChildBlazesArraysObject[
                __ChildCollectionStr
            ]=_.map(
                LocalData.ChildObjectsArraysObject[
                    __ChildCollectionStr
                ],
                function(__ChildObjectsDict)
                {
                    
                    //return
                    return BlazesDict[ __ChildCollectionStr][__ChildObjectsDict._id]
                }
            )
        }
    )

    //Debug
    /*
    console.log(
        'We are going to the parent parentify'
    )
    */

    //make it parentify
    parentify(LocalData)

    //set to true
    LocalData.HasChildBool=true

    //Debug
    /*
    console.log(
        'end of childify l 100 \n',
        'LocalData.TemplateStr is \n',
        LocalData.TemplateStr
    )
    */
}

DataClass.prototype.parentify = function()
{

    //Define
    var LocalData=this

    //Debug
    /*
    console.log(
        'parentify l 147 \n',
        'LocalData.TemplateStr is \n',
        LocalData.TemplateStr
    )
    */

    //map
    _.map(            
        LocalData.ChildBlazesArraysObject,
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
    LocalData.HasParentBool=true

    //Debug
    /*
    console.log(
        'End of the parentify l 170 \n',
        'LocalData.TemplateStr is \n',
        LocalData.TemplateStr
    )
    */
}

DataClass.prototype.defaultify = function()
{

    //Define
    var LocalData=this

    //Debug
    /*
    console.log(
            'init l 132',
            'LocalData.ParentObject is \n',
            LocalData.ParentObject,
            '\n',
            'Now we init default attributes'
        )
    */
    
    //map
    if (LocalData.Abstraction.DefaultObject == undefined || LocalData.Abstraction.DefaultObject == null)
    {
        LocalData.Abstraction.DefaultObject={}
    }
    LocalData.Abstraction.DefaultObject['ParentInt']=-1

    //Debug
    /*
    console.log(
        'init l 407',
        'LocalData.Abstraction.TemplateStr is \n',
        LocalData.Abstraction.TemplateStr,
        '\n',
        'LocalData.Abstraction.DefaultObject is \n',
        LocalData.Abstraction.DefaultObject
    )
    */

    //Check
    var UpdateBlazeKeyStrsList=_.filter(
        _.keys(LocalData.Abstraction.DefaultObject),
        function(__KeyStr){

            //Debug
            /*
            console.log(
                'init l 80 \n',
                '\n',
                '__KeyStr is \n',
                __KeyStr,
                '\n',
                'LocalData.Blaze.data[__KeyStr] is \n',
                LocalData.Blaze.data[
                __KeyStr]
            )
            */

            //return 
            return LocalData.Blaze.data[
                __KeyStr] === undefined || LocalData.Blaze.data[
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
                                    LocalData.Abstraction.DefaultObject[__UpdateKeyStr]
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
    _.extend(LocalData.Blaze.data,UpdatingBlaze)

    if (LocalData.CollectionStr != undefined && LocalData.CollectionStr != null)
    {

        //Debug
        /*
        console.log(
            'init l 542 \n',
            'LocalData.TemplateStr is \n',
            LocalData.TemplateStr,
            '\n',
            'LocalData.Blaze.data._id is \n',
            LocalData.Blaze.data._id,
            '\n',
            'Meteor.Collection.get(LocalData.CollectionStr).findOne({_id:LocalData.Blaze.data._id}) is \n',
            Meteor.Collection.get(
                LocalData.CollectionStr
            ).findOne(
                {_id:LocalData.Blaze.data._id}
            )
        )
        */

        //
        var QueryDict={}
        //QueryDict[LocalData.TemplateKeyStr]=LocalData.Blaze.data[LocalData.TemplateKeyStr]
        QueryDict={_id:LocalData.Blaze.data._id}

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
            LocalData.CollectionStr
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
            'Meteor.Collection.get(LocalData.CollectionStr).findOne({_id:LocalData.Blaze.data._id}) is \n',
            Meteor.Collection.get(LocalData.CollectionStr).findOne({_id:LocalData.Blaze.data._id})
        )
        */
    }
}

DataClass.prototype.globalify=function()
{

    //Define
    var LocalData=this

    //Debug
    /*
    console.log(
        'init l 529 \n',
        'set in the BlazesDict',
        'LocalData.CollectionStr is ',
        LocalData.CollectionStr
    )
    */

    //Set in a global ref
    if (LocalData.CollectionStr != undefined && LocalData.CollectionStr != null)
    {    

        //Debug
        /*
        console.log(
            'init l 135 \n',
            'set in the BlazesDict',
            'LocalData.CollectionStr is ',
            LocalData.CollectionStr
        )
        */

        //Put in a global Dict
        if(BlazesDict[
            LocalData.CollectionStr
            ]== undefined || BlazesDict[LocalData.CollectionStr]== null)
        {
            BlazesDict[LocalData.CollectionStr]={}
        }   
        BlazesDict[LocalData.CollectionStr][LocalData.Blaze.data._id]=LocalData
    } 

    //Debug
    /*
    console.log(
        'init l 542 \n',
        'end \n'
    )
    */
}

DataClass.prototype.datafy = function()
{

    //Define
    var LocalData=this

    //Point back
    LocalData.Blaze.Data=this

    //familify
    //LocalData.familify()
    
    //defaultify
    LocalData.defaultify()
    
    //globalify
    //LocalData.globalify()
}


