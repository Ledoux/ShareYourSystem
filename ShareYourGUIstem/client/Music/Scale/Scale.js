/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Interface client

*/

ScaleAbstraction=new AbstractionClass(
  {
    'ParentTemplateStr':'Music',
    'TemplateStr':'Scale',
    'CollectionStr':"scales",
    'DefaultInstanceObject':{},
    'ChildHelpersObject':
    {
    }
  }
)

Template.Scale.rendered = function()
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
            'Instance':LocalInstance,
            //'NumBeatsInt':_.size(LocalInstance.NoteFlatStrsArray),
        }
    )
    LocalInstance.Score.pushVoice(
        _.map(
                LocalInstance.NoteFlatStrsArray,
                function(__NoteFlatStr)
                {   
                    return {
                        'VoiceStr':'0',
                        'NoteStr':__NoteFlatStr.toLowerCase()+"/4",
                        'DurationStr':"q"
                    }
                }
            )
    )

}

ScaleBand = new BandJS();
ScaleBand.setTimeSignature(4,4);
ScaleBand.setTempo(120);

Template.Scale.events = {
    'click .InputScore': function()
    {  
        //
        var Piano = ScaleBand.createInstrument();

        //map
        _.map(
                this.NoteFlatStrsArray,
                function(__NoteFlatStr)
                {
                    Piano.note('quarter',__NoteFlatStr+"4")
                }
            )

        //
        var Player = ScaleBand.finish();
        Player.play()

    }
}

Template.Scale.helpers(
    _.extend(
        ScaleAbstraction['ChildHelpersObject'],
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
