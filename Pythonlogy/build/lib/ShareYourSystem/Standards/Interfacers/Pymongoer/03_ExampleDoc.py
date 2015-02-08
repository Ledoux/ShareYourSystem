
#ImportModules
import ShareYourSystem as SYS

#Definition a Pymongoer 
MyPymongoer=SYS.PymongoerClass().pymongo(
	**{
		'FolderingPathStr':SYS.Pymongoer.LocalFolderPathStr
	}
)

#build a parent Database
MyPymongoer.PymongoneDatabaseVariable.ThingsCollection.remove(
	{}
)
MyPymongoer.PymongoneDatabaseVariable.ThingsCollection.insert(
	{'MyStr':'hello'}
)

#build a child
import collections
MyPymongoer.PymongoneDatabaseVariable.ChildDatabase=MyPymongoer.PymongoneClientVariable.ChildDatabase
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
