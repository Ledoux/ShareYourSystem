# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Parenter completes the list of grand-parent nodes that 
a child node could have. It is a recursive top-down set
of the pointers and the pathStrs.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Commander"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
#</ImportSpecificModules>

#<DefineLocals>
WalkingStr="zz"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class WalkerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'WalkingSocketDict',
									#'WalkedOrderedDict',
									#'WalkedTopOrderedDict'
								]

	def default_init(self,
				_WalkingSocketDict=None,
				_WalkedOrderedDict=None,
				_WalkedTopOrderedDict=None,
				**_KwargVariablesDict
			):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_walk(self):
		
		#Init the WalkedTopOrderedDict
		WalkedTopOrderedDict=None
		if 'IdStr' not in self.WalkingSocketDict:

			#Definition the IdStr of this walk
			IdStr=str(id(self.WalkingSocketDict))

			#set the _WalkingSocketDict
			self.WalkingSocketDict.update(
									{
										'IdStr':IdStr,
										'TopVariable':self,
									}
								)

			#Definition WalkedTopOrderedDictKeyStr
			WalkedTopOrderedDictKeyStr='Walked'+WalkingStr+IdStr+WalkingStr+'OrderedDict'

			#set the corresponding WalkedOrderedDict
			self.__setattr__(
								WalkedTopOrderedDictKeyStr,
								collections.OrderedDict(**
									{
										'IndexInt':-1,
										'TopIntsList':['/'],
										'TopVariablesList':[self]
									}
								)
							)

			#Alias this Dict
			self.WalkedTopOrderedDict=getattr(
				self,
				WalkedTopOrderedDictKeyStr
			)

		else:

			#Get the information at the top
			WalkedTopOrderedDictKeyStr='Walked'+WalkingStr+self.WalkingSocketDict['IdStr']+WalkingStr+'OrderedDict'
			self.WalkedTopOrderedDict=getattr(
				self.WalkingSocketDict['TopVariable'],
				WalkedTopOrderedDictKeyStr
			)
			self.WalkedTopOrderedDict['IndexInt']+=1
			self.WalkedTopOrderedDict['TopIntsList']+=[str(
				self.WalkedTopOrderedDict['IndexInt'])]
			self.WalkedTopOrderedDict['TopVariablesList']+=[self]

		#A command just before is possible
		if 'BeforeCommandLiargVariablesList' in self.WalkingSocketDict:

			#debug
			'''
			self.debug(
					('self.WalkingSocketDict.',self.WalkingSocketDict,
						['BeforeCommandLiargVariablesList']
					)
				)
			'''

			#command
			self.command(
				*self.WalkingSocketDict['BeforeCommandLiargVariablesList']
			)

			

			#debug
			'''
			self.debug(
					'Ok we have before commanded'
				)
			'''

		#Debug
		'''
		self.debug(('self.',self,['WalkingSocketDict']))
		'''
		
		#get
		WalkedValueVariable=self[
			self.WalkingSocketDict['RouteGetVariable']
		]

		#filter self for the walk to avoid circular call
		if WalkedValueVariable==self:
			WalkedValueVariable=[]
		elif type(WalkedValueVariable)==list:
			WalkedValueVariable=SYS._filter(
				lambda __ElementVariable:
				__ElementVariable!=self,
				WalkedValueVariable
			)

		#Command a walk in variables getted with RouteGetVariable
		self.command(
						WalkedValueVariable,
						[
							(
								'walk',
								self.WalkingSocketDict		
							)
						]
					)

		#An command just after is possible
		if 'AfterCommandLiargVariablesList' in self.WalkingSocketDict:

			#debug
			'''
			self.debug(('self.WalkingSocketDict.',self.WalkingSocketDict,['AfterCommandLiargVariablesList']))
			'''

			#command
			self.command(
				*self.WalkingSocketDict[
					'AfterCommandLiargVariablesList'
				]
			)

		#Retrieve the previous Path
		if len(self.WalkedTopOrderedDict['TopIntsList'])>0:
			self.WalkedTopOrderedDict['TopIntsList']=self.WalkedTopOrderedDict[
			'TopIntsList'][:-1] 
			self.WalkedTopOrderedDict['TopVariablesList']=self.WalkedTopOrderedDict[
			'TopVariablesList'][:-1]

		#Return self
		if self.WalkingSocketDict['TopVariable']==self:
			self.WalkedOrderedDict=WalkedTopOrderedDict
			del self.__dict__[WalkedTopOrderedDictKeyStr]
			return self
#</DefineClass>
