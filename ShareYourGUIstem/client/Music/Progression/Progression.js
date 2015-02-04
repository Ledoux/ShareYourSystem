/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Interface client

*/

ProgressionAbstraction=new AbstractionClass(
  {
    'ParentTemplateStr':'Music',
    'TemplateStr':'Progression',
    'CollectionStr':"progressions",
    'DefaultInstanceObject':{},
    'ChildHelpersObject':
    {
    }
  }
)


Template.Progression.rendered = function()
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

 
}

//init
ProgressionPlayer = new PlayerClass();

Template.Progression.events = {
    'click .InputScore': function()
    {  
        //set
        ProgressionPlayer.Song=InstancesDictObject[this._id].Song

        //play
        ProgressionPlayer.play()
    }
}

Template.Progression.helpers(
    _.extend(
        ProgressionAbstraction['ChildHelpersObject'],
        {
            'SvgId':function(){
                return 'Svg'+this._id
            },
            'InputId':function(){
                return 'Input'+this._id
            },
        }
    )
)
