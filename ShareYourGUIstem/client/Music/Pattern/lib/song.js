/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

song

*/


//
SongClass = function(_InitDictObject){

    //define
    var LocalSong=this
    
    //default values
    LocalSong.VoicesObject={}
    LocalSong.NumBeatsInt=4
    LocalSong.BeatValueInt=4

    //extend
    _.extend(
        this,
        _InitDictObject
    )

    //Define children
    LocalSong.Score=new ScoreClass(
            {
                'Song':LocalSong
            }
        )
    LocalSong.Player=undefined
    LocalSong.NoteDictObjectsArraysObject={}
}


