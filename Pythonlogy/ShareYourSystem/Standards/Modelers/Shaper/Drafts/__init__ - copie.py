# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Shaper instances help for storing data in formated tables :
if the shape of a rowed variable is depending on other flexible int attribute
in the environment, it then build or set another table with the good format 
size to store again.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Modelers.Recoverer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
import collections
import numpy
from ShareYourSystem.Functers import Argumenter,Switcher,Alerter,Hooker
from ShareYourSystem.Standards.Modelers import Modeler,Tabularer,Tabler,Inserter
#</ImportSpecificModules>

#<DefineLocals>
ShapingJoiningStr='__'
ShapingTuplingStr='_'
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class ShaperClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'ShapingDimensionTuplesList',
									'ShapedStr',									
									'ShapedVariablePointer', 						
									'ShapedDimensionVariablesList', 							
									'ShapedDatabasingSealTuplesList', 					
									'ShapedNotDatabasingSealTuplesList',  				
									'ShapedGettingStrsList', 					
									'ShapedColClassAndGettingStrTuplesList'
								]

	def default_init(self,
					_ShapingDimensionTuplesList=None,
					_ShapedStr="",									
					_ShapedVariablePointer=None, 						
					_ShapedDimensionVariablesList=None, 							
					_ShapedDatabasingSealTuplesList=None, 					
					_ShapedNotDatabasingSealTuplesList=None,  				
					_ShapedGettingStrsList=None, 					
					_ShapedColClassAndGettingStrTuplesList=None, 			
					**_KwargVariablesDict):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Alerter.AlerterClass()
	@Switcher.SwitcherClass()
	@Hooker.HookerClass(**{
								'HookingBeforeVariablesList':[
									{'CallingVariable':Modeler.ModelerClass.model}
								],
								'HookingAfterVariablesList':[
									{'CallingMethodStr':"shape"},
									{'CallingMethodStr':"database"}
								]
							}
						)
	def model(self,**_KwargVariablesDict):

		'''
		#<NotHook>
		#shape and database first
		self.shape()
		self.database()
		#</NotHook>
		'''

		#Get the new DatabasedKeyStr
		if self.ShapedStr!="":

			#debug
			'''
			self.debug(
						[
							'We set the new DatabasedKeyStr',
							('self.',self,['ShapedStr','ModeledSuffixStr'])
						]
					)
			'''

			#set
			self.DatabasedKeyStr=self.ShapedStr+ShapingJoiningStr+self.ModeledSuffixStr

		else:
			self.DatabasedKeyStr=self.ModeledSuffixStr

		#debug
		'''
		self.debug(
					[
						'We set the new DatabasedKeyStr',
						('self.',self,['ShapedStr','DatabasedKeyStr'])
					]
				)	
		'''

		#debug
		'''
		self.debug(
					[
						'We have to check if this model was already defined',
						'self.DatabasedKeyStr is '+str(self.DatabasedKeyStr),
						"self.DatabasedModelClassesOrderedDict.keys() is "+str(
							self.DatabasedModelClassesOrderedDict.keys())
					]
				)
		'''

		#Check
		if self.DatabasedModelClassesOrderedDict==None:
			self.DatabasedModelClassesOrderedDict=collections.OrderedDict()
		if self.DatabasedKeyStr in self.DatabasedModelClassesOrderedDict:

			#debug
			'''
			self.debug('Yes it is already modeled')
			'''

			#set DatabasedBool to True
			self.SwitchingModelBool=True

		else:

			#debug
			'''
			self.debug('Nope, ModeleIsBool has to be False')
			'''

			#set and DatabasedKeyStr
			self['SwitchingModelBool']=False

			#debug
			'''
			self.debug(
						[
							'Now we set in the good format the shaping columning tuples',
							('self.',self,
									[
										'ShapedGettingStrsList',
										'ShapedColClassAndGettingStrTuplesList'
									]
							)
						]
					)
			'''

			#set also the ShapingColumningTuplesList inside of the ColumningTuplesList
			self.DatabasingSealTuplesList=self.ShapedNotDatabasingSealTuplesList+map(
					lambda __ShapedGettingStr,__ShapedColClassAndGettingStrTuple:
					(
						__ShapedGettingStr,
						__ShapedColClassAndGettingStrTuple[0](
								shape=self.ShapedVariablePointer[__ShapedColClassAndGettingStrTuple[1]]
							)
					),
					self.ShapedGettingStrsList,
					self.ShapedColClassAndGettingStrTuplesList
				)

			#debug
			'''
			self.debug("Now self.DatabasingSealTuplesList is "+str(
				self.DatabasingSealTuplesList))
			'''

		'''
		#<NotHook>
		#model then
		Modeler.ModelerClass.model(self)
		#</NotHook>
		'''

	#@Alerter.AlerterClass()
	@Switcher.SwitcherClass()
	@Hooker.HookerClass(**{
							'HookingAfterVariablesList':[{'CallingVariable':Tabularer.TabularerClass.tabular}]
							}
						)
	def tabular(self,**_KwargVariablesDict):

		'''
		#<NotHook>
		#tabular first
		Tabularer.TabularerClass.tabular(self)
		#</NotHook>
		'''

		#debug
		'''
		self.debug(
					[
						'We add the ShapedStr to the TabularedSuffix Str ?',
						('self.',self,[
											'TabularedSuffixStr',
											'ShapedStr'
										])
					]
				)
		'''

		#Add the ShapedStr
		if self.ShapedStr!="":

			#debug
			'''
			self.debug(' ShapingJoiningStr not in self.TabularedSuffixStr is '+str( ShapingJoiningStr not in self.TabularedSuffixStr))
			'''

			if ShapingJoiningStr not in self.TabularedSuffixStr:

				#debug
				'''
				self.debug('Yes we add')
				'''

				#Add
				self.TabularedSuffixStr=self.ShapedStr+ShapingJoiningStr+self.TabularedSuffixStr

			#debug
			'''
			self.debug("self.TabularedSuffixStr is "+self.TabularedSuffixStr)
			'''

	@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':Inserter.InserterClass.insert}]})
	def insert(self,**_KwargVariablesDict):

		'''
		#<NotHook>
		#insert first
		Inserter.InserterClass.insert(self)
		#</NotHook>
		'''

		#debug
		'''
		self.debug(
					[
						'We are going to check if it was Inserted',
						('self.',self,[
											'InsertedErrorBool',
											'TabledKeyStr',
											'TabledTable'
										])
					]
			)
		'''

		if self.InsertedErrorBool:

			#Debuf
			'''
			self.debug(
						[
							('So yes we have to retable again...'),
							('self.',self,[
										'ShapedGettingStrsList',
										'ShapedColClassAndGettingStrTuplesList',
										'ShapedDimensionKeyStrsList',
										'ShapedDimensionVariablesList'
									])
						]
					)
			'''

			#Definition the InsertedOldDimensionListsList
			InsertedGettingStrsListsList=map(
					lambda __ShapedColClassAndGettingStrTuple:
					list(
							[__ShapedColClassAndGettingStrTuple[1]]
							if type(__ShapedColClassAndGettingStrTuple[1]
								) in SYS.StrTypesList
							else
							__ShapedColClassAndGettingStrTuple[1]
						),
					self.ShapedColClassAndGettingStrTuplesList
				)
			
			#Definition the InsertedOldDimensionListsList
			InsertedOldDimensionListsList=map(
												lambda __InsertedGettingStrsList:
												self.ShapedVariablePointer.pick(__InsertedGettingStrsList),
												InsertedGettingStrsListsList
										)

			#Definition the InsertedNewDimensionListsList
			InsertedNewDimensionListsList=map(
												lambda __ShapedGettingStr:
												list(
														numpy.shape(
															self.RowedVariablePointer[__ShapedGettingStr]
														)
												),
												self.ShapedGettingStrsList
											)

			#debug
			'''
			self.debug(('vars ',vars(),[
											'InsertedGettingStrsListsList',
											'InsertedOldDimensionListsList',
											'InsertedNewDimensionListsList'
										]))
			'''

			#set the shaping attributes to their new values
			map(
					lambda __InsertedGettingStrsList,__InsertedOldDimensionList,__InsertedNewDimensionList:
					self.ShapedVariablePointer.update(
						zip(
							__InsertedGettingStrsList,
							__InsertedNewDimensionList
							)
					)
					if __InsertedNewDimensionList!=__InsertedOldDimensionList
					else None,
					InsertedGettingStrsListsList,
					InsertedOldDimensionListsList,
					InsertedNewDimensionListsList
				)

			#debug
			'''
			self.debug(('self.ShapedVariablePointer',self.ShapedVariablePointer,SYS.flat(
				InsertedGettingStrsListsList)))
			'''

			#set again the ColumnTuplesList
			self.DatabasingSealTuplesList=copy.copy(self.ShapedCopyDatabasingSealTuplesList)

			#Reset some bools
			map(
				lambda __KeyStr:
				self.__setitem__(
									'Switching'+__KeyStr+'Bool',
									False
								),
				['Model','Shape','Tabular','Table']
			)

			#Table
			self.table()

			#debug
			'''
			self.debug('Ok table again is done, so now we insert')
			'''

			#Reset to False
			self.InsertedErrorBool=False

			#Insert again
			#self.insert()
			#Functer.getFunctingFunctionWithFuncFunction(Inserter.InserterClass.insert)(self)
			Inserter.InserterClass.insert(self)
	
	#@Alerter.AlerterClass()
	@Switcher.SwitcherClass()
	@Argumenter.ArgumenterClass()
	def shape(self,_DimensionsTupleList=None,**_KwargVariablesDict):

		#Init
		if self.ShapingDimensionsTupleList==None:
			self.ShapingDimensionsTupleList=[]

		#Init
		if self.ShapedGettingStrsList==None:
			self.ShapedGettingStrsList=[]
		if self.ShapedColClassAndGettingStrTuplesList==None:
			self.ShapedColClassAndGettingStrTuplesList=[]

		#set the ShapedOldDatabasingSealTuplesList
		self.ShapedCopyDatabasingSealTuplesList=copy.copy(self.DatabasingSealTuplesList)

		#debug
		'''
		self.debug('We are going to filter the shaping tuples among the columning tuples')
		'''

		#Unpack
		[
			self.ShapedDatabasingSealTuplesList,
			self.ShapedNotDatabasingSealTuplesList
		]=SYS.groupby(
					lambda __ColumnTuple:
					type(__ColumnTuple[1])==tuple,
					self.DatabasingSealTuplesList,
				)

		#set the ShapedGettingStrsList and ShapedColClassAndGettingStrTuplesList
		FilteredList=map(list,
				SYS.unzip(self.ShapedDatabasingSealTuplesList,[0,1])
			)
		if len(FilteredList)>0:
			[
				self.ShapedGettingStrsList,
				self.ShapedColClassAndGettingStrTuplesList
			]=FilteredList

		#debug
		'''
		self.debug(
					('self.',self,[
									'ShapedNotDatabasingSealTuplesList',
									'ShapedGettingStrsList',
									'ShapedColClassAndGettingStrTuplesList'
								]
					)
			)
		'''

		#set the ShapedGettingStrsList
		self.ShapedDimensionKeyStrsList=list(set(SYS.unzip(
			self.ShapedColClassAndGettingStrTuplesList,[1]
			)))

		#debug
		'''
		self.debug(("self.",self,['ShapedGettingStrsList']))
		'''

		#set the ShapedVariablePointer to get inside the shaped variables
		if self.ShapedVariablePointer==None and hasattr(self,'NodedDatabaseParentPointer'):
			self.ShapedVariablePointer=self.NodedDatabaseParentPointer

		#set the ShapedVariablesList setting
		self.ShapedDimensionVariablesList=map(
				lambda  __GettedVariable:
				(__GettedVariable)
				if type(__GettedVariable)==int 
				else tuple(__GettedVariable),
				map(
					lambda __ShapedDimensionKeyStr:
					self.ShapedVariablePointer[__ShapedDimensionKeyStr],
					self.ShapedDimensionKeyStrsList
				)
			)

		#Bind with DatabasedShapedStr setting
		self.ShapedStr=ShapingJoiningStr.join(
									map(
											lambda __ShapingGettingStr,__ShapedVariable:
											ShapingJoiningStr+str(
												__ShapingGettingStr
												)+ShapingTuplingStr+str(
												__ShapedVariable),
											self.ShapedDimensionKeyStrsList,
											self.ShapedDimensionVariablesList
										)
		)

		#debug 
		'''
		self.debug(('self.',self,['ShapedDimensionVariablesList','ShapedStr']))
		'''

		#<NotHook>
		#Return self
		return self
		#</NotHook>

	#</DefineMethods>

#</DefineClass>

