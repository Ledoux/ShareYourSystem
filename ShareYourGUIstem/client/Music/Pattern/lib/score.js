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
    _.map(_.values(DurationStrToDurationIntDict),function(__Int){return __Int.toString()}),
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
    LocalScore.Svg=$(".SvgScore#Svg"+this.ScoreStr+LocalScore.Song.Instance._id)[0]

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
    console.log(
        'pushVoice l 101\n',
        'NoteDictObjectsArray is \n',
        NoteDictObjectsArray
    )

    // Create the notes
    _.map(
            NoteDictObjectsArray,
            function(__NoteDictObject)
            {

                //Debug
                console.log(
                    '__NoteDictObject is \n',
                    __NoteDictObject
                )

                //Check
                if(__NoteDictObject!=undefined)
                {
                    //split
                    LocalScore.splitNote(__NoteDictObject)
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

                        //
                        if(__VoiceDictObject.StepCountInt<TotalBeatsInt)
                        {
                            //compute
                            var DiffInt=TotalBeatsInt-__VoiceDictObject.StepCountInt

                            //Debug
                            console.log(
                                'DiffInt is \n',
                                DiffInt,
                                '\n',
                                'DurationIntToDurationStrDict[DiffInt.toString()] is \n',
                                DurationIntToDurationStrDict[DiffInt.toString()],
                                '\n',
                                'BarDictObject.NoteDictObjectsArray is \n',
                                BarDictObject.NoteDictObjectsArray
                            )

                            //push
                            __VoiceDictObject['NoteDictObjectsArray'].push(
                                {
                                    'StaveNote':new Vex.Flow.StaveNote(
                                        { 
                                            keys: [
                                                   "a/4" 
                                                ], 
                                            duration: DurationIntToDurationStrDict[
                                                    DiffInt.toString()
                                                ] + 'r'
                                        }
                                    )
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

ScoreClass.prototype.setNote=function(_NoteDictObject)
{
    //define
    var LocalScore=this

    //Debug
    console.log(
        "setNote l 355 \n",
       '_NoteDictObject is \n',
       _NoteDictObject 
    )

    //init
    var StaveNote=new Vex.Flow.StaveNote(
        { 
            keys: [
                _NoteDictObject['NoteStr']
                ], 
            duration: _NoteDictObject['DurationStr'] 
        }
    )

    //check for sharp and flat
    if(_NoteDictObject['NoteStr'][1]=="#")
    {
        StaveNote.addAccidental(0, new Vex.Flow.Accidental("#"))
    }
    if(_NoteDictObject['NoteStr'][1]=="b")
    {
        StaveNote.addAccidental(0, new Vex.Flow.Accidental("b"))
    }

    //link
    _NoteDictObject['StaveNote']=StaveNote

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

            LocalScore.BarDictObjectsArray[LocalScore.BarCountInt.toString()]['Stave'
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
                LocalScore.BarDictObjectsArray[LocalScore.BarCountInt.toString()]['Stave'
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
            ]['VoiceDictObjectsObject'][_NoteDictObject['VoiceStr']]==undefined)
    {
        LocalScore.BarDictObjectsArray[
                LocalScore.BarCountInt.toString()
            ]['VoiceDictObjectsObject'][
            _NoteDictObject['VoiceStr']
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
        'score.js setNote l 348 \n',
        'push the note'
    )
    */

    //push         
    LocalScore.BarDictObjectsArray[
                LocalScore.BarCountInt.toString()
            ]['VoiceDictObjectsObject'][_NoteDictObject['VoiceStr']
            ]['NoteDictObjectsArray'].push(
                _NoteDictObject
            )

    //set step count int
    LocalScore.BarDictObjectsArray[
                LocalScore.BarCountInt.toString()
            ]['VoiceDictObjectsObject'][_NoteDictObject['VoiceStr']
            ]['StepCountInt']=LocalScore.StepCountInt+DurationStrToDurationIntDict[
            _NoteDictObject['DurationStr']]

    //set
    _NoteDictObject['BarCountInt']=LocalScore.BarCountInt

}

ScoreClass.prototype.splitNote=function(_NoteDictObject)
{
    //define
    var LocalScore=this

    //increment
    var StepCountInt=LocalScore.StepCountInt+DurationStrToDurationIntDict[
        _NoteDictObject['DurationStr']
    ]

    //Define
    var TotalBeatsInt=LocalScore.Song.NumBeatsInt*LocalScore.Song.BeatValueInt

    //Split at the half or not
    if (LocalScore.Song.NumBeatsInt==4 && LocalScore.Song.BeatValueInt==4)
    {
        var HalfBeatsInt=TotalBeatsInt/2

        //Debug
        console.log(
            'splitNote l 547\n',
            'TotalBeatsInt is \n',
            TotalBeatsInt,
            '\n',
            'StepCountInt is \n',
            StepCountInt
        )

        //Check
        if(LocalScore.StepCountInt<HalfBeatsInt && StepCountInt>HalfBeatsInt)
        {
            //Debug
            console.log(
                'The half of the bar is crossed\n',
                'LocalScore.StepCountInt is \n',
                LocalScore.StepCountInt,
                '\n',
                'StepCountInt is \n',
                StepCountInt,
                '\n',
                'HalfBeatsInt is \n',
                HalfBeatsInt
            )

            //compute
            var FirstDiffInt=HalfBeatsInt-LocalScore.StepCountInt
            var SecondDiffInt=StepCountInt-HalfBeatsInt

            //first Note
            var FirstNoteDictObject=_.extend(
                {},
                _NoteDictObject
            )

            //Debug
            console.log(
                'FirstDiffInt is \n',
                FirstDiffInt,
                '\n',
                'DurationIntToDurationStrDict is \n',
                DurationIntToDurationStrDict
            )

            //setNote
            FirstNoteDictObject['DurationStr']=DurationIntToDurationStrDict[FirstDiffInt.toString()]
            LocalScore.setNote(FirstNoteDictObject)

            //Debug
            console.log(
                'SecondDiffInt is \n',
                SecondDiffInt,
                '\n',
                'DurationIntToDurationStrDict is \n',
                DurationIntToDurationStrDict
            )

            //second Note
            var SecondNoteDictObject=_.extend(
                {},
                _NoteDictObject
            )
            SecondNoteDictObject['DurationStr']=DurationIntToDurationStrDict[SecondDiffInt.toString()]
            LocalScore.StepCountInt=HalfBeatsInt
            LocalScore.splitNote(SecondNoteDictObject)

        }
        else
        {
            //just set
            LocalScore.setNote(
                _NoteDictObject
            )

            //set
            LocalScore.StepCountInt=StepCountInt
        }
    }

    //Check
    if(StepCountInt>TotalBeatsInt)
    {
        //compute
        var FirstDiffInt=TotalBeatsInt-LocalScore.StepCountInt
        var SecondDiffInt=StepCountInt-TotalBeatsInt

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
        FirstNoteDictObject['DurationStr']=DurationIntToDurationStrDict[FirstDiffInt.toString()]
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
        SecondNoteDictObject['DurationStr']=DurationIntToDurationStrDict[SecondDiffInt.toString()]
        LocalScore.BarCountInt+=1
        LocalScore.StepCountInt=0
        LocalScore.splitNote(SecondNoteDictObject)
    }

    else
    {
        //just set
        LocalScore.setNote(
            _NoteDictObject
        )

        //set
        LocalScore.StepCountInt=StepCountInt
        
        //Check
        if(LocalScore.StepCountInt==TotalBeatsInt)
        {
            LocalScore.StepCountInt=0,
            LocalScore.BarCountInt+=1
        }
    }

}
