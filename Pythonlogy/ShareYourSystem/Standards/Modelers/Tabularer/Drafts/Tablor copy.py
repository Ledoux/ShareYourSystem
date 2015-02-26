#<ImportSpecificModules>
import collections
import tables
import os
import ShareYourSystem as SYS
import sys
#</ImportSpecificModules>

#<DefineLocals>
ModelingJoinStr=SYS.Modeler.ModelingJoinStr
#</DefineLocals>

#<DefineClass>
class TablerClass(
					SYS.GrouperClass,
					SYS.ModelerClass
				):
	
	#<DefineHookMethods>
	def initAfter(self):

		#<DefineSpecificDo>
		pass
		#self.TabularedCalibratedModelClass=None
		#self.TabularedCalibratedTable=None
		#self.TabularedCalibratedKeyStr=""
		#self.TabularedRowedPointer=None
		#self.TabularedRowedTuplesList=[]
		#self.IsRowingBool=True
		#</DefineSpecificDo>

		self.RepresentingKeyVariablesList+=['ModeledOrderedDict']

	#</DefineHookMethods>

	#<DefineMethod>
	def modelAfter(self,**_ModelingVariablesList):

		#debug
		print('Tabler modelAfter method')
		print(self.ModeledDict)

		#Definition the ModelClass
		ModelClass=self.ModeledDict['ModelClassesOrderedDict'][self.ModeledDict['ShapingStr']]

		#Definition the TableStr
		TableStr=ModelingJoinStr.join(
						ModelClass.__name__.split(ModelingJoinStr)[1:-1]
					)+ModelingJoinStr+'Table'

		#Definition the TablePathStr
		TablePathStr=self.GroupedPathStr+'/'+TableStr

		#Create the Table if not already
		if TablePathStr not in self.HdformatedFileVariable:
			self.ModeledDict['Table']=self.HdformatedFileVariable.create_table(
												self.HdformatedFileVariable.getNode(self.GroupedPathStr),
												TableStr,
												ModelClass,
												ModelClass.__doc__ 
												if ModelClass.__doc__!=None 
												else "This is the "+ModelClass.__name__
									)
		else:
			self.ModeledDict['Table']=self.HdformatedFileVariable.getNode(
				TablePathStr)
		
	"""					
	def tabular(self,_TabularingStr):

		#debug
		print('tabular method')
		print('self.GroupedPathStr is ',self.GroupedPathStr)
		
		#Definition the DoneTabularingStr
		DoneTabularingStr=SYS.getDoneStrWithDoStr(_TabularingStr)
		
		#Check that the ModeledOrderedDict exists 
		ModeledOrderedSetTagStr="Modeled"+DoneTabularingStr+"OrderedDict"
		if hasattr(self,ModeledOrderedSetTagStr):
			ModeledOrderedDict=getattr(self,ModeledOrderedSetTagStr)

			#Hdformat maybe if it was not done
			if hasattr(self,'HdformatedFileVariable')==None:
				self.hdformat()
			print("iiii",self)

			#Check that the TabularedTablesOrderedDict exists 
			TabularedTablesOrderedSetTagStr="Tabulared"+DoneTabularingStr+"OrderedDict"
			if hasattr(self,TabularedTablesOrderedSetTagStr):
				TabularedTablesOrderedDict=getattr(self,TabularedTablesOrderedSetTagStr)

				#Definition the ModelingJoinStr
				ModelingJoinStr=SYS.Modeler.ModelingJoinStr

				#debug
				#print('ModelingJoinStr is : ',ModelingJoinStr)

				#Create the table or get it and set it again
				map(
						lambda __TableStrAndTableGroupedPathStrTuple,__ModeledDescriptionClass:
						TabularedTablesOrderedDict.__setitem__(
							ModelingJoinStr.join(
								__TableStrAndTableGroupedPathStrTuple[0].split(ModelingJoinStr)[:-1]
								),
							self.HdformatedFileVariable.create_table(
											self.HdformatedFileVariable.getNode(self.GroupedPathStr),
											__TableStrAndTableGroupedPathStrTuple[0],
											__ModeledDescriptionClass,
											__ModeledDescriptionClass.__doc__ 
											if __ModeledDescriptionClass.__doc__!=None 
											else "This is the "+__ModeledDescriptionClass.__name__
								)
						) 
						if __TableStrAndTableGroupedPathStrTuple[1] not in self.HdformatedFileVariable
						else
						#Get the Node and set it to the TabularedDict
						TabularedTablesOrderedDict.__setitem__(
								ModelingJoinStr.join(
								__TableStrAndTableGroupedPathStrTuple[0].split(ModelingJoinStr)[:-1]
								),
								self.HdformatedFileVariable.getNode(__TableStrAndTableGroupedPathStrTuple[1])
							),
						#Map on (__TableStr,__TableGroupedPathStr),__ModeledDescriptionClass
						map(
							lambda __TableStr:
							(
								__TableStr,
								SYS.getPastedPathStrWithPathStrsList(
									[self.GroupedPathStr,__TableStr])
							),
							map(
								lambda __ClassKeyStr:
								#'Class'.join(__ClassKeyStr.split('Class')[:-1])+'Table'
								__ClassKeyStr+ModelingJoinStr+DoneTabularingStr+'Table'
								,ModeledOrderedDict.keys()
								)	
						),
						ModeledOrderedDict.values()
					)

				#Do a smart joining link to the corresponding OrderedDict
				map(
						lambda __Table:
						#TabularedTablesOrderedDict.__setitem__(
							#'__'.join(__Table.name.split('__')[1:-1])
						DoneTabularingStr.join(__Table.name.split(DoneTabularingStr)[1:])
							#__Table.name
						#	,__Table
						#)
						,filter(
								lambda __Node:
								type(__Node)==tables.table.Table,
								self.HdformatedFileVariable.getNode(self.GroupedPathStr)._f_iterNodes()
						)
					)
				
			else:
				print('WARNING tabular method : not such TabularedClassStr ',
						TabularedClassStr)


		else:
			print('WARNING tabular method : not such ModeledOrderedSetTagStr ',
				ModeledOrderedSetTagStr)

		#Return self
		return self

	"""
	"""
		'''
			#debug
			#print('ModeledGettingStrsList is ',ModeledGettingStrsList)

			#Build the Table of it doesn't exist yet
			if TableStr not in TabularedTablesOrderedDict:

				#Build maybe the model
				ModeledOrderedSetTagStr="Modeled"+DoneTabularingStr+"OrderedDict"
				ModeledOrderedDict=getattr(self,ModeledOrderedSetTagStr)
				if TableStr not in ModeledOrderedDict:
					self.model(_CalibratingStr)

				#Tabular
				self.tabular(_CalibratingStr)

			#debug
			#print('TabularedTablesOrderedDict is ',TabularedTablesOrderedDict)

			#Definition the Table
			self.TabularedCalibratedModelClass=ModeledOrderedDict[TableStr]
			self.TabularedCalibratedTable=TabularedTablesOrderedDict[TableStr]
			self.TabularedCalibratedKeyStr=TableStr

		else:

			print('WARNING calibrate method : not such TabularedTablesOrderedSetTagStr ',
						TabularedTablesOrderedSetTagStr)
		'''
	"""

	def row(self,_RowingStr,**_RowingVariablesDict):
		"""Call the Output<HookStr> methods and return self.OutputedPointer (self by default)"""

		#Refresh the attributes and set maybe default values in the _RowingVariablesDict
		LocalOutputedPointer=self
		LocalRowingVariablesDict=dict({'RowingStr':_RowingStr},**_RowingVariablesDict)
		self.TabularedRowedTuplesList=[]
		self.IsRowingBool=True

		#Calibrate the good table
		self.calibrate(_RowingStr)

		#Hook methods
		for OrderStr in ["Before","After"]:
		
			#Definition the HookMethodStr
			HookingMethodStr='row'+OrderStr

			#Check that there is HookingMethods for it
			if HookingMethodStr in self.__class__.HookingMethodStrToMethodsListDict:

				#Call the specific Appended methods 
				for HookingMethod in self.__class__.HookingMethodStrToMethodsListDict[HookingMethodStr]:

					#Call the HookMethod
					OutputVariable=HookingMethod(self,**LocalRowingVariablesDict)

					if type(OutputVariable)==dict:
						if 'LocalRowingVariablesDict' in OutputVariable:
							LocalRowingVariablesDict=OutputVariable['LocalRowingVariablesDict']
						if 'LocalOutputedPointer' in OutputVariable:
							LocalOutputedPointer=OutputVariable['LocalOutputedPointer']

					#Check Bool
					if self.IsRowingBool==False:
						return LocalOutputedPointer

		#Return the OutputVariable
		return LocalOutputedPointer

	def rowBefore(self,**_RowingVariablesDict):

		#Check that the TabularedCalibratedTable is ok
		if self.TabularedCalibratedTable!=None:

			#set the TabularedRowedPointer
			self.TabularedRowedPointer=self.TabularedCalibratedTable.row

			#Get the ModelingTuplesList
			ModelingTuplesList=self.ModelingDict[
				SYS.getDoingStrWithDoStr(_RowingVariablesDict['RowingStr'])+'TuplesList'
				]

			#Get the InsertingTuplesList
			self.TabularedRowedTuplesList=zip(
									SYS.unzip(ModelingTuplesList,[0]),
									self.pick(SYS.unzip(ModelingTuplesList,[0]))
								)

	def insert(self):

		#Get the row
		Row=self.TabularedCalibratedTable.row

		#set the InsertingTuples in the Row
		map(
				lambda __InsertingTuple:
				Row.__setitem__(*__InsertingTuple),
				self.TabularedRowedTuplesList
			)

		#Append
		Row.append()
		self.TabularedCalibratedTable.insert()

	'''
	def insert(self,_InsertingStr,_JoiningStr=""):

		#Check that the TabularedCalibratedTable is ok
		if self.TabularedCalibratedTable!=None:

			#Definition the DoneJoiningStr 
			if _JoiningStr!="":
				DoneJoiningStr=SYS.getDoneStrWithDoStr(_JoiningStr)
				JoiningOrderedDict=getattr(self,DoneJoiningStr+'OrderedDict')
				DoneJoiningKeyStrKeyStr=DoneJoiningStr+'KeyStr'
			else:
				JoiningOrderedDict={}

			#Get the ModelingTuplesList
			ModelingTuplesList=self.ModelingDict[DoingModelingStr+'TuplesList']

			#Get the InsertingTuplesList
			InsertingTuplesList=zip(
									SYS.unzip(ModelingTuplesList,[0]),
									self.pick(SYS.unzip(ModelingTuplesList,[0]))
								)

			#If it is an output add the joins
			if _InsertingStr=="Output":

				#Join before
				self.join()

				InsertingTuplesList+=zip( 
										map(
												lambda __JoiningChildObjects:
												SYS.getRowIntColumnStrWithKeyStr(
													getattr(
														__JoiningChildObjects,
														DoneJoiningKeyStrKeyStr
													)
												),
												JoiningOrderedDict.values()
											),
										self.JoinedModeledFeaturedIntsTuplesList
									)+[('ModeledFeaturedIntsTuple',self.ModeledFeaturedIntsTuple)]
	'''


#</DefineClass>

#<DefineAttestingFunctions>
def attest_tabular():

	#Build Hdf groups
	Tabler=SYS.TablerClass().hdformat().update(
								[
									(
										'App_Structure_ChildGrouper1',
										SYS.GrouperClass().update(
										[
											(
												'App_Structure_GrandChildTabler1',
												SYS.TablerClass()
											)
										])
									)
								]	
							).walk(
										[
											'StructuredOrderedDict.items()'
										],
										**{
												'BeforeUpdateList':
												[
													('parentize',{'ArgsVariable':"Structure"}),
													('group',{'ArgsVariable':"Structure"})
												]
											}
									).update(
								map(
										lambda __Tuple:
										(
											'/App_Structure_ChildGrouper1/App_Structure_GrandChildTabler1/'+__Tuple[0],
											__Tuple[1]
										),
										[
											('MyInt',0),
											('MyStr',"hello"),
											('UnitsInt',3),
											('MyIntsList',[2,4,1]),
											('App_Model_FeaturingDict',
														{
															'ColumningTuplesList':
															[
																('MyInt',tables.Int64Col()),
																('MyStr',tables.StrCol(10)),
																('MyIntsList',(tables.Int64Col,'UnitsInt'))
															]
														}
														),
											('model',{'ArgsVariable':"Feature"}),
											#('calibrate',{'ArgsVariable':"Feature"}),
											#('UnitsInt',2),
											#('MyIntsList',[2,4]),
											#('calibrate',{'ArgsVariable':"Feature"}),
											#('row',{'ArgsVariable':"Feature"}),
											#('insert',{})
										]
									)
							).hdfclose()
																
	#Return the object itself
	#Get the h5ls version of the stored hdf
	print(Tabler)
	print(os.popen('h5ls -dlr '+Tabler.HdformatingPathStr).read())
	return os.popen('h5ls -dlr '+Tabler.HdformatingPathStr).read()
	#</DefineMethods>

#</DefineAttestingFunctions>
