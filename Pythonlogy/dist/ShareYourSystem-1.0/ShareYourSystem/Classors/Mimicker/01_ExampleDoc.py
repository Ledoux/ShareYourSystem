#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Doer,Mimicker
from ShareYourSystem.Objects import Initiator
import operator

#Definition 
@Doer.DoerClass()
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
		Initiator.InitiatorClass.__init__(self,**_KwarVariablesDict)

	def do_make(self):
		
		#print
		print('I am in the do_make of the Maker')

		#cast
		self.MadeMyInt=int(self.MakingMyFloat)

#Definition
@Mimicker.MimickerClass(**{
	'MimickingDoMethodStr':'make'
})
class BuilderClass(MakerClass):

	#Definition
	RepresentingKeyStrsList=[
							]

	def default_init(self,
					**_KwarVariablesDict
				):
		MakerClass.__init__(self,**_KwarVariablesDict)

	#<DefineDoMethod>
	def mimic_make(self):
		
		#print
		print('I am in the mimic_make of the Builder')

		#call the parent method
		MakerClass.make(self)

		#cast
		self.MadeMyInt+=10

#Definition an instance
MyBuilder=BuilderClass()

#Print
print('Before make, MyBuilder is ')
SYS._print(MyBuilder,**{
	'RepresentingKeyStrsList':['MakingMyFloat','MadeMyInt']
})

#make once
MyBuilder.make(3.)

#Print
print('After the first make, MyBuilder is ')
SYS._print(MyBuilder,**{
	'RepresentingKeyStrsList':['MakingMyFloat','MadeMyInt']
})

#Definition the AttestedStr
SYS._attest(
	[
		'BuilderClass.make is '+str(BuilderClass.make),
		'MyBuilder is '+SYS._str(
		MyBuilder,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False,
			'RepresentingKeyStrsList':['MakingMyFloat','MadeMyInt']
		}
		)
	]
) 

#Print



