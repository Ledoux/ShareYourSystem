# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Recorder

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Computers.Matrixer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Recorder','Record','Recording','Recorded')
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Itemizers import Pointer,Networker
#</ImportSpecificModules>

#<DefineLocals>
class TracesClass(Networker.NetworkerClass):pass 
class EventsClass(Networker.NetworkerClass):pass 
RecordSampleTeamKeyStr=Networker.NetworkOutPrefixStr+'Samples'
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class RecorderClass(BaseClass):
	
	def default_init(self,
						_RecordedNetworkBool=False,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_record(
			self
		):	

		#debug
		'''
		self.debug(
				[
					'We record here',
					'network in the Traces and Events
				]
			)
		'''

		#/###################/#
		# Network the traces, events samples
		#

		#Check
		if self.RecordedNetworkBool==False:

			#debug
			'''
			self.debug(
					[
						'network in the Traces and Events
					]
				)
			'''

			#set
			self.PointingInManagementKeyStr=Pointer.PointManagementPrefixStr+'Recorder'

			#network
			self.network(
				[
					'Traces',
					'Events',
					'Samples'
				]
			)

		#/###################/#
		# Make monit the samples
		#

		#Check
		if RecordSampleTeamKeyStr in self.TeamDict:

			#debug
			self.debug(
				[
					'We make monit the networked samples'
				]
			)

			#map
			map(
					lambda __DerivePointer:
					__DerivePointer.PointToVariable.monit(),
					self.TeamDict[RecordSampleTeamKeyStr].ManagementDict.values()
				)

#</DefineClass>

#<DefineLocals>
RecorderClass.TeamingClassesDict.update(
	{
		'Traces':TracesClass,
		'Events':EventsClass
	}
)
#</DefineLocals>

#</DefinePrint>
RecorderClass.PrintingClassSkipKeyStrsList.extend(
	[
		'RecordedNetworkBool'
	]
)
#<DefinePrint>
