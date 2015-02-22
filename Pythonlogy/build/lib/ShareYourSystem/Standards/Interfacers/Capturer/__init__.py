# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Capturer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Hdformater"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from cStringIO import StringIO
import sys
import copy
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class CapturerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'CapturingStopBool',
								'CapturedStdoutVariable',
								'CapturedPrintStrsList'
							]

	def default_init(self,
						_CapturingStopBool={
								'DefaultingSetType':property,
								'PropertizingInitVariable':False,
								'PropertizingDocStr':''
						},
						_CapturedStdoutVariable=sys.stdout,
						_CapturedPrintStrsList=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)
	
	def setCapturingStopBool(self,_SettingValueVariable):

		#set
		self._CapturingStopBool=_SettingValueVariable

		#reset the CapturedStrsList
		if _SettingValueVariable:

			#Check
			if self.CapturedPrintStrsList!=None:

				if hasattr(sys.stdout,'getvalue'):
					
					#extend
					self.CapturedPrintStrsList.extend(
						sys.stdout.getvalue().splitlines()
					)

			#reset
       		sys.stdout = self.CapturedStdoutVariable

	def do_capture(self):

		#debug
		'''
		self.debug('We capture here ')
		'''

		#set
		self.CapturedStdoutVariable = sys.stdout
        
		#init
		sys.stdout = StringIO()

#</DefineClass>
