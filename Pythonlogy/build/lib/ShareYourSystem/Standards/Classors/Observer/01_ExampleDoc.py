#ImportModules
import ShareYourSystem as SYS
import operator

#Definition a MakerClass decorated by the ObserverClass
@SYS.ObserverClass(**{
	'ObservingIsBool':True,
	'ObservingWrapMethodStr':'make'
})
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
		self.__class__.__bases__[0].__init__(self,**_KwarVariablesDict)

	def do_make(self):
		
		#cast
		self.MadeMyInt=int(self.MakingMyFloat)

#Definition the AttestedStr
SYS._attest(
	[
		'MakerClass.make is '+str(MakerClass.make),
		'MakerClass.DeriveClassor.ObservingWrapMethodStr is '+str(
			MakerClass.DeriveClassor.ObservingWrapMethodStr),
		'MakerClass.DeriveClassor.ObservedWrapMethodStr is '+str(
			MakerClass.DeriveClassor.ObservedWrapMethodStr),
	]
) 

#Print


