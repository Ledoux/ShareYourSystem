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

		#Check
		if self.DatabasedModelClassesOrderedDict==None:
			self.DatabasedModelClassesOrderedDict=collections.OrderedDict()

		#Unnzip
		DatabasedGetKeyStrsList=SYS.unzip(self.DatabasingSealTuplesList,[0])

		#debug
		'''
		self.debug(
					[
						('Now change the shape of the shaping cols'),
						('self.',self,['ShapedSealDimensionGetKeyStrsListsList'])
					]
				)	
		'''

		ShapedDatabasingSealTuplesList=map(
				self.DatabasingSealTuplesList.__getitem__,
				self.ShapedIndexIntsList
			)

		#debug
		'''
		self.debug(
					'ShapedDatabasingSealTuplesList is '+str(ShapedDatabasingSealTuplesList)
				)
		'''	

		#set the shaping cols
		map(
				lambda __ShapedIndexInt,__ShapedDatabasingSealTuple:
				self.DatabasingSealTuplesList.__setitem__(
					__ShapedIndexInt,
					__ShapedDatabasingSealTuple
				),
				self.ShapedIndexIntsList,
				map(
					lambda __ShapedDatabasingSealTuple,__ShapedSealDimensionGetKeyStrsList:
					(
						__ShapedDatabasingSealTuple[0],
						__ShapedDatabasingSealTuple[1],
						__ShapedDatabasingSealTuple[2].__class__(
						shape=self.NodePointDeriveNoder.pick(
							__ShapedSealDimensionGetKeyStrsList)
						)
					),
					ShapedDatabasingSealTuplesList,
					self.ShapedSealDimensionGetKeyStrsListsList	
				)
			)

		#debug	
		'''		
		self.debug("Now self.DatabasingSealTuplesList is "+str(
			self.DatabasingSealTuplesList))
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
		if self.DatabasingHdfBool:

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
			DatabasedGetKeyStrsList=SYS.unzip(self.DatabasingSealTuplesList,[0])

			#set
			self.ShapedIndexIntsList=map(
					lambda __ShapedSealGetKeyStr:
					DatabasedGetKeyStrsList.index(__ShapedSealGetKeyStr),
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

			#Bind with DatabasedShapedStr setting
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

