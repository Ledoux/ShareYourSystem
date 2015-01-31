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

console.log(Vex)

Template.Scale.rendered = function()
{

    var renderer = new Vex.Flow.Renderer(
        $("#"+this.data._id)[0],
        Vex.Flow.Renderer.Backends.RAPHAEL
    );

    var ctx = renderer.getContext();
    var stave = new Vex.Flow.Stave(10, 0, 500);
    stave.addClef("treble").setContext(ctx).draw()

    // Create the notes
    var notes = _.map(
            this.data.NoteSharpsArray,
            function(__NoteSharp)
            {
                //init
                StaveNote=new Vex.Flow.StaveNote(
                    { keys: [__NoteSharp[0].toLowerCase()+"/4"], duration: "q" }
                    )

                //check for sharp and flat
                if(__NoteSharp.slice(1)=="#")
                {
                    StaveNote.addAccidental(0, new Vex.Flow.Accidental("#"))
                }
                if(__NoteSharp.slice(1)=="b")
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
        num_beats: _.size(this.data.NoteSharpsArray),
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
