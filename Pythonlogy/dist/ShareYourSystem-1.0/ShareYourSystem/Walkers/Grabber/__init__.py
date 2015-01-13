# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Grabber

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Walkers.Router"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
import collections
from ShareYourSystem.Functers import Argumenter
from ShareYourSystem.Noders import Noder
#</ImportSpecificModules>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class GrabberClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'GrabbingNodeStr',
									'GrabbingPickVariablesList',
									'GrabbedVariablesOrderedDict'
								]

	def default_init(self,
				_GrabbingNodeStr=None,
				_GrabbingPickVariablesList=None,
				_GrabbedVariablesOrderedDict=None,
				**_KwargVariablesDict):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Argumenter.ArgumenterClass()
	def do_grab(self):
			
		#Init
		if self.GrabbedVariablesOrderedDict==None:
			self.GrabbedVariablesOrderedDict=collections.OrderedDict()

		#debug
		'''
		self.debug(('self.',self,['GrabbingNodeStr','GrabbingPickVariablesList']))
		'''
		
		#Walk inside the Tree in order to parent
		self.walk(
					{
						'BeforeUpdateList':
						[
							('route',{'LiargVariablesList':[
																self.GrabbingPickVariablesList
															]
										})
						],
						'GatherVariablesList':[
						Noder.NodingPrefixGetStr+self.GrabbingNodeStr+Noder.NodingSuffixGetStr]
					}
				)

		#Link
		self.GrabbedVariablesOrderedDict=self.RoutedVariablesOrderedDict
		

#</DefineClass>
