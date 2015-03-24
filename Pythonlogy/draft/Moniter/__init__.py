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
BaseModuleStr="ShareYourSystem.Standards.Recorders.Tracer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
Tracer=BaseModule
from ShareYourSystem.Standards.Itemizers import Networker
#</ImportSpecificModules>

#<DefineLocals>
class SamplesClass(Networker.NetworkerClass):pass
MoniterSampleTeamStr='Samples'
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class MoniterClass(BaseClass):
	
	def default_init(self,
						_MonitorDeriveTracerVariable=None,
						_MoniterDeriveTracerVariable=None,
						_MoniteringLabelIndexIntsArray=None,
						_MoniteringTimeIndexIntsArray=None,
						_MoniteredTraceFloatsArray=None,
						**_KwargVariablesDict
					):
		
		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#init
		self.MonitorDeriveTracerVariable=self
		
	def do_monit(self):
	
		#debug
		'''
		self.debug(
			[
				'We monit here',
				('self.',self,['MoniteringLabelIndexIntsArray'])
			]
		)
		'''

		#/##################/#
		# Find the grand parent Tracer
		# 

		#Check
		if self.ParentGrandDeriveTeamerVariable!=None:
			self.MonitorDeriveTracerVariable=self.ParentGrandDeriveTeamerVariable

		#debug
		'''
		self.debug(
				[
					'Before just check',
					('self.',self,[
						'ParentGrandDeriveTeamerVariable',
						'MonitorDeriveTracerVariable'
					])
				]
			)
		'''
		
		#/##################/#
		# pick
		# 

		if type(self.MoniteringLabelIndexIntsArray)!=None.__class__:

			#debug
			'''
			self.debug(
				[
					'We pick in the label',
					('self.',self,['MoniteringLabelIndexIntsArray'])
				]
			)
			'''

			#pick
			self.MoniteredTraceFloatsArray=self.MonitorDeriveTracerVariable.TracedValueFloatsArray[
					self.MoniteringLabelIndexIntsArray,
					:
				]
			
		if type(self.MoniteringTimeIndexIntsArray)!=None.__class__:

			#debug
			'''
			self.debug(
				[
					'We pick in the time',
					('self.',self,['MoniteringTimeIndexIntsArray'])
				]
			)
			'''

			#pick
			self.MoniteredTraceFloatsArray=self.MoniteredTraceFloatsArray[
				:,
				self.MoniteringTimeIndexIntsArray
			]

#</DefineClass>

#<DefineLocals>

Tracer.TracerClass.TeamingClassesDict.update(
	{
		MoniterSampleTeamStr:SamplesClass
	}
)
SamplesClass.ManagingValueClass=MoniterClass

#</DefineLocals>

#</DefinePrint>
MoniterClass.PrintingClassSkipKeyStrsList.extend(
	[
		'MonitorDeriveTracerVariable',
		'MoniteringLabelIndexIntsArray',
		'MoniteringTimeIndexIntsArray',
		#'MoniteredTraceFloatsArray'
	]
)
#<DefinePrint>