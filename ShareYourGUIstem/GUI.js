//Define collections
Patches = new Meteor.Collection('patches');
Systems = new Meteor.Collection('systems');
Coops = new Meteor.Collection('coops');
Boxes = new Meteor.Collection('boxes');
Connectors = new Meteor.Collection('connectors');
Messages = new Meteor.Collection('messages');

//client side
if (Meteor.isClient) {

  //require
  require('raphael')

  //starup
	Meteor.startup(function () {

      //get
      PatchDiv=$('#PatchDiv')
      PatchDivOffset=PatchDiv.offset()

      //Debug
      /*
      console.log(PatchDiv)
      console.log(PatchDivOffset.left,PatchDivOffset.top)
      */

	    // code to run on client at startup
      paper=Raphael($('#PatchSvg').get(0))

      //define
      Raphael.st.draggable = function() {
        var me = this,
            lx = 0,
            ly = 0,
            ox = 0,
            oy = 0,
            moveFnc = function(dx, dy) {
                lx = dx + ox;
                ly = dy + oy;
                me.transform('t' + lx + ',' + ly);
            },
            startFnc = function() {},
            endFnc = function() {
                ox = lx;
                oy = ly;
            };

        this.drag(moveFnc, startFnc, endFnc);
      };
      mySet = paper.set();
      mySet.push(paper.circle(400, 150, 50).attr('fill', 'red'));
      mySet.push(paper.circle(400, 150, 40).attr('fill', 'white'));
      mySet.push(paper.circle(400, 150, 30).attr('fill', 'red'));
      mySet.push(paper.circle(400, 150, 20).attr('fill', 'white'));
      mySet.push(paper.circle(400, 150, 10).attr('fill', 'red'));
      mySet.draggable();


	  });

  Template.GUI.helpers({
    'patches': function () {
        return Patches.find();
    },
    'DisplayPatchStrsList':function()
    {
      return Session.get('PatchStrsList')
    }
  });
  
  Session.set('PatchStrsList',['Default','Default2'])
}

//server side
if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });

  Meteor.methods({

      removeAllPosts: function() {
        return Messages.remove({});

      },

      mongo:function(_CollectionStr,_MethodStr,_CollectionDict)
      {
        //Debug
        console.log('l 86 GUI.js')
        console.log('mongo method')
        console.log("_CollectionStr is ",_CollectionStr)
        console.log("_MethodStr is ",_MethodStr)
        console.log("_CollectionDict is ",_CollectionDict)

        //get
        Meteor.Collection.get(_CollectionStr)[_MethodStr](_CollectionDict)
      },

      box:function(_BoxDict){

        //Debug
        console.log(
            'We box here',
            '_BoxDict is ',
            _BoxDict,
            ''
        )

        //Give x and y
        if(_BoxDict['ParentPathStr']==''){

          //Debug
          console.log('This is the top')

          //set
          _BoxDict['x']=400
          _BoxDict['y']=100
        }

        //insert
        Boxes.insert(_BoxDict)

      }

    }
  )
}


