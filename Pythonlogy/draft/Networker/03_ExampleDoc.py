#/######################/#
# Import
#

#ImportModules
import ShareYourSystem as SYS

#/######################/#
# Define you hierarchic objects
#

#add
SYS.addSingPlural('Component','Components')

#Define a Moduler class
@SYS.ClasserClass()
class MultiplierClass(SYS.NetworkerClass):
								
	def default_init(self,
						_MultiplyingFirstFloat=0,
						_MultiplyingSecondFloat=0,
						_MultipliedTotalFloat=0,
						**_KwargVariablesDict
					):

		#Call the parent init method
		SYS.NetworkerClass.__init__(self,**_KwargVariablesDict)
			
		#Build the model		
		self['#map@set'](
			[
				('-Models',[
						('|Parameter',[
							('ModelKeyStrsList',['MultiplyingFirstFloat','MultiplyingSecondFloat'])
						]),
						('|Result',[
							('ModelKeyStrsList',['MultipliedTotalFloat']),
							('PointKeyVariablesList',['/^/|Parameter'])
						])
					]
				)
			]
		)

#Define a Moduler class
@SYS.ClasserClass()
class ModulerClass(SYS.NetworkerClass):
								
	def default_init(self,
						_ModulingPowerFloat=0.5,
						_ModuledTotalFloat=0,
						**_KwargVariablesDict
					):

		#Call the parent init method
		SYS.NetworkerClass.__init__(self,**_KwargVariablesDict)

		#Build the components and the models
		self['#map@set'](
			[
				#MODELS
				(
					'-Models',
					[
						('|Parameter',[
							('ModelKeyStrsList',['ModulingPowerFloat']),
							(
								'PointKeyVariablesList',
								[
									'/^/^/-Components/|Real/-Models/|Result',
									'/^/^/-Components/|Image/-Models/|Result',
								]
							)
						]), 
						('|Result',[
							('ModelKeyStrsList',['ModuledTotalFloat']),
							('PointKeyVariablesList',['/^/|Parameter'])
						])
					]
				),
				#COMPONENTS
				(
					'-Components',{
						'|Real':MultiplierClass(),
						'|Image':MultiplierClass()
					}
				)
			]
		)
						
#/######################/#
# Build your total model and insert
#

MyModuler=ModulerClass(
	).network(
		[
			'Components',
			'Models'
		]
	)

#/######################/#
# Print
#

#print
print('MyModuler is ')
SYS._print(MyModuler)

