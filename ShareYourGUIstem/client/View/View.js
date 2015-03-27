/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

View client

*/

ViewAbstraction=new AbstractionClass(
  {
    'TemplateStr':'View',
    'CollectionStr':"views",
    'DefaultInstanceObject':{},
  }
)

Template.View.rendered=function(){

	/*
	var dataset = [ 5, 10, 15, 20, 25 ];

	d3.select("body").selectAll("p")
	    .data(dataset)
	    .enter()
	    .append("p")
	    .text(function(d) { return d; });
	*/
	

	//select
	var svg=d3.select('#barChart')
				.attr("width", 200)
				.attr("height", 200);

	//declare a Deps.autorun block
	Deps.autorun(function(){

		console.log(
			Boxes
		)

		//perform a reactive query on the collection to get an array
		var dataset = Boxes.find().fetch();

		Bar=_.map(
					dataset,
					function(_Object){
						return _Object['value']
					}
				)


		console.log(
				'dataset is \n',
				dataset
				//Bar
		)
		//update scale domains and axises



		//select elements that correspond to documents
		var SvgBars = svg.selectAll("rect"
			).data(
				dataset,
				function(d){

					console.log(d)
					return d._id
				}
			).enter(
			).append('rect'
			).attr({
			    x: function (d) { return d.x; },
			    y: function (d) { return d.y; },
			    width:  function (d) { return d.width; },
			    height: function (d) { return d.height; }
			  })

		console.log(
			SvgBars 
		)



			//.attr("width", 50
			//).attr("height", 100);

		//bind dataset to objects using key function

		//handle new documents via enter()
		//SvgBars.enter()
		//	.append("rect")

		//handle updates to documents via transition()
		//SvgBars.transition()

        //handle removed documents via exit()
        //SvgBars.exit()
        //    .remove();
    });


	

}

Template.View.events({
    'click #add':function(){
        Bars.insert({
            value:Math.floor(Math.random() * 25)
        });
    },
    'click #remove':function(){
        var toRemove = Random.choice(Bars.find().fetch());
        Bars.remove({_id:toRemove._id});
    },
    'click #randomize':function(){
        //loop through bars
        Bars.find({}).forEach(function(bar){
            //update the value of the bar
            Bars.update({_id:bar._id},{$set:{value:Math.floor(Math.random() * 25)}});
        });
    }
});