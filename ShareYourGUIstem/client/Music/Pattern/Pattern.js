/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Interface client

*/

PatternAbstraction=new AbstractionClass(
  {
    'ParentTemplateStr':'Music',
    'TemplateStr':'Pattern',
    'CollectionStr':"patterns",
    'DefaultInstanceObject':{},
    'ChildHelpersObject':
    {
    }
  }
)


Template.Pattern.rendered = function()
{
    //Debug
    /*
    console.log(
            '".SvgScore#"+this.data._id" is \n',
            '.SvgScore#Svg'+this.data._id,
            '\n',
            "$('.SvgScore#Svg'+this.data._id)[0] is \n",
            $(".SvgScore#Svg"+this.data._id)[0]
        )
    */

    //Define
    LocalInstance=InstancesDictObject[this.data._id]

    /////////////////////////////////////
    //Melody Score
    /////////////////////////////////////
    //init
    LocalInstance.MelodyScore=new ScoreClass(
        {
            'Instance':LocalInstance,
            'ScoreStr':"Melody",
            'NumBeatsInt':_.size(LocalInstance.PatternCursorIntsArray)+1,
        }
    )

    //init
    NoteInt=0

    //set
    LocalInstance.NoteDictObjectsArray=_.union(
                [
                    {
                        'VoiceStr':'0',
                        'NoteStr':'c/4',
                        'DurationStr':"q"
                    }
                ],
                _.map(
                        LocalInstance.PatternCursorIntsArray,
                        function(__PatternCursorInt)
                        {   

                            //increment
                            NoteInt+=__PatternCursorInt

                            //Debug
                            console.log(
                                'NoteInt is \n',
                                NoteInt
                            )

                            //return 
                            return {
                                'VoiceStr':'0',
                                'NoteStr':NoteIntToNoteFlatStrDict[
                                            NoteInt%_.size(
                                                NoteIntToNoteFlatStrDict
                                            )
                                        ]+'/4',
                                'DurationStr':"q"
                            }
                        }
                    )
                )

    //map
    LocalInstance.MelodyScore.pushVoice(LocalInstance.NoteDictObjectsArray)
        

    /////////////////////////////////////
    //Rhythm Score
    /////////////////////////////////////

    console.log(new Vex.Flow.StaveNote({keys:['c/4'],duration:"hq16"}))

    /*
    //init
    LocalInstance.RhythmScore=new ScoreClass(
        {
            'Instance':LocalInstance,
            'ScoreStr':"Rhythm"
        }
    )

    //set
    LocalInstance.NoteDictObjectsArray=_.map(
                _.filter(
                    LocalInstance.PatternCursorIntsArray,
                    function(__PatternCursorInt)
                    {
                        return __PatternCursorInt!=0
                    }
                ),
                function(__PatternCursorInt)
                {   
                    //Debug
                    console.log(
                        'DurationIntToDurationStrDict[__PatternCursorInt] is \n',
                        DurationIntToDurationStrDict[__PatternCursorInt]
                    )

                    //return 
                    return {
                        'VoiceStr':'0',
                        'NoteStr':"a/4",
                        'DurationStr':DurationIntToDurationStrDict[__PatternCursorInt]
                    }
                }
            )

    //push
    LocalInstance.RhythmScore.pushVoice(
            LocalInstance.NoteDictObjectsArray
        )
    */
}

PatternBand = new BandJS();
PatternBand.setTimeSignature(4,4);
PatternBand.setTempo(120);

Template.Pattern.events = {
    'click .InputScore': function()
    {  
        //
        var Piano = PatternBand.createInstrument();

        //map
        _.map(
                InstanceDictObjects[this._id].NoteDictObjectsArray,
                function(__NoteDictObject)
                {
                    Piano.note(
                        DurationStrToBandDurationStr[__NoteDictObject['DurationStr']],
                        __NoteDictObject['NoteStr']+"4"
                    )
                }
            )

        //
        var Player = PatternBand.finish();
        Player.play()

    }
}

Template.Pattern.helpers(
    _.extend(
        PatternAbstraction['ChildHelpersObject'],
        {
            'SvgMelodyId':function(){
                return 'SvgMelody'+this._id
            },
            'InputMelodyId':function(){
                return 'InputMelody'+this._id
            },
            'SvgRhythmId':function(){
                return 'SvgRhythm'+this._id
            },
            'InputRhythmId':function(){
                return 'InputRhythm'+this._id
            }
        }
    )
)
