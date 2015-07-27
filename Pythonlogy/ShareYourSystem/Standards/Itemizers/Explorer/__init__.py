# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>



"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Conditioner"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Explorer','Explore','Exploring','Explored')
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass(**{})
class ExplorerClass(BaseClass):
	
	def default_init(
					self,	
					_ExploringMethodStr = "",
					_ExploringRangeVariable = None, 
					_ExploringConditionVariable = None,
					_ExploringTrialsInt = 1000, 
					_ExploringSuccessesInt = 1,
					_ExploredCheckBool = False,
					_ExploredParameterStrsList = None,
					_ExploredRangeTuplesList = None,
					_ExploredConditionTuplesList = None, 
					_ExploredKeepStrsList = None,	
					_ExploredStoreTuplesListsList = None,
					_ExploredTrialsInt = 0,
					_ExploredSucessesInt = 0,											
					**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_explore(self):
		""" """

		#debug
		'''
		self.debug(
			[
				"We explore here"
			]
		)
		'''

		#Check
		if self.ExploredSucessesInt < self.ExploringSuccessesInt:

			#
			# Prepare
			#

			#Check
			if hasattr(self.ExploringRangeVariable,'items'):
				self.ExploredRangeTuplesList=self.ExploringRangeVariable.items()

			#Check
			if hasattr(self.ExploringConditionVariable,'items'):
				self.ExploredConditionTuplesList=self.ExploringConditionVariable.items()

			#Check
			if len(self.ExploredRangeTuplesList)!=len(self.ExploredParameterStrsList):
				self.ExploredParameterStrsList = map(
					lambda __TuplesList:__TuplesList[0],
					self.ExploredRangeTuplesList
				)

			#
			# Pick
			#

			#Check
			while self.ExploringTrialsInt > self.ExploredTrialsInt :

				#count
				self.ExploredTrialsInt +=1

				#debug
				'''
				self.debug(
					[
						"We test with a new trial set",
						('self.',self,[
								'ExploredTrialsInt'
							])
					]
				)
				'''

				#init the ranges
				map(
					lambda __TuplesList:
					setattr(
						self,
						__TuplesList[0],
						__TuplesList[1](self)
					),
					self.ExploredRangeTuplesList
				)

				#
				# Test
				#

				#call
				getattr(self,self.ExploringMethodStr)()

				#
				# Each Check
				#

				#init
				self.ExploredCheckBool = True

				#loop
				for __ConditionTuple in self.ExploredConditionTuplesList:

					#Check
					if __ConditionTuple[1](self) == False:

						#set
						self.ExploredCheckBool = False

						#break
						break

				#debug
				'''
				self.debug(
					[
						('self.',self,[
								'ExploredCheckBool'
							])
					]
				)
				'''

				#
				# Total Check
				#

				#Check
				if self.ExploredCheckBool:

					#count
					self.ExploredSucessesInt += 1

					#keep
					self.ExploredStoreTuplesListsList.append(
						map(
							lambda __KeyStr:
							(__KeyStr,getattr(self,__KeyStr)),
							self.ExploredKeepStrsList+self.ExploredParameterStrsList
						)
					)

					#debug
					'''
					self.debug(
						[
							"it is a sucess",
							('self.',self,['ExploredStoreTuplesListsList'])
						]
					)
					'''

					#break maybe
					if self.ExploredSucessesInt >= self.ExploringSuccessesInt:
						
						#break
						break

			#debug
			'''
			self.debug(
				[
					('We reached the max of Trials ot pick')
				]
			)
			'''
			
		else:

			#debug
			'''
			self.debug(
				[
					('We reached the sufficient number of sucesses')
				]
			)
			'''

#</DefineClass>

#<DefineLocals>
#<DefineLocals>

#</DefinePrint>
ExplorerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'ExploringMethodStr',
		'ExploringRangeVariable', 
		'ExploringConditionVariable', 
		'ExploringTrialsInt',
		'ExploringSuccessesInt',
		'ExploredRangeTuplesList',
		'ExploredConditionTuplesList',
		'ExploredParameterStrsList',
		'ExploredKeepStrsList',
		'ExploredCheckBool',
		'ExploredStoreTuplesListsList',
		'ExploredTrialsInt',
		'ExploredSucessesInt'
	]
)
#<DefinePrint>
