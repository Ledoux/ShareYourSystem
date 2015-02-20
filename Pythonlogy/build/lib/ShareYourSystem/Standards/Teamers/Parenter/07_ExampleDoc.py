
#ImportModules
import ShareYourSystem as SYS

#define and get two children
MyParenter=SYS.ParenterClass(
	).get(
		'NeuronsList'
	).array(
		[
			['&Layers'],
			['$First','$Second'],
			['&Neurons'],
			['$E','$I']
		]
	).command(
		'&$',
		{
			'parent':[],
			'/Top/NeuronsList.append':{
				'#set':[">>self"],
				'#if':[
					('/^/ParentKeyStr',SYS.operator.eq,"Neurons")
				]
			}
		},
		_AfterWalkBool=True
	)

#print
print('MyParenter.NeuronsList is ')
SYS._print(MyParenter.NeuronsList)

