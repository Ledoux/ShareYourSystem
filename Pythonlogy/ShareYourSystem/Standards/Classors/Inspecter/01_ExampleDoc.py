#ImportModules
import ShareYourSystem as SYS

"""
#define
@SYS.InspecterClass()
class MakerClass(SYS.ObjectClass):

	def default_init(self,
			_MakingMyStr,
			_MakingMyInt=0,
			**_KwargVariablesDict
		):
		SYS.ObjectClass.__init__(self,**_KwargVariablesDict)

	def do_make(self):

		#str
		self.MadeMyStr=str(self.MakingMyStr)

#print
print('MakerClass.InspectedArgumentDict is ')
SYS._print(
		MakerClass.InspectedArgumentDict
	)
 
#Print
"""



class A():

	def a(self):pass

class B(A):

	def a(self):pass


print(B.a==A.a)

