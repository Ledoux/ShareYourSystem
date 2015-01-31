/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

sticker

*/

//define
StickerClass = function(_InitDictObject) {

    //Debug
    /*
    console.log(
        'l 24 StickerClass \n',
        'We init a new Sticker \n',
        'PatchRaphael is ',
        PatchRaphael
    )
    */

    //alias
    var LocalSticker=this

    //extend
    _.extend(LocalSticker,_InitDictObject)

    //Debug
    /*
    console.log(
        '_InitDictObject is \n',
        _InitDictObject,
        '\n',
        Meteor.PatchRaphael
    )
    */
    
    //Define the set
    LocalSticker.set=Meteor.PatchRaphael.set()
    LocalSticker.set.Sticker=LocalSticker
        
    //Debug
    /*
    console.log(
        'LocalSticker l 39',
        'LocalSticker.set is',
        LocalSticker.set,
        '\n'
    )
    */

    LocalSticker.dragStickerSetStart = function() {

        //Debug
        /*
        console.log(
                'l 212 dragStickerSetStart \n'
            )
        */

        //map
        LocalSticker.set.items.map(
                function(__Element){

                    //set
                    __Element.ox=__Element.attr('x')
                    __Element.oy=__Element.attr('y')

                    //Debug
                    /*
                    console.log(
                        'dragStickerSetStart l 113',
                        '__Element.ox is \n',
                        __Element.ox,
                        '\n',
                        '__Element.oy is \n',
                        __Element.oy,
                        '\n'
                    )
                    */     
                }

            )

    }

    LocalSticker.dragStickerSetMove = function(_dx,_dy) {

        //Debug
        /*
        console.log(
                'l 242 dragStickerSetMove \n',
            )
        */

        LocalSticker.set.items.map(
                function(__Element){

                    //Debug
                    /*
                    console.log(
                        'dragStickerSetMove l 113',
                        '__Element.ox is \n',
                        __Element.ox,
                        '\n',
                        '__Element.oy is \n',
                        __Element.oy,
                        '\n'
                    )
                    */

                    //set
                    __Element.attr(
                            {
                                x:__Element.ox+_dx,
                                y:__Element.oy+_dy
                            }
                        )
                }

            )


        //update the db at each dx,dy... (not obligatory) 
        Meteor.Collection.get(LocalSticker.CollectionStr).update(
            {_id:LocalSticker.Blaze.data._id},
            {
                $set:{
                    x:LocalSticker.AnchorRect.attr('x'),
                    y:LocalSticker.AnchorRect.attr('y')
                }
            }
        )

        //set
        LocalSticker.Blaze.Infox.set(LocalSticker.AnchorRect.attr('x'))
        LocalSticker.Blaze.Infoy.set(LocalSticker.AnchorRect.attr('y'))
    }

    LocalSticker.dragStickerSetStop = function() {

        //Debug
        /*
        console.log(
                'l 264 dragStickerSetStop \n',
                'LocalSticker.StickerBlaze.data._id is \n',
                LocalSticker.StickerBlaze.data._id
            )
        */

        //update the db
        Meteor.Collection.get(LocalSticker.CollectionStr).update(
            {_id:LocalSticker.Blaze.data._id},
            {
                $set:{
                    x:LocalSticker.AnchorRect.attr('x'),
                    y:LocalSticker.AnchorRect.attr('y')
                }
            }
        )

    }

    //Debug
    /*
    console.log(
        'l 155 StickerClass',
        'End of the StickerClass definition'
        )
    */
}

