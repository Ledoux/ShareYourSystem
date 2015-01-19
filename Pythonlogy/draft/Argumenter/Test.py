#Import Modules
from ShareYourSystem.Classors import Representer,Doer
from ShareYourSystem.Classors.Representer import _print
from ShareYourSystem.Functers import Argumenter

#Print a version of the class
_print(dict(Argumenter.ArgumenterClass.__dict__.items()))

#Print a version of this object
_print(Argumenter.ArgumenterClass())

#Print a version of his __dict__
_print(Argumenter.ArgumenterClass().__dict__)

#Definition a class that is going to have a method with an argumenting decoration
class MakerClass(object):

	def __init__(self,**_KwargVariablesDict):
		self.MakingInt=1
		self.MakingFloat=2.
		self.MakingStr=""

	@Argumenter.ArgumenterClass()
	def make(self,_Int=None,_Str=None,**_KwargVariablesDict):

		#debug
		print('self.MakingInt is '+str(self.MakingInt))
		print('self.MakingFloat is '+str(self.MakingFloat))
		print('self.MakingStr is '+str(self.MakingStr))


#Print a version of this doing class
_print(dict(MakerClass.__dict__.items()))

#Get an instance
MyMaker=MakerClass()

#Show the default value of the instance
print('At the beginning the object is...')
print('')

#Change the int
print('do with the object...')
MyMaker.make(3,"hello")
print('')

#Change the int
print('do again with the object, but...')
MyMaker.make(5,**{'MakingFloat':4.})
print('')



