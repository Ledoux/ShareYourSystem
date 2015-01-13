#ImportModules
from ShareYourSystem.Classors import Deriver

#Print a version of the class
print('Deriver.DeriverClass.DerivedClass is ')
print(Deriver.DeriverClass.DerivedClass)

#Print a version of this object
print(Deriver.DeriverClass())

#Print a version of his __dict__
print(Deriver.DeriverClass().__dict__)

#Definition the Parent class
class ParentMakerClass():
	pass

#Definition the deriving ChildClass class
@Deriver.DeriverClass()
class ChildMakerClass(ParentMakerClass):
	pass

#Print some special attributes of the class
print('ParentMakerClass.DerivedClassesList is ')
print(ParentMakerClass.DerivedClassesList)

