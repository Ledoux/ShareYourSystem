#ImportModules
import ShareYourSystem as SYS

#Definition 
@SYS.MapperClass(**{
		'MappingDoMethodStr':'make',
		'MappingDoneStrsList':['MadeMyInt']
	}
)
class MakerClass(SYS.InitiatorClass):

	#Definition
	RepresentingKeyStrsList=[
								'MakingMyFloat',
								'MadeMyInt'
							]

	def default_init(self,
					_MakingMyFloat=0.,
					_MadeMyInt=0,
					**_KwarVariablesDict
				):
		SYS.InitiatorClass.__init__(self,**_KwarVariablesDict)

	def do_make(self):
		
		#print
		print('I am in the do_make of the Maker')

		#cast
		self.MadeMyInt=int(self.MakingMyFloat)

#define
MyMaker=MakerClass(
	).make(
		3.
	)

#print
print('MyMaker.MadeMyInt is '+str(MyMaker.MadeMyInt))
