/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

midi

*/

//Rhythm
VexflowDurationStrToBandDurationIntDict={
    'q':'quarter',
}

BandDurationStrToVexflowDurationStrDict=_.object(
    _.values(VexflowDurationStrToBandDurationIntDict),
    _.keys(VexflowDurationStrToBandDurationIntDict)
    )

//
PlayerClass = function(_InitDictObject){

    //define
    var LocalPlayer=this
    LocalPlayer.TempoInt=120

    //extend
    _.extend(
        this,
        _InitDictObject
    )

    //set
    LocalPlayer.Band = new BandJS();
    LocalPlayer.Band.setTempo(LocalPlayer.TempoInt);
    LocalPlayer.InstrumentsObject={}

}

PlayerClass.prototype.play=function()
{
    //define
    var LocalPlayer=this

    //set
    LocalPlayer.Band.setTimeSignature(
                        LocalPlayer.Song.NumBeatsInt,
                        LocalPlayer.Song.BeatValueInt
                    );

    //map
    _.map(
            LocalPlayer.Song.NoteDictObjectsArraysObject,
            function(__NoteDictObjectsArray,__KeyStr)
            {

                //create
                LocalPlayer.InstrumentsObject[__KeyStr] = LocalPlayer.Band.createInstrument();

                //map
                _.map(
                    __NoteDictObjectsArray,
                    function(__NoteDictObject)
                    {
                        //Debug
                        /*
                        console.log(
                                'play l 66\n',
                                '__NoteDictObject is \n',
                                __NoteDictObject,
                                ''
                            )
                        */
                        
                        //Define
                        var BandDurationInt=VexflowDurationStrToBandDurationIntDict[
                                __NoteDictObject['DurationStr']
                            ]

                        //Debug
                        /*
                        console.log(
                                'play l 66\n',
                                'BandDurationInt is \n',
                                BandDurationInt,
                                '\n',
                                '__NoteDictObject["NoteStr"] is \n',
                                __NoteDictObject['NoteStr'],
                                '\n',
                                'LocalPlayer.InstrumentsObject[__KeyStr] is \n',
                                LocalPlayer.InstrumentsObject[__KeyStr]
                            )
                        */

                        //note
                        LocalPlayer.InstrumentsObject[__KeyStr].note(
                            BandDurationInt,
                            __NoteDictObject['NoteStr'].replace('/','')
                        )

                        //Debug
                        /*
                        console.log(
                                'play l 98 \n',
                                'Ok we have noted'
                            )
                        */
                    }
                )
            }
        )

    //play
    LocalPlayer.Player = LocalPlayer.Band.finish();
    LocalPlayer.Player.play()

}


