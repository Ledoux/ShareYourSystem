#<ImportSpecificModules>
import collections
import tables
import os
import ShareYourSystem as SYS
import sys
#</ImportSpecificModules>

#<DefineLocals>
DatabasingJoinStr=SYS.Modeler.DatabasingJoinStr
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

		self.RepresentingKeyVariablesList+=['DatabasedOrderedDict']

	#</DefineHookMethods>

	#<DefineMethod>
	def modelAfter(self,**_DatabasingVariablesList):

		#debug
		print('Tabler modelAfter method')
		print(self.DatabasedDict)

		#Definition the ModelClass
		ModelClass=self.DatabasedDict['ModelClassesOrderedDict'][self.DatabasedDict['ShapingStr']]

		#Definition the TableStr
		TableStr=DatabasingJoinStr.join(
						ModelClass.__name__.split(DatabasingJoinStr)[1:-1]
					)+DatabasingJoinStr+'Table'

		#Definition the TablePathStr
		TablePathStr=self.GroupedPathStr+'/'+TableStr

		#Create the Table if not already
		if TablePathStr not in self.HdformatedFileVariable:
			self.DatabasedDict['Table']=self.HdformatedFileVariable.create_table(
												self.HdformatedFileVariable.getNode(self.GroupedPathStr),
												TableStr,
												ModelClass,
												ModelClass.__doc__ 
												if ModelClass.__doc__!=None 
												else "This is the "+ModelClass.__name__
									)
		else:
			self.DatabasedDict['Table']=self.HdformatedFileVariable.getNode(
				TablePathStr)
		
	"""					
	def tabular(self,_TabularingStr):

		#debug
		print('tabular method')
		print('self.GroupedPathStr is ',self.GroupedPathStr)
		
		#Definition the DoneTabularingStr
		DoneTabularingStr=SYS.getDoneStrWithDoStr(_TabularingStr)
		
		#Check that the DatabasedOrderedDict exists 
		DatabasedOrderedDictKeyStr="Databased"+DoneTabularingStr+"OrderedDict"
		if hasattr(self,DatabasedOrderedDictKeyStr):
			DatabasedOrderedDict=getattr(self,DatabasedOrderedDictKeyStr)

			#Hdformat maybe if it was not done
			if hasattr(self,'HdformatedFileVariable')==None:
				self.hdformat()
			print("iiii",self)

			#Check that the TabularedTablesOrderedDict exists 
			TabularedTablesOrderedDictKeyStr="Tabulared"+DoneTabularingStr+"OrderedDict"
			if hasattr(self,TabularedTablesOrderedDictKeyStr):
				TabularedTablesOrderedDict=getattr(self,TabularedTablesOrderedDictKeyStr)

				#Definition the DatabasingJoinStr
				DatabasingJoinStr=SYS.Modeler.DatabasingJoinStr

				#debug
				#print('DatabasingJoinStr is : ',DatabasingJoinStr)

				#Create the table or get it and set it again
				map(
						lambda __TableStrAndTableGroupedPathStrTuple,__DatabasedModelClass:
						TabularedTablesOrderedDict.__setitem__(
							DatabasingJoinStr.join(
								__TableStrAndTableGroupedPathStrTuple[0].split(DatabasingJoinStr)[:-1]
								),
							self.HdformatedFileVariable.create_table(
											self.HdformatedFileVariable.getNode(self.GroupedPathStr),
											__TableStrAndTableGroupedPathStrTuple[0],
											__DatabasedModelClass,
											__DatabasedModelClass.__doc__ 
											if __DatabasedModelClass.__doc__!=None 
											else "This is the "+__DatabasedModelClass.__name__
								)
						) 
						if __TableStrAndTableGroupedPathStrTuple[1] not in self.HdformatedFileVariable
						else
						#Get the Node and set it to the TabularedDict
						TabularedTablesOrderedDict.__setitem__(
								DatabasingJoinStr.join(
								__TableStrAndTableGroupedPathStrTuple[0].split(DatabasingJoinStr)[:-1]
								),
								self.HdformatedFileVariable.getNode(__TableStrAndTableGroupedPathStrTuple[1])
							),
						#Map on (__TableStr,__TableGroupedPathStr),__DatabasedModelClass
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
								__ClassKeyStr+DatabasingJoinStr+DoneTabularingStr+'Table'
								,DatabasedOrderedDict.keys()
								)	
						),
						DatabasedOrderedDict.values()
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
			print('WARNING tabular method : not such DatabasedOrderedDictKeyStr ',
				DatabasedOrderedDictKeyStr)

		#Return self
		return self

	"""
	"""
		'''
			#debug
			#print('DatabasedGettingStrsList is ',DatabasedGettingStrsList)

			#Build the Table of it doesn't exist yet
			if TableStr not in TabularedTablesOrderedDict:

				#Build maybe the model
				DatabasedOrderedDictKeyStr="Databased"+DoneTabularingStr+"OrderedDict"
				DatabasedOrderedDict=getattr(self,DatabasedOrderedDictKeyStr)
				if TableStr not in DatabasedOrderedDict:
					self.model(_CalibratingStr)

				#Tabular
				self.tabular(_CalibratingStr)

			#debug
			#print('TabularedTablesOrderedDict is ',TabularedTablesOrderedDict)

			#Definition the Table
			self.TabularedCalibratedModelClass=DatabasedOrderedDict[TableStr]
			self.TabularedCalibratedTable=TabularedTablesOrderedDict[TableStr]
			self.TabularedCalibratedKeyStr=TableStr

		else:

			print('WARNING calibrate method : not such TabularedTablesOrderedDictKeyStr ',
						TabularedTablesOrderedDictKeyStr)
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

			#Get the DatabasingTuplesList
			DatabasingTuplesList=self.DatabasingDict[
				SYS.getDoingStrWithDoStr(_RowingVariablesDict['RowingStr'])+'TuplesList'
				]

			#Get the FlushingTuplesList
			self.TabularedRowedTuplesList=zip(
									SYS.unzip(DatabasingTuplesList,[0]),
									self.pick(SYS.unzip(DatabasingTuplesList,[0]))
								)

	def flush(self):

		#Get the row
		Row=self.TabularedCalibratedTable.row

		#set the FlushingTuples in the Row
		map(
				lambda __FlushingTuple:
				Row.__setitem__(*__FlushingTuple),
				self.TabularedRowedTuplesList
			)

		#Append
		Row.append()
		self.TabularedCalibratedTable.flush()

	'''
	def flush(self,_FlushingStr,_JoiningStr=""):

		#Check that the TabularedCalibratedTable is ok
		if self.TabularedCalibratedTable!=None:

			#Definition the DoneJoiningStr 
			if _JoiningStr!="":
				DoneJoiningStr=SYS.getDoneStrWithDoStr(_JoiningStr)
				JoiningOrderedDict=getattr(self,DoneJoiningStr+'OrderedDict')
				DoneJoiningKeyStrKeyStr=DoneJoiningStr+'KeyStr'
			else:
				JoiningOrderedDict={}

			#Get the DatabasingTuplesList
			DatabasingTuplesList=self.DatabasingDict[DoingDatabasingStr+'TuplesList']

			#Get the FlushingTuplesList
			FlushingTuplesList=zip(
									SYS.unzip(DatabasingTuplesList,[0]),
									self.pick(SYS.unzip(DatabasingTuplesList,[0]))
								)

			#If it is an output add the joins
			if _FlushingStr=="Output":

				#Join before
				self.join()

				FlushingTuplesList+=zip( 
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
										self.JoinedDatabasedFeaturedIntsTuplesList
									)+[('DatabasedFeaturedIntsTuple',self.DatabasedFeaturedIntsTuple)]
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
											#('flush',{})
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
