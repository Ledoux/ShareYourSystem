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
from ShareYourSystem.Standards.Modelers import Databaser,Tabularer,Tabler,Inserter
#</ImportSpecificModules>

#<DefineLocals>
ShapingJoiningStr='__'
ShapingTuplingStr='_'
#</DefineLocals>

#<DefineClass>
@DecorationClass(
	**{
		'ClassingSwitchMethodStrsList':[
			'shape',
			'model',
			'database',
			'tabular'
		]
	}
)
class ShaperClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'ShapingDimensionTuplesList',
								'ShapedSealGetKeyStrsList',	
								'ShapedSealDimensionGetKeyStrsListsList',
								'ShapedIndexIntsList',														
								'ShapedDimensionGetKeyStrsList',	
								'ShapedDimensionIntsList',							
								'ShapedStr'
							]

	def default_init(self,
					_ShapingDimensionTuplesList=None,										
					_ShapedSealGetKeyStrsList=None, 
					_ShapedSealDimensionGetKeyStrsListsList=None,  
					_ShapedIndexIntsList=None,
					_ShapedDimensionGetKeyStrsList=None, 
					_ShapedDimensionIntsList=None,
					_ShapedStr="",							
					**_KwargVariablesDict):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def mimic_database(self):

		#debug
		'''
		self.debug(
					[
						'self.shape is '+SYS._str(self.shape)
					]
			)
		'''
		
		#<NotHook>
		#database and shape first
		'''
		self.debug('We database first')
		'''
		self.model()
		'''
		self.debug(
					[
						'We shape first',
						'self.shape is '+str(self.shape)
					]
				)
		'''
		self.shape()
		#</NotHook>

		#Get the new ModeledKeyStr
		if self.ShapedStr!="":

			#debug
			'''
			self.debug(
						[
							'We set the new ModeledKeyStr',
							('self.',self,['ShapedStr','ModeledSuffixStr'])
						]
					)
			'''

			#set
			self.ModeledKeyStr=self.ShapedStr+ShapingJoiningStr+self.ModeledSuffixStr

		else:
			self.ModeledKeyStr=self.ModeledSuffixStr

		#debug
		'''
		self.debug(
					[
						'We set the new ModeledKeyStr',
						('self.',self,['ShapedStr','ModeledKeyStr'])
					]
				)	
		'''

		#Check
		if self.ModeledDescriptionClassesOrderedDict==None:
			self.ModeledDescriptionClassesOrderedDict=collections.OrderedDict()

		#Unnzip
		ModeledGetKeyStrsList=SYS.unzip(self.ModelingSealTuplesList,[0])

		#debug
		'''
		self.debug(
					[
						('Now change the shape of the shaping cols'),
						('self.',self,['ShapedSealDimensionGetKeyStrsListsList'])
					]
				)	
		'''

		ShapedModelingSealTuplesList=map(
				self.ModelingSealTuplesList.__getitem__,
				self.ShapedIndexIntsList
			)

		#debug
		'''
		self.debug(
					'ShapedModelingSealTuplesList is '+str(ShapedModelingSealTuplesList)
				)
		'''	

		#set the shaping cols
		map(
				lambda __ShapedIndexInt,__ShapedModelingSealTuple:
				self.ModelingSealTuplesList.__setitem__(
					__ShapedIndexInt,
					__ShapedModelingSealTuple
				),
				self.ShapedIndexIntsList,
				map(
					lambda __ShapedModelingSealTuple,__ShapedSealDimensionGetKeyStrsList:
					(
						__ShapedModelingSealTuple[0],
						__ShapedModelingSealTuple[1],
						__ShapedModelingSealTuple[2].__class__(
						shape=self.NodePointDeriveNoder.pick(
							__ShapedSealDimensionGetKeyStrsList)
						)
					),
					ShapedModelingSealTuplesList,
					self.ShapedSealDimensionGetKeyStrsListsList	
				)
			)

		#debug	
		'''		
		self.debug("Now self.ModelingSealTuplesList is "+str(
			self.ModelingSealTuplesList))
		'''
		
		#database then
		Databaser.DatabaserClass.database(self)

	def mimic_tabular(self):


		#tabular first
		Tabularer.TabularerClass.tabular(self)

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

	def mimic_insert(self):

		#debug
		'''
		self.debug(
					[
						('self.',self,[
											'We check the good dimensions of the shaping variables'
											'TabledKeyStr',
											'TabledTable'
										])
					]
			)
		'''

		try:

			#insert first
			BaseClass.insert(self)

		except ValueError:

			#Definition the InsertedOldDimensionIntsListsList
			InsertedOldDimensionIntsList=map(
					lambda __ShapedSealDimensionGetKeyStrsList:
					self.NodePointDeriveNoder.pick(
						__ShapedSealDimensionGetKeyStrsList),
					self.ShapedSealDimensionGetKeyStrsListsList
					)

			#Definition the InsertedNewDimensionIntsListsList
			InsertedNewDimensionIntsListsList=map(
												lambda __ShapedSealGetKeyStr:
												list(
														numpy.shape(
															self.NodePointDeriveNoder[__ShapedSealGetKeyStr]
														)
												),
												self.ShapedSealGetKeyStrsList
											)

			#debug
			'''
			self.debug(('vars ',vars(),[
											'InsertedOldDimensionIntsList',
											'InsertedNewDimensionIntsListsList'
										]))
			'''

			#set the shaping attributes to their new values
			map(
					lambda __ShapedSealDimensionGetKeyStrsList,__InsertedOldDimensionList,__InsertedNewDimensionList:
					self.__setitem__(
						'ShapedErrorBool',
						True
						).NodePointDeriveNoder.update(
						zip(
							__ShapedSealDimensionGetKeyStrsList,
							__InsertedNewDimensionList
							)
					) if __InsertedNewDimensionList!=__InsertedOldDimensionList
					else None,
					self.ShapedSealDimensionGetKeyStrsListsList,
					InsertedOldDimensionIntsList,
					InsertedNewDimensionIntsListsList
					)

			#debug
			'''
			self.debug('We reset some methods')
			'''

			#reboot
			self.reboot(['Model','Shape','Tabular','Table'])
			

			#Table
			self.table()

			#debug
			'''
			self.debug('Ok table again is done, so now we insert')
			'''

			#insert first
			BaseClass.insert(self)
	
	def do_shape(self):

		#Check
		if self.ModelingHdfBool:

			#debug
			'''
			self.debug(
						[
							'We shape here',
							#("self.",self,['ShapingDimensionTuplesList'])
						]
					)
			'''

			#Check
			if len(self.ShapingDimensionTuplesList)>0:

				#set
				[
					self.ShapedSealGetKeyStrsList,
					self.ShapedSealDimensionGetKeyStrsListsList
				]=SYS.unzip(self.ShapingDimensionTuplesList,[0,1])

				#Flat and set
				self.ShapedDimensionGetKeyStrsList=list(
					set(
						SYS.flat(
							self.ShapedSealDimensionGetKeyStrsListsList
							)
						)
					)

			else:

				#Default
				self.ShapedSealGetKeyStrsList=[]
				self.ShapedDimensionGetKeyStrsList=[]
				self.ShapedSealDimensionGetKeyStrsListsList=[]

			#debug
			'''
			self.debug(("self.",self,[
										'ShapedSealGetKeyStrsList',
										'ShapedDimensionGetKeyStrsList'
									]))
			'''

			#Definition
			ModeledGetKeyStrsList=SYS.unzip(self.ModelingSealTuplesList,[0])

			#set
			self.ShapedIndexIntsList=map(
					lambda __ShapedSealGetKeyStr:
					ModeledGetKeyStrsList.index(__ShapedSealGetKeyStr),
					self.ShapedSealGetKeyStrsList
				)

			#Check
			if hasattr(self,'NodePointDeriveNoder') and self.NodePointDeriveNoder!=None:

				#Pick
				self.ShapedDimensionIntsList=self.NodePointDeriveNoder.pick(
					self.ShapedDimensionGetKeyStrsList
				)

			else:

				#Default
				self.ShapedDimensionIntsList=[]
						

			#debug
			'''
			self.debug(("self.",self,['ShapedDimensionIntsList']))
			'''

			#Bind with ModeledShapedStr setting
			self.ShapedStr=ShapingJoiningStr.join(
										map(
												lambda __ShapedSealGetKeyStr,__ShapedDimensionVariable:
												ShapingJoiningStr+str(
													__ShapedSealGetKeyStr
													)+ShapingTuplingStr+str(
													__ShapedDimensionVariable),
												self.ShapedDimensionGetKeyStrsList,
												self.ShapedDimensionIntsList
											)
			)

			#debug 
			'''
			self.debug(('self.',self,['ShapedStr']))
			'''
#</DefineClass>

