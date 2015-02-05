/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

score

*/

//Melody
NoteSharpStrsArray=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
NoteFlatStrsArray=["C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B"]
NoteIntToNoteSharpStrDict=_.object(
    _.range(_.size(NoteSharpStrsArray)),
    NoteSharpStrsArray
)
NoteSharpStrToNoteIntDict=_.object(
    _.values(NoteIntToNoteSharpStrDict),
    _.keys(NoteIntToNoteSharpStrDict)
)
NoteIntToNoteFlatStrDict=_.object(
    _.range(_.size(NoteFlatStrsArray)),
    NoteFlatStrsArray
)
NoteFlatStrToNoteIntDict=_.object(
    _.values(NoteIntToNoteFlatStrDict),
    _.keys(NoteIntToNoteFlatStrDict)
)

//Rhythm
DurationStrToDurationIntDict={
    'w':16,
    'hq':12,
    'h':8,
    'qd':6,
    'q':4,
    '8d':3,
    '8':2,
    '16':1
}

DurationIntToDurationStrDict=_.object(
    _.map(_.values(DurationStrToDurationIntDict),function(___IndexInt){return ___IndexInt.toString()}),
    _.keys(DurationStrToDurationIntDict)
    )

//
ScoreClass = function(_InitDictObject){

    //define
    var LocalScore=this

    //Default
    LocalScore.ScoreStr=""
    LocalScore.StepCountInt=0
    LocalScore.BarCountInt=0
    LocalScore.BarMaxInt=4
    LocalScore.SystemCountInt=0
    LocalScore.width=275
    //LocalScore.width=350

    //extend
    _.extend(
    	this,
    	_InitDictObject
    )

    //Debug
    /*
    console.log(
    	'score l 25 \n',
    	'LocalScore is \n',
    	LocalScore
    )
	*/
	
    //jQuery
    LocalScore.Svg=$(".SvgScore#Svg"+this.Song.SongStr+LocalScore.Song.Instance._id)[0]

    //Debug
    /*
    console.log(
        'LocalScore.Svg is \n',
        LocalScore.Svg
    )  
    */

    //Renderer a svg raphael
    LocalScore.Renderer = new Vex.Flow.Renderer(
        LocalScore.Svg,
        Vex.Flow.Renderer.Backends.RAPHAEL
    );

    //Draw an empty stave
    LocalScore.Context = LocalScore.Renderer.getContext();
    LocalScore.BarDictObjectsArray={}

}


ScoreClass.prototype.pushVoice=function(_VoiceStr)
{

	//define
    var LocalScore=this

    //get
    var NoteDictObjectsArray=LocalScore.Song.NoteDictObjectsArraysObject[_VoiceStr]

    //Debug
    /*
    console.log(
        'pushVoice l 101\n',
        'NoteDictObjectsArray is \n',
        NoteDictObjectsArray
    )   
    */

    // Create the notes
    _.map(
            NoteDictObjectsArray,
            function(__NoteDictObject)
            {

                //Debug
                /*
                console.log(
                    'pushVoice l 118 \n',
                    'We PUSH a new NOTE\n',
                    '__NoteDictObject is \n',
                    __NoteDictObject
                )
                */

                //Check
                if(__NoteDictObject!=undefined)
                {
                    //split
                    LocalScore.pushNote(__NoteDictObject)
                }

            }
        )


    //Debug
    /*
    console.log(
        //'LocalScore.NotesArray is \n',
        //LocalScore.NotesArray,
        //'\n',
        //'LocalScore.Song.NumBeatsInt is \n',
        //LocalScore.Song.NumBeatsInt,
        //'LocalScore.NoteDictObjectsArray is \n',
        //LocalScore.NoteDictObjectsArray,
        //'\n',
        'LocalScore.BarDictObjectsArray is \n',
        LocalScore.BarDictObjectsArray
    )
    */

    //map
    _.map(
        _.range(_.size(LocalScore.BarDictObjectsArray)),
        function(__IndexInt)
        {

            //get
            var BarDictObject=LocalScore.BarDictObjectsArray[__IndexInt]

            //Debug
            /*
            console.log(
                'BarDictObject is \n',
                BarDictObject
            )
            */
        
            //Debug
            /*
            console.log(
                '__IndexInt is \n',
                __IndexInt,
                '\n',
                '_.size(LocalScore.BarDictObjectsArray) is \n',
                _.size(LocalScore.BarDictObjectsArray)
            )
            */

            //Define
            var TotalBeatsInt=LocalScore.Song.NumBeatsInt*LocalScore.Song.BeatValueInt

            //Check for the last if it has to be complete
            if(__IndexInt==_.size(LocalScore.BarDictObjectsArray)-1)
            {
                //Debug
                /*
                console.log(
                    'OK?',
                    'LocalScore.StepCountInt is \n',
                    LocalScore.StepCountInt,
                    '\n',
                    'LocalScore.BarCountInt is \n',
                    LocalScore.BarCountInt
                )
                */
                

                _.map(
                    BarDictObject['VoiceDictObjectsObject'],
                    function(__VoiceDictObject,__VoiceStr)
                    {

                        //Debug
                        /*
                        console.log(
                            'We check if the voice has enough notes \n',
                            '__VoiceDictObject is \n',
                            __VoiceDictObject,
                            '\n',
                            'TotalBeatsInt is \n',
                            TotalBeatsInt
                        )
                        */

                        //Check
                        if(__VoiceDictObject.StepCountInt<TotalBeatsInt)
                        {
                            //compute
                            var DiffInt=TotalBeatsInt-__VoiceDictObject.StepCountInt

                            //Debug
                            /*
                            console.log(
                                'We add a silence\n',
                                'DiffInt is \n',
                                DiffInt,
                                '\n',
                                'DurationIntToDurationStrDict[DiffInt.toString()] is \n',
                                DurationIntToDurationStrDict[DiffInt.toString()]
                            )
                            */

                            //push silence
                            LocalScore.pushNote(
                                {
                                    'NoteStr':"a/4",
                                    'DurationInt':DiffInt,
                                    'DurationStr':DurationIntToDurationStrDict[DiffInt.toString()],
                                    'VoiceStr':__VoiceStr,
                                    'SilentBool':true
                                }
                            )

                            //Debug
                            /*
                            console.log(
                                'After  __VoiceDictObject is \n',
                                 __VoiceDictObject
                            )
                            */  

                        }

                        //add the end
                        /*
                        __VoiceDictObject['NoteDictObjectsArray'].push(
                            {
                                'StaveNote':new Vex.Flow.BarNote(3)
                            }
                        )
                        */
                    }
                )
            }

            //Debug
            /*
            console.log(
                "BarDictObject['VoiceDictObjectsObject'] is ",
                BarDictObject['VoiceDictObjectsObject']
            )
            */

            //map
            _.map(
                    _.values(BarDictObject['VoiceDictObjectsObject']),
                    function(__VoiceDictObject)
                    {
                        //Debug
                        /*
                        console.log(
                            '__VoiceDictObject is \n',
                            __VoiceDictObject
                        )
                        */

                        //add
                        __VoiceDictObject['Voice'].addTickables(
                            _.map(
                                __VoiceDictObject['NoteDictObjectsArray'],
                                function(__NoteDictObject)
                                {

                                    //Debug
                                    /*
                                    console.log(
                                        '__NoteDictObject.StaveNote is \n',
                                        __NoteDictObject.StaveNote
                                    )
                                    */

                                    //return 
                                    return  __NoteDictObject.StaveNote
                                }
                            )
                        );

                        //Debug
                        /*
                        console.log(
                            'format'
                        )
                        */

                        // Format and justify the notes to 500 pixels
                        var Formatter = new Vex.Flow.Formatter().
                        joinVoices(
                            [__VoiceDictObject['Voice']]
                        ).format([__VoiceDictObject['Voice']], 200);

                        // Render voice
                        __VoiceDictObject['Voice'].draw(
                            LocalScore.Context,
                            BarDictObject['Stave']
                        );

                    }
                )

        }
    )
    
    //map draw
    /*
    _.map(
        _.range(_.size(LocalScore.BarDictObjectsArray)),
        function(__IndexInt)
        {
            if(__IndexInt==_.size(LocalScore.BarDictObjectsArray)-1)
            {
                LocalScore.BarDictObjectsArray[__IndexInt
                ]['Stave'].setEndBarType(Vex.Flow.Barline.type.REPEAT_END);
            }
            LocalScore.BarDictObjectsArray[__IndexInt]['Stave'].draw()
        }
    )
    */
}

ScoreClass.prototype.getDurationStrsArray=function(_TotalDurationInt)
{
    //define
    var LocalScore=this

    //Debug
    /*
    console.log(
        "getDurationStrsArray l 355 \n",
       '_TotalDurationInt is \n',
       _TotalDurationInt 
    )
    */

    //Define
    var DurationStr=DurationIntToDurationStrDict[_TotalDurationInt]

    //Check
    if(DurationStr!=undefined)
    {
        return [DurationStr]
    }
    else
    {
        //Debug
        /*
        console.log(
            '_.keys(DurationIntToDurationStrDict) is \n',
            _.keys(DurationIntToDurationStrDict)
        )
        */

        //define
        var DiffIntsArray=_.filter(
            _.map(
                _.keys(DurationIntToDurationStrDict),
                function(__DurationInt)
                {
                    return _TotalDurationInt-parseInt(__DurationInt)
                }
            ),
            function(___IndexInt)
            {
                return ___IndexInt>=0
            }
        )

        //define
        var BigDurationInt=_TotalDurationInt-DiffIntsArray[_.size(DiffIntsArray)-1]

        //Debug
        /*
        console.log(
            'DiffIntsArray is \n',
            DiffIntsArray,
            '\n',
            'BigDurationInt is \n',
            BigDurationInt
        )
        */

        //return
        return _.union(
                        [DurationIntToDurationStrDict[BigDurationInt]],
                        LocalScore.getDurationStrsArray(
                            _TotalDurationInt-BigDurationInt
                        )
        )
        
    }


}

ScoreClass.prototype.pushNote=function(_NoteDictObject)
{
    //define
    var LocalScore=this

    //Count to avoid circular calls
    LocalScore.CallsCountInt=0

    //call split
    LocalScore.splitNote(_NoteDictObject)

}

ScoreClass.prototype.setNote=function(_NoteDictObject)
{
    //define
    var LocalScore=this

    //Check
    LocalScore.CallsCountInt+=1

    //Debug
    /*
    console.log(
        'setNote l 458 \n',
        ' LocalScore.CallsCountInt is \n',
         LocalScore.CallsCountInt
    )
    */

    //Check
    if(LocalScore.CallsCountInt<50)
    {

        //Debug
        /*
        console.log(
            "setNote l 355 \n",
           '_NoteDictObject is \n',
           _NoteDictObject 
        )
        */

        //Define
        var DurationStr=_NoteDictObject['DurationStr']

        //Check
        if(DurationStr==undefined)
        {
            
            //get
            var DurationStrsArray=LocalScore.getDurationStrsArray(
                parseInt(_NoteDictObject['DurationInt'])
            )

            //Debug
            /*
            console.log(
                'setNote the DurationStr is undefined\n',
                '_NoteDictObject["DurationInt"] is \n',
                _NoteDictObject['DurationInt'],
                '\n',
                'so we split the note into \n',
                DurationStrsArray
            )
            */

            //map
            _.map(
                    DurationStrsArray,
                    function(__DurationStr)
                    {

                        //Debug
                        /*
                        console.log(
                            'Split note continue with l 490\n',
                            '__DurationStr is \n',
                            __DurationStr
                        )
                        */

                        //set
                        LocalScore.setNote(
                            _.extend(
                                _NoteDictObject,
                                {
                                    'DurationStr':__DurationStr
                                }
                            )
                        )
                    }
                )


        }
        else
        {

            //Copy to make sure
            var PushedNoteDictObject=_.extend(
                            {},
                            _NoteDictObject
                        )

            //Debug
            /*
            console.log(
                'ICI setNote ok for the duration\n',
                'DurationStr is \n',
                DurationStr,
                '\n',
                'PushedNoteDictObject is \n',
                PushedNoteDictObject
            )
            */

            //Check for silence
            var VexflowDurationStr=PushedNoteDictObject['DurationStr']
            if(PushedNoteDictObject['SilentBool']==true)
            {
                VexflowDurationStr+='r'
            }

            //Debug
            /*
            console.log(
                'We set the StaveNote\n',
                'VexflowDurationStr is \n',
                VexflowDurationStr
            )
            */

            //init
            var StaveNote=new Vex.Flow.StaveNote(
                { 
                    keys: [
                            PushedNoteDictObject['NoteStr']
                        ], 
                    duration: VexflowDurationStr
                }
            )

            //check
            /*
            if(StaveNote.duration!=PushedNoteDictObject['DurationStr'])
            {
                console.log('WARNING not properly outputed by vexflow')
            }
            */

            //check for sharp and flat
            if(PushedNoteDictObject['NoteStr'][1]=="#")
            {
                StaveNote.addAccidental(0, new Vex.Flow.Accidental("#"))
            }
            if(PushedNoteDictObject['NoteStr'][1]=="b")
            {
                StaveNote.addAccidental(0, new Vex.Flow.Accidental("b"))
            }

            if(PushedNoteDictObject['DurationStr'].charAt(
                PushedNoteDictObject['DurationStr'].length-1)=='d')
            {
                //Debug
                /*
                console.log('WE ADD A DOT')
                */

                //
                StaveNote.addDotToAll();
            }

            //link
            PushedNoteDictObject['StaveNote']=StaveNote

            //Debug
            /*
            console.log(
                'score.js setNote l 292 \n',
                'Maybe init the bar'
            )
            */

            //init maybe the bar
            if(LocalScore.BarDictObjectsArray[
                    LocalScore.BarCountInt.toString()
                ]==undefined)
            {

                //first Bar
                if(LocalScore.BarCountInt.toString()==0)
                {
                    LocalScore.BarDictObjectsArray[LocalScore.BarCountInt.toString()]={
                    'VoiceDictObjectsObject':{},
                    'Stave': new Vex.Flow.Stave(
                                10, 
                                0, 
                                LocalScore.width
                            )
                    }

                    LocalScore.BarDictObjectsArray[
                        LocalScore.BarCountInt.toString()
                    ]['Stave'
                    ].addClef(
                                "treble"
                    ).addTimeSignature(LocalScore.Song.NumBeatsInt+'/'+LocalScore.Song.BeatValueInt
                    ).setContext(
                        LocalScore.Context
                    ).draw()
                }
                else
                {
                    if(LocalScore.BarCountInt<=LocalScore.BarMaxInt)
                    {
                        //place a stave just on the right
                        LocalScore.BarDictObjectsArray[LocalScore.BarCountInt.toString()]={
                        'VoiceDictObjectsObject':{},
                        'Stave': new Vex.Flow.Stave(
                                    LocalScore.BarDictObjectsArray[
                                        (LocalScore.BarCountInt-1).toString()
                                    ]['Stave'].x+LocalScore.BarDictObjectsArray[
                                        (LocalScore.BarCountInt-1).toString()
                                    ]['Stave'].width, 
                                    LocalScore.BarDictObjectsArray[
                                        (LocalScore.BarCountInt-1).toString()
                                    ]['Stave'].y, 
                                    LocalScore.width
                                )
                        }

                        //set
                        LocalScore.BarDictObjectsArray[
                            LocalScore.BarCountInt.toString()
                        ]['Stave'
                        ].setContext(
                            LocalScore.Context
                        ).draw()
                    }
                    else
                    {
                        //increment
                        LocalScore.SystemCountInt+=1

                        //replace the score to the left
                        LocalScore.BarDictObjectsArray[LocalScore.BarCountInt.toString()]={
                        'VoiceDictObjectsObject':{},
                        'Stave': new Vex.Flow.Stave(
                                    10, 
                                    LocalScore.BarDictObjectsArray[
                                        (LocalScore.BarCountInt-1).toString()
                                    ]['Stave'].y+LocalScore.BarDictObjectsArray[
                                        (LocalScore.BarCountInt-1).toString()
                                    ]['Stave'].height, 
                                    LocalScore.width
                                )
                        }

                        //set
                        LocalScore.BarDictObjectsArray[LocalScore.BarCountInt.toString()]['Stave'
                        ].setContext(
                            LocalScore.Context
                        ).draw()
                    }

                }
                
            }

            //Debug
            /*
            console.log(
                'score.js setNote l 321 \n',
                'Maybe init the voice'
            )
            */

            //init maybe the voice
            if (LocalScore.BarDictObjectsArray[
                        LocalScore.BarCountInt.toString()
                    ]['VoiceDictObjectsObject'][
                        PushedNoteDictObject['VoiceStr']
                    ]==undefined)
            {
                LocalScore.BarDictObjectsArray[
                        LocalScore.BarCountInt.toString()
                    ]['VoiceDictObjectsObject'][
                    PushedNoteDictObject['VoiceStr']
                    ]={
                        'Voice':new Vex.Flow.Voice(
                            {
                                num_beats:  LocalScore.Song.NumBeatsInt,
                                beat_value: LocalScore.Song.BeatValueInt,
                                resolution: Vex.Flow.RESOLUTION
                            }
                        ),
                        'NoteDictObjectsArray':[]
                    }
            }

            //Debug
            /*
            console.log(
                'score.js setNote l 695 \n',
                'push the note in the voice\n',
                'PushedNoteDictObject is \n',
                PushedNoteDictObject
            )
            */

            //define
            var NoteIndexInt=_.size(
                LocalScore.BarDictObjectsArray[
                        LocalScore.BarCountInt.toString()
                    ]['VoiceDictObjectsObject'][_NoteDictObject['VoiceStr']
                    ]['NoteDictObjectsArray']
                )

            //set
            PushedNoteDictObject['IndexInt']=NoteIndexInt

            //push         
            LocalScore.BarDictObjectsArray[
                        LocalScore.BarCountInt.toString()
                    ]['VoiceDictObjectsObject'][_NoteDictObject['VoiceStr']
                    ]['NoteDictObjectsArray'].push(
                        PushedNoteDictObject   
                    )

            //Define
            var DurationInt=DurationStrToDurationIntDict[
                        PushedNoteDictObject['DurationStr']
                    ]

            //Debug
            /*
            console.log(
                'We update the StepCountInt in the voice object\n',
                'LocalScore.StepCountInt is \n',
                LocalScore.StepCountInt,
                '\n',
                "DurationInt is \n",
                DurationInt,
                '\n',
                "PushedNoteDictObject['DurationStr'] is \n",
                PushedNoteDictObject['DurationStr']
            )
            */

            //set step count int
            LocalScore.BarDictObjectsArray[
                        LocalScore.BarCountInt.toString()
                    ]['VoiceDictObjectsObject'][
                    PushedNoteDictObject['VoiceStr']
                    ]['StepCountInt']=LocalScore.StepCountInt+DurationInt

            //Debug
            /*
            console.log(
                'The StepCountInt in the corresponding voice object is \n',
                LocalScore.BarDictObjectsArray[
                        LocalScore.BarCountInt.toString()
                    ]['VoiceDictObjectsObject'][
                    PushedNoteDictObject['VoiceStr']
                    ]['StepCountInt']
            )
            */

            //set
            _NoteDictObject['BarCountInt']=LocalScore.BarCountInt
            _NoteDictObject['VoiceDictObject']=LocalScore.BarDictObjectsArray[
                        LocalScore.BarCountInt.toString()
                    ]['VoiceDictObjectsObject'][PushedNoteDictObject['VoiceStr']
                ]
        }
    }

}

ScoreClass.prototype.splitNote=function(_NoteDictObject)
{
    //define
    var LocalScore=this

    //Check
    LocalScore.CallsCountInt+=1

    //Debug
    /*
    console.log(
        'splitNote l 747 \n',
        ' LocalScore.CallsCountInt is \n',
         LocalScore.CallsCountInt
    )
    */

    //Check
    if(LocalScore.NoteSplitBool)
    {
        //Debug
        /*
        console.log(
            'WE CAN MAYBER MERGE HERE\n',
            'LocalScore.LastNoteDictObject is \n',
            LocalScore.LastNoteDictObject,
            '\n',
            '_NoteDictObject is \n',
            _NoteDictObject
        )
        */

        if(LocalScore.LastNoteDictObject['NoteStr']==_NoteDictObject['NoteStr'])
        {
            /*
            console.log(
                'YES WE MERGE\n',
                'LocalScore.LastNoteDictObject is \n',
                LocalScore.LastNoteDictObject,
                '\n',
                '_NoteDictObject is \n',
                _NoteDictObject
            )
            */
        }

    }

    //init
    LocalScore.NoteSplitBool=false

    //Check
    if(LocalScore.CallsCountInt<50)
    {

        //Define
        var DurationInt=DurationStrToDurationIntDict[
            _NoteDictObject['DurationStr']
        ]

        //Debug
        /*
        console.log(
            'splitNote l 763 \n',
            'DurationInt is \n',
            DurationInt
        )
        */

        //Check
        if(DurationInt==undefined)
        {

            var DurationStrsArray=LocalScore.getDurationStrsArray(
                _NoteDictObject['DurationInt']
            )

            //Debug
            /*
            console.log(
                'splitNote, this DurationInt not exists \n',
                'but _NoteDictObject["DurationInt"] is \n',
                _NoteDictObject['DurationInt'],
                '\n',
                'so we split the note \n',
                DurationStrsArray
            )
            */

            //map
            _.map(
                DurationStrsArray,
                function(__DurationStr)
                {
                    //Debug
                    /*
                    console.log(
                        'splitNote the split continues with\n',
                        __DurationStr
                    )
                    */

                    //splitNote
                    LocalScore.splitNote(
                        _.extend(    
                            _NoteDictObject,
                            {
                                'DurationInt':DurationStrToDurationIntDict[__DurationStr],
                                'DurationStr':__DurationStr
                            }
                        )
                    )
                }
            )
        }
        else
        {
            //Debug
            /*
            console.log(
                'This DurationInt exists \n',
                'DurationInt is \n',
                DurationInt
            )
            */

            //set
            LocalScore.NoteDictObject=_NoteDictObject

            //increment
            LocalScore.NewStepCountInt=LocalScore.StepCountInt+DurationInt

            //Define
            LocalScore.TotalBeatsInt=LocalScore.Song.NumBeatsInt*LocalScore.Song.BeatValueInt

            //init
            LocalScore.HalfBeatsIntsArray=[]

            //Split at the half or not
            if (LocalScore.Song.NumBeatsInt==4 && LocalScore.Song.BeatValueInt==4)
            {
                LocalScore.HalfBeatsIntsArray=[8]
            }
            if (LocalScore.Song.NumBeatsInt==3 && LocalScore.Song.BeatValueInt==4)
            {
                LocalScore.HalfBeatsIntsArray=[4,8]
            }

            //Debug
            /*
            console.log(
                'LocalScore.HalfBeatsIntsArray is \n',
                LocalScore.HalfBeatsIntsArray
            )
            */

            //define
            var SplitHalfBool=false

            //for over all the halksplits
            for (__IndexInt = 0; __IndexInt < _.size(LocalScore.HalfBeatsIntsArray); __IndexInt++) {

                //set
                LocalScore.HalfBeatsInt=LocalScore.HalfBeatsIntsArray[__IndexInt]

                //Check
                if (LocalScore.StepCountInt<LocalScore.HalfBeatsInt && LocalScore.NewStepCountInt>LocalScore.HalfBeatsInt)
                {
                    //set
                    SplitHalfBool=true

                    //Debug
                    /*
                    console.log(
                        'We split half here',
                        'LocalScore.HalfBeatsInt is \n',
                        LocalScore.HalfBeatsInt
                    )
                    */

                    //plit half
                    LocalScore.splitHalfNote()
                }

                //break
                break
            }

            //Debug
            /*
            console.log(
                'SplitHalfBool is \n',
                SplitHalfBool
            )
            */

            //continue if not split
            if(SplitHalfBool==false)
            {

                //Check
                if(LocalScore.NewStepCountInt>LocalScore.TotalBeatsInt)
                {
                    //compute
                    var FirstDiffInt=LocalScore.TotalBeatsInt-LocalScore.StepCountInt
                    var SecondDiffInt=LocalScore.NewStepCountInt-LocalScore.TotalBeatsInt

                    //first Note
                    var FirstNoteDictObject=_.extend(
                        {},
                        _NoteDictObject
                    )

                    //Debug
                    /*
                    console.log(
                        'FirstDiffInt is \n',
                        FirstDiffInt,
                        '\n',
                        'DurationIntToDurationStrDict is \n',
                        DurationIntToDurationStrDict
                    )
                    */

                    //setNote
                    SecondNoteDictObject['DurationInt']=FirstDiffInt
                    FirstNoteDictObject['DurationStr']=DurationIntToDurationStrDict[
                        FirstDiffInt.toString()
                    ]
                    LocalScore.setNote(FirstNoteDictObject)
                    
                    //Debug
                    /*
                    console.log(
                        'SecondDiffInt is \n',
                        SecondDiffInt,
                        '\n',
                        'DurationIntToDurationStrDict is \n',
                        DurationIntToDurationStrDict
                    )
                    */

                    //second Note
                    var SecondNoteDictObject=_.extend(
                        {},
                        _NoteDictObject
                    )
                    SecondNoteDictObject['DurationInt']=SecondDiffInt
                    SecondNoteDictObject['DurationStr']=DurationIntToDurationStrDict[
                        SecondDiffInt.toString()
                    ]
                    LocalScore.StepCountInt+=FirstDiffInt
                    LocalScore.splitNote(SecondNoteDictObject)
                }

                else
                {
                    //Debug
                    /*
                    console.log(
                        'It doent cross the half neither the end so just set'
                    )
                    */

                    //just set
                    LocalScore.setNote(
                        _NoteDictObject
                    )

                    //set
                    LocalScore.StepCountInt=_NoteDictObject['VoiceDictObject']['StepCountInt']
                    
                    //Check
                    if(LocalScore.StepCountInt==LocalScore.TotalBeatsInt)
                    {
                        LocalScore.StepCountInt=0
                        LocalScore.BarCountInt+=1
                    }

                    //
                    LocalScore.NoteSplitBool=true
                    LocalScore.LastNoteDictObject=_NoteDictObject


                }
            }
        }
    }
}

ScoreClass.prototype.splitHalfNote=function()
{
    //define
    var LocalScore=this

    /*
    console.log(
        'splitHalfNote l 547\n',
        'LocalScore.TotalBeatsInt is \n',
        LocalScore.TotalBeatsInt,
        '\n',
        'LocalScore.StepCountInt is \n',
        LocalScore.StepCountInt,
        '\n',
        'LocalScore.NewStepCountInt is \n',
        LocalScore.NewStepCountInt,
        '\n',
        'LocalScore.HalfBeatsInt is \n',
        LocalScore.HalfBeatsInt
    )
    */

    //compute
    var FirstDiffInt=LocalScore.HalfBeatsInt-LocalScore.StepCountInt
    var SecondDiffInt=LocalScore.NewStepCountInt-LocalScore.HalfBeatsInt

    //first Note
    var FirstNoteDictObject=_.extend(
        {},
        LocalScore.NoteDictObject
    )

    //Debug
    /*
    console.log(
        'it has crossed\n',
        'FirstDiffInt is \n',
        FirstDiffInt,
        '\n',
        'DurationIntToDurationStrDict is \n',
        DurationIntToDurationStrDict
    )
    */

    //setNote
    FirstNoteDictObject['DurationInt']=FirstDiffInt
    FirstNoteDictObject['DurationStr']=DurationIntToDurationStrDict[
        FirstDiffInt.toString()
    ]
    LocalScore.setNote(FirstNoteDictObject)

    //Debug
    /*
    console.log(
        'We set the second note after the half\n',
        'SecondDiffInt is \n',
        SecondDiffInt,
        '\n',
        'DurationIntToDurationStrDict is \n',
        DurationIntToDurationStrDict
    )
    */

    //second Note
    LocalScore.StepCountInt=LocalScore.HalfBeatsInt
    var SecondNoteDictObject=_.extend(
        {},
        LocalScore.NoteDictObject
    )
    SecondNoteDictObject['DurationInt']=SecondDiffInt
    SecondNoteDictObject['DurationStr']=DurationIntToDurationStrDict[
        SecondDiffInt.toString()
    ]

    //Check
    LocalScore.splitNote(SecondNoteDictObject)

    //Debug
    /*
    console.log(
        'The second note after the half is setted\n',
        'LocalScore.StepCountInt is \n',
        LocalScore.StepCountInt
    )
    */
}
