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
    //Define
    ////////////////////////////////
    var LocalAbstraction=this

    ////////////////////////////////
    //update`
    ////////////////////////////////
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

    //set meteor links at the parent level
    if(LocalAbstraction.ParentTemplateStr!=undefined && LocalAbstraction.ParentTemplateStr!=null)
    {
        //set
        LocalAbstraction.ParentTemplateKeyStr='Parent'+LocalAbstraction.ParentTemplateStr+'Str'

    }

    ////////////////////////////////
    //set meteor links at the child level
    ////////////////////////////////

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
    ////////////////////////////////
    //add in the global Dict
    ////////////////////////////////
    AbstractionsDictObject[
        LocalAbstraction.TemplateStr+'Abstraction'
    ]=this

}


AbstractionClass.prototype.tini=function()
{
    //Define
    var LocalAbstraction=this
    


    //set parent
    LocalAbstraction.ParentAbstraction=AbstractionsDictObject[
        LocalAbstraction.ParentTemplateStr+'Abstraction'
    ]

    //Debug
    /*
    console.log(
        'tini l 104 \n',
        'LocalAbstraction.ParentAbstraction is \n',
        LocalAbstraction.ParentAbstraction,
        '\n',
        'LocalAbstraction.ParentTemplateStr is \n',
        LocalAbstraction.ParentTemplateStr,
        '\n',
        'AbstractionsDictObject is \n',
        AbstractionsDictObject
    )
    */
}
