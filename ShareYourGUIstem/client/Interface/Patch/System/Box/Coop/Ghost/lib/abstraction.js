/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

abstraction

*/

AbstractionsDictObject={}
CollectionsDictObject={}
CollectionStrToTemplateStrDictObject={}

////////////////////////////////
//Define Class
////////////////////////////////
AbstractionClass = function(_UpdateDictObject)
{

    ////////////////////////////////
    //update`
    ////////////////////////////////

    //define
    var LocalAbstraction=this

    //extend
    _.extend(LocalAbstraction,_UpdateDictObject)

    ////////////////////////////////
    //set meteor links at this level
    ////////////////////////////////

    //set
    LocalAbstraction.TemplateKeyStr=LocalAbstraction.TemplateStr+'Str'
    LocalAbstraction.CollectionKeyStr=LocalAbstraction.CollectionStr[0].toUpperCase(
        ) + LocalAbstraction.CollectionStr.slice(1)
    eval(
        LocalAbstraction.CollectionKeyStr+" = new Meteor.Collection(\"" + LocalAbstraction.CollectionStr + "\")"
      )
    eval(
        "CollectionsDictObject[\"" + LocalAbstraction.CollectionKeyStr + "\"] = " + LocalAbstraction.CollectionKeyStr
      )
    LocalAbstraction.Collection=CollectionsDictObject[LocalAbstraction.CollectionKeyStr]
    LocalAbstraction.Template=Template[LocalAbstraction.TemplateStr]
    CollectionStrToTemplateStrDictObject[LocalAbstraction.CollectionStr]=LocalAbstraction.TemplateStr

    ////////////////////////////////
    //add in the global Dict
    ////////////////////////////////
    AbstractionsDictObject[
        LocalAbstraction.TemplateStr+'Abstraction'
    ]=this

    ////////////////////////////////
    //look for children abstraction already setted
    ////////////////////////////////

    //setChildAbstractionsArray
    LocalAbstraction.setChildAbstractionsArray()

    ////////////////////////////////
    //prepare to receive Instances
    ////////////////////////////////
    LocalAbstraction.InstancesDictObject={}

}

AbstractionClass.prototype.setChildAbstractionsArray=function()
{
    ////////////////////////////////
    //set meteor links at the children level
    ////////////////////////////////

    //Define
    var LocalAbstraction=this

    //Check
    if(LocalAbstraction.ChildHelpersObject!=undefined && LocalAbstraction.ChildHelpersObject!=null)
    {

        //keys
        LocalAbstraction.ChildCollectionStrsArray=_.keys(LocalAbstraction.ChildHelpersObject)

    }
    else
    {
        LocalAbstraction.ChildCollectionStrsArray=[]
    }
    LocalAbstraction.ChildAbstractionsArray=_.map(
            LocalAbstraction.ChildCollectionStrsArray,
            function(__ChildCollectionStr)
            {
                //Debug
                /*
                console.log(
                    'abstraction l 81 \n',
                    '__ChildCollectionStr is \n',
                    __ChildCollectionStr,
                    '\n',
                    '_.keys(AbstractionsDictObject) is \n',
                    _.keys(AbstractionsDictObject)
                )
                */

                //return 
                return AbstractionsDictObject[
                        CollectionStrToTemplateStrDictObject[
                        __ChildCollectionStr
                    ]+'Abstraction'
                ]
            }
    )
}

AbstractionClass.prototype.tini=function()
{

    ////////////////////////////////
    //set meteor links at the parent level
    ////////////////////////////////

    //Define
    var LocalAbstraction=this
    
    //set meteor links at the parent level
    if(LocalAbstraction.ParentTemplateStr!=undefined && LocalAbstraction.ParentTemplateStr!=null)
    {
        //set
        LocalAbstraction.ParentTemplateKeyStr='Parent'+LocalAbstraction.ParentTemplateStr+'Str'

    }

    //Debug
    /*
    console.log(
        'abstraction l 115 \n',
        'we set finally the parent Abstraction \n',
        'LocalAbstraction is \n',
        LocalAbstraction
    )
    */

    //set parent
    LocalAbstraction.ParentAbstraction=AbstractionsDictObject[
        LocalAbstraction.ParentTemplateStr+'Abstraction'
    ]

    //observe 
    LocalAbstraction.Collection.find().observe(
        {
            'added':function(_NewObject)
            {

                ////////////////////////////////
                //set an Instance at this level
                ////////////////////////////////

                //Debug
                /*
                console.log(
                    'abstraction tini setting added l 125 \n',
                    '_NewObject is \n',
                    _NewObject,
                    '\n',
                    'InstancesDictObject is \n',
                    InstancesDictObject
                )
                */

                //Define
                var AddedInstance=InstancesDictObject[_NewObject._id]

                //Check
                if(AddedInstance==undefined)
                {
                    //Init
                    AddedInstance=new InstanceClass(
                        _.extend(
                            _NewObject,
                            {
                                'Abstraction':LocalAbstraction
                            }
                        )
                    )

                    //Define an instance for it
                    InstancesDictObject[_NewObject._id]=AddedInstance
                }

                ////////////////////////////////
                //look for a parent Instance !
                ////////////////////////////////
                AddedInstance.findParent()
    
                ////////////////////////////////
                //look for the children Instance !
                ////////////////////////////////
                AddedInstance.findChildren()

                ////////////////////////////////
                //Make findParent for the children !
                ////////////////////////////////

                //Debug
                /*
                console.log(
                    'abstraction added l 209',
                    'AddedInstance.NameStr is \n',
                    AddedInstance.NameStr,
                    '\n',
                    'we make the children find this parent'
                )
                */
                
                //map map
                _.map(
                    AddedInstance.ChildInstancesDictsObject,
                    function(__ChildInstancesDict)
                    {
                        _.map(
                            __ChildInstancesDict,
                            function(__ChildInstance)
                            {
                                __ChildInstance.findParent()
                            }
                        )
                    }
                )

                ////////////////////////////////
                //For top object do a parent walk !
                ////////////////////////////////
                //not yet necessary
                


            },
            'changed':function(_OldObject,_NewObject)
            {
                //Debug
                /*
                console.log(
                    'abstraction tini setting changed l 197 \n',
                    '_OldObject is \n',
                    _OldObject,
                    '\n',
                    '_NewObject is \n',
                    _NewObject,
                    //'\n',
                    //'InstancesDictObject is \n',
                    //InstancesDictObject,
                    //'\n',
                    'InstancesDictObject[_NewObject._id].NameStr is \n',
                    InstancesDictObject[_NewObject._id].NameStr,
                    '\n',
                    '_.keys(InstancesDictObject[_NewObject._id]) is \n',
                    _.keys(InstancesDictObject[_NewObject._id])
                )
                */

                //extend
                _.extend(
                    InstancesDictObject[_NewObject._id],
                    _NewObject
                )

                //Debug
                /*
                console.log(
                    'abstraction tini setting changed l 224 \n',
                    'after extend',
                    //'\n',
                    //'InstancesDictObject[_NewObject._id] is \n',
                    //InstancesDictObject[_NewObject._id],
                    '\n',
                    '_.keys(InstancesDictObject[_NewObject._id]) is \n',
                    _.keys(InstancesDictObject[_NewObject._id])
                )   
                */


            },
            'removed':function(_OldObject)
            {
                //Debug
                /*
                console.log(
                    'abstraction tini setting removed l 213 \n',
                    '_OldObject is \n',
                    _OldObject,
                    '\n',
                    'InstancesDictObject is \n',
                    InstancesDictObject
                )
                */

                //Check
                if(_OldObject!=undefined)
                {

                    //Find
                    var RemovedInstance=InstancesDictObject[_OldObject._id]

                    //Debug
                    /*
                    console.log(
                        'abstraction tini setting removed l 213 \n',
                        'RemovedInstance is \n',
                        RemovedInstance
                    )
                    */

                    //delete in the parent 
                    if(RemovedInstance.ParentInstance!=undefined)
                    {

                        //Debug
                        /*
                        console.log(
                            'abstraction tini setting removed l 243 \n',
                            'RemovedInstance.ParentInstance is \n',
                            RemovedInstance.ParentInstance
                        )
                        */

                        if(RemovedInstance.ParentInstance.ChildInstancesDictsObject[
                            RemovedInstance.Abstraction.CollectionStr
                        ]!=undefined)
                        {
                            delete RemovedInstance.ParentInstance.ChildInstancesDictsObject[
                                RemovedInstance.Abstraction.CollectionStr][
                                    RemovedInstance.NameStr
                                ]
                        }
                    }

                    //delete
                    delete InstancesDictObject[_OldObject._id]
                }
            }
        }
    )
}
