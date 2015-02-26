#<ImportSpecificModules>
import collections
import copy
import tables
import os
import ShareYourSystem as SYS
import sys
#</ImportSpecificModules>

#<DefineLocals>
ModelingJoinStr='__'
ModelingLinkStr='_'
#</DefineLocals>

#<DefineClass>
class ModelerClass(SYS.StructurerClass):
	
	#<DefineHookMethods>
	def initAfter(self):

		#<DefineSpecificDo>
		self.IsModelingBool=True							#<NotRepresented>
		self.ModeledDict={} 								#<NotRepresented>
		self.ModeledOrderedDict=collections.OrderedDict()	#<NotRepresented>
		#</DefineSpecificDo>

	def model(self,_ModelStr="",**_ModelingVariablesDict):
		"""Call the Output<HookStr> methods and return self.OutputedPointer (self by default)"""

		#debug
		print('Modeler model method')
		print('_ModelStr is ',_ModelStr)
		print('')

		#Reinit attributes
		LocalOutputedPointer=self
		if _ModelStr=="":
			_ModelStr=self.ModeledDict['ModelStr']
		else:
			self.ModeledDict=self['App_Model_'+SYS.getDoingStrWithDoStr(_ModelStr)+'Dict']
			if self.ModeledDict!=None:
				if 'IsModeledBool' not in self.ModeledDict:

					#set variables
					IsModeledBool=False
					ModelStr=_ModelStr
					ModelingStr=SYS.getDoingStrWithDoStr(ModelStr)
					ModeledStr=SYS.getDoneStrWithDoStr(ModelStr)
					ModeledSuffixStr=SYS.getClassStrWithTypeStr(ModeledStr+'Model')
					ModeledKeyStr=""

					#Put them in the ModeledDict
					LocalVars=vars()
					map(
							lambda __GettingStr:
							self.ModeledDict.__setitem__(__GettingStr,LocalVars[__GettingStr]),
							[
								'IsModeledBool',
								'ModelStr',
								'ModelingStr',
								'ModeledStr',
								'ModeledSuffixStr',
								'ModeledKeyStr'
							]
						)

		#set IsModelingBool
		self.IsModelingBool=True
		
		#Hook methods
		for OrderStr in ["Before","After"]:
		
			#Definition the HookMethodStr
			HookingMethodStr='model'+OrderStr

			#Check that there is HookingMethods for it
			if HookingMethodStr in self.__class__.HookingMethodStrToMethodsListDict:

				#Call the specific Appended methods 
				for HookingMethod in self.__class__.HookingMethodStrToMethodsListDict[HookingMethodStr]:

					#Call the HookMethod
					OutputVariable=HookingMethod(self,**_ModelingVariablesDict)

					if type(OutputVariable)==dict:
						if 'LocalModelingVariablesDict' in OutputVariable:
							LocalModelingVariablesDict=OutputVariable['LocalModelingVariablesDict']
						if 'LocalOutputedPointer' in OutputVariable:
							LocalOutputedPointer=OutputVariable['LocalOutputedPointer']

					#Check Bool
					if self.IsModelingBool==False:
						return LocalOutputedPointer

		#debug
		print('END Modeler model method')
		print('_ModelStr is ',_ModelStr)
		print('')

		#Return the OutputVariable
		return LocalOutputedPointer

	def modelBefore(self,**_ModelingVariablesDict):

		#debug
		'''
		print('Modeler modelBefore method')
		print("self.ModeledDict['ModelStr'] is ",self.ModeledDict['ModelStr'])
		print('')
		'''

		#set the global config of this model if it was not already
		if 'ModelClassesOrderedDict' not in self.ModeledDict:

			#debug
			print('This is the first model of this Model')
			print('ModelClassesOrderedDict not exists')
			print('')

			'''
			#Get the AlmostShapingColumningTuplesList and NotShapedColumningTuplesList
			[
				self.ModeledDict['AlmostShapingColumningTuplesList'],
				self.ModeledDict['NotShapedColumningTuplesList']
			]=SYS.groupby(
								lambda __ModeledTuple:
								type(__ModeledTuple[1])==tuple,
								self.ModeledDict['ColumningTuplesList']
							)
			'''

			#debug
			'''
			print("self.ModeledDict['AlmostShapingColumningTuplesList'] is ",self.ModeledDict['AlmostShapingColumningTuplesList'])
			print("self.ModeledDict['NotShapedColumningTuplesList'] is ",self.ModeledDict['NotShapedColumningTuplesList'])
			print('')
			'''

			#Init the ModelClassesOrderedDict
			self.ModeledDict['ModelClassesOrderedDict']=collections.OrderedDict()

		#debug
		print('We are going to define a ModeledDescriptionClass for this Model ?')
		print("self.ModeledDict['ModelStr'] is ",self.ModeledDict['ModelStr'])
		print("self.ModeledDict['IsModeledBool'] is ",self.ModeledDict['IsModeledBool'])
		print('')

		#Check
		if self.ModeledDict['IsModeledBool']==False:

			#debug
			print('Yes we define a new ModeledDescriptionClass...')
			print('')

			#Definition the ModelClass
			class ModeledDescriptionClass(tables.IsDescription):

				#Add a tabulared Int (just like a unique KEY in mysql...) 
				RowInt=tables.Int64Col()

			#set the not shaping cols in the ModelClass
			map(
					lambda __NotShapingColumningTuple:
					ModeledDescriptionClass.columns.__setitem__(
						__NotShapingColumningTuple[0],
						#copy.copy(__NotShapingColumningTuple[1])
						__NotShapingColumningTuple[1]
						),
					self.ModeledDict['ColumningTuplesList']
				)

			#set a name if it was not already
			if self.ModeledDict['ModeledKeyStr']=="":
				self.ModeledDict['ModeledKeyStr']=self.ModeledDict['ModeledSuffixStr']

			#Alias
			ModeledKeyStr=self.ModeledDict['ModeledKeyStr']

			#Give a name
			ModeledDescriptionClass.__name__=ModeledKeyStr		

			#set the ModelClass
			self.ModeledDict['ModelClassesOrderedDict'][ModeledKeyStr]=ModeledDescriptionClass

			#Put local variables in the ModeledDict
			LocalVars=vars()
			map(
					lambda __GettingStr:
					self.ModeledDict.__setitem__(__GettingStr,LocalVars[__GettingStr]),
					[
						'ModeledDescriptionClass'
					]
				)

	#</DefineHookMethods>

#</DefineClass>

#<DefineAttestingFunctions>
def attest_model():

	#Build Hdf groups
	Modeler=SYS.ModelerClass().update(
								[
									('App_Model_ParameterizingDict',
											{
												'ColumningTuplesList':
												[
													('MyInt',tables.Int64Col()),
													('MyStr',tables.StrCol(10)),
													('MyIntsList',tables.Int64Col(shape=3))
												]
											}
									)
								]
								).model('Parameter')
																
	#Return the object itself
	return 'Attest gives : \n\n\n\n'+SYS.represent(
							Modeler
						)+'\n\n\n\n'+SYS.represent(
							Modeler.ModeledDescriptionClass.__dict__
						)
#</DefineAttestingFunctions>
