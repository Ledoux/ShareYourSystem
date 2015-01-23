#ImportModules
import operator
import ShareYourSystem as SYS,Binder
from ShareYourSystem.Standards.Objects import Initiator

#Definition a MakerClass decorated by the BinderClass
@Binder.BinderClass(**{
	'ObservingWrapMethodStr':'make',
	'BindingMethodStr':'printSomething'
})
class MakerClass(Initiator.InitiatorClass):

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
		pass

	#Definition a Binding function
	def printSomething(self,*_LiargVariablesList,**_KwarVariablesDict):

		#print
		print('_KwarVariablesDict is ')
		print(_KwarVariablesDict)
		print('')

		#Print
		print('I am going to make.')

	def do_make(self):
		
		#Print
		print('I make')
		
		#cast
		self.MadeMyInt=int(self.MakingMyFloat)

#Definition of instances
MyMaker=MakerClass().make(3.)

#Definition the AttestedStr
SYS._attest(
	[
		'MakerClass.make is '+str(MakerClass.make),
		'MyMaker is '+SYS._str(
		MyMaker,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

#Print



