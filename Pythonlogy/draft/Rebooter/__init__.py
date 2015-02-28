# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Rebooter

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Objects.Debugger"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import copy
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class RebooterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
		'RebootingDoStrsList',
		'RebootingNameStrsList',
		'RebootingAllDoBool',
		'RebootingAllNameBool',
		'RebootingDoingIsBool',
		'RebootedWatchBoolKeyStrsList',
		'RebootingSetDoIsBool'
	]

	def default_init(self,
						_RebootingNameStrsList=None,
						_RebootingDoStrsList=None,
						_RebootingAllNameBool=True,
						_RebootingAllDoBool=True,
						_RebootingSetDoIsBool=True,
						_RebootedWatchBoolKeyStrsList=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_reboot(self):

		#set
		if self.RebootingAllNameBool:

			#filter
			self.RebootingNameStrsList=SYS.filterNone(
				map(
					lambda __MroClass:
					__MroClass.NameStr 
					if hasattr(__MroClass,'DoStr')
					else None,
					self.__class__.__mro__
				)
			)

		#set
		if self.RebootingAllDoBool:

			#filter
			self.RebootingDoStrsList=SYS.filterNone(
				map(
					lambda __MroClass:
					__MroClass.DoStr 
					if hasattr(__MroClass,'DoStr')
					else None,
					self.__class__.__mro__
				)
			)
		
		#debug
		'''
		self.debug(
					('self.',self,[
						'RebootingDoStrsList',
						'RebootingNameStrsList'
						])
				)
		'''
		
		#map
		map(
				lambda __RebootingNameStr:
				self.setSwitch(
					__RebootingNameStr,
					self.RebootingDoStrsList
				),
				self.RebootingNameStrsList
			)


		#Check
		if self.RebootingSetDoIsBool:

			#debug
			'''
			self.debug(('self.',self,['RebootingNameStrsList']))
			'''

			#map
			map(
					lambda __RebootingClass:
					self.setDone(
						__RebootingClass
					) 
					#if hasattr(__RebootingClass,'DoneAttributeVariablesOrderedDict')
					#else None,
					,map(
							lambda __RebootingClassStr:
							getattr(
								SYS,
								__RebootingClassStr
							) 
							#if hasattr(SYS,__RebootingClassStr)
							#else None
							,map(SYS.getClassStrWithNameStr,self.RebootingNameStrsList)
						)
				)


#</DefineClass>

