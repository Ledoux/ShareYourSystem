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
BaseModuleStr="ShareYourSystem.Standards.Modelers.Modeler"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import copy
import tables
from ShareYourSystem.Standards.Classors import Doer
#</ImportSpecificModules>

#<DefineLocals>
AnalyzingColStrsList=[
							'Int',
							'Float',
							'Str'
					]
DatabasingJoinStr='__'
DatabasingLinkStr='_'
#</DefineLocals>

#<DefineFunctions>
def getDatabasedColWithGetKeyStr(_GetKeyStr):

	#Definition
	global AnalyzingColStrsList

	#Definition
	DatabasedColStr=SYS._filter(
		lambda __AnalyzingColStr:
		_GetKeyStr.endswith(__AnalyzingColStr),
		AnalyzingColStrsList
		)[0]

	#Get the Col Class
	DatabasedColClass=getattr(tables,DatabasedColStr+'Col')

	#Return
	if _GetKeyStr=='Str':
		return DatabasedColClass(length=100)
	else:
		return DatabasedColClass() 

def getDatabasingColumnTupleWithGetKeyStr(_GetKeyStr):
	return (_GetKeyStr,_GetKeyStr,getDatabasedColWithGetKeyStr(_GetKeyStr))

#</DefineFunctions>

#<DefineClass>
@DecorationClass(**{
	'ClassingSwitchMethodStrsList':["database"]
})
class DatabaserClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'DatabasingSealTuplesList', 									
								'DatabasedModelClassesOrderedDict',																
								'DatabasedModelClass', 													
								'DatabasedKeyStr'
							]

	def default_init(
					self,
					_DatabasingSealTuplesList={
								'DefaultingSetType':property,
								'PropertizingInitVariable':[],
								'PropertizingDocStr':''
						}, 								
					_DatabasedModelClassesOrderedDict=None,																
					_DatabasedModelClass=None, 													
					_DatabasedKeyStr="",
					**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_database(self):
		""" """

		#debug
		'''
		self.debug(('self.',self,['DatabasingSealTuplesList']))
		'''
		
		#<NotHook>
		#model first
		self.model()
		#</NotHook>

		#set a name if it was not already
		if self.DatabasedKeyStr=="":

			#debug
			'''
			self.debug(('self.',self,['DatabasingKeyStr','ModeledSuffixStr']))
			'''

			#Link set
			self.DatabasedKeyStr=self.ModeledSuffixStr

		#Definition the ModelClass
		class ModelClass(tables.IsDescription):

			#Add (just like a unique KEY in mysql...) 
			RowInt=tables.Int64Col()

		#debug
		'''
		self.debug(('self.',self,['DatabasedGetStrToColumnStrOrderedDict']))
		'''
		
		#set the cols in the ModelClass
		map(
				lambda __DatabasingColumnTuple:
				ModelClass.columns.__setitem__(
					__DatabasingColumnTuple[1],
					__DatabasingColumnTuple[2]
					),
				self.DatabasingSealTuplesList
			)

		#Give a name
		ModelClass.__name__=SYS.getClassStrWithNameStr(self.DatabasedKeyStr)

		#set the ModelClass
		if self.DatabasedModelClassesOrderedDict==None:
			self.DatabasedModelClassesOrderedDict=collections.OrderedDict()
		self.DatabasedModelClassesOrderedDict[self.DatabasedKeyStr]=ModelClass

		#set the DatabasedModelClass
		self.DatabasedModelClass=ModelClass

#</DefineClass>
