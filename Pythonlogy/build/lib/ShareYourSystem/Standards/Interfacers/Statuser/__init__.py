# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Statuser

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Processer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import os
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class StatuserClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
							'StatusingProcessStr',
							'StatusedSnapshotStr',
							'StatusedLineStrsList',
							'StatusedIdStrsList'
						]

	def default_init(self,
						_StatusingProcessStr="",
						_StatusedSnapshotStr="",
						_StatusedLineStrsList=None,
						_StatusedIdStrsList=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)
	
	def do_status(self):

		#debug
		'''
		self.debug(('self.',self,['StatusingProcessStr']))
		'''

		#Check
		if self.StatusingProcessStr!="":

			#call
			self.StatusedSnapshotStr=self.process(
				"ps -ef | grep "+self.StatusingProcessStr
			).ProcessedBashStr

			#debug
			'''
			self.debug(('self.',self,['StatusedSnapshotStr']))
			'''

			#map
			if self.StatusingProcessStr=='Python':

				#filter
				self.StatusedLineStrsList=SYS._filter(
						lambda __LineStr:
						SYS.PythonPathStr in __LineStr,
						self.StatusedSnapshotStr.split('\n')
					)
			else:

				#split
				self.StatusedLineStrsList=self.StatusedSnapshotStr.split('\n')

			#debug
			'''
			self.debug(
					[
						('self.',self,['StatusedLineStrsList']),

					]
				)
			'''
			
			#filter
			self.StatusedLineStrsList=SYS._filter(
					lambda __StatusedLineStr:
					__StatusedLineStr!='',
					self.StatusedLineStrsList
				)

			#call
			self.StatusedIdStrsList=map(
				lambda __LineStr:
				__LineStr.split()[1],
				self.StatusedLineStrsList	
			)

			#debug
			'''
			self.debug(('self.',self,['StatusedIdStrsList']))
			'''

#</DefineClass>
