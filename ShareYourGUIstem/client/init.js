/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

init

*/

update = function(_UpdatedObject,_UpdatingObject)
{
    _.each(
                _UpdatingObject,
                function(__Value,__Key){
                    _UpdatedObject[__Key]=__Value
                }
        )
}

childify = function(_Blaze)
{
    //Debug
    /*
    console.log(
        'childify l 26 \n',
        '_Blaze.TemplateStr is \n',
        _Blaze.TemplateStr
    )
    */

    //map
    _.map(
        _Blaze.ChildCollectionStrsArray,
        function(__ChildCollectionStr)
        {
            //Define
            var LocalChildCollection=Meteor.Collection.get(
                __ChildCollectionStr
            )

            //Define
            var FindDict={}
            FindDict[_Blaze.TemplateKeyStr]=_Blaze.data[_Blaze.TemplateKeyStr]
            
            //Debug
            /*
            console.log(
                'childify l 46',
                'FindDict is \n',
                FindDict
            )
            */

            //Get the object
            _Blaze.ChildObjectsArraysObject[
                __ChildCollectionStr
            ]=LocalChildCollection.find(
                    FindDict
                ).fetch()

            //get the Blazes
            _Blaze.ChildBlazesArraysObject[
                __ChildCollectionStr
            ]=_.map(
                _Blaze.ChildObjectsArraysObject[
                    __ChildCollectionStr
                ],
                function(__ChildObjectsDict)
                {
                    return BlazesDict[__ChildObjectsDict._id]
                }
            )

            //Debug
            /*
            console.log(
                'childify l 75',
                '_Blaze.TemplateStr is \n',
                _Blaze.TemplateStr,
                '\n',
                '_Blaze.ChildObjectsArraysObject is \n',
                _Blaze.ChildObjectsArraysObject,
                '\n',
                '_Blaze.ChildBlazesArraysObject is \n',
                _Blaze.ChildBlazesArraysObject
            )
            */

        }
    )

    //set to true
    _Blaze.isChildBool=true

    //Debug
    /*
    console.log(
        'childify l 79 \n'
    )
    */
}


init = function(
                _Blaze,
                _OptionsObject
            )
{
    //Define at this level
    _Blaze.TemplateStr=_OptionsObject['TemplateStr']
    _Blaze.TemplateKeyStr=_Blaze.TemplateStr+'Str'
    _Blaze.CollectionStr=SingularToPluralDict[
        _Blaze.TemplateStr[0].toLowerCase()+_Blaze.TemplateStr.slice(1)
    ]
    _Blaze.Template=Template[_Blaze.TemplateStr]


    //Debug
    /*
    console.log(
            'init l 17',
            'We define at this level \n',
            '_Blaze.TemplateStr is \n',
            _Blaze.TemplateStr,
            '\n',
            '_Blaze.CollectionStr is \n',
            _Blaze.CollectionStr
        )
    */

    //Define at the parent level
    _Blaze.ParentTemplateStr=_OptionsObject['ParentTemplateStr']
    

    //Debug
    /*
    console.log(
            'init l 17',
            'We maybe find a parent \n',
            '_Blaze.ParentTemplateStr is \n',
            _Blaze.ParentTemplateStr,
            '\n',
            '_Blaze.ParentCollectionStr is \n',
            _Blaze.ParentCollectionStr
        )
    */

    //Check
    if (_Blaze.ParentTemplateStr != undefined && _Blaze.ParentTemplateStr != null)
    {

        //set
        _Blaze.ParentCollectionStr=SingularToPluralDict[
            _Blaze.ParentTemplateStr[0].toLowerCase()+_Blaze.ParentTemplateStr.slice(1)
        ]

        //Define
        _Blaze.ParentTemplateKeyStr=_Blaze.ParentTemplateStr+'Str'

        //Define
        var FindDict={}
        FindDict[
            _Blaze.ParentTemplateStr+'Str'
        ]=_Blaze.data[
            _Blaze.ParentTemplateKeyStr
        ]

        //Set a ParentCollection
        _Blaze.ParentCollection=Meteor.Collection.get(
           _Blaze.ParentCollectionStr
        )

        //Set a ParentObject
        _Blaze.ParentObject=_Blaze.ParentCollection.findOne(
            FindDict
        )

        //Debug
        /*
        console.log(
            'init l 72 \n',
            '_Blaze.ParentObject is \n',
            _Blaze.ParentObject,
            'BlazesDict is \n',
            BlazesDict,
            '\n',
            '_Blaze.ParentCollectionStr is \n',
            _Blaze.ParentCollectionStr,
            '\n',
            'BlazesDict[_Blaze.ParentCollectionStr] is \n',
            BlazesDict[
                    _Blaze.ParentCollectionStr
                ]
        )
        */

        //Set a ParentBlaze
        _Blaze.ParentBlaze=BlazesDict[
                    _Blaze.ParentCollectionStr
                ][_Blaze.ParentObject._id]

        //childify the parent parent
        if(_Blaze.ParentBlaze!=undefined && _Blaze.ParentBlaze!=null)
        {
            if(_Blaze.ParentBlaze.ParentBlaze!=undefined && _Blaze.ParentBlaze.ParentBlaze!=null)
            {
                if(_Blaze.ParentBlaze.ParentBlaze.isChildBool==false)
                {
                    childify(_Blaze.ParentBlaze.ParentBlaze)
                }
            }
        }

        //Debug
        /*
        console.log(
            'init l 90 \n',
            '_Blaze.ParentBlaze is \n',
            _Blaze.ParentBlaze
        )
        */
    }

    //Define at the children level
    _Blaze.ChildCollectionStrsArray=_OptionsObject['ChildCollectionStrsArray']
    _Blaze.ChildCollectionsArray=[]
    _Blaze.ChildObjectsArraysObject={}
    _Blaze.ChildBlazesArraysObject={}

    //Debug
    /*
    console.log(
            'init l 235',
            'Now we define maybe children',
            '_Blaze.TemplateStr is \n',
            _Blaze.TemplateStr,
            '\n',
            '_Blaze.ChildCollectionStrsArray is \n',
            _Blaze.ChildCollectionStrsArray
        )
    */

    //Check
    _Blaze.isChildBool=false
    _Blaze.HelpersDict={}
    _.map(
        _Blaze.ChildCollectionStrsArray,
        function(__ChildCollectionStr)
        {
            //Define
            var LocalChildCollection=Meteor.Collection.get(
                __ChildCollectionStr
            )

            //push
            _Blaze.ChildCollectionsArray.push(
                LocalChildCollection
            )

            //Debug
            console.log(
                'We define a default block helpers methods for Childs',
                '__ChildCollectionStr is \n',
                __ChildCollectionStr
            )

            //Define block helpers
            _Blaze.HelpersDict[__ChildCollectionStr]=function()
            {
                /*
                //Debug
                console.log(
                  'Block helpers l 21',
                  'this is \n',
                  this
                )
                */
                
                //set
                var FindDict={}
                FindDict[_Blaze.TemplateKeyStr]=_Blaze.data[_Blaze.TemplateKeyStr]

                //return
                return LocalChildCollection.find(
                    FindDict
               )
            }
        }
    )

    //Debug
    /*
    console.log(
        'init l 291',
        '_Blaze.TemplateStr is \n',
        _Blaze.TemplateStr,
        '\n',
        '_Blaze.HelpersDict is \n',
        _Blaze.HelpersDict
    )
    */
    
    //set
    _Blaze.Template.helpers(_Blaze.HelpersDict)

    //Debug
    /*
    console.log(
            'init l 181',
            '_Blaze.ChildCollectionStrsArray is \n',
            _Blaze.ChildCollectionStrsArray,
            '\n',
            '_Blaze.ChildCollectionsArray is \n',
            _Blaze.ChildCollectionsArray
        )
    */


    //Debug
    /*
    console.log(
            'init l 132',
            '_Blaze.ParentObject is \n',
            _Blaze.ParentObject,
            '\n',
            'Now we init default attributes'
        )
    */
    
    //map
    var DefaultObject=_OptionsObject['DefaultObject']

    //Debug
    /*
    console.log(
        'init l 99',
        'DefaultObject is \n',
        DefaultObject,
        '\n',
        '_.keys(_OptionsObject) is \n',
        _.keys(_OptionsObject)
    )
    */

    //Check
    if (DefaultObject != undefined && DefaultObject != null)
    {
        UpdateKeyStrsList=_.filter(
            _.keys(DefaultObject),
            function(__KeyStr){

                //Debug
                /*
                console.log(
                    'init l 80 \n',
                    '\n',
                    '__KeyStr is \n',
                    __KeyStr,
                    '\n'
                    )
                */

                return _Blaze.data[
                    __KeyStr] === undefined || _Blaze.data[
                    __KeyStr] === null
            }
        )

        //object
        UpdatingObject=_.object(
                            _.map(
                                UpdateKeyStrsList,
                                function(__UpdateKeyStr){
                                    return [
                                        __UpdateKeyStr,
                                        DefaultObject[__UpdateKeyStr]
                                    ]
                                }
                            )
                        )

        //update in the data
        update(_Blaze.data,UpdatingObject)

        
        if (_Blaze.CollectionStr != undefined && _Blaze.CollectionStr != null)
        {

            //update in the db
            Meteor.Collection.get(
                _Blaze.CollectionStr
            ).update(
                {_id:_Blaze.data._id},
                {
                    $set:UpdatingObject
                }
            )
        }
    }

    //Debug
    /*
    console.log(
        'init l 348 \n',
        'set in the BlazesDict',
        '_Blaze.CollectionStr is ',
        _Blaze.CollectionStr
    )
    */

    //Set in a global ref
    if (_Blaze.CollectionStr != undefined && _Blaze.CollectionStr != null)
    {    

        //Debug
        /*
        console.log(
            'init l 135 \n',
            'set in the BlazesDict',
            '_Blaze.CollectionStr is ',
            _Blaze.CollectionStr
        )
        */

        //Put in a global Dict
        if(BlazesDict[
            _Blaze.CollectionStr
            ]== undefined || BlazesDict[_Blaze.CollectionStr]== null)
        {
            BlazesDict[_Blaze.CollectionStr]={}
        }   
        BlazesDict[_Blaze.CollectionStr][_Blaze.data._id]=_Blaze
    } 
}

