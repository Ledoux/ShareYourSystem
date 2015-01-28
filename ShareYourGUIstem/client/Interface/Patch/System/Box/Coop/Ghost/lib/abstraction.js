/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

abstraction

*/


AbstractionsDictObject={}
CollectionsDictObject={}

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

    //map
    LocalAbstraction.ChildCollectionsArray=_.map(
            LocalAbstraction.ChildCollectionStrsArray,
            function(__ChildCollectionStr)
            {
                return Meteor.Collection.get(__ChildCollectionStr)
            }
    )

    ////////////////////////////////
    //add in the global Dict
    ////////////////////////////////
    AbstractionsDictObject[
        LocalAbstraction.TemplateKeyStr+'Abstraction'
    ]=this

}


AbstractionClass.prototype.tini=function()
{
    //Define
    var LocalAbstraction=this
    
    //set parent
    LocalAbstraction.ParentAbstraction=AbstractionsDictObject[LocalAbstraction.ParentTemplateStr]

}
