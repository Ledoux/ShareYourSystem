
#ImportModules
import ShareYourSystem as SYS

#Definition a Pymongoer 
MyPymongoer=SYS.PymongoerClass().pymongo(
	**{
		'FolderingPathStr':SYS.Pymongoer.LocalFolderPathStr
	}
)

#remove
MyPymongoer.PymongoneDatabaseVariable.ThingsCollection.remove({})
MyPymongoer.PymongoneDatabaseVariable.ThingsCollection.insert({'MyStr':'hello'})

#Definition the AttestedStr
SYS._print('MyPymongoer is '+SYS._str(MyPymongoer)+'\n')

#print
print('ThingsCollection fetch gives')
SYS._print(
	list(MyPymongoer.PymongoneDatabaseVariable.ThingsCollection.find())
)

#kill
if MyPymongoer.PymongonePopenVariable!=None:
	MyPymongoer.PymongonePopenVariable.kill()
