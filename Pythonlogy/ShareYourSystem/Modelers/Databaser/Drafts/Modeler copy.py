#<ImportSpecificModules>
import collections
import copy
import tables
import os
import ShareYourSystem as SYS
import sys
#</ImportSpecificModules>

#<DefineLocals>
DatabasingJoinStr='__'
DatabasingLinkStr='_'
#</DefineLocals>

#<DefineClass>
class ModelerClass(SYS.StructurerClass):
	
	#<DefineHookMethods>
	def initAfter(self):

		#<DefineSpecificDo>
		self.IsDatabasingBool=True							#<NotRepresented>
		self.DatabasedDict={} 								#<NotRepresented>
		self.DatabasedOrderedDict=collections.OrderedDict()	#<NotRepresented>
		#</DefineSpecificDo>

	def model(self,_ModelStr="",**_DatabasingVariablesDict):
		"""Call the Output<HookStr> methods and return self.OutputedPointer (self by default)"""

		#debug
		print('Modeler model method')
		print('_ModelStr is ',_ModelStr)
		print('')

		#Reinit attributes
		LocalOutputedPointer=self
		if _ModelStr=="":
			_ModelStr=self.DatabasedDict['ModelStr']
		else:
			self.DatabasedDict=self['App_Model_'+SYS.getDoingStrWithDoStr(_ModelStr)+'Dict']
			if self.DatabasedDict!=None:
				if 'IsDatabasedBool' not in self.DatabasedDict:

					#set variables
					IsDatabasedBool=False
					ModelStr=_ModelStr
					DatabasingStr=SYS.getDoingStrWithDoStr(ModelStr)
					DatabasedStr=SYS.getDoneStrWithDoStr(ModelStr)
					ModeledSuffixStr=SYS.getClassStrWithTypeStr(DatabasedStr+'Model')
					DatabasedKeyStr=""

					#Put them in the DatabasedDict
					LocalVars=vars()
					map(
							lambda __GettingStr:
							self.DatabasedDict.__setitem__(__GettingStr,LocalVars[__GettingStr]),
							[
								'IsDatabasedBool',
								'ModelStr',
								'DatabasingStr',
								'DatabasedStr',
								'ModeledSuffixStr',
								'DatabasedKeyStr'
							]
						)

		#set IsDatabasingBool
		self.IsDatabasingBool=True
		
		#Hook methods
		for OrderStr in ["Before","After"]:
		
			#Definition the HookMethodStr
			HookingMethodStr='model'+OrderStr

			#Check that there is HookingMethods for it
			if HookingMethodStr in self.__class__.HookingMethodStrToMethodsListDict:

				#Call the specific Appended methods 
				for HookingMethod in self.__class__.HookingMethodStrToMethodsListDict[HookingMethodStr]:

					#Call the HookMethod
					OutputVariable=HookingMethod(self,**_DatabasingVariablesDict)

					if type(OutputVariable)==dict:
						if 'LocalDatabasingVariablesDict' in OutputVariable:
							LocalDatabasingVariablesDict=OutputVariable['LocalDatabasingVariablesDict']
						if 'LocalOutputedPointer' in OutputVariable:
							LocalOutputedPointer=OutputVariable['LocalOutputedPointer']

					#Check Bool
					if self.IsDatabasingBool==False:
						return LocalOutputedPointer

		#debug
		print('END Modeler model method')
		print('_ModelStr is ',_ModelStr)
		print('')

		#Return the OutputVariable
		return LocalOutputedPointer

	def modelBefore(self,**_DatabasingVariablesDict):

		#debug
		'''
		print('Modeler modelBefore method')
		print("self.DatabasedDict['ModelStr'] is ",self.DatabasedDict['ModelStr'])
		print('')
		'''

		#set the global config of this model if it was not already
		if 'ModelClassesOrderedDict' not in self.DatabasedDict:

			#debug
			print('This is the first model of this Model')
			print('ModelClassesOrderedDict not exists')
			print('')

			'''
			#Get the AlmostShapingColumningTuplesList and NotShapedColumningTuplesList
			[
				self.DatabasedDict['AlmostShapingColumningTuplesList'],
				self.DatabasedDict['NotShapedColumningTuplesList']
			]=SYS.groupby(
								lambda __DatabasedTuple:
								type(__DatabasedTuple[1])==tuple,
								self.DatabasedDict['ColumningTuplesList']
							)
			'''

			#debug
			'''
			print("self.DatabasedDict['AlmostShapingColumningTuplesList'] is ",self.DatabasedDict['AlmostShapingColumningTuplesList'])
			print("self.DatabasedDict['NotShapedColumningTuplesList'] is ",self.DatabasedDict['NotShapedColumningTuplesList'])
			print('')
			'''

			#Init the ModelClassesOrderedDict
			self.DatabasedDict['ModelClassesOrderedDict']=collections.OrderedDict()

		#debug
		print('We are going to define a DatabasedModelClass for this Model ?')
		print("self.DatabasedDict['ModelStr'] is ",self.DatabasedDict['ModelStr'])
		print("self.DatabasedDict['IsDatabasedBool'] is ",self.DatabasedDict['IsDatabasedBool'])
		print('')

		#Check
		if self.DatabasedDict['IsDatabasedBool']==False:

			#debug
			print('Yes we define a new DatabasedModelClass...')
			print('')

			#Definition the ModelClass
			class DatabasedModelClass(tables.IsDescription):

				#Add a tabulared Int (just like a unique KEY in mysql...) 
				RowInt=tables.Int64Col()

			#set the not shaping cols in the ModelClass
			map(
					lambda __NotShapingColumningTuple:
					DatabasedModelClass.columns.__setitem__(
						__NotShapingColumningTuple[0],
						#copy.copy(__NotShapingColumningTuple[1])
						__NotShapingColumningTuple[1]
						),
					self.DatabasedDict['ColumningTuplesList']
				)

			#set a name if it was not already
			if self.DatabasedDict['DatabasedKeyStr']=="":
				self.DatabasedDict['DatabasedKeyStr']=self.DatabasedDict['ModeledSuffixStr']

			#Alias
			DatabasedKeyStr=self.DatabasedDict['DatabasedKeyStr']

			#Give a name
			DatabasedModelClass.__name__=DatabasedKeyStr		

			#set the ModelClass
			self.DatabasedDict['ModelClassesOrderedDict'][DatabasedKeyStr]=DatabasedModelClass

			#Put local variables in the DatabasedDict
			LocalVars=vars()
			map(
					lambda __GettingStr:
					self.DatabasedDict.__setitem__(__GettingStr,LocalVars[__GettingStr]),
					[
						'DatabasedModelClass'
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
							Modeler.DatabasedModelClass.__dict__
						)
#</DefineAttestingFunctions>
