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
BaseModuleStr="ShareYourSystem.Databasers.Recoverer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
import collections
import numpy
from ShareYourSystem.Functers import Argumenter,Switcher,Alerter,Hooker
from ShareYourSystem.Databasers import Modeler,Tabularer,Tabler,Flusher
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
									'ShapedModelingSealTuplesList', 					
									'ShapedNotModelingSealTuplesList',  				
									'ShapedGettingStrsList', 					
									'ShapedColClassAndGettingStrTuplesList'
								]

	def default_init(self,
					_ShapingDimensionTuplesList=None,
					_ShapedStr="",									
					_ShapedVariablePointer=None, 						
					_ShapedDimensionVariablesList=None, 							
					_ShapedModelingSealTuplesList=None, 					
					_ShapedNotModelingSealTuplesList=None,  				
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

		#Get the new ModeledKeyStr
		if self.ShapedStr!="":

			#debug
			'''
			self.debug(
						[
							'We set the new ModeledKeyStr',
							('self.',self,['ShapedStr','DatabasedSuffixStr'])
						]
					)
			'''

			#set
			self.ModeledKeyStr=self.ShapedStr+ShapingJoiningStr+self.DatabasedSuffixStr

		else:
			self.ModeledKeyStr=self.DatabasedSuffixStr

		#debug
		'''
		self.debug(
					[
						'We set the new ModeledKeyStr',
						('self.',self,['ShapedStr','ModeledKeyStr'])
					]
				)	
		'''

		#debug
		'''
		self.debug(
					[
						'We have to check if this model was already defined',
						'self.ModeledKeyStr is '+str(self.ModeledKeyStr),
						"self.ModeledClassesOrderedDict.keys() is "+str(
							self.ModeledClassesOrderedDict.keys())
					]
				)
		'''

		#Check
		if self.ModeledClassesOrderedDict==None:
			self.ModeledClassesOrderedDict=collections.OrderedDict()
		if self.ModeledKeyStr in self.ModeledClassesOrderedDict:

			#debug
			'''
			self.debug('Yes it is already modeled')
			'''

			#set ModeledBool to True
			self.SwitchingModelBool=True

		else:

			#debug
			'''
			self.debug('Nope, ModeleIsBool has to be False')
			'''

			#set and ModeledKeyStr
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
			self.ModelingSealTuplesList=self.ShapedNotModelingSealTuplesList+map(
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
			self.debug("Now self.ModelingSealTuplesList is "+str(
				self.ModelingSealTuplesList))
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

	@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':Flusher.FlusherClass.flush}]})
	def flush(self,**_KwargVariablesDict):

		'''
		#<NotHook>
		#flush first
		Flusher.FlusherClass.flush(self)
		#</NotHook>
		'''

		#debug
		'''
		self.debug(
					[
						'We are going to check if it was Flushed',
						('self.',self,[
											'FlushedErrorBool',
											'TabledKeyStr',
											'TabledTable'
										])
					]
			)
		'''

		if self.FlushedErrorBool:

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

			#Definition the FlushedOldDimensionListsList
			FlushedGettingStrsListsList=map(
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
			
			#Definition the FlushedOldDimensionListsList
			FlushedOldDimensionListsList=map(
												lambda __FlushedGettingStrsList:
												self.ShapedVariablePointer.pick(__FlushedGettingStrsList),
												FlushedGettingStrsListsList
										)

			#Definition the FlushedNewDimensionListsList
			FlushedNewDimensionListsList=map(
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
											'FlushedGettingStrsListsList',
											'FlushedOldDimensionListsList',
											'FlushedNewDimensionListsList'
										]))
			'''

			#set the shaping attributes to their new values
			map(
					lambda __FlushedGettingStrsList,__FlushedOldDimensionList,__FlushedNewDimensionList:
					self.ShapedVariablePointer.update(
						zip(
							__FlushedGettingStrsList,
							__FlushedNewDimensionList
							)
					)
					if __FlushedNewDimensionList!=__FlushedOldDimensionList
					else None,
					FlushedGettingStrsListsList,
					FlushedOldDimensionListsList,
					FlushedNewDimensionListsList
				)

			#debug
			'''
			self.debug(('self.ShapedVariablePointer',self.ShapedVariablePointer,SYS.flat(
				FlushedGettingStrsListsList)))
			'''

			#set again the ColumnTuplesList
			self.ModelingSealTuplesList=copy.copy(self.ShapedCopyModelingSealTuplesList)

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
			self.debug('Ok table again is done, so now we flush')
			'''

			#Reset to False
			self.FlushedErrorBool=False

			#Flush again
			#self.flush()
			#Functer.getFunctingFunctionWithFuncFunction(Flusher.FlusherClass.flush)(self)
			Flusher.FlusherClass.flush(self)
	
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

		#set the ShapedOldModelingSealTuplesList
		self.ShapedCopyModelingSealTuplesList=copy.copy(self.ModelingSealTuplesList)

		#debug
		'''
		self.debug('We are going to filter the shaping tuples among the columning tuples')
		'''

		#Unpack
		[
			self.ShapedModelingSealTuplesList,
			self.ShapedNotModelingSealTuplesList
		]=SYS.groupby(
					lambda __ColumnTuple:
					type(__ColumnTuple[1])==tuple,
					self.ModelingSealTuplesList,
				)

		#set the ShapedGettingStrsList and ShapedColClassAndGettingStrTuplesList
		FilteredList=map(list,
				SYS.unzip(self.ShapedModelingSealTuplesList,[0,1])
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
									'ShapedNotModelingSealTuplesList',
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

		#Bind with ModeledShapedStr setting
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

