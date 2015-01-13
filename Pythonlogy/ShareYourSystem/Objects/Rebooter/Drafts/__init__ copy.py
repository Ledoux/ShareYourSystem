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
BaseModuleStr="ShareYourSystem.Objects.Concluder"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
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
						_RebootingDoStrsList=None,
						_RebootingNameStrsList=None,
						_RebootingAllDoBool=True,
						_RebootingAllNameBool=True,
						_RebootingSetDoIsBool=True,
						_RebootedWatchBoolKeyStrsList=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_reboot(self):

		#debug
		'''
		self.debug(
					[
						'self.__dict__.keys() is '+str(self.__dict__.keys()),
						('self.',self,[
										'RebootingDoStrsList',
										'RebootingNameStrsList'
										])
					]
				)
		'''

		#filter
		self.RebootedWatchBoolKeyStrsList=SYS._filter(
				lambda _KeyStr:
				(_KeyStr.startswith('_Watch') or _KeyStr.startswith('Watch')) and (
					'Watch'.join(
						_KeyStr.split('Watch')[1:]
					).split('With')[0] in self.RebootingDoStrsList
					if self.RebootingAllDoBool==False else True
				 	) and (
					any(
						map(
							lambda __NameStr:
							_KeyStr.endswith(__NameStr+'Bool'),
							self.RebootingNameStrsList
						)
					) if self.RebootingAllNameBool==False else True
				),
				self.__dict__.keys()
			)

		#map
		map(
				lambda __RebootedWatchBoolKeyStr:
				self.__setattr__(
					__RebootedWatchBoolKeyStr 
					if __RebootedWatchBoolKeyStr[0]!='_' 
					else __RebootedWatchBoolKeyStr[1:],
					False
				),
				self.RebootedWatchBoolKeyStrsList
			)


		#Check
		if self.RebootingSetDoIsBool:

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

