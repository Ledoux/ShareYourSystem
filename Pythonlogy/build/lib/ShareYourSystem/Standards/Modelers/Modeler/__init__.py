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
BaseModuleStr="ShareYourSystem.Standards.Teamers.Parenter"
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
					_ModelingDescriptionTuplesList={
						'DefaultValueType':property,
						'PropertyInitVariable':[],
						'PropertyDocStr':''
					}, 	
					_ModelingMongoBool=False,
					_ModelingHdfBool=False,							
					_ModeledDescriptionClassesOrderedDict=None,																
					_ModeledDescriptionClass=None, 													
					_ModeledKeyStr="",
					**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_model(self):
		""" """

		#debug
		self.debug(
			[
				('self.',self,['ModelingDescriptionTuplesList'])
			]
		)

		#set a name if it was not already
		if self.ModeledKeyStr=="":

			#debug
			'''
			self.debug(('self.',self,['ModelingKeyStr']))
			'''

			#Link set
			self.ModeledKeyStr=self.ManagementTagStr

		#Check
		if len(self.ModelingDescriptionTuplesList)>0:
			self.ModelingHdfBool=True
			self.ModelingMongoBool=False
		else:
			self.ModelingHdfBool=False
			self.ModelingMongoBool=True

		#Check
		if self.ModelingHdfBool:

			#import 
			import tables

			#Definition the DescriptionClass
			class DescriptionClass(tables.IsDescription):

				#Add (just like a unique KEY in mysql...) 
				RowInt=tables.Int64Col()

			#debug
			'''
			self.debug(('self.',self,['ModeledGetStrToColumnStrOrderedDict']))
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
			DescriptionClass.__name__=SYS.getClassStrWithNameStr(self.ModeledKeyStr)

			#set the ModelClass
			if self.ModeledDescriptionClassesOrderedDict==None:
				self.ModeledDescriptionClassesOrderedDict=collections.OrderedDict()
			self.ModeledDescriptionClassesOrderedDict[self.ModeledKeyStr]=DescriptionClass

			#set the ModeledDescriptionClass
			self.ModeledDescriptionClass=DescriptionClass

	def propertize_setParentKeyStr(self,_SettingValueVariable):

		#call the parent base
		BaseClass.propertize_setParentKeyStr(self,_SettingValueVariable)

		#debug
		self.debug(
			[
				'We know the ParentKeyStr',
				'We model here',
			]
		)

		#model
		self.model()

	def propertize_setModelingDescriptionTuplesList(self,_SettingValueVariable):

		#call the parent base
		BaseClass.propertize_setModelingDescriptionTuplesList(self,_SettingValueVariable)

		#debug
		self.debug(
			[
				'There are ModelingDescriptionTuplesList',
				'We model here',
				('self.',self,['WatchBeforeModelWithModelerBool'])
			]
		)

		self.setSwitch()

		#model
		self.model()


#</DefineClass>


#</DefinePrint>
ModelerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'ModelingDescriptionTuplesList', 
		'_ModelingDescriptionTuplesList', 
		'ModelingMongoBool',
		'ModelingHdfBool',									
		'ModeledDescriptionClassesOrderedDict',																
		#'ModeledDescriptionClass', 													
		'ModeledKeyStr'
	]
)
#<DefinePrint>
