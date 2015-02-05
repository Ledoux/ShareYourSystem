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

    //get
    LocalInstance=InstancesDictObject[this.data._id]

    //Debug
    /*
    console.log(
        'Scale rendered \n',
        'LocalInstance is \n',
        LocalInstance
    )
    */
    
    //init
    LocalInstance.Song=new SongClass(
            {
                'Instance':LocalInstance,
                'NumBeatsInt':_.size(LocalInstance.NoteFlatStrsArray),
            }
        )

    //map
    LocalInstance.Song.NoteDictObjectsArraysObject['0']=_.map(
                LocalInstance.NoteFlatStrsArray,
                function(__NoteFlatStr)
                {   
                    return {
                        'VoiceStr':'0',
                        'NoteStr':__NoteFlatStr+"/4",
                        'DurationStr':"q"
                    }
                }
            )

    //push
    LocalInstance.Song.Score.pushVoice('0')

}

//init
ScalePlayer = new PlayerClass();

Template.Scale.events = {
    'click .InputScore': function()
    {  

        //set
        ScalePlayer.Song=InstancesDictObject[this._id].Song
        InstancesDictObject[this._id].Song.Player=ScalePlayer

        //Debug
        console.log(
            'InstancesDictObject[this._id].Song is \n',
            InstancesDictObject[this._id].Song
        )

        //play
        InstancesDictObject[this._id].Song.Player.play()

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
