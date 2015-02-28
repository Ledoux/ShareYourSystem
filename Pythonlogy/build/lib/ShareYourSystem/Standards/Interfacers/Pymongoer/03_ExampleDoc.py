
#ImportModules
import ShareYourSystem as SYS

#Definition a Pymongoer 
MyPymongoer=SYS.PymongoerClass(
	).pymongo(
		**{
		'FolderingPathStr':SYS.Pymongoer.LocalFolderPathStr
		}
)

#build a parent Database
MyDatabase=MyPymongoer.PymongoneClientVariable['MyDatabase']
MyDatabase=ThingsCollection.remove(
	{}
)
MyDatabase.ThingsCollection.insert(
	{'MyStr':'hello'}
)

#build a child
import collections
MyPymongoer.PymongoneClientVariable.ChildDatabase=MyPymongoer.PymongoneClientVariable.ChildDatabase
MyPymongoer.PymongoneDatabaseVariable.ChildDatabase.ThingsCollection.remove(
	{}
)
MyPymongoer.PymongoneDatabaseVariable.ChildDatabase.ThingsCollection.insert(
	[{'MyInt':1},{'MyInt':3}]
)

#Definition the AttestedStr
SYS._print('MyPymongoer is '+SYS._str(MyPymongoer)+'\n')

#print
print('ChildDatabase ThingsCollection fetch gives')
SYS._print(
	list(MyPymongoer.PymongoneDatabaseVariable.ChildDatabase.ThingsCollection.find())
)

#kill
if MyPymongoer.PymongonePopenVariable!=None:
	MyPymongoer.PymongonePopenVariable.kill()
