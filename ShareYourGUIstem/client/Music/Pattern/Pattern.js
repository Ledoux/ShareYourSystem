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

    LocalInstance=InstancesDictObject[this.data._id]
    LocalInstance.MelodyScore=new Score(
        {
            'Instance':LocalInstance,
            'ScoreStr':"Melody"
        }
    )
    LocalInstance.MelodyScore.drawShortScore()

    LocalInstance.RhythmScore=new Score(
        {
            'Instance':LocalInstance,
            'ScoreStr':"Rhythm"
        }
    )
    LocalInstance.RhythmScore.drawShortScore()
    
}

PattenrBand = new BandJS();
PattenrBand.setTimeSignature(4,4);
PattenrBand.setTempo(120);

Template.Pattern.events = {
    'click .InputScore': function()
    {  
        //
        var Piano = PattenrBand.createInstrument();

        //map
        _.map(
                this.NoteFlatsArray,
                function(__NoteFlat)
                {
                    Piano.note('quarter',__NoteFlat+"4")
                }
            )

        //
        var Player = PattenrBand.finish();
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
