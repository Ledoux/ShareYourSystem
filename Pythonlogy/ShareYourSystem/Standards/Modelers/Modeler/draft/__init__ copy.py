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
#</ImportSpecificModules>

#<DefineLocals>
AnalyzingColStrsList=[
							'Int',
							'Float',
							'Str'
					]
ModelingJoinStr='__'
ModelingLinkStr='_'
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
					_ModeledDescriptionKeyStr="",						
					_ModeledDescriptionClassesOrderedDict=None,																
					_ModeledDescriptionClass=None, 													
					**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_model(self):
		""" """

		#Debug
		self.debug('model start')
		
		#/###################/#
		# Define the ModeledKeyStr 
		#

		if self.ModeledDescriptionKeyStr=='':
			self.ModeledDescriptionKeyStr=self.ModelTagStr

		#/###################/#
		# Special case of hdf when we have to define Model Description class
		#

		#Check
		if self.ModelingHdfBool:

			#import 
			import tables

			#Definition the DescriptionClass
			class DescriptionClass(tables.IsDescription):

				#Add (just like a unique KEY in mysql...) 
				RowInt=tables.Int64Col()

			#debug
			self.debug(
				[
					'We add descriptions in the description Class',
					('self.',self,['ModelingDescriptionTuplesList'])
				]
			)
			
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

	def propertize_setParentKeyStr(self,_SettingValueVariable):

		#call the parent base
		BaseClass.propertize_setParentKeyStr(self,_SettingValueVariable)

		#debug
		'''
		self.debug(
			[
				'We know the ParentKeyStr',
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

#</DefineClass>


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
	]
)
#<DefinePrint>
