
#ImportModules
import tables
import ShareYourSystem as SYS

#Definition of a Controller instance with a noded datar
MyController=SYS.ControllerClass(
	).command(
		'/&Models/$Things',
		{
			'model':[
				#ModelingSealTuplesList
				[
					#GetStr #ColumnStr #Col
					('MyInt','MyInt',tables.Int64Col()),
					('MyStr','MyStr',tables.StringCol(10)),
					('MyIntsList','MyIntsList',tables.Int64Col(shape=3))
				]
			]
		}
	)


#print
SYS._print('MyController is ')
print(MyController)

