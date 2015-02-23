
#ImportModules
import ShareYourSystem as SYS


MyParenter=SYS.ParenterClass(
	).get(
		'MyList'
	).set(
		'MyList.append',
		{
			'#set':[4]
		}
	)

#print
print('MyParenter.MyList is ')
SYS._print(MyParenter.MyList)


"""
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
		'+&.values+$.values',
		{
			'parent':[],
			'call#RecruitmentVariable':SYS.GetClass(
					lambda _InstanceVariable:_InstanceVariable[
						'/Top/NeuronsList'
					].append(_InstanceVariable) 
					if _InstanceVariable['/^/ParentKeyStr']=="Neurons"
					else None
				),
			#'/Top/NeuronsList.append':{
			#	'#set':[">>self"],
			#	'#if':[
			#		('/^/ParentKeyStr',SYS.operator.eq,"Neurons")
			#	]
			#}
		},
		_AfterWalkBool=True
	)

#print
print('MyParenter.NeuronsList is ')
SYS._print(MyParenter.NeuronsList)
"""
