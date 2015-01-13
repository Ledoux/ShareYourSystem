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
BaseModuleStr="ShareYourSystem.Databasers.Databaser"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import copy
import tables
from ShareYourSystem.Classors import Doer
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

	#Definition
	global AnalyzingColStrsList

	#Definition
	ModeledColStr=SYS._filter(
		lambda __AnalyzingColStr:
		_GetKeyStr.endswith(__AnalyzingColStr),
		AnalyzingColStrsList
		)[0]

	#Get the Col Class
	ModeledColClass=getattr(tables,ModeledColStr+'Col')

	#Return
	if _GetKeyStr=='Str':
		return ModeledColClass(length=100)
	else:
		return ModeledColClass() 

def getModelingColumnTupleWithGetKeyStr(_GetKeyStr):
	return (_GetKeyStr,_GetKeyStr,getModeledColWithGetKeyStr(_GetKeyStr))

#</DefineFunctions>

#<DefineClass>
@DecorationClass(**{
	'ClassingSwitchMethodStrsList':["model"]
})
class ModelerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'ModelingSealTuplesList', 									
									'ModeledClassesOrderedDict',																
									'ModeledClass', 													
									'ModeledKeyStr'
								]

	def default_init(
					self,
					_ModelingSealTuplesList={
								'DefaultingSetType':property,
								'PropertizingInitVariable':[],
								'PropertizingDocStr':''
						}, 								
					_ModeledClassesOrderedDict=None,																
					_ModeledClass=None, 													
					_ModeledKeyStr="",
					**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_model(self):
		""" """

		#debug
		'''
		self.debug(('self.',self,['ModelingSealTuplesList']))
		'''
		
		#<NotHook>
		#database first
		self.database()
		#</NotHook>

		#set a name if it was not already
		if self.ModeledKeyStr=="":

			#debug
			'''
			self.debug(('self.',self,['DatabasingKeyStr','DatabasedSuffixStr']))
			'''

			#Link set
			self.ModeledKeyStr=self.DatabasedSuffixStr

		#Definition the ModelClass
		class ModeledClass(tables.IsDescription):

			#Add a tabulared Int (just like a unique KEY in mysql...) 
			ModeledInt=tables.Int64Col()

		#debug
		'''
		self.debug(('self.',self,['ModeledGetStrToColumnStrOrderedDict']))
		'''
		
		#set the cols in the ModelClass
		map(
				lambda __ModelingColumnTuple:
				ModeledClass.columns.__setitem__(
					__ModelingColumnTuple[1],
					__ModelingColumnTuple[2]
					),
				self.ModelingSealTuplesList
			)

		#Give a name
		ModeledClass.__name__=SYS.getClassStrWithNameStr(self.ModeledKeyStr)

		#set the ModelClass
		if self.ModeledClassesOrderedDict==None:
			self.ModeledClassesOrderedDict=collections.OrderedDict()
		self.ModeledClassesOrderedDict[self.ModeledKeyStr]=ModeledClass

		#set the ModeledClass
		self.ModeledClass=ModeledClass

#</DefineClass>
