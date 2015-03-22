# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

A Tracer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Recorders.Matrixer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Tracer','Trace','Tracing','Traced')
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Itemizers import Pointer,Networker
from ShareYourSystem.Standards.Recorders import Recorder
#</ImportSpecificModules>

#<DefineLocals>
TracerPrefixStr='*'
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class TracerClass(BaseClass):
	
	def default_init(self,
						_TraceDeriveRecorderVariable=None,
						_TraceKeyStr="",
						_TracingKeyVariable=None,
						_TracedValueFloatsArray=None,
						_TracedInitFloatsArray=None,
						**_KwargVariablesDict
					):
		
		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#init
		self.TraceDeriveRecorderVariable=self
	
	def do_trace(self):
		
		#/##################/#
		# Find the parent recorder
		#

		#debug
		'''
		self.debug(
			[
				'We trace here',
				'Networker.NetworkInTeamKeyStr in self.TeamDict is ',
				str(Networker.NetworkInTeamKeyStr in self.TeamDict),
				#('self.',self,['NetworkDeriveNetworkerVariable']),
				'self.TeamDict.keys() is ',
				str(self.TeamDict.keys()),
				'Networker.NetworkInTeamKeyStr is ',
				Networker.NetworkInTeamKeyStr
			]
		)
		'''

		"""
		#Check
		if Networker.NetworkInTeamKeyStr in self.TeamDict:

			#debug
			'''
			self.debug(
				[
					'self.TeamDict[Networker.NetworkInTeamKeyStr].ManagementDict.keys() is ',
					str(self.TeamDict[Networker.NetworkInTeamKeyStr].ManagementDict.keys())
				]
			)
			'''

			#get
			self.TraceDeriveRecorderVariable=self.TeamDict[
				Networker.NetworkInTeamKeyStr
			].ManagementDict[Pointer.PointManagementPrefixStr+'Recorder'].PointToVariable

			#debug
			'''
			self.debug(
				[
					'Ok we have setted the TraceDeriveRecorderVariable',
					('self.',self,['TraceDeriveRecorderVariable'])
				]
			)
			'''
		"""

		#debug
		'''
		self.debug(
			[
				'We set the TraceDeriveRecorderVariable
				('self.',self,['ParentDeriveTeamerVariable'])
			]
		)
		'''

		#get
		self.TraceDeriveRecorderVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

		#/##################/#
		# First get the array to trace
		#

		#debug
		'''
		self.debug(
			[
				'We trace here',
				('self.',self,['TracingKeyVariable'])
			]
		)	
		'''

		#get
		if type(self.TracingKeyVariable)==None.__class__:

			#Check
			if self.ManagementTagStr.startswith(TracerPrefixStr):

				#get
				self.TracedValueFloatsArray=getattr(
					self.TraceDeriveRecorderVariable,
					SYS.deprefix(
						self.ManagementTagStr,
						TracerPrefixStr
					)
				)

		elif type(self.TracingKeyVariable).__name__!='ndarray':
	
			#get
			self.TracedValueFloatsArray=self.TraceDeriveRecorderVariable[
				self.TracingKeyVariable
			]


		else:

			#alias
			self.TracedValueFloatsArray=self.TracingKeyVariable


		#alias
		if self.TraceKeyStr=="":
			self.TraceKeyStr=str(self.TracingKeyVariable)

		#debug
		'''
		self.debug(
			[
				'We have setted the TracedValueFloatsArray'
			]
		)
		'''

		#Check
		if type(self.TracedValueFloatsArray)!=None.__class__:

			#/##################/#
			# Prepare initial conditions
			# with the Matrixer

			#debug
			'''
			self.debug(
				[
					'We prepare the initial conditions',
					'len(self.TracedValueFloatsArray) is ',
					str(len(self.TracedValueFloatsArray))
				]
			)
			'''

			#matrix
			self.TracedInitFloatsArray=self.matrix(
					_SizeTuple=(len(self.TracedValueFloatsArray),1)
				).MatrixedRandomFloatsArray[:,0]

			#debug
			'''
			self.debug(
				[
					'We have prepared the initial conditions',
					('self.',self,['TracedInitFloatsArray'])
				]
			)
			'''

	def propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable):

		"""
		#/##################/#
		# Find the parent recorder
		#

		#debug
		'''
		self.debug(
			[
				'We have parented',
				'We trace here',
				'Networker.NetworkInTeamKeyStr in self.TeamDict is ',
				str(Networker.NetworkInTeamKeyStr in self.TeamDict),
				#('self.',self,['NetworkDeriveNetworkerVariable']),
				'self.TeamDict.keys() is ',
				str(self.TeamDict.keys()),
				'Networker.NetworkInTeamKeyStr is ',
				Networker.NetworkInTeamKeyStr
			]
		)
		'''

		#Check
		if Networker.NetworkInTeamKeyStr in self.TeamDict:

			#debug
			'''
			self.debug(
				[
					'self.TeamDict[Networker.NetworkInTeamKeyStr].ManagementDict.keys() is ',
					str(self.TeamDict[Networker.NetworkInTeamKeyStr].ManagementDict.keys())
				]
			)
			'''

			#get
			self.TraceDeriveRecorderVariable=self.TeamDict[
				Networker.NetworkInTeamKeyStr
			].ManagementDict[Pointer.PointManagementPrefixStr+'Recorder'].PointToVariable

			#debug
			'''
			self.debug(
				[
					'Ok we have setted the TraceDeriveRecorderVariable',
					('self.',self,['TraceDeriveRecorderVariable'])
				]
			)
			'''
		"""

		#/##################/#
		# trace
		#

		#Check
		if self.ParentDeriveTeamerVariable!=None and self.ParentDeriveTeamerVariable.TeamTagStr=='Traces':

			#trace
			self.trace()

		#/##################/#
		# Base method
		#

		#call the base method
		BaseClass.propertize_setWatchAfterParentWithParenterBool(
			self,
			_SettingValueVariable
		)

#</DefineClass>

#<DefineLocals>

#set
Recorder.TracesClass.ManagingValueClass=TracerClass

#</DefineLocals>

#<DefinePrint>
TracerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'TraceKeyStr',
		'TracingKeyVariable',
		'TracedValueFloatsArray',
		'TraceDeriveRecorderVariable',
		'TracedInitFloatsArray',
	]
)
#</DefinePrint>