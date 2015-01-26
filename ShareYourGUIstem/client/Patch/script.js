/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Patch defines the svg support for displaying all the views of the instances
defining in a certain Patch.

*/


//starup
Meteor.startup(

    function () {

        /*
            Define here the global variables for the raphael env
        */


        // require
        require('raphael')

        //build the Raphael environment
        PatchRaphael=Raphael($('#PatchSvg').get(0))

        //get
        PatchSvg=$('#PatchSvg')
        PatchSvgOffset=PatchSvg.offset()

        //Debug
        /*
        console.log(
                    'l Patch 36\n',
                    'PatchSvg is ',
                    PatchSvg,
                    '\n',
                    'PatchSvgOffset is ',
                    PatchSvgOffset,
                    '\n'
                )
        */
        
        //init
        InstancesSet=PatchRaphael.set()
    }
)

Template.Patch.helpers(
    {
        'instances': function () 
        {
            return Instances.find(
                {
                    PatchStr:
                   {
                    $in:
                    Session.get('PatchStrsList')
                    //Patches.find({},{name:true}).map(function(object){return object['name']})
                   }
               }
           )
        },

        'connectors': function () {
            return Connectors.find();
        }
    }
)



