/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

score

*/


DurationStrToDurationIntDict={
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



Score = function(_InitDictObject){

    //define
    var LocalScore=this

    //Default
    LocalScore.ScoreStr=""
    LocalScore.NumBeatsInt=4
    LocalScore.BeatValueInt=4
    LocalScore.StepCountInt=0
    LocalScore.BarCountInt=0

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
    LocalScore.Svg=$(".SvgScore#Svg"+this.ScoreStr+this.Instance._id)[0]

    //Renderer a svg raphael
    LocalScore.Renderer = new Vex.Flow.Renderer(
        LocalScore.Svg,
        Vex.Flow.Renderer.Backends.RAPHAEL
    );

    //Draw an empty stave
    LocalScore.Context = LocalScore.Renderer.getContext();
    LocalScore.Stave = new Vex.Flow.Stave(10, 0, 500);
    LocalScore.Stave.addClef(
                    "treble"
                ).setContext(
                    LocalScore.Context
                ).draw()
}


Score.prototype.push=function()
{

	//define
    var LocalScore=this

    // Create the notes
    LocalScore.BarDictObjectsArray={}
    _.map(
            LocalScore.NoteDictObjectsArray,
            function(__NoteDictObject)
            {

                //Debug
                /*
                console.log(
                    '__NoteDictObject is \n',
                    __NoteDictObject
                )
                */

                //split
                LocalScore.splitNote(__NoteDictObject)

            }
        )


    //Debug
    console.log(
        //'LocalScore.NotesArray is \n',
        //LocalScore.NotesArray,
        //'\n',
        //'LocalScore.NumBeatsInt is \n',
        //LocalScore.NumBeatsInt,
        //'LocalScore.NoteDictObjectsArray is \n',
        //LocalScore.NoteDictObjectsArray,
        //'\n',
        'LocalScore.BarDictObjectsArray is \n',
        LocalScore.BarDictObjectsArray
    )

    //map
    _.map(
        _.range(_.size(LocalScore.BarDictObjectsArray)),
        function(__IndexInt)
        {

            //get
            var BarDictObject=LocalScore.BarDictObjectsArray[__IndexInt]

            // Create a voice in 4/4
            var Voice = new Vex.Flow.Voice(
                {
                    num_beats:  LocalScore.NumBeatsInt,
                    beat_value: LocalScore.BeatValueInt,
                    resolution: Vex.Flow.RESOLUTION
                }
             );

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
                
                if(LocalScore.StepCountInt<16)
                {

                    //compute
                    var DiffInt=16-LocalScore.StepCountInt

                    //Debug
                    console.log(
                        'DiffInt is \n',
                        DiffInt,
                        '\n',
                        'DurationIntToDurationStrDict[DiffInt.toString()] is \n',
                        DurationIntToDurationStrDict[DiffInt.toString()]
                    )

                    //push
                    BarDictObject.NoteDictObjectsArray.push(
                        {
                            'StaveNote':Vex.Flow.StaveNote(
                                { 
                                    keys: [
                                           "c/4" 
                                        ], 
                                    duration: DurationIntToDurationStrDict[
                                            DiffInt.toString()
                                        ]+'r' 
                                }
                            )
                        }
                    )

                    //Debug
                    console.log(
                        'BarDictObject is \n',
                        BarDictObject
                    )

                }
            }



            //add
            Voice.addTickables(
                _.map(
                    BarDictObject.NoteDictObjectsArray,
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

            // Format and justify the notes to 500 pixels
            var Formatter = new Vex.Flow.Formatter().
            joinVoices(
                [Voice]
            ).format([Voice], 200);

            // Render voice
            Voice.draw(
                LocalScore.Context,
                LocalScore.Stave
            );

            //update
            BarDictObject['Voice']=Voice

        }
    )

}

Score.prototype.setNote=function(_NoteDictObject)
{
    //define
    var LocalScore=this

    //Debug
    console.log(
       '_NoteDictObject is \n',
       _NoteDictObject 
    )

    //init
    var StaveNote=new Vex.Flow.StaveNote(
        { keys: [
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

    //set to the bar dict
    if(LocalScore.BarDictObjectsArray[LocalScore.BarCountInt.toString()]==undefined){
                    LocalScore.BarDictObjectsArray[LocalScore.BarCountInt.toString()]={
                        'NoteDictObjectsArray':[]
                    }
                }

    //push         
    LocalScore.BarDictObjectsArray[
                LocalScore.BarCountInt.toString()
            ]['NoteDictObjectsArray'].push(_NoteDictObject)

    //set
    _NoteDictObject['BarCountInt']=LocalScore.BarCountInt

}

Score.prototype.splitNote=function(_NoteDictObject)
{
    //define
    var LocalScore=this

    //increment
    var StepCountInt=LocalScore.StepCountInt+DurationStrToDurationIntDict[
        _NoteDictObject['DurationStr']
    ]

    //Check
    if(StepCountInt>16)
    {
        //compute
        var FirstDiffInt=16-LocalScore.StepCountInt
        var SecondDiffInt=StepCountInt-16

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
        LocalScore.BarCountInt+=1
        LocalScore.StepCountInt=0
        LocalScore.splitNote(SecondNoteDictObject)
    }
    else
    {
        //juste set
        LocalScore.setNote(
            _NoteDictObject
        )
        LocalScore.StepCountInt=StepCountInt
        if(LocalScore.StepCountInt==16)
        {
            LocalScore.StepCountInt=0,
            LocalScore.BarCountInt+=1
        }
    }

}
