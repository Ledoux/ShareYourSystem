
#ImportModules
import tables
import ShareYourSystem as SYS

#Define
MyController=SYS.ControllerClass(
	).set(
		'/&Models/$Things',
		{
			'ModelingDescriptionTuplesList':
			[
				#GetStr #ColumnStr #Col
				('MyInt','MyInt',tables.Int64Col()),
				('MyStr','MyStr',tables.StringCol(10)),
				('MyIntsList','MyIntsList',tables.Int64Col(shape=3))
			]	
		}
	)


#print
print('MyController is ')
SYS._print(MyController)

