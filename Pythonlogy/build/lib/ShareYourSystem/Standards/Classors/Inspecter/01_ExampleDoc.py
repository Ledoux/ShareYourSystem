#ImportModules
import ShareYourSystem as SYS

#define
@SYS.InspecterClass()
class MakerClass(SYS.InitiatorClass):

	def default_init(self,
			_MakingMyStr,
			_MakingMyInt=0,
			**_KwargVariablesDict
		):
		SYS.InitiatorClass.__init__(self,**_KwargVariablesDict)

	def do_make(self):

		#str
		self.MadeMyStr=str(self.MakingMyStr)

#print
print('MakerClass.InspectedArgumentDict is ')
SYS._print(
		MakerClass.InspectedArgumentDict
	)
 
#Print
