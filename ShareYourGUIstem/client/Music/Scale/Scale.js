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
    
    var renderer = new Vex.Flow.Renderer(
        $(".SvgScore#Svg"+this.data._id)[0],
        Vex.Flow.Renderer.Backends.RAPHAEL
    );

    var ctx = renderer.getContext();
    var stave = new Vex.Flow.Stave(10, 0, 500);
    stave.addClef("treble").setContext(ctx).draw()

    // Create the notes
    var notes = _.map(
            this.data.NoteFlatsArray,
            function(__NoteFlat)
            {
                //init
                StaveNote=new Vex.Flow.StaveNote(
                    { keys: [__NoteFlat[0].toLowerCase()+"/4"], duration: "q" }
                    )

                //check for sharp and flat
                if(__NoteFlat.slice(1)=="#")
                {
                    StaveNote.addAccidental(0, new Vex.Flow.Accidental("#"))
                }
                if(__NoteFlat.slice(1)=="b")
                {
                    StaveNote.addAccidental(0, new Vex.Flow.Accidental("b"))
                }

                //return 
                return StaveNote
            }
        )

    //
    //console.log(notes)

    // Create a voice in 4/4
    var voice = new Vex.Flow.Voice({
        num_beats: _.size(this.data.NoteFlatsArray),
        beat_value: 4,
        resolution: Vex.Flow.RESOLUTION
    });

    // Add notes to voice
    voice.addTickables(notes);

    // Format and justify the notes to 500 pixels
    var formatter = new Vex.Flow.Formatter().
    joinVoices([voice]).format([voice], 200);

    // Render voice
    voice.draw(ctx, stave);

}

Template.Scale.events = {
    'click .InputScore': function()
    {   
        //
        var conductor = new BandJS();
        conductor.setTimeSignature(4,4);
        conductor.setTempo(120);

        //
        var piano = conductor.createInstrument();

        //map
        _.map(
                this.NoteFlatsArray,
                function(__NoteFlat)
                {
                    piano.note('quarter',__NoteFlat+"4")
                }
            )

        //
        var player = conductor.finish();
        player.play()
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
