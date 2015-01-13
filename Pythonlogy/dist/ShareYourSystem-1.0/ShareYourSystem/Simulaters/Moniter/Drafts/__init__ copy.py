# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Moniter

"""


#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Simulaters.Populater"
DecorationModuleStr="ShareYourSystem.Classors.Representer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineDoStrsList>
DoStrsList=["Moniter","Monit","Monitering","Monitered"]
#<DefineDoStrsList>

#<DefineClass>
@DecorationClass()
class MoniterClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
									'MonitoringTypeStr',
									'MonitoringIndexIntsList',
									'MonitoredDeriveSimulaterPointedVariable',
									'MonitoredDeriveClockerPointedVariable'
								]
	
	def default_init(self,
						_MonitoringTypeStr='State',
						_MonitoringDeriveSimulaterGetStr="/",
						_MonitoringDeriveClockerGetStr="/NodedParentVariable/<Clockome>RecordClocker",
						_MonitoringVariableStr="",
						_MonitoringIndexIntsList=None,
						_MonitoredDeriveSimulaterPointedVariable=None,
						_MonitoredDeriveClockerPointedVariable=None,
						**_KwargVariablesDict
					):
		
		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)
	
	#<DefineDoMethod>	
	def do_monit(self):

		#link
		self.link(
					[
						[self.MonitoringDeriveSimulaterGetStr,'MonitoredDeriveSimulater'],
						[self.MonitoringDeriveClockerGetStr,'MonitoredDeriveClocker']
					]
				)

#</DefineClass>

