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
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Hdformater"
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
ModelOneColStrsList=[
					'Int',
					'Float',
					'Str',
					'Bool'
				]
ModelListColStrsList=map(lambda __Str:__Str+'sList',ModelOneColStrsList)
ModelArrayColStrsList=map(lambda __Str:__Str+'sArray',ModelOneColStrsList)
ModelJoinStr='__'
ModelLinkStr='_'
ModelOrderStr='xx'
ModelDimensionStr='_'
#</DefineLocals>

#<DefineClass>
@DecorationClass(**{
	'ClassingSwitchMethodStrsList':["model"],
	'ClassingStructureVariable':[
		('Model','Models'),
		('Component','Components')
	]
})
class ModelerClass(BaseClass):
	
	def default_init(
					self,
					_ModelKeyStrsList={
						'DefaultValueType':property,
						'PropertyInitVariable':[],
						'PropertyDocStr':'I say what has to be stored'
					},
					_ModelTagStr="Model",
					_ModelingDescriptionTuplesList={
						'DefaultValueType':property,
						'PropertyInitVariable':[],
						'PropertyDocStr':'I described variables for storing them in hdf'
					}, 		
					_ModelMongoBool=True,
					_ModelHdfBool=False,
					_ModelDescriptionTuplesList=None,
					_ModeledParentSingularStr="",	
					_ModeledParentControllerDeriveModelerVariable=None,	
					_ModeledTopControllerDeriveModelerVariable=None,				
					_ModeledDescriptionClassesOrderedDict=None,																
					_ModeledDescriptionClass=None,
					_ModeledHdfGroupVariable=None,
					_ModeledMongoTopClientVariable=None,
					_ModeledMongoLocalDatabaseVariable=None,
					_ModeledMongoDatabaseKeyStr=None,
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

		#/#################/#
		# Determine if it is an inside structure or the top
		#

		#debug
		'''
		self.debug(
			[
				'We model here',
				'First look for deeper teams in the structure',
				('self.',self,[
					'FolderingPathVariable',
					'HdformatingFileKeyStr'
				])
			]
		)
		'''
		
		#Check
		if self.ParentedTotalSingularListDict!=None and len(self.ParentedTotalSingularListDict)>0:

			#debug
			'''
			self.debug(
				[
					'self.ParentedTotalSingularListDict.keys() is ',
					str(self.ParentedTotalSingularListDict.keys())
				]
			)
			'''

			#get
			self.ModeledParentSingularStr=self.ParentedTotalSingularListDict.keys()[0]

		#debug
		'''
		self.debug(
			[
				'Ok',
				('self.',self,['ModeledParentSingularStr'])
			]
		)
		'''

		#/###############/#
		# Cases depending on the level
		#

		#Check
		if (self.ParentDeriveTeamerVariable==None or 'Models' in self.TeamDict or self.ParentDeriveTeamerVariable.TeamTagStr not in [
			'Models'
		]):


			#/###############/#
			# It is a controller 
			#

			#debug
			'''
			self.debug(
					[
						'Controller Level',
					]
				)
			'''

			#/###############/#
			# Determine the parent
			#

			#set
			self.ModeledParentControllerDeriveModelerVariable=self

			#Check
			if self.ModeledParentSingularStr=='Component':

				#/###############/#
				# It is a component controller 
				#

				#debug
				'''
				self.debug(
						[
							'Component Controller Level',
							'We set the ModeledTopControllerDeriveModelerVariable',
							#('self.',self,['StructureTopDeriveStructurerRigidVariable'])
						]
					)
				'''

				#set
				self.ModeledTopControllerDeriveModelerVariable=self.StructureTopDeriveStructurerRigidVariable

			else:

				#/###############/#
				# It is the top controller 
				#

				#debug
				'''
				self.debug(
						[
							'Top Controller Level',
						]
					)
				'''

				#set
				self.ModeledTopControllerDeriveModelerVariable=self

				#/###############/#
				# structure
				#

				#debug
				self.debug(
					[
						'We are going to structure',
						'add in the StructuringCommandSetVariable'
					]
				)

				#add
				self.StructuringManagerCommandSetList=['model']

				#structure
				self.structure(
					[
						'Components',
						'Models'
					],
					'#all'
				)

				#debug
				'''
				self.debug(
					[
						'Ok we have structured',
						'self==self.StructureTopDeriveStructurerRigidVariable is ',
						str(self==self.StructureTopDeriveStructurerRigidVariable),
						'self.HdformatingFileKeyStr is ',
						self.HdformatingFileKeyStr
					]
				)
				'''

			#Check
			if 'Models' not in self.TeamDict:

				#debug
				'''
				self.debug(
					[
						'It is a special one level model'
					]
				)
				'''

				#/###############/#
				# set the tag
				#

				#Link set
				self.ModelTagStr='Model'

				#/###############/#
				# Determine the parent
				#

				#Check
				if self.ParentDeriveTeamerVariable!=None:

					#debug
					'''
					self.debug(
						[
							'There is a parent parent'
						]
					)
					'''

					#set
					self.ModeledParentControllerDeriveModelerVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

				else:

					#debug
					'''
					self.debug(
						[
							'There is no parent'
						]
					)
					'''

					#set
					self.ModeledParentControllerDeriveModelerVariable=self

				
				#set
				if self.StructureTopDeriveStructurerRigidVariable!=None:

					#debug
					'''
					self.debug(
						[
							'self.StructureTopDeriveStructurerRigidVariable!=None'
						]
					)
					'''

					#set
					self.ModeledTopControllerDeriveModelerVariable=self.StructureTopDeriveStructurerRigidVariable
				else:

					#debug
					'''
					self.debug(
						[
							'self.StructureTopDeriveStructurerRigidVariable==None'
						]
					)
					'''

					#set
					self.ModeledTopControllerDeriveModelerVariable=self

				#debug
				'''
				self.debug(
					[
						'self.ModeledTopControllerDeriveModelerVariable.HdformatingFileKeyStr is ',
						self.ModeledTopControllerDeriveModelerVariable.HdformatingFileKeyStr
					]
				)
				'''

				#/###############/#
				# SetModel
				#

				#set
				self.setModel()

		elif self.ModeledParentSingularStr=='Model':

			#debug
			'''
			self.debug(
					[
						'Model Level',
						'We determine the controller and top controller',
						('self.',self,['StructureTopDeriveStructurerRigidVariable'])
					]
				)
			'''

			#/###############/#
			# set the tag
			#

			#Link set
			self.ModelTagStr=self.ManagementTagStr+'Model'


			#/###############/#
			# Determine the parent
			#

			#set
			self.ModeledParentControllerDeriveModelerVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#set
			self.ModeledTopControllerDeriveModelerVariable=self.StructureTopDeriveStructurerRigidVariable

			#debug
			'''
			self.debug(
				[
					'We have determined the parents',
					('self.',self,[
						'ModeledParentControllerDeriveModelerVariable'
					]),
					'Now we model'
				]
			)
			'''

			#/###############/#
			# SetModel
			#

			#set
			self.setModel()

			#debug
			'''
			self.debug(
				[
					'Ok we have modeled',
				]
			)
			'''

		#debug
		'''
		self.debug(
			[
				'Ok end of model'
			]
		)
		'''

	def setModel(self):

		#Debug
		'''
		self.debug(
				[
					'model start',
					'Determine if it is going to be mongo or hdf',
					('self.',self,['ModeledTopControllerDeriveModelerVariable'])
				]
			)
		'''

		#/###################/#
		# Determine if it is Mongo or Hdf
		#

		#Check
		if self.ModeledTopControllerDeriveModelerVariable.HdformatingFileKeyStr!="":
			self.ModelMongoBool=False
			self.ModelHdfBool=True

		#Debug
		'''
		self.debug(
				[
					'Ok we now what database to use',
					('self.',self,[
						'ModelMongoBool',
						'ModelHdfBool'
					])
				]
			)
		'''
		
		#/###################/#
		# Mongo Case
		#

		#Check
		if self.ModelMongoBool:

			#debug
			'''
			self.debug(
					'We model mongo here'
				)
			'''

			#set
			#self.ModeledMongoSuffixStr=self.ModelTagStr+'Collection'
			self.ModeledMongoSuffixStr=self.ModelTagStr

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
			if self.ModeledParentControllerDeriveModelerVariable.PymongoneClientVariable==None:

				#debug
				'''
				self.debug('We have to pymongo first...')
				'''

				#pymongo
				self.ModeledParentControllerDeriveModelerVariable.pymongo()

			#Link
			self.ModeledMongoTopClientVariable=self.ModeledParentControllerDeriveModelerVariable.PymongoneClientVariable
			
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

				#/#################/#
				# Check for the name
				#

				#Check
				if self.ModeledParentControllerDeriveModelerVariable.PymongoingDatabaseStr=="":

					#Check
					if self.ModeledParentControllerDeriveModelerVariable.ParentTagStr=="":

						#set
						self.ModeledMongoDatabaseKeyStr='Default'

					else:
		
						#set
						self.ModeledMongoDatabaseKeyStr=self.ModeledParentControllerDeriveModelerVariable.ParentTagStr

					#set
					self.ModeledParentControllerDeriveModelerVariable.PymongoingDatabaseStr=self.ModeledMongoDatabaseKeyStr

				else:

					#set
					self.ModeledMongoDatabaseKeyStr=self.ModeledParentControllerDeriveModelerVariable.PymongoingDatabaseStr

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
				]=self.ModeledParentControllerDeriveModelerVariable

				#alias
				self.ModeledParentControllerDeriveModelerVariable.Database=self.ModeledMongoLocalDatabaseVariable

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
		if self.ModelHdfBool:

			#/###################/#
			# Check maybe the Description was not yet done although there are ModelKeystrs
			#

			#debug
			'''
			self.debug(
				[
					'We setModel hdf here',
					('self.',self,['_ModelKeyStrsList'])
				]
			)
			'''
			
			#Check
			if len(self._ModelKeyStrsList)>len(self.ModelingDescriptionTuplesList):

				#bind
				self.propertize_setModelKeyStrsList(self._ModelKeyStrsList)

			#/################/#
			# Model is to modify modeling description so keep an old version of this before
			#

			#debug
			'''
			self.debug(
					[
						'Keep maybe a copy of ModelingDescriptionTuplesList',
						('self.',self,[
							'ModelingDescriptionTuplesList',
							'ModelDescriptionTuplesList'
						])
					]
				)
			'''
			
			#keep a memory
			if self.ModelDescriptionTuplesList==None:

				#copy
				self.ModelDescriptionTuplesList=copy.deepcopy(
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
							("self.",self,[
								'ModelDimensionTuplesList'
							])
						]
					)
			'''

			#Check
			if self.ModelDimensionTuplesList!=None and len(self.ModelDimensionTuplesList)>0:

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

				#/###################/#
				# Check the dimension that are not defined or equal to zero
				# set them to one

				#map map
				self.ModeledDescriptionDimensionIntsListsList=map(
						lambda __ModeledDescriptionDimensionGetKeyStrsList:
						map(
							lambda __ModeledDescriptionDimensionGetKeyStr,__ShapeInt:
							self.ModeledParentControllerDeriveModelerVariable.set(
								__ModeledDescriptionDimensionGetKeyStr,
								__ShapeInt+1 
							)[__ModeledDescriptionDimensionGetKeyStr]
							if __ShapeInt==0 else __ShapeInt,
							__ModeledDescriptionDimensionGetKeyStrsList,
							map(
								lambda __ModeledDescriptionDimensionGetKeyStr:
								self.ModeledParentControllerDeriveModelerVariable[
									__ModeledDescriptionDimensionGetKeyStr
								],
								__ModeledDescriptionDimensionGetKeyStrsList
							),
						),
						self.ModeledDescriptionDimensionGetKeyStrsListsList
					)


				#get the corresponding real dimensions
				'''
				self.ModeledDescriptionDimensionIntsListsList=map(
						lambda __ModeledDescriptionDimensionGetKeyStrsList:
						self.ModeledParentControllerDeriveModelerVariable[
							Getter.GetMapStr
						](
							*__ModeledDescriptionDimensionGetKeyStrsList
						).ItemizedMapValueVariablesList,
						self.ModeledDescriptionDimensionGetKeyStrsListsList
					)
				'''

				#debug
				'''
				self.debug(
					[
						('self.',self,[
							'ModeledDescriptionDimensionIntsListsList'
						])
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
			ModeledGetKeyStrsList=SYS.unzip(
				self.ModelingDescriptionTuplesList,
				[0]
			)

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
			if self.ModeledParentControllerDeriveModelerVariable!=None:

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
				self.ModeledDimensionIntsList=self.ModeledParentControllerDeriveModelerVariable[
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
					self.ModelingDescriptionTuplesList.__setitem__(
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
					"After the shape we check for the modeling description",
					('self.',self,[
							'ModelingDescriptionTuplesList',
							'ModelKeyStrsList'
						]
					)
				]
			)
			'''

			"""
			#/###################/#
			# Check maybe the Description was not yet done although there are ModelKeystrs
			#

			#Check
			if len(self._ModelKeyStrsList)>len(self.ModelingDescriptionTuplesList):

				#bind
				self.propertize_setModelKeyStrsList(self._ModelKeyStrsList)
			"""
			
			#debug
			'''
			self.debug(
				[
					"After the bind",
					('self.',self,[
							'ModelingDescriptionTuplesList',
							'ModelKeyStrsList'
						]
					)
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
					('self.',self,[
						'ModelingDescriptionTuplesList'
					])
				]
			)
			'''

			#set the cols in the ModelClass
			map(
					lambda __ModelingColumnTuple:
					DescriptionClass.columns.__setitem__(
						__ModelingColumnTuple[1],
						__ModelingColumnTuple[2]
						),
					self.ModelingDescriptionTuplesList
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
			'''
			self.debug(
				[
					'We tabular for hdf here...',
					'self.ModeledParentControllerDeriveModelerVariable.HdformatedFileVariable is ',
					str(self.ModeledParentControllerDeriveModelerVariable.HdformatedFileVariable)
				]
			)
			'''

			#set
			if self.ModeledHdfSuffixStr=="":
				self.ModeledHdfSuffixStr=self.ModelTagStr+'Table'

			#Check
			if self.ModeledParentControllerDeriveModelerVariable.HdformatedFileVariable==None:

				#/##################/#
				# If it is the top controller we have to hdformat
				#

				#debug
				'''
				self.debug(
						[
							'Look if the controller is the top one',	
							'self.ModeledParentControllerDeriveModelerVariable.ParentTopDeriveTeamerVariable==self.ModeledParentControllerDeriveModelerVariable',
							str(self.ModeledParentControllerDeriveModelerVariable.ParentTopDeriveTeamerVariable==self.ModeledParentControllerDeriveModelerVariable)					
						]
					)
				'''

				#Check
				if self.ModeledParentControllerDeriveModelerVariable.ParentTopDeriveTeamerVariable==self.ModeledParentControllerDeriveModelerVariable:

					#/##################/#
					# Set a default name
					#

					#Check
					if self.ModeledParentControllerDeriveModelerVariable.HdformatingFileKeyStr=='':

						#set
						self.ModeledParentControllerDeriveModelerVariable.HdformatingFileKeyStr=self.ModeledParentControllerDeriveModelerVariable.ControlTagStr+'.hdf5'


					#/##################/#
					# hdformat
					#

					#debug
					'''
					self.debug(
						[
							'We have to make hdformat the controller first...',
							('self.ModeledParentControllerDeriveModelerVariable.',
								self.ModeledParentControllerDeriveModelerVariable,
							[
								'ControlTagStr'
							])
						]
					)
					'''

					#Hdformat
					self.ModeledParentControllerDeriveModelerVariable.hdformat()

					#debug
					'''
					self.debug(
						[
							'Ok the top controller has hdformated',
							('self.ModeledParentControllerDeriveModelerVariable.',
								self.ModeledParentControllerDeriveModelerVariable,
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
					self.ModeledParentControllerDeriveModelerVariable.HdformatedFileVariable=self.ParentTopDeriveTeamerVariable.HdformatedFileVariable
				
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
			self.ModeledParentControllerDeriveModelerVariable.HdformatGroupPathStr=self.ModeledParentControllerDeriveModelerVariable.ModelTagStr

			#debug
			'''
			self.debug(
					[
						'Ok the group is setted'
					]
				)
			'''

			#Link
			self.ModeledHdfTopFileVariable=self.ModeledParentControllerDeriveModelerVariable.HdformatedFileVariable
			
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
							'self.ModeledParentControllerDeriveModelerVariable.',
							self.ModeledParentControllerDeriveModelerVariable,
							['HdformatGroupPathStr']
						)
					]
				)
				'''

				#Definition Modeled attributes
				self.ModeledHdfGroupVariable=self.ModeledHdfTopFileVariable.getNode(
					self.ModeledParentControllerDeriveModelerVariable.HdformatGroupPathStr
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
					'Ok we have setted which hdf table',
					('self.',self,[
							'ModeledHdfKeyStr',
							'ModeledHdfIndexInt'
						]),
					'Now we create the table, or get it, depending if it is new or not',
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

	"""
	def propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable):


		#/#################/#
		# Call the base method
		#

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
		# Tag a name with the parent
		#

		#Link set
		self.ModelTagStr=self.ManagementTagStr+'Model'


		#/#################/#
		# Call the model
		#

		#model
		self.model()
	"""

	def mimic_structure(self):

		#/#################/#
		# Call the base method
		#

		#call the base method
		BaseClass.structure(self)

		#debug
		'''
		self.debug(
			[
				'We have structured',
				'We model here',
			]
		)
		'''
		
		#/#################/#
		# Tag a name with the parent
		#

		#Link set
		self.ModelTagStr=self.ManagementTagStr+'Model'

		#/#################/#
		# Call the model
		#

		#model
		self.model()


	def propertize_setModelingDescriptionTuplesList(self,_SettingValueVariable):

		#set
		self._ModelingDescriptionTuplesList=_SettingValueVariable

		#/###################/#
		# Update the ModelKeyStrsList
		#

		#extend
		self._ModelKeyStrsList=SYS.unzip(
				_SettingValueVariable,
				[0]
			)

		#debug
		'''
		self.debug(
			[
				'We have binded ModelingDescriptionTuplesList to ModelKeyStrsList',
				('self.',self,[
					'ModelingDescriptionTuplesList'
				]),
				'Now set the dimensions'
			]
		)
		'''
		
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

	def propertize_setModelKeyStrsList(self,_SettingValueVariable):	

		#set
		self._ModelKeyStrsList=_SettingValueVariable

		#debug
		'''
		self.debug(
				[
					'Do we have to bind with Description',
					('self.',self,[
						'ModelHdfBool',
						'ModelKeyStrsList'
					])
				]
			)
		'''

		#/###################/#
		# Set ModelingDescriptionTuplesList
		#

		#Check
		if self.ModelHdfBool:

			#/###################/#
			# Set ModelingDescriptionTuplesList
			#

			#debug
			'''
			self.debug(
					[
						'We know the ModelKeyStrsList',
						'we set the ModelingDescriptionTuplesList',
						('self.',self,['_ModelKeyStrsList'])
					]
				)
			'''

			#map
			self.ModelingDescriptionTuplesList=map(
				lambda __KeyStr,__ModelingDescriptionTuple:
				self.getModelDescriptionTupleWithKeyStr(__KeyStr)
				if __ModelingDescriptionTuple==None else __ModelingDescriptionTuple,
				_SettingValueVariable,
				self.ModelingDescriptionTuplesList
			)
	
	def getModelDescriptionTupleWithKeyStr(self,_KeyStr):
		return (
				_KeyStr,
				_KeyStr,
				self.getModelColVariableWithKeyStr(_KeyStr)
			)

	def getModelColVariableWithKeyStr(self,_KeyStr):

		#import
		import tables

		#Definition
		global ModelOneColStrsList,ModelListColStrsList,ModelArrayColStrsList

		#/##################/#
		# Look for one single type
		#

		#Definition
		List=SYS._filter(
			lambda __ModelOneColStr:
				_KeyStr.endswith(__ModelOneColStr),
				ModelOneColStrsList
			)

		#Check
		if len(List)==1:

			#Get
			ModelOneColStr=List[0]
			
			#Debug
			'''
			print('l 55 getModelColVariableWithKeyStr')
			print('ModeledColStr is ')
			print(ModeledColStr)
			print('')
			'''

			#Get the Col Class
			if ModelOneColStr=='Str':
				ModelColClass=getattr(
									tables,
									'StringCol'
								)
			else:
				ModelColClass=getattr(
									tables,
									ModelOneColStr+'Col'
								)

			#Return
			if ModelOneColStr=='Str':
				return ModelColClass(100)
			else:
				return ModelColClass()

		else:

			#/##################/#
			# Look for a shaped type
			#

			#Check
			for __TypeStr in ['List','Array']:

				#Definition
				ModeledEndBoolsList=map(
					lambda __ModelListColStr:
						_KeyStr.endswith(__ModelListColStr),
						globals()['Model'+__TypeStr+'ColStrsList']
					)

				#Check
				if True in ModeledEndBoolsList:

					#/####################/#
					# Get the type
					#

					#get
					ModelOneColStr=ModelOneColStrsList[ModeledEndBoolsList.index(True)]

					#debug
					'''
					self.debug(
						[
							'ModelOneColStr is ',
							ModelOneColStr
						]
					)
					'''

					#Get the Col Class
					if ModelOneColStr=='Str':
						ModelColClass=getattr(
											tables,
											'StringCol'
										)
					else:
						ModelColClass=getattr(
											tables,
											ModelOneColStr+'Col'
										)

					#/####################/#
					# Look if there is no a shape
					#

					#Check
					if _KeyStr in self.__class__.DefaultAttributeVariablesOrderedDict:

						#get
						ClassValueVariable=self.__class__.DefaultAttributeVariablesOrderedDict[_KeyStr]

						#debug
						'''
						self.debug(
							[
								'There is a shape ',
								"ClassValueVariable['ShapeKeyStrsList'] is ",
								str(ClassValueVariable['ShapeKeyStrsList'])
							]
						)
						'''

						#Check
						if hasattr(ClassValueVariable,'items') and 'ShapeKeyStrsList' in ClassValueVariable:
							
							#return
							return (ModelColClass,ClassValueVariable['ShapeKeyStrsList'])

					#Return
					if ModelOneColStr=='Str':
						return ModelColClass(100,shape=(1))
					else:
						return ModelColClass(shape=(1))

	
	def mimic__print(self,**_KwargVariablesDict):

		#/##################/#
		# Modify the printing Variable
		#

		#Check
		if self.PrintingSelfBool:

			#/##################/#
			# Display or not several things
			#

			#map
			map(
					lambda __KeyStr:
					self.PrintingCopyVariable.PrintingInstanceSkipKeyStrsList.append(
						__KeyStr
					) if getattr(self.PrintingCopyVariable,__KeyStr)==None
					else (
						self.PrintingCopyVariable.PrintingInstanceForceKeyStrsList.append(
							__KeyStr
						)
						if self.__class__.__name__=='ModelerClass'
						else self.PrintingCopyVariable.PrintingInstanceForceBaseKeyStrsList.append(
							__KeyStr
						)
					),
					[
						'ModeledMongoCollection',
						'ModeledDescriptionClass',
						'ModeledHdfTable',
					]
				)


		#/##################/#
		# Call the base method
		#

		#call
		BaseClass._print(self,**_KwargVariablesDict)

#</DefineClass>

#<DefineLocals>
Controller.ModelsClass.ManagingValueClass=ModelerClass
#<DefineLocals>

#</DefinePrint>
ModelerClass.PrintingClassSkipKeyStrsList.extend(
	[
		#'ModelKeyStrsList',	
		'ModelTagStr',
		'ModelingDescriptionTuplesList', 
		'_ModelingDescriptionTuplesList', 
		'ModelMongoBool',
		'ModelHdfBool',	
		'ModelDescriptionTuplesList',						
		'ModeledDescriptionClassesOrderedDict',																
		#'ModeledDescriptionClass', 													
		'ModeledParentControllerDeriveModelerVariable',
		'ModeledTopControllerDeriveModelerVariable',
		'ModeledParentSingularStr',	
		'ModeledHdfGroupVariable', 
		'ModeledHdfTopFileVariable',
		'ModeledMongoTopClientVariable',
		'ModeledMongoLocalDatabaseVariable',
		'ModeledMongoDatabaseKeyStr',									
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
