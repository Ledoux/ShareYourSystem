#/######################/#
# Import
#

#ImportModules
import ShareYourSystem as SYS

#/######################/#
# Define you hierarchic objects
#

#Define a Sumer class
@SYS.ClasserClass()
class MultiplierClass(SYS.ControllerClass):
								
	def default_init(self,
						_MultiplyingFirstFloat=0,
						_MultiplyingSecondFloat=0,
						_MultipliedTotalFloat=0,
						**_KwargVariablesDict
					):

		#Call the parent init method
		SYS.ControllerClass.__init__(self,**_KwargVariablesDict)
			
		#Build the model		
		self['#map@set'](
			{
				'-Models':[
					('|Parameter',[
						('ModelKeyStrsList',['MultiplyingFirstFloat','MultiplyingSecondFloat'])
					]),
					('|Result',[
						('ModelKeyStrsList',['MultipliedTotalFloat']),
						('ParentingTriggerVariable',['<->/^/|Parameter'])
					])
				]
			}
		)

	def do_multiply(self):
		
		#debug
		'''
		self.debug(('self.',self,['MultiplyingFirstFloat','MultiplyingSecondFloat']))
		'''

		#set the SumedTotalFloat
		self.MultipliedTotalFloat=self.MultiplyingFirstFloat*self.MultiplyingSecondFloat

#Define a Moduler class
@SYS.ClasserClass()
class ModulerClass(SYS.ControllerClass):
								
	def default_init(self,
						_ModulingPowerFloat=0,
						_ModuledTotalFloat=0,
						**_KwargVariablesDict
					):

		#Call the parent init method
		SYS.ControllerClass.__init__(self,**_KwargVariablesDict)

		#Build the components and the models
		self['#map@set'](
			{
				#COMPONENTS
				'-Components':{
					'|Real':{},
					'|Image':{}
				},
				#MODELS
				'-Models':[
					('|Parameter',[
						('ModelKeyStrsList',['ModulingPowerFloat'])
					]),
					('|Result',[
						('ModelKeyStrsList',['ModuledTotalFloat']),
						(
							'ParentingTriggerVariable',
							[
								'<->/^/|Parameter',
								'<->/^/^/-Components/|Real/-Models/|Parameter',
								'<->/^/^/-Components/|Image/-Models/|Parameter',
							]
						)
					])
				]
			}
		)
						
	def do_module(self):
		
		#debug
		'''
		self.debug(('self.',self,['SumingFirstFloat','SumingSecondFloat']))
		'''

		#set the SumedTotalFloat
		self.ModuledTotalFloat=sum(
								[
									self['/-Components/|Real'].multiply().MultipliedTotalFloat,
									self['/-Components/|Real'].multiply().MultipliedTotalFloat
								]
							)**self.ModulingPowerFloat

#/######################/#
# Build your model
#


"""
print(MultiplierClass(
	)['#map@set'](
		[
			('/-Components/|Real/MultiplyingFirstFloat',2.),
			('MultiplyingSecondFloat',3.)
		]
	).multiply()
)

print(
	ModulerClass()['#map@set'](
		[
			('MultiplyingFirstFloat',2.),
			('MultiplyingSecondFloat',3.)
		]
	).multiply()
)
"""


print(ModulerClass())

"""
#Definition of a Storer instance with a noded data
MySumer=SumerClass(
	**{
			'HdformatingFileKeyStr':'Modulus_1.hdf5',
			'FolderingPathStr':SYS.Joiner.LocalFolderPathStr
		}
	)['#map@set'](
		{
			'-Models':[
				('|Parameter',[
					('ModelKeyStrsList',['SumingFirstFloat','SumingSecondFloat'])
				]),
				('|Result',[
					('ModelKeyStrsList',['SumedTotalFloat']),
					('ParentingTriggerVariable',['<->/^/|Parameter'])
				])
			]
		}
	).get('?v')

#/######################/#
# Insert in the model
#

MySumer['#map@set'](
		[
			('SumingFirstFloat',1),
			('SumingSecondFloat',3)
		]
	).sum(
	).command(
		'/-Models/|Result',
		[
			'#call:insert',
			('setSwitch',['insert'])
		]
	)['#map@set'](
		[
			('SumingFirstFloat',3),
			('SumingSecondFloat',5)
		]
	).sum(
	).command(
		'/-Models/|Result',
		'#call:insert'
	)

#/######################/#
# Print
#

#print
print('MySumer is ')
SYS._print(MySumer)

#view
print('hdf5 file is : \n'+SYS._str(MySumer.hdfview()))

#close
MySumer.file(_ModeStr='c')
"""