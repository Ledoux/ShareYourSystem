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
BaseModuleStr="ShareYourSystem.Standards.Viewers.Pyploter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Recorder','Record','Recording','Recorded')
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineLocals>
RecorderPrefixStr='*'
#</DefineLocals>

#<DefineClass>
@DecorationClass(**{
	'ClassingStructureVariable':[
			('Trace','Traces'),
			('Sample','Samples')
		]
})
class RecorderClass(BaseClass):
	
	def default_init(self,
						_RecordKeyStr="",
						_RecordingKeyVariable=None,
						_RecordingLabelVariable=None,
						_RecordedTraceFloatsArray=None,
						_RecordedInitFloatsArray=None,
						_RecordedParentSingularStr="",		
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_record(
			self
		):	

		#/#################/#
		# Determine if it is an inside structure or the top
		#

		#debug
		'''
		self.debug(
			[
				'We record here',
				'First look for deeper teams in the structure',
			]
		)
		'''

		#Check
		if self.ParentedTotalSingularListDict!=None and len(self.ParentedTotalSingularListDict)>0:

			#debug
			'''
			self.debug(
				[
					'self.ParentedTotalSingularListDict.keys() is ',
					str(self.ParentedTotalSingularListDict.keys())
				]
			)
			'''

			#get
			self.RecordedParentSingularStr=self.ParentedTotalSingularListDict.keys()[0]

		#debug
		'''
		self.debug(
			[
				'Ok',
				('self.',self,['RecordedParentSingularStr'])
			]
		)
		'''

		#debug
		'''
		self.debug(
				[
					'We are at this level',
					('self.',self,['RecordedParentSingularStr'])
				]
			)
		'''
		
		#/###################/#
		# Cases
		#

		#Check
		if self.ParentDeriveTeamerVariable==None or 'Traces' in self.TeamDict or self.ParentDeriveTeamerVariable.TeamTagStr not in [
			'Traces',
			'Samples'
		]:

			#/###################/#
			# Recorder level
			# network

			#debug
			'''
			self.debug(
				[
					'This is the Recorder level',
					'we structure Traces and Samples'
				]
			)
			'''

			#structure
			self.structure(
				[
					'Traces',
					'Samples'
				],
				'#all',
				_ManagerCommandSetList=['record']
			)
			
		#Check
		elif self.RecordedParentSingularStr=='Trace':

			#/###################/#
			# Traces level
			#

			#debug
			'''
			self.debug(
					[
						'This is the Traces level',
						'First get the array to trace',
						('self.',self,['RecordingKeyVariable'])
					]
				)
			'''

			#get
			RecordedTopDeriveRecorderVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#/##################/#
			# First get the array to trace
			#

			#get
			if type(self.RecordingKeyVariable)==None.__class__:

				#Check
				if self.ManagementTagStr.startswith(RecorderPrefixStr):

					#debug
					self.debug(
						[
							('self.',self,['ManagementTagStr'])
						]
					)

					#get
					self.RecordedTraceFloatsArray=getattr(
						RecordedTopDeriveRecorderVariable,
						SYS.deprefix(
							self.ManagementTagStr,
							RecorderPrefixStr
						)
					)

			elif type(self.RecordingKeyVariable).__name__!='ndarray':
		
				#get
				self.RecordedTraceFloatsArray=RecordedTopDeriveRecorderVariable[
					self.RecordingKeyVariable
				]

			else:

				#alias
				self.RecordedTraceFloatsArray=self.RecordingKeyVariable

				#alias
				if self.RecordKeyStr=="":
					self.RecordKeyStr=str(self.RecordingKeyVariable)

			#debug
			'''
			self.debug(
				[
					'We have getted the RecordedTraceFloatsArray',
					('self.',self,['RecordedTraceFloatsArray']),
					'Now set the init'
				]
			)
			'''

			#Check
			if type(self.RecordedTraceFloatsArray)!=None.__class__:

				#/##################/#
				# Prepare initial conditions
				# with the Matrixer

				#debug
				'''
				self.debug(
					[
						'We prepare the initial conditions',
						'len(self.RecordedTraceFloatsArray) is ',
						str(len(self.RecordedTraceFloatsArray))
					]
				)
				'''

				#matrix
				self.RecordedInitFloatsArray=self.numscipy(
						_SizeTuple=(len(self.RecordedTraceFloatsArray),1)
					).NumscipiedRandomFloatsArray[:,0]

				#debug
				'''
				self.debug(
					[
						'We have prepared the initial conditions',
						('self.',self,['RecordedInitFloatsArray'])
					]
				)
				'''

	
#</DefineClass>

#</DefinePrint>
RecorderClass.PrintingClassSkipKeyStrsList.extend(
	[
		'RecordKeyStr',
		'RecordingKeyVariable',
		'RecordingLabelVariable',
		'RecordedTraceFloatsArray',
		'RecordedInitFloatsArray',
		'RecordedParentSingularStr'
	]
)
#<DefinePrint>
