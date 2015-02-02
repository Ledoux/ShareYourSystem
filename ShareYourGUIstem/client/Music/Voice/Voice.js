/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Interface client

*/

VoiceAbstraction=new AbstractionClass(
  {
    'ParentTemplateStr':'Music',
    'TemplateStr':'Voice',
    'CollectionStr':"voices",
    'DefaultInstanceObject':{},
    'ChildHelpersObject':
    {
    }
  }
)


Template.Voice.rendered = function()
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
    LocalInstance.Score=new Score(
        {
            'Instance':LocalInstance
        }
    )
    //LocalInstance.Score.drawShortScore()
    
}

VoiceBand = new BandJS();
VoiceBand.setTimeSignature(4,4);
VoiceBand.setTempo(120);

Template.Voice.events = {
    'click .InputScore': function()
    {  
        //
        var Piano = VoiceBand.createInstrument();

        //map
        _.map(
                this.NoteFlatsArray,
                function(__NoteFlat)
                {
                    Piano.note('quarter',__NoteFlat+"4")
                }
            )

        //
        var Player = VoiceBand.finish();
        Player.play()

    }
}

Template.Voice.helpers(
    _.extend(
        VoiceAbstraction['ChildHelpersObject'],
        {
            'SvgId':function(){
                return 'Svg'+this._id
            },
            'InputId':function(){
                return 'Input'+this._id
            }
        }
    )
)
