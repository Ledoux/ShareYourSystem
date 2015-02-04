/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

join

*/


JoinPrefixStr="*"

////////////////////////////////
//Define Class
////////////////////////////////
JoinClass = function(_UpdateDictObject)
{

    ////////////////////////////////
    //update`
    ////////////////////////////////

    //define
    var LocalJoin=this

    //extend
    _.extend(LocalJoin,_UpdateDictObject)

    ////////////////////////////////
    //set meteor links at this level
    ////////////////////////////////

}

JoinClass.prototype.join=function(_FindDictObject,_FilterDictObject)
{

    //Define local
    var LocalJoin=this

    //Default
    if(_FindDictObject['OrderArray']==undefined)
    {
        _FindDictObject['OrderArray']=
        _.map(
            _.filter(
                _.keys(_FindDictObject),
                    function(__KeyStr)
                    {
                        //return __KeyStr!='OrderArray'
                        return __KeyStr[0]==JoinPrefixStr
                    }
                ),
            function(__KeyStr)
            {
                return __KeyStr
            }
        )
    }

    //Debug
    console.log(
        '_FindDictObject["OrderArray"] is \n',
        _FindDictObject['OrderArray']
    )

    //Define
    LocalJoin.FilterKeyStrsArray=_.filter(
        _.keys(_FilterDictObject),
        function(__KeyStr)
        {
            return _.contains(_FindDictObject['OrderArray'],__KeyStr)==false
        }
    )

    //init
    LocalJoin.GlobalFilterDict=_.object(
        _.map(
            LocalJoin.FilterKeyStrsArray,
            function(__FilterKeyStr)
            {
                return [__FilterKeyStr,_FilterDictObject[__FilterKeyStr]]
            }
        )
    )

    //init
    LocalJoin.FoundDictObjectsArraysArray=[]
    LocalJoin.FoundKeyStrsArraysArray=[]
    LocalJoin.FoundIdDictsArraysArray=[]

    //map
    _.map(
        _FindDictObject['OrderArray'],
        function(__JoinStr)
        {
            //Debug
            /*
            console.log(
                '__JoinStr is \n',
                __JoinStr
            )
            */

            //split
            var CollectionStr=__JoinStr.split(JoinPrefixStr).slice(1,2)[0]
            var JoinKeyStr=__JoinStr.split(CollectionStr).slice(1)[0].slice(1)

            //Debug
            console.log(
                'CollectionStr is \n',
                CollectionStr,
                '\n',
                'JoinKeyStr is \n',
                JoinKeyStr
            )

            //init
            var MapFilterDictObject=_.extend(
                        {
                        },
                        LocalJoin.GlobalFilterDict
                    )

            //extend
            if(_FilterDictObject[__JoinStr]!=undefined)
            {
                MapFilterDictObject=_.extend(
                    MapFilterDictObject,
                    _FilterDictObject[__JoinStr]
                )
            }

            //Debug
            /*
            console.log(
                'MapFilterDictObject is \n',
                MapFilterDictObject
            )
            */

            //Check
            var MapCollection=undefined
            if(CollectionStr==LocalJoin.Abstraction.Collection._name || CollectionStr=='this')
            {
                MapCollection=LocalJoin.Abstraction.Collection
            }
            else
            {
                MapCollection=Meteor.Collection.get(CollectionStr)
            }

            //Debug
            /*
            console.log(
                'MapCollection is \n',
                MapCollection
            )
            */

            //find
            var MapFoundDictObjectsArray=MapCollection.find(
                            _FindDictObject[__JoinStr],
                            _.extend(
                                {   
                                    _id:1
                                },
                                MapFilterDictObject
                            )
                        ).fetch()

            //push
            LocalJoin.FoundDictObjectsArraysArray.push(MapFoundDictObjectsArray)

            //Get the corresponding ids
            LocalJoin.FoundIdDictsArraysArray.push(
                _.map(
                        MapFoundDictObjectsArray,
                        function(__DictObject)
                        {

                            //Debug
                            /*
                            console.log(
                                'MapCollection.Abstraction is \n',
                                MapCollection.Abstraction
                            )
                            */

                            //set
                            var LocalDictObject={}
                            LocalDictObject[
                                'Join'+JoinKeyStr+MapCollection.Abstraction.TemplateStr+'IdStr'
                            ]=__DictObject._id
                            return LocalDictObject
                        }
                    )
            )

            //Get the corresponding ids
            LocalJoin.FoundKeyStrsArraysArray.push(
                _.map(
                        MapFoundDictObjectsArray,
                        function(__DictObject)
                        {

                            //Debug
                            /*
                            console.log(
                                'l 84 \n',
                                'MapFilterDictObject is \n',
                                MapFilterDictObject
                            )
                            */

                            //return
                            return _.map(
                                    _.keys(MapFilterDictObject),
                                    function(__KeyStr)
                                    {
                                        return '('+__KeyStr+'_'+__DictObject[__KeyStr]+')'
                                    }
                                ).join('_')
                        }
                    )
            )
        }
    )

    //Debug
    /*
    console.log(
        'LocalJoin.FoundKeyStrsArraysArray is \n',
        LocalJoin.FoundKeyStrsArraysArray,
        '\n',
        'LocalJoin.FoundIdDictsArraysArray is \n',
        LocalJoin.FoundIdDictsArraysArray
    )
    */

    LocalJoin.JoinKeyCartesianArray=cartesianproduct(LocalJoin.FoundKeyStrsArraysArray)
    LocalJoin.JoinIdCartesianArray=cartesianproduct(LocalJoin.FoundIdDictsArraysArray)

    //Debug
    /*
    console.log(
        'LocalJoin.JoinKeyCartesianArray is \n',
        LocalJoin.JoinKeyCartesianArray,
        '\n',
        'LocalJoin.JoinIdCartesianArray is \n',
        LocalJoin.JoinIdCartesianArray
    )
    */

    LocalJoin.JoinDictObjectsArray=_.map(
        LocalJoin.JoinIdCartesianArray,
        function(__IdDictObjectsArray)
        {

            //Debug
            /*
            console.log(
                '__IdDictObjectsArray is \n',
                __IdDictObjectsArray
            )
            */

            //union
            var JoinDictObject={}

            //map
            _.map(
                __IdDictObjectsArray,
                function(__IdDictObject)
                {
                    //Debug
                    /*
                    console.log(
                        '__IdDictObject is \n',
                        __IdDictObject
                    )
                    */

                    //extend
                    _.extend(
                        JoinDictObject,
                        __IdDictObject
                    )
                }
            )

            //return 
            return JoinDictObject   
        }
    )

    //Debug
    /*
    console.log(
        'LocalJoin.JoinDictObjectsArray is \n',
        LocalJoin.JoinDictObjectsArray
    )
    */
}

JoinClass.prototype.insert=function()
{
    //Define local
    var LocalJoin=this

    //map
    _.map(
        _.range(
            _.size(
                LocalJoin.JoinDictObjectsArray
            )
        ),
        function(__IndexInt)
        {
            //get
            var JoinDictObject=LocalJoin.JoinDictObjectsArray[__IndexInt]
            var KeyStrsArray=LocalJoin.JoinKeyCartesianArray[__IndexInt]

            //Debug
            /*
            console.log(
                'KeyStrsArray is \n',
                KeyStrsArray
            )
            */

            //call
            Meteor.call(
                'mongo',
                LocalJoin.Abstraction.CollectionStr,
                'insert',
                _.extend(   
                    JoinDictObject,
                    {
                        'JoinStr':KeyStrsArray.join('_')
                    }
                )
            )
        }
    )
}

JoinClass.prototype.find=function()
{





}



