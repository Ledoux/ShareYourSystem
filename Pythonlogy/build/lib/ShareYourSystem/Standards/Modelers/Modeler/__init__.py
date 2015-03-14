# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Modeler defines the model to be stored in a database like Django or PyTable.
Here are defined the relations between attributes of an instance and their corresponding
types in the databased structures.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Parenter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import copy
from ShareYourSystem.Standards.Classors import Doer
from ShareYourSystem.Standards.Itemizers import Getter
from ShareYourSystem.Standards.Controllers import Controller
#</ImportSpecificModules>

#<DefineLocals>
AnalyzingColStrsList=[
						'Int',
						'Float',
						'Str'
					]
ModelJoinStr='__'
ModelLinkStr='_'
ModelOrderStr='xx'
ModelDimensionStr='_'
#</DefineLocals>

#<DefineFunctions>
def getModeledColWithGetKeyStr(_GetKeyStr):

	#import
	import tables

	#Definition
	global AnalyzingColStrsList

	#Definition
	ModeledColStr=SYS._filter(
		lambda __AnalyzingColStr:
			_GetKeyStr.endswith(__AnalyzingColStr),
			AnalyzingColStrsList
		)[0]

	#Debug
	'''
	print('l 55 getModeledColWithGetKeyStr')
	print('ModeledColStr is ')
	print(ModeledColStr)
	print('')
	'''

	#Get the Col Class
	if ModeledColStr=='Str':
		ModeledColClass=getattr(
							tables,
							'StringCol'
						)
	else:
		ModeledColClass=getattr(
							tables,
							ModeledColStr+'Col'
						)

	#Return
	if ModeledColStr=='Str':
		return ModeledColClass(100)
	else:
		return ModeledColClass() 

def getModelingColumnTupleWithGetKeyStr(_GetKeyStr):
	return (
			_GetKeyStr,
			_GetKeyStr,
			getModeledColWithGetKeyStr(_GetKeyStr)
	)

#</DefineFunctions>

#<DefineClass>
@DecorationClass(**{
	'ClassingSwitchMethodStrsList':["model"]
})
class ModelerClass(BaseClass):
	
	def default_init(
					self,
					_ModelKeyStrsList=None,
					_ModelDeriveControllerVariable=None,
					_ModelTagStr="",
					_ModelingDescriptionTuplesList={
						'DefaultValueType':property,
						'PropertyInitVariable':[],
						'PropertyDocStr':'I described variables for storing them in hdf'
					}, 		
					_ModelingMongoBool=True,
					_ModelingHdfBool=False,						
					_ModeledDescriptionClassesOrderedDict=None,																
					_ModeledDescriptionClass=None,
					_ModeledMongoDeriveNoderVariable=None,
					_ModeledHdfGroupVariable=None,
					_ModeledMongoTopClientVariable=None,
					_ModeledMongoLocalDatabaseVariable=None,
					_ModeledHdfTopFileVariable=None,
					_ModeledMongoSuffixStr="",
					_ModeledHdfSuffixStr="",
					_ModeledHdfKeyStrsList=None,
					_ModeledMongoKeyStrsList=None,
					_ModeledMongoCollectionsOrderedDict=None,
					_ModeledHdfTablesOrderedDict=None,
					_ModeledMongoKeyStr="", 	
					_ModeledHdfKeyStr="", 
					_ModeledMongoIndexInt=-1, 	
					_ModeledHdfIndexInt=-1, 			
					_ModeledMongoCollection=None, 	
					_ModeledHdfTable=None, 							
					_ModeledDescriptionGetKeyStrsList=None, 
					_ModeledDescriptionDimensionGetKeyStrsListsList=None,
					_ModeledDescriptionDimensionIntsListsList=None,  
					_ModeledShapeIndexIntsList=None,
					_ModeledDimensionGetKeyStrsList=None, 
					_ModeledDimensionIntsList=None,
					_ModeledShapeStr="",
					_ModelDimensionTuplesList=None,	 													
					**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_model(self):
		""" """

		#Debug
		'''
		self.debug('model start')
		'''

		#/###################/#
		# Mongo Case
		#

		#Check
		if self.ModelingMongoBool:

			#debug
			'''
			self.debug(
					'We model mongo here'
				)
			'''

			#set
			self.ModeledMongoSuffixStr=self.ModelTagStr+'Collection'

			#debug
			'''
			self.debug(
				[
					('self.',self,[
							'PymongoneClientVariable',
							'ModeledMongoSuffixStr'
						]
					)
				]
			)
			'''

			#Check
			if self.ModelDeriveControllerVariable.PymongoneClientVariable==None:

				#debug
				'''
				self.debug('We have to pymongo first...')
				'''

				#pymongo
				self.ModelDeriveControllerVariable.pymongo()

			#Link
			self.ModeledMongoTopClientVariable=self.ModelDeriveControllerVariable.PymongoneClientVariable
			
			#Check
			if self.ModeledMongoTopClientVariable!=None:

				#debug
				'''
				self.debug(
							[	
								'Looking for names of collections here',
								('self.',self,[
									'ModeledMongoTopClientVariable'
									]),
							]
						)
				'''

				#set
				self.ModeledMongoDatabaseKeyStr=self.ModelDeriveControllerVariable.ControlTagStr

				#set
				self.ModelDeriveControllerVariable.PymongoingDatabaseKeyStr=self.ModeledMongoDatabaseKeyStr

				#set
				self.ModeledMongoLocalDatabaseVariable=self.ModeledMongoTopClientVariable[
						self.ModeledMongoDatabaseKeyStr
				]

				#debug
				'''
				self.debug(
						[
							('self.',self,[
								'ModeledMongoDatabaseKeyStr',
								'ModeledMongoLocalDatabaseVariable'
								]),
							"id(self.ModeledMongoLocalDatabaseVariable) is "+str(
								id(self.ModeledMongoLocalDatabaseVariable))
						]
					)
				'''

				#set
				self.ModeledMongoLocalDatabaseVariable.__dict__[
					'ParentDerivePymongoer'
				]=self.ModelDeriveControllerVariable

				#alias
				self.ModelDeriveControllerVariable.Database=self.ModeledMongoLocalDatabaseVariable

				#debug
				'''
				self.debug(
							[	
								('self.',self,[
									'ModeledMongoLocalDatabaseVariable'
									]),
								"'ParentDerivePymongoer' in self.ModeledMongoLocalDatabaseVariable.__dict__",
								'ParentDerivePymongoer' in self.ModeledMongoLocalDatabaseVariable.__dict__
							]
						)
				'''

				#Get and sort
				self.ModeledMongoKeyStrsList=map(
					str,
					sorted(
						filter(
								lambda __KeyStr:
								__KeyStr.endswith(
									self.ModeledMongoSuffixStr
								),
								self.ModeledMongoLocalDatabaseVariable.collection_names()
							)
						)
				)
				
				#debug
				'''
				self.debug(
					[	
						('self.',self,[
							'ModeledMongoKeyStrsList'
							])
					]
				)
				'''
				
				#update
				self.ModeledMongoCollectionsOrderedDict.update(
					map(
							lambda __ModeledKeyStr:
							(
								__ModeledKeyStr,
								self.ModeledMongoLocalDatabaseVariable[
									__ModeledKeyStr
								]
							),
							self.ModeledMongoKeyStrsList
						)
				)

				#debug
				'''
				self.debug(("self.",self,[
											'ModeledMongoSuffixStr',
											'ModeledMongoKeyStrsList'
											]))
				'''

			#debug
			'''
			self.debug(
						[
							'ModeledMongoKeyStrsList',
							'ModeledMongoSuffixStr',
							'ModeledMongoKeyStr'
						]
					)
			'''

			#Get the suffix Strs of all the tables and their index
			ModeledMongoList=SYS.unzip(map(
					lambda __StrsList:
					(
						__StrsList[1],
						ModelOrderStr.join(__StrsList[2:])
					),
					map(
							lambda __ModeledMongoKeyStr:
							__ModeledMongoKeyStr.split(ModelOrderStr),
							self.ModeledMongoKeyStrsList
						)
				),[0,1]
			)

			#debug
			'''
			self.debug(('vars ',vars(),['ModeledHdfList']))
			'''
			
			#Unpack if it is possible
			if len(ModeledMongoList)>0:

				#Unpack
				[ModeledMongoIndexIntsTuple,ModeledMongoSuffixStrsList]=ModeledMongoList

				#debug
				'''
				self.debug(
							[
								'There are already some tables',
								'ModeledMongoSuffixStrsList is '+str(ModeledMongoSuffixStrsList),
								"self.ModeledMongoSuffixStr is "+str(
									self.ModeledMongoSuffixStr)
							]
						)
				'''

				if self.ModeledMongoSuffixStr not in ModeledMongoSuffixStrsList:

					#Increment the IndexStr
					ModeledMongoIndexInt=max(map(int,ModeledMongoIndexIntsTuple))+1

					#Strify
					ModeledMongoIndexStr=str(ModeledMongoIndexInt)

					#debug
					'''
					self.debug('IndexStr of this new table is '+str(IndexStr))
					'''
					
				else:

					#Get the already setted one
					ModeledMongoIndexStr=self.ModeledMongoKeyStrsList[
							ModeledMongoSuffixStrsList.index(self.ModeledMongoSuffixStr)
						].split(ModelOrderStr)[1]

					#Intify
					ModeledMongoIndexInt=(int)(ModeledMongoIndexStr)

					#debug
					'''
					self.debug('IndexStr of this not new table is '+str(IndexStr))
					'''

			else:

				#debug
				'''
				self.debug('There are no tables here')
				'''

				#set to empty lists 
				[ModeledMongoIndexIntsTuple,ModeledMongoSuffixStrsList]=[[],[]]

				#Init the list
				ModeledMongoIndexInt=0

				#Strify
				ModeledMongoIndexStr="0"

			#Bind with ModeledHdfKeyStr setting
			self.ModeledMongoKeyStr=ModelOrderStr+ModeledMongoIndexStr+ModelOrderStr+self.ModeledMongoSuffixStr

			#set the ModeledInt
			self.ModeledMongoIndexInt=ModeledMongoIndexInt

			#debug
			'''
			self.debug("self.ModeledMongoKeyStr is "+str(self.ModeledMongoKeyStr))
			'''
			
			#debug
			'''
			self.debug(
						[
							'Here we create the collection or get it depending if it is new or not',
							'self.ModeledMongoKeyStr is '+self.ModeledMongoKeyStr,
							'self.ModeledTopFileVariable!=None is '+str(self.ModeledTopFileVariable!=None)
						]
					)
			'''

			#Check
			if self.ModeledMongoKeyStr!="" and self.ModeledMongoLocalDatabaseVariable!=None:

				#debug
				'''
				self.debug(
							[
								('self.',self,[
									'ModeledMongoKeyStr',
									'ModeledMongoKeyStrsList'
									]
								),
								'self.ModeledMongoLocalDatabaseVariable.collection_names() is ',
								str(self.ModeledMongoLocalDatabaseVariable.collection_names())
							]
						)
				'''
				
				#Create the collection if not already
				if self.ModeledMongoKeyStr not in self.ModeledMongoKeyStrsList:

					#debug
					'''
					self.debug(
								[
									'The collection not exists',
								]
							)
					'''

					#Create the collections
					self.ModeledMongoCollection=self.ModeledMongoLocalDatabaseVariable.create_collection(
						self.ModeledMongoKeyStr
					)

					#Append
					self.ModeledMongoKeyStrsList.append(self.ModeledMongoKeyStr)

				else:

					#debug
					'''
					self.debug(
						[
							'The collection exists',
						]
					)
					'''

					#Else just get it 
					self.ModeledMongoCollection=self.ModeledMongoLocalDatabaseVariable[
						self.ModeledMongoKeyStr
					]
					
				#set the in the ModeledMongoCollectionsOrderedDict
				self.ModeledMongoCollectionsOrderedDict[
					self.ModeledMongoKeyStr
				]=self.ModeledMongoCollection

				#debug
				'''
				self.debug("self.ModeledMongoCollectionsOrderedDict is "+str(self.ModeledMongoCollectionsOrderedDict))
				'''
				
			#debug
			'''
			self.debug(
						[
							'Table is done here for mongo...',
							('self.',self,[
								'ModeledMongoCollection',
								'ModeledMongoTopDatabaseVariable'
								]
							)
						]
					)
			'''

		#/###################/#
		# Hdf Case
		#

		#Check
		if self.ModelingHdfBool:

			#/################/#
			# Model is to modify modeling description so keep an old version of this before
			#

			#keep a memory
			if self.ModelingDescriptionTuplesList!=None:
				self.ModeledDescriptionTuplesList=copy.deepcopy(
					self.ModelingDescriptionTuplesList
				)

			#/################/#
			# Pick the shape ints and their get key strs
			#

			#debug
			'''
			self.debug(
						[
							'We model shape here',
							("self.",self,['ModelDimensionTuplesList'])
						]
					)
			'''

			#Check
			if len(self.ModelDimensionTuplesList)>0:

				#set
				[
					self.ModeledDescriptionGetKeyStrsList,
					ModeledDescriptionDimensionGetTuplesList 
					
				]=SYS.unzip(self.ModelDimensionTuplesList,[0,1])

				#list
				self.ModeledDescriptionGetKeyStrsList=list(self.ModeledDescriptionGetKeyStrsList)

				#debug
				'''
				self.debug(
					[
						'ModeledDescriptionDimensionGetTuplesList is ',
						str(ModeledDescriptionDimensionGetTuplesList)
					]
				)
				'''

				#unzip
				self.ModeledDescriptionDimensionGetKeyStrsListsList=SYS.unzip(
						list(ModeledDescriptionDimensionGetTuplesList),[1]
					)

				#debug
				'''
				self.debug(
					[
						('self.',self,['ModeledDescriptionDimensionGetKeyStrsListsList'])
					]
				)
				'''

				#get the corresponding real dimensions
				self.ModeledDescriptionDimensionIntsListsList=map(
						lambda __ModeledDescriptionDimensionGetKeyStrsList:
						self.ModelDeriveControllerVariable[
							Getter.GetMapStr
						](
							*__ModeledDescriptionDimensionGetKeyStrsList
						).ItemizedMapValueVariablesList,
						self.ModeledDescriptionDimensionGetKeyStrsListsList
					)

				#debug
				'''
				self.debug(
					[
						('self.',self,['ModeledDescriptionDimensionIntsListsList'])
					]
				)
				'''

			else:

				#Default
				self.ModeledDescriptionGetKeyStrsList=[]
				self.ModeledDimensionGetKeyStrsList=[]
				self.ModeledDescriptionDimensionGetKeyStrsListsList=[]

			#debug
			'''
			self.debug(
				[
					("self.",self,[
										'ModeledDescriptionGetKeyStrsList',
										'ModeledDescriptionDimensionGetKeyStrsListsList',
										'ModeledDescriptionDimensionIntsListsList'
									])
				]
			)
			'''

			#/################/#
			# Find where in the description takes list it has to be modified
			#

			#Definition
			ModeledGetKeyStrsList=SYS.unzip(self.ModelingDescriptionTuplesList,[0])

			#set
			self.ModeledShapeIndexIntsList=map(
					lambda __ModeledDescriptionGetKeyStr:
					ModeledGetKeyStrsList.index(__ModeledDescriptionGetKeyStr),
					self.ModeledDescriptionGetKeyStrsList
				)

			#debug
			'''
			self.debug(
					[
						'We know the index of the shape description tuples',
						('self.',self,['ModeledShapeIndexIntsList'])
					]
				)
			'''

			#/################/#
			# set flat all the get key str for the shaping int 
			#

			#Check
			if self.ModelDeriveControllerVariable!=None:

				#debug
				'''
				self.debug(
						[	
							'We flat the DimensionGetKeyStrsLists',
							('self.',self,[
								'ModeledDescriptionDimensionGetKeyStrsListsList'
								])
						]
					)
				'''

				#Flat and set
				self.ModeledDimensionGetKeyStrsList=list(
					set(
						SYS.flat(
							self.ModeledDescriptionDimensionGetKeyStrsListsList
							)
						)
					)

				#debug
				'''
				self.debug(
						[
							('self.',self,[
								'ModeledDimensionGetKeyStrsList'
								])
						]
					)
				'''

				#Pick
				self.ModeledDimensionIntsList=self.ModelDeriveControllerVariable[
					Getter.GetMapStr
				](
					*self.ModeledDimensionGetKeyStrsList
				).ItemizedMapValueVariablesList

			else:

				#Default
				self.ModeledDimensionIntsList=[]
						

			#/################/#
			# map a join str with this
			#

			#debug
			'''
			self.debug(
				[
					'No we set the ModeledShapeStr',
					("self.",self,[
						'ModeledDimensionGetKeyStrsList',
						'ModeledDimensionIntsList'
					])
				]
			)
			'''

			#Bind with ModeledShapeStr setting
			self.ModeledShapeStr=ModelJoinStr.join(
				map(
						lambda __ModeledDescriptionGetKeyStr,__ModeledDimensionVariable:
						ModelJoinStr+str(
							__ModeledDescriptionGetKeyStr
							)+ModelDimensionStr+str(
							__ModeledDimensionVariable),
						self.ModeledDimensionGetKeyStrsList,
						self.ModeledDimensionIntsList
					)
			)

			#debug 
			'''
			self.debug(
				[
					('self.',self,['ModeledShapeStr'])
				]
			)
			'''

			#/#################/#
			# Adapt the name of the description model given the shape
			#

			#debug
			'''
			self.debug(
					[
						'Ok we have shaped',
						('self.',self,['ModeledShapeStr'])
					]
				)
			'''

			#Get the new ModeledKeyStr
			if self.ModeledShapeStr!="":

				#debug
				'''
				self.debug(
							[
								'We set the new ModeledHdfSuffixStr',
								('self.',self,['ModeledShapeStr','ModelTagStr'])
							]
						)
				'''

				#set
				self.ModeledHdfSuffixStr=self.ModeledShapeStr+ModelJoinStr+self.ModelTagStr

			else:

				#set
				self.ModeledHdfSuffixStr=self.ModelTagStr

			#debug
			'''
			self.debug(
						[
							'We have set the new ModeledHdfSuffixStr',
							('self.',self,[
								'ModeledShapeStr',
								'ModeledHdfSuffixStr'
							])
						]
					)	
			'''

			#/#################/#
			# Set the good format for the Description tuples list
			#

			#Unnzip
			ModeledGetKeyStrsList=SYS.unzip(self.ModelingDescriptionTuplesList,[0])

			#debug
			'''
			self.debug(
						[
							('Now change the shape of the shaping cols'),
							('self.',self,[
								'ModelingDescriptionTuplesList',
								'ModeledShapeIndexIntsList'
								])
						]
					)	
			'''

			#map
			ModeledShapeDescriptionTuplesList=map(
					self.ModelingDescriptionTuplesList.__getitem__,
					self.ModeledShapeIndexIntsList
				)

			#debug
			'''
			self.debug(
					[
						'ModeledShapeDescriptionTuplesList is '+str(
							ModeledShapeDescriptionTuplesList
						),
						('self.',self,['ModeledDescriptionDimensionIntsListsList'])
					]
				)
			'''

			#map
			ModeledShapeDescriptionTuplesList=map(
					lambda __ModeledShapeDescriptionTuple,__ModeledDescriptionDimensionIntsList:
					(
						__ModeledShapeDescriptionTuple[0],
						__ModeledShapeDescriptionTuple[1],
						__ModeledShapeDescriptionTuple[2][0](
							shape=__ModeledDescriptionDimensionIntsList
						)
					),
					ModeledShapeDescriptionTuplesList,
					self.ModeledDescriptionDimensionIntsListsList
				)

			#debug
			'''
			self.debug(
					[
						'ModeledShapeDescriptionTuplesList is '+str(
							ModeledShapeDescriptionTuplesList)
					]
				)
			'''

			#set the shaping cols
			map(
					lambda __ModeledIndexInt,__ModeledModelingDescriptionTuple:
					self.ModeledDescriptionTuplesList.__setitem__(
						__ModeledIndexInt,
						__ModeledModelingDescriptionTuple
					),
					self.ModeledShapeIndexIntsList,
					ModeledShapeDescriptionTuplesList
				)

			#debug
			'''	
			self.debug(
				[
					"After the shape",
					"Now self.ModeledDescriptionTuplesList is "+SYS._str(
					self.ModeledDescriptionTuplesList)
				]
			)
			'''

			#/###################/#
			# Define the Description
			#

			#import 
			import tables

			#Definition the DescriptionClass
			class DescriptionClass(tables.IsDescription):

				#Add (just like a unique KEY in mysql...) 
				RowInt=tables.Int64Col()

			#debug
			'''
			self.debug(
				[
					'We add descriptions in the description Class',
					('self.',self,['ModeledDescriptionTuplesList'])
				]
			)
			'''

			#set the cols in the ModelClass
			map(
					lambda __ModeledColumnTuple:
					DescriptionClass.columns.__setitem__(
						__ModeledColumnTuple[1],
						__ModeledColumnTuple[2]
						),
					self.ModeledDescriptionTuplesList
				)

			#Give a name
			DescriptionClass.__name__=SYS.getClassStrWithNameStr(self.ModelTagStr)

			#set the ModelClass
			if self.ModeledDescriptionClassesOrderedDict==None:
				self.ModeledDescriptionClassesOrderedDict=collections.OrderedDict()
			self.ModeledDescriptionClassesOrderedDict[self.ModelTagStr]=DescriptionClass

			#set the ModeledDescriptionClass
			self.ModeledDescriptionClass=DescriptionClass

			#/###################/#
			# Begin to set the hdf file 
			# first look if we have to hdformat
			#

			#debug
			self.debug(
				[
					'We tabular for hdf here...',
					'self.ModelDeriveControllerVariable.HdformatedFileVariable is ',
					str(self.ModelDeriveControllerVariable.HdformatedFileVariable)
				]
			)
			
			#set
			if self.ModeledHdfSuffixStr=="":
				self.ModeledHdfSuffixStr=self.ModelTagStr+'Table'

			#Check
			if self.ModelDeriveControllerVariable.HdformatedFileVariable==None:

				#/##################/#
				# If it is the top controller we have to hdformat
				#

				#debug
				'''
				self.debug(
						[
							'Look if the controller is the top one',	
							'self.ModelDeriveControllerVariable.ParentTopDeriveTeamerVariable==self.ModelDeriveControllerVariable',
							str(self.ModelDeriveControllerVariable.ParentTopDeriveTeamerVariable==self.ModelDeriveControllerVariable)					
						]
					)
				'''

				#Check
				if self.ModelDeriveControllerVariable.ParentTopDeriveTeamerVariable==self.ModelDeriveControllerVariable:

					#/##################/#
					# Set a default name
					#

					#Check
					if self.ModelDeriveControllerVariable.HdformatingFileKeyStr=='':

						#set
						self.ModelDeriveControllerVariable.HdformatingFileKeyStr=self.ModelDeriveControllerVariable.ControlTagStr+'.hdf5'


					#/##################/#
					# hdformat
					#

					#debug
					'''
					self.debug(
						[
							'We have to make hdformat the controller first...',
							('self.ModelDeriveControllerVariable.',
								self.ModelDeriveControllerVariable,
							[
								'ControlTagStr'
							])
						]
					)
					'''

					#Hdformat
					self.ModelDeriveControllerVariable.hdformat()

					#debug
					'''
					self.debug(
						[
							'Ok the top controller has hdformated',
							('self.ModelDeriveControllerVariable.',
								self.ModelDeriveControllerVariable,
							[
								'HdformatedFileVariable',
								'ControlTagStr'
							])
						]
					)
					'''

				else:

					#/##################/#
					# If it is not the top we have just 
					# to alias with the one of the top
					#

					#alias
					self.ModelDeriveControllerVariable.HdformatedFileVariable=self.ParentTopDeriveTeamerVariable.HdformatedFileVariable
				
			#/##################/#
			# Set the group path str to trigger 
			# a set in the hdf

			#debug
			'''
			self.debug(
					[
						'We set in the hdf the group branch'
					]
				)
			'''

			#Set
			self.ModelDeriveControllerVariable.HdfGroupPathStr=self.ModelDeriveControllerVariable.ControlTagStr

			#debug
			'''
			self.debug(
					[
						'Ok the group is setted'
					]
				)
			'''

			#Link
			self.ModeledHdfTopFileVariable=self.ModelDeriveControllerVariable.HdformatedFileVariable
			
			#debug
			'''
			self.debug(
				[
					'Ok the hdf file is setted',
					('self.',self,[
									'ModeledHdfTopFileVariable'
								])
				]
			)
			'''

			#/#################/#
			# Check for all the tables already defined here
			#

			#Check
			if self.ModeledHdfTopFileVariable!=None:

				#debug
				'''
				self.debug(
					[	
						'Looking for names of tables here',
						(
							'self.ModelDeriveControllerVariable.',
							self.ModelDeriveControllerVariable,
							['HdfGroupPathStr']
						)
					]
				)
				'''

				#Definition Modeled attributes
				self.ModeledHdfGroupVariable=self.ModeledHdfTopFileVariable.getNode(
					self.ModelDeriveControllerVariable.HdfGroupPathStr
				)

				#debug
				'''
				self.debug(
							[
								('looking for tables with the same Model Tag Str as : '),
								('self.',self,['ModelTagStr'])
							]
						)
				'''

				#Get and sort
				self.ModeledHdfKeyStrsList=sorted(
					filter(
							lambda __KeyStr:
							__KeyStr.endswith(self.ModelTagStr),
							self.ModeledHdfGroupVariable._v_leaves.keys()
						)
				)
				
				#update
				self.ModeledHdfTablesOrderedDict.update(
					map(
							lambda __ModeledKeyStr:
							(
								__ModeledKeyStr,
								self.ModeledHdfGroupVariable._f_getChild(
									__ModeledKeyStr
								)
							),
							self.ModeledHdfKeyStrsList
						)
				)

				#debug
				'''
				self.debug(
					[
						("self.",self,[
										'ModeledHdfTablesOrderedDict'
									])
					]
				)
				'''

			#/################/#
			# Refind all the names of the tables
			#

			#debug
			'''
			self.debug(
						('self.',self,[
							'ModeledHdfKeyStrsList',
							'ModeledHdfSuffixStr',
							'ModeledHdfKeyStr'
						])
					)
			'''

			#Get the suffix Strs of all the tables and their index
			ModeledHdfList=SYS.unzip(map(
					lambda __StrsList:
					(
						__StrsList[1],
						ModelOrderStr.join(__StrsList[2:])
					),
					map(
							lambda __ModeledHdfKeyStr:
							__ModeledHdfKeyStr.split(ModelOrderStr),
							self.ModeledHdfKeyStrsList
						)
				),[0,1]
			)

			#debug
			'''
			self.debug(
				[
					'All the corresponding table models are ',
					('vars()[\'',vars(),['ModeledHdfList'],"\']")
				]
			)
			'''

			#/##################/#
			# Find if there are already some tables here and deduce the index of the table
			#

			#Unpack if it is possible
			if len(ModeledHdfList)>0:

				#Unpack
				[ModeledHdfIndexIntsTuple,ModeledHdfSuffixStrsList]=ModeledHdfList

				#debug
				'''
				self.debug(
							[
								'There are already some tables',
								'ModeledHdfSuffixStrsList is '+str(ModeledHdfSuffixStrsList),
								"self.ModeledHdfSuffixStr is "+str(
									self.ModeledHdfSuffixStr)
							]
						)
				'''

				if self.ModeledHdfSuffixStr not in ModeledHdfSuffixStrsList:

					#Increment the IndexStr
					ModeledHdfIndexInt=max(map(int,ModeledHdfIndexIntsTuple))+1

					#Strify
					ModeledHdfIndexStr=str(ModeledHdfIndexInt)

					#debug
					'''
					self.debug('IndexStr of this new table is '+str(IndexStr))
					'''
					
				else:

					#Get the already setted one
					ModeledHdfIndexStr=self.ModeledHdfKeyStrsList[
							ModeledHdfSuffixStrsList.index(self.ModeledHdfSuffixStr)
						].split(ModelOrderStr)[1]

					#Intify
					ModeledHdfIndexInt=(int)(ModeledHdfIndexStr)

					#debug
					'''
					self.debug('IndexStr of this not new table is '+str(IndexStr))
					'''

			else:

				#debug
				'''
				self.debug('There are no tables here')
				'''

				#set to empty lists 
				[ModeledHdfIndexIntsTuple,ModeledHdfSuffixStrsList]=[[],[]]

				#Init the list
				ModeledHdfIndexInt=0

				#Strify
				ModeledHdfIndexStr="0"

			#/##################/#
			# set the table key str
			#

			#debug
			'''
			self.debug(
					[
						'We set the table key str',
						('self.',self,[
							'ModeledHdfSuffixStr'
						]),
						'ModeledHdfIndexStr is '+str(ModeledHdfIndexStr)
					]
				)
			'''

			#Bind with ModeledHdfKeyStr setting
			self.ModeledHdfKeyStr=ModelOrderStr+ModeledHdfIndexStr+ModelOrderStr+self.ModeledHdfSuffixStr

			#set the ModeledInt
			self.ModeledHdfIndexInt=ModeledHdfIndexInt

			#debug
			'''
			self.debug(
				[
					"self.ModeledHdfKeyStr is "+str(self.ModeledHdfKeyStr)
				]
			)
			'''

			#debug
			'''
			self.debug(
						[
							'Here we create the table or get it depending if it is new or not',
							('self.',self,[
								'ModeledHdfKeyStr',
								'ModeledHdfTopFileVariable'
								])
						]
					)
			'''
			
			#Check
			if self.ModeledHdfKeyStr!="" and self.ModeledHdfTopFileVariable!=None:

				#debug
				'''
				self.debug(
							[
								('self.',self,[
									'ModeledHdfKeyStr',
									'ModeledHdfKeyStrsList'
								])
							]
						)
				'''
				
				#Create the Table if not already
				if self.ModeledHdfKeyStr not in self.ModeledHdfKeyStrsList:

					#debug
					'''
					self.debug(
								[
									'The table not exists',
								]
							)
					'''

					#Create the Table in the hdf5
					self.ModeledHdfTable=self.ModeledHdfTopFileVariable.create_table(
						self.ModeledHdfGroupVariable,
						self.ModeledHdfKeyStr,
						self.ModeledDescriptionClass,
						self.ModeledDescriptionClass.__doc__ 
						if self.ModeledDescriptionClass.__doc__!=None 
						else "This is the "+self.ModeledDescriptionClass.__name__
					)

					#Append
					self.ModeledHdfKeyStrsList.append(
						self.ModeledHdfKeyStr
					)

				else:

					#debug
					'''
					self.debug(
									[
										'The table exists',
										"self.ModeledGroupVariable is "+str(self.ModeledGroupVariable)
									]
								)
					'''

					#Else just get it 
					self.ModeledHdfTable=self.ModeledHdfGroupVariable._f_getChild(
						self.ModeledHdfKeyStr
					)

				#set the in the TablesOrderedDict
				self.ModeledHdfTablesOrderedDict[
					self.ModeledHdfKeyStr
				]=self.ModeledHdfTable

				#debug
				'''
				self.debug("self.ModeledHdfTablesOrderedDict is "+str(
					self.ModeledHdfTablesOrderedDict))
				'''
				
			#debug
			'''
			self.debug(
						[
							'Table is done here for hdf...',
							('self.',self,[
								'ModeledHdfTable',
								'ModeledHdfTopFileVariable'
								]
							)
						]
					)
			'''


	def propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable):

		#call the base method
		BaseClass.propertize_setWatchAfterParentWithParenterBool(
			self,
			_SettingValueVariable
		)

		#debug
		'''
		self.debug(
			[
				'We have parented',
				'We model here',
			]
		)
		'''

		#/#################/#
		# Give some things from the controller
		#

		#get the parent-parent Teamer
		if self.ParentDeriveTeamerVariable!=None:
			if self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable!=None:
				self.ModelDeriveControllerVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

		#Link set
		self.ModelTagStr=self.ManagementTagStr+'Model'

		#debug
		'''
		self.debug(
				[
					'We have setted the ModelDeriveControllerVariable',
					('self.',self,[
						'ModelDeriveControllerVariable',
						'ModelTagStr'
					])
				]
			)
		'''

		#model
		self.model()

	def propertize_setModelingDescriptionTuplesList(self,_SettingValueVariable):

		#set
		self._ModelingDescriptionTuplesList=_SettingValueVariable

		#/###################/#
		# Update the ModelKeyStrsList
		#

		#check
		if self.ModelKeyStrsList==None:
			self.ModelKeyStrsList=[]

		#extend
		self.ModelKeyStrsList.extend(
			SYS.unzip(
				_SettingValueVariable,
				[0]
			)
		)

		#/###################/#
		# Check if it is a hdf or mongo model
		#

		#debug
		'''
		self.debug(
			[
				('self.',self,['ModelingDescriptionTuplesList'])
			]
		)
		'''

		#Check
		if len(self.ModelingDescriptionTuplesList)>0:
			self.ModelingHdfBool=True
			self.ModelingMongoBool=False
		else:
			self.ModelingHdfBool=False
			self.ModelingMongoBool=True

		#/###################/#
		# Look for items where it is a get dimension
		#

		#filter
		self.ModelDimensionTuplesList=map(
			lambda __DescriptionTuple:
			(__DescriptionTuple[0], __DescriptionTuple[2]),
			SYS._filter(
				lambda __DescriptionTuple:
				type(__DescriptionTuple[2]) in [list,tuple],
				_SettingValueVariable
			)
		)

		#debug
		'''
		self.debug(
				[
					'We have setted the ModelDimensionTuplesList',
					('self.',self,['ModelDimensionTuplesList'])
				]
			)
		'''

#</DefineClass>

#<DefineLocals>
Controller.ModelsClass.ManagingValueClass=ModelerClass
#<DefineLocals>

#</DefinePrint>
ModelerClass.PrintingClassSkipKeyStrsList.extend(
	[
		#'ModelKeyStrsList',	
		'ModelingDescriptionTuplesList', 
		'_ModelingDescriptionTuplesList', 
		'ModelingMongoBool',
		'ModelingHdfBool',							
		'ModeledDescriptionClassesOrderedDict',																
		#'ModeledDescriptionClass', 													
		'ModelDeriveControllerVariable',
		'ModeledMongoDeriveNoderVariable',	
		'ModeledHdfGroupVariable', 
		'ModeledHdfTopFileVariable',
		'ModeledMongoTopClientVariable',
		'ModeledMongoLocalDatabaseVariable',									
		'ModeledMongoSuffixStr',
		'ModeledHdfSuffixStr',																
		'ModeledMongoKeyStrsList',
		'ModeledHdfKeyStrsList', 	
		'ModeledMongoCollectionsOrderedDict',												
		'ModeledHdfTablesOrderedDict',
		'ModeledMongoKeyStr', 	
		'ModeledHdfKeyStr', 
		'ModeledMongoIndexInt', 	
		'ModeledHdfIndexInt', 			
		'ModeledMongoCollection', 	
		'ModeledHdfTable',
		'ModeledDescriptionGetKeyStrsList',
		'ModeledDescriptionDimensionGetKeyStrsListsList',
		'ModeledDescriptionDimensionIntsListsList',  
		'ModeledShapeIndexIntsList',
		'ModeledDimensionGetKeyStrsList', 
		'ModeledDimensionIntsList',
		'ModeledShapeStr',
		'ModelDimensionTuplesList'
	]
)
#<DefinePrint>
