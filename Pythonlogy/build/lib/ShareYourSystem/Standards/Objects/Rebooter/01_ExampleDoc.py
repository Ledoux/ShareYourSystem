#ImportModules
import ShareYourSystem as SYS

#Definition 
@SYS.ClasserClass(**
{
	'ClassingSwitchMethodStrsList':['make']
})
class MakerClass(SYS.RebooterClass):

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
		SYS.RebooterClass.__init__(self,**_KwarVariablesDict)

	def do_make(self):
		
		#print
		print('I am in the do_make of the Maker')

		#cast
		self.MadeMyInt=int(self.MakingMyFloat)

#Definition
@SYS.ClasserClass(**{
	'ClassingSwitchMethodStrsList':["make"]
})
class BuilderClass(MakerClass):

	#Definition
	RepresentingKeyStrsList=[
							]

	def default_init(self,
					**_KwarVariablesDict
				):
		MakerClass.__init__(self,**_KwarVariablesDict)

	def mimic_make(self):
		
		#print
		print('I am in the mimic_make of the Builder')

		#call the parent method
		MakerClass.make(self)

		#cast
		self.MadeMyInt+=10

	def do_build(self):
		pass


#Definition an instance
MyBuilder=BuilderClass()

#Print
print('Before make, MyBuilder is ')
SYS._print(MyBuilder,**{
	'RepresentingKeyStrsList':[
	'MakingMyFloat',
	'MadeMyInt',
	]
})

#make once
MyBuilder.make(3.)

#Print
print('After the first make, MyBuilder is ')
SYS._print(MyBuilder,**{
	'RepresentingKeyStrsList':[
	'MakingMyFloat',
	'MadeMyInt',
	]
})

#make again
MyBuilder.make(5.)

#Print
print('After the second make, MyBuilder is ')
SYS._print(MyBuilder,**{
	'RepresentingKeyStrsList':[
	'MakingMyFloat',
	'MadeMyInt',
	]
})

#make again
print('Now we reboot')
MyBuilder.reboot(
					#_NameStrsList=['Maker','Builder'],
					#_DoStrsList=['Make'],
					#_AllDoBool=True,
					#_AllNameBool=True,
				)

#Print
print('After the reboot, MyBuilder is ')
SYS._print(MyBuilder,**{
	'RepresentingKeyStrsList':[
	'MakingMyFloat',
	'MadeMyInt',
	]
})

#make again
MyBuilder.make(8.)

#Definition the AttestedStr
SYS._attest(
	[
		'MyBuilder is '+SYS._str(
		MyBuilder,
		**{
			'RepresentingAlineaIsBool':False,
			'RepresentingKeyStrsList':[
				'MakingMyFloat',
				'MadeMyInt',
				'RebootedWatchBoolKeyStrsList'
			]
			}
		)
	]
) 