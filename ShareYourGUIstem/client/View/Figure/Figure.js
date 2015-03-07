/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Figure client

*/

FigureAbstraction=new AbstractionClass(
  {
    'TemplateStr':'Figure',
    'CollectionStr':"figures",
    'DefaultInstanceObject':{},
    'ChildHelpersObject':
    {
      'plots': function () 
      {

          //set
          var Find=Plots.find()

          //Debug
          /*
          console.log(
            'Template Figure helpers l 35 \n',
            'Find.fetch() is \n',
            Find.fetch()
          )
          */

          //return
          return Find
      }
    }
  }
)


