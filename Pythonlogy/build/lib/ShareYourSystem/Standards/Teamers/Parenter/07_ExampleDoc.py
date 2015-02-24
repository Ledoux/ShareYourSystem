
#ImportModules
import ShareYourSystem as SYS

#define and get two children
MyParenter=SYS.ParenterClass(
	).array(
		[
			['&Layers'],
			['$First','$Second'],
			['&Neurons'],
			['$E','$I']
		]
	).command(
		'+&.values+$.values',
		'#call:parent',
		_AfterWalkBool=True
	).command(
		'+&.values+$.values',
		{
			#'#bound:recruit':lambda _InstanceVariable:_InstanceVariable[
			#		'/Top/NeuronsDict'
			#	].__setitem__(
			#		_InstanceVariable.ManagementKeyStr,
			#		_InstanceVariable
			#	) 
			#	if _InstanceVariable['/^/ParentKeyStr']=="Neurons"
			#	else None,
			'#bound:recruit':lambda _InstanceVariable:_InstanceVariable[
					'/Top/NeuronsDict'
				]
			#'/Top/LayersDict.__setitem__':{
			#	'#value:#map@get':["/~/ManagementKeyStr",">>self"],
			#	'#if':[
			#		('/^/ParentKeyStr',SYS.operator.eq,"#direct:Layers")
			#	]
			#}
		}
	)


#print
#print('MyParenter.NeuronsDict.keys() is ')
#SYS._print(MyParenter.NeuronsDict.keys())

#print
#print('MyParenter.LayersDict.keys() is ')
#SYS._print(MyParenter.LayersDict.keys())
