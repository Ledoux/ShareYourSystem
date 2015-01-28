/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

abstraction

*/


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
    LocalAbstraction.CollectionStr=SingularToPluralDict[
        LocalAbstraction.TemplateStr[0].toLowerCase()+LocalAbstraction.TemplateStr.slice(1)
    ]
    LocalAbstraction.Template=Template[LocalAbstraction.TemplateStr]

    //set meteor links at the parent level
    if(LocalAbstraction.ParentTemplateStr!=undefined && LocalAbstraction.ParentTemplateStr!=null)
    {
        //set
        LocalAbstraction.ParentCollectionStr=SingularToPluralDict[
            LocalAbstraction.ParentTemplateStr[0].toLowerCase(
                )+LocalAbstraction.ParentTemplateStr.slice(1)
        ]

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

    //map
    LocalAbstraction.ChildCollectionsArray=_.map(
            LocalAbstraction.ChildCollectionStrsArray,
            function(__ChildCollectionStr)
            {
                return Meteor.Collection.get(__ChildCollectionStr)
            }
    )
}


