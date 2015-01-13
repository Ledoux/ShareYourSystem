#ImportModules
from ShareYourSystem.Classors import Inspecter

#Print special attributes of the class
print(Inspecter.InspecterClass.__dict__)

#Print a version of this object
print(Inspecter.InspecterClass())

#Print a version of his __dict__
print(Inspecter.InspecterClass().__dict__)


@Inspecter.InspecterClass()
class MakerClass():
	def make(self,_MakingStr,*_LiargVariablesList,**_KwargVariablesDict):
		pass

#Print a version of the class
print('')
print('MakerClass.InspectedArgumentDict is ')
print(MakerClass.InspectedArgumentDict)

#Print a version of this object
print(MakerClass())

#Print a version of his __dict__
print(MakerClass().__dict__)