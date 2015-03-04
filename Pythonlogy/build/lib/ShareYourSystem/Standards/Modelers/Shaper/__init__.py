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
BaseModuleStr="ShareYourSystem.Standards.Modelers.Findoer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
import collections
import numpy
from ShareYourSystem.Standards.Modelers import Modeler,Tabularer,Tabler
from ShareYourSystem.Standards.Itemizers import Getter,Setter
#</ImportSpecificModules>

#<DefineLocals>
ShapeJoiningStr='__'
ShapeTuplingStr='_'
#</DefineLocals>

#<DefineClass>
@DecorationClass(
	**{
		'ClassingSwitchMethodStrsList':[
			'shape',
			'model',
			'tabular'
		]
	}
)
class ShaperClass(BaseClass):

	def default_init(self,
					_ShapingDimensionTuplesList=None,										
					_ShapedDescriptionGetKeyStrsList=None, 
					_ShapedDescriptionDimensionGetKeyStrsListsList=None,
					_ShapedDescriptionDimensionIntsListsList=None,  
					_ShapedIndexIntsList=None,
					_ShapedDimensionGetKeyStrsList=None, 
					_ShapedDimensionIntsList=None,
					_ShapedStr="",					
					**_KwargVariablesDict
				):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_shape(self):

		#/################/#
		# Pick the shape ints and their get key strs
		#

		#debug
		self.debug(
					[
						'We shape here',
						("self.",self,['ShapingDimensionTuplesList'])
					]
				)

		#Check
		if len(self.ShapingDimensionTuplesList)>0:

			#set
			[
				self.ShapedDescriptionGetKeyStrsList,
				ShapedDescriptionDimensionGetTuplesList 
				
			]=SYS.unzip(self.ShapingDimensionTuplesList,[0,1])

			#list
			self.ShapedDescriptionGetKeyStrsList=list(self.ShapedDescriptionGetKeyStrsList)

			#debug
			self.debug(
				[
					'ShapedDescriptionDimensionGetTuplesList is ',
					str(ShapedDescriptionDimensionGetTuplesList)
				]
			)

			#unzip
			self.ShapedDescriptionDimensionGetKeyStrsListsList=SYS.unzip(
					list(ShapedDescriptionDimensionGetTuplesList),[1]
				)

			#debug
			self.debug(
				[
					('self.',self,['ShapedDescriptionDimensionGetKeyStrsListsList'])
				]
			)

			#get the corresponding real dimensions
			self.ShapedDescriptionDimensionIntsListsList=map(
					lambda __ShapedDescriptionDimensionGetKeyStrsList:
					self.ModelDeriveControllerVariable[Getter.GetMapStr](
						*__ShapedDescriptionDimensionGetKeyStrsList
					).ItemizedMapValueVariablesList,
					self.ShapedDescriptionDimensionGetKeyStrsListsList
				)

			#debug
			self.debug(
				[
					('self.',self,['ShapedDescriptionDimensionIntsListsList'])
				]
			)

		else:

			#Default
			self.ShapedDescriptionGetKeyStrsList=[]
			self.ShapedDimensionGetKeyStrsList=[]
			self.ShapedDescriptionDimensionGetKeyStrsListsList=[]

		#debug
		self.debug(
			[
				("self.",self,[
									'ShapedDescriptionGetKeyStrsList',
									'ShapedDescriptionDimensionGetKeyStrsListsList',
									'ShapedDescriptionDimensionIntsListsList'
								])
			]
		)

		#/################/#
		# Find where in the description tuokes list it has to be modified and
		#

		#Definition
		ModeledGetKeyStrsList=SYS.unzip(self.ModelingDescriptionTuplesList,[0])

		#set
		self.ShapedIndexIntsList=map(
				lambda __ShapedDescriptionGetKeyStr:
				ModeledGetKeyStrsList.index(__ShapedDescriptionGetKeyStr),
				self.ShapedDescriptionGetKeyStrsList
			)

		#debug
		'''
		self.debug(
				[
					'Check if we know already the modeler',
					'self.ModelDeriveControllerVariable!=None is '+str(
						self.ModelDeriveControllerVariable!=None
					)
				]
			)
		'''

		#/################/#
		# set flat all the get key str for the shaping int 
		#

		#Check
		if self.ModelDeriveControllerVariable!=None:

			#Flat and set
			self.ShapedDimensionGetKeyStrsList=list(
				set(
					SYS.flat(
						self.ShapedDescriptionDimensionGetKeyStrsListsList
						)
					)
				)

			#Pick
			self.ShapedDimensionIntsList=self.ModelDeriveControllerVariable[Getter.GetMapStr
			](
				*self.ShapedDimensionGetKeyStrsList
			).ItemizedMapValueVariablesList

		else:

			#Default
			self.ShapedDimensionIntsList=[]
					

		#/################/#
		# map a join str with this
		#

		#debug
		'''
		self.debug(("self.",self,['ShapedDimensionIntsList']))
		'''

		#Bind with ModeledShapedStr setting
		self.ShapedStr=ShapeJoiningStr.join(
			map(
					lambda __ShapedDescriptionGetKeyStr,__ShapedDimensionVariable:
					ShapeJoiningStr+str(
						__ShapedDescriptionGetKeyStr
						)+ShapeTuplingStr+str(
						__ShapedDimensionVariable),
					self.ShapedDimensionGetKeyStrsList,
					self.ShapedDimensionIntsList
				)
		)

		#debug 
		'''
		self.debug(
			[
				('self.',self,['ShapedStr'])
			]
		)
		'''

	def mimic_model(self):

		#/#################/#
		# Check if we have to shape before
		#

		#debug
		self.debug(
					[	
						'Do we have to shape before model',
						('self.',self,['ModelingHdfBool'])
					]
			)
	
		#Check
		if self.ModelingHdfBool:

			#shape
			self.shape()

			#/#################/#
			# Adapt the name of the descriptionmodel given the shape
			#

			#debug
			self.debug(
					[
						'Ok we have shaped',
						('self.',self,['ShapedStr'])
					]
				)

			#Get the new ModeledKeyStr
			if self.ShapedStr!="":

				#debug
				'''
				self.debug(
							[
								'We set the new ModeledDescriptionKeyStr',
								('self.',self,['ShapedStr','ModelTagStr'])
							]
						)
				'''

				#set
				self.ModeledDescriptionKeyStr=self.ShapedStr+ShapeJoiningStr+self.ModelTagStr

			else:
				self.ModeledDescriptionKeyStr=self.ModeledSuffixStr

			#debug
			self.debug(
						[
							'We set the new ModeledDescriptionKeyStr',
							('self.',self,['ShapedStr','ModeledDescriptionKeyStr'])
						]
					)	


			#/#################/#
			# Set the good format for the Description tuples list
			#

			#Unnzip
			ModeledGetKeyStrsList=SYS.unzip(self.ModelingDescriptionTuplesList,[0])

			#debug
			self.debug(
						[
							('Now change the shape of the shaping cols'),
							('self.',self,[
								'ModelingDescriptionTuplesList',
								'ShapedIndexIntsList'
								])
						]
					)	

			#map
			ShapedModelingDescriptionTuplesList=map(
					self.ModelingDescriptionTuplesList.__getitem__,
					self.ShapedIndexIntsList
				)

			#debug
			self.debug(
					[
						'ShapedModelingDescriptionTuplesList is '+str(
							ShapedModelingDescriptionTuplesList
						),
						('self.',self,['ShapedDescriptionDimensionIntsListsList'])
					]
				)

			#map
			ModeledShapeDescriptionTuplesList=map(
					lambda __ShapedModelingDescriptionTuple,__ShapedDescriptionDimensionIntsList:
					(
						__ShapedModelingDescriptionTuple[0],
						__ShapedModelingDescriptionTuple[1],
						__ShapedModelingDescriptionTuple[2][0](
							shape=__ShapedDescriptionDimensionIntsList
						)
					),
					ShapedModelingDescriptionTuplesList,
					self.ShapedDescriptionDimensionIntsListsList
				)

			#debug
			self.debug(
					[
						'ModeledShapeDescriptionTuplesList is '+str(
							ModeledShapeDescriptionTuplesList)
					]
				)

			#set the shaping cols
			map(
					lambda __ShapedIndexInt,__ShapedModelingDescriptionTuple:
					self.ModelingDescriptionTuplesList.__setitem__(
						__ShapedIndexInt,
						__ShapedModelingDescriptionTuple
					),
					self.ShapedIndexIntsList,
					ModeledShapeDescriptionTuplesList
				)

			#debug	
			self.debug(
				[
					"After the shape",
					"Now self.ModelingDescriptionTuplesList is "+SYS._str(
					self.ModelingDescriptionTuplesList)
				]
			)
		
		#/#################/#
		# base method
		#

		#debug
		self.debug(
				'Now we call the base model method'
			)

		#model then
		BaseClass.model(self)

	def mimic_tabular(self):

		#/#################/#
		# first tabular
		#

		#debug
		self.debug(
				'First we tabular with the base'
			)

		#tabular Tabularer method first
		Tabularer.TabularerClass.tabular(self)

		#Check
		if self.ModelingHdfBool:
		
			#/#################/#
			# Now adapt also the name of the tables
			#

			#debug
			self.debug(
						[
							'We add the ShapedStr to the TabularedSuffix Str ?',
							('self.',self,[
												'ShapedStr',
												'TabularedHdfSuffixStr'
											])
						]
					)

			#Add the ShapedStr
			if self.ShapedStr!="":

				#debug
				'''
				self.debug(
					[
						' ShapeJoiningStr not in self.TabularedSuffixStr is '+str(
							ShapeJoiningStr not in self.TabularedSuffixStr))
					]
				)
				'''

				#Check
				if ShapeJoiningStr not in self.TabularedHdfSuffixStr:

					#debug
					'''
					self.debug('Yes we add')
					'''

					#Add
					self.TabularedHdfSuffixStr=self.ShapedStr+ShapeJoiningStr+self.TabularedHdfSuffixStr

				#debug
				self.debug(
					[
						('self.',self,['TabularedHdfSuffixStr'])
					]
				)

		#/##################/#
		# Rehook with the table process
		#

		#then table
		BaseClass.table(self)

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
					lambda __ShapedDescriptionDimensionGetKeyStrsList:
					self.ModelDeriveControllerVariable[Getter.GetMapStr](
						__ShapedDescriptionDimensionGetKeyStrsList
					).ItemizedMapValueVariablesList,
					self.ShapedDescriptionDimensionGetKeyStrsListsList
				)

			#Definition the InsertedNewDimensionIntsListsList
			InsertedNewDimensionIntsListsList=map(
				lambda __ShapedDescriptionGetKeyStr:
				list(
						numpy.shape(
							self.ModelDeriveControllerVariable[__ShapedDescriptionGetKeyStr]
						)
				),
				self.ShapedDescriptionGetKeyStrsList
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
					lambda __ShapedDescriptionDimensionGetKeyStrsList,__InsertedOldDimensionList,__InsertedNewDimensionList:
					self.__setitem__(
						'ShapedErrorBool',
						True
						).ModelDeriveControllerVariable[Setter.SetMapStr](
						zip(
							__ShapedDescriptionDimensionGetKeyStrsList,
							__InsertedNewDimensionList
							)
					) if __InsertedNewDimensionList!=__InsertedOldDimensionList
					else None,
					self.ShapedDescriptionDimensionGetKeyStrsListsList,
					InsertedOldDimensionIntsList,
					InsertedNewDimensionIntsListsList
					)

			#debug
			self.debug(
				[
					'We reset some methods',
					('self.',self,['SwitchedMethodDict'])
				]
			)

			#reboot
			self.setSwitch(
				[
					'model',
					'shape',
					'tabular',
					'table'
				]
			)
			self.setDone(
				[
					Modeler.ModelerClass,
					Tabularer.TabularerClass,
					Tabler.TableClass,
					SYS.ShaperClass
				]
			)
			

			#Table
			self.table()

			#debug
			'''
			self.debug('Ok table again is done, so now we insert')
			'''

			#insert first
			BaseClass.insert(self)

	def propertize_setModelingDescriptionTuplesList(self,_SettingValueVariable):

		#set
		BaseClass.propertize_setModelingDescriptionTuplesList(self,_SettingValueVariable)

		#filter
		self.ShapingDimensionTuplesList=map(
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
					'We have setted the ShapingDimensionTuplesList',
					('self.',self,['ShapingDimensionTuplesList'])
				]
			)
		'''
#</DefineClass>


#</DefinePrint>
ShaperClass.PrintingClassSkipKeyStrsList.extend(
	[
		'ShapingDimensionTuplesList',
		'ShapedDescriptionGetKeyStrsList',	
		'ShapedDescriptionDimensionIntsListsList',
		'ShapedIndexIntsList',														
		'ShapedDimensionGetKeyStrsList',	
		'ShapedDimensionIntsList',							
		'ShapedStr'
	]
)
#<DefinePrint>
