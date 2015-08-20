# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>



"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Structurer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Coordinater','Coordinate','Coordinating','Coordinated')
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class CoordinaterClass(BaseClass):
	
	def default_init(
					self,	
					_CoordinatingMethodVariable = None,	
					_CoordinatedMethodStrsList = None,	
					_CoordinatedParentSingularStr = "",								
					**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_coordinate(self):
		""" """

		#debug
		'''
		self.debug(
			[
				('self.',self,['CoordinatingMethodVariable'])
			]
		)
		'''

		#Check
		if type(self.CoordinatingMethodVariable)==str:
			self.CoordinatedMethodStrsList = [self.CoordinatingMethodVariable]
		else:
			self.CoordinatedMethodStrsList = self.CoordinatingMethodVariable

		#DefaultDoFunction
		map(
			lambda __CoordinatingMethodStr:
			setattr(
				self.__class__,
				__CoordinatingMethodStr,
				self.__class__.doCoordinateMethod
			) if getattr(self,"do_"+__CoordinatingMethodStr).__name__=="DefaultDoFunction"
			else None,
			self.CoordinatedMethodStrsList
		)
			
		#/###############/#
		# Parent Top case
		#

		#Check
		if self.ParentDeriveTeamerVariable==None:
			
			#debug
			self.debug(
				[
					"self.TeamingClassesDict is "+str(
						self.TeamingClassesDict
					)
				]
			)

			#structure
			self.structure()

			#DefaultDoFunction
			map(
				lambda __CoordinatingTopMethodStr:
				getattr(self,__CoordinatingTopMethodStr)()
				if hasattr(self,__CoordinatingTopMethodStr)
				else None,
				map(
					lambda __CoordinatingMethodStr:
					__CoordinatingMethodStr+"Top",
					self.CoordinatedMethodStrsList
				)
			)

	def doCoordinateMethod(self):

		#debug
		'''
		self.debug(
			[
				"We do the doCoordinateMethod"
			]
		)
		'''

		#Check
		if self.ParentDeriveTeamerVariable != None:

			#/###############/#
			# Component Case
			#

			#Check
			if self.ParentedTotalSingularListDict!=None and len(
				self.ParentedTotalSingularListDict
			)>0:

				#get
				self.CoordinatedParentSingularStr = self.ParentedTotalSingularListDict.keys()[0]

				#debug
				'''
				self.debug(
					[
						('self.',self,[
								'CoordinatedParentSingularStr',
								#'StructureTopDeriveStructurerRigidVariable',
								'StructuringManagerCommandSetList'
							]
						)
					]
				)
				'''

				#map
				map(
					lambda __methodStr:
					getattr(self,__methodStr)() 
					if hasattr(self,__methodStr) else None,
					map(
						lambda __hookStr:
						__hookStr+self.CoordinatedParentSingularStr,
						self.StructureTopDeriveStructurerRigidVariable.StructuringManagerCommandSetList
					)
				)


	def mimic_structure(self):

		#Check
		if self.ParentDeriveTeamerVariable == None:

			#/###############/#
			# Parent Top case
			#

			#debug
			'''
			self.debug(
				[
					"We structure coordinate the top here",
					('self.',self,['CoordinatedMethodStrsList'])
				]
			)
			'''

			#call
			BaseClass.structure(
				self,
				self.TeamingClassesDict.keys(),
				"#all",
				_ManagerCommandSetList=self.CoordinatedMethodStrsList
			)

			
#</DefineClass>

#<DefineLocals>
#<DefineLocals>

#</DefinePrint>
CoordinaterClass.PrintingClassSkipKeyStrsList.extend(
	[
		"CoordinatingMethodVariable",	
		"CoordinatedMethodStrsList",
		"CoordinatedParentSingularStr"
	]
)
#<DefinePrint>
