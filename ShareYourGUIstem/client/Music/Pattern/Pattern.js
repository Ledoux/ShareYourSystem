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
    LocalInstance.MelodySong=new SongClass(
        {
            'Instance':LocalInstance,
            'SongStr':"Melody",
            'NumBeatsInt':_.size(LocalInstance.CursorIntsArray)+1,
        }
    )

    //init
    NoteInt=0

    //set
    LocalInstance.MelodySong.NoteDictObjectsArraysObject['0']=_.union(
                [
                    {
                        'VoiceStr':'0',
                        'NoteStr':'c/4',
                        'DurationStr':"q"
                    }
                ],
                _.map(
                        LocalInstance.CursorIntsArray,
                        function(__CursorInt)
                        {   

                            //increment
                            NoteInt+=__CursorInt

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
    LocalInstance.MelodySong.Score.pushVoice('0')
            
    /////////////////////////////////////
    //Rhythm Score
    /////////////////////////////////////

    //init
    LocalInstance.RhythmSong=new SongClass(
        {
            'Instance':LocalInstance,
            'SongStr':"Rhythm"
        }
    )

    //set
    LocalInstance.RhythmSong.NoteDictObjectsArraysObject['0']=_.map(
                _.filter(
                    LocalInstance.CursorIntsArray,
                    function(__CursorInt)
                    {
                        return __CursorInt!=0
                    }
                ),
                function(__CursorInt)
                {   
                    //Debug
                    console.log(
                        'DurationIntToDurationStrDict[__CursorInt] is \n',
                        DurationIntToDurationStrDict[__CursorInt]
                    )

                    //return 
                    return {
                        'VoiceStr':'0',
                        'NoteStr':"a/4",
                        'DurationStr':DurationIntToDurationStrDict[__CursorInt]
                    }
                }
            )

    //Debug
    console.log(
        'Pattern rendered\n',
        'LocalInstance.SumInt is \n',
        LocalInstance.SumInt
    )

    //push
    LocalInstance.RhythmSong.Score.pushVoice('0')
}

//init
PatternPlayer = new PlayerClass();

Template.Pattern.events = {
    'click .MelodyInputScore': function()
    {  
        //set
        PatternPlayer.Song=InstancesDictObject[this._id].MelodySong

        //play
        PatternPlayer.play()
    },
    'click .RhythmInputScore': function()
    {  
        //set
        PatternPlayer.Song=InstancesDictObject[this._id].RhythmSong

        //play
        PatternPlayer.play()
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
