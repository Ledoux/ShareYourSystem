# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Findoer (sorry Finder is already an important module in python standards, so just to be sure to not override...)
instances helps to find in a hdf5 table RowedVariablesList corresponding to the FindingWhereVariable.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Modelers.Retriever"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>

#from ShareYourSystem.Functers import Argumenter,Hooker
from ShareYourSystem.Standards.Modelers import Rower
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class FindoerClass(BaseClass):
	
	def default_init(self,
					_FindingWhereVariable=None,
					_FindingRecoverBool=False,
					_FoundMongoRowDictsList=None,	
					_FoundHdfRowDictsList=None,			
					_FoundFilterRowDictsList=None, 
					_FoundMongoIsBool=False,
					_FoundHdfIsBool=False,
					**_KwargVariablesDict
				):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)
		
	def do_find(self):

		#debug
		'''
		self.debug(
			[
				'we are going to find',
				("self.",self,[
						'FindingWhereVariable'
					])
			]
		)
		'''

		#/###################/#
		# Case of mongo
		#

		#If the FoundMongoIsBool was not yet setted
		if self.FoundMongoIsBool==False:

			#debug
			'''
			self.debug(
				[
					'FoundMongoRowDictsList was not yet setted'
				]
			)
			'''
			
			#Check
			if self.ModelingMongoBool:

				#find in the list
				self.FoundMongoRowDictsList=list(
					self.TabledMongoCollection.find(
						self.FindingWhereVariable
					)
				)
				
				#set
				self.FoundMongoIsBool=True

				#debug
				'''
				self.debug(
							[
								("self.",self,['FoundMongoRowDictsList'])
							]
						)
				'''

		#/###################/#
		# Case of hdf
		#

		#If the FoundHdfIsBool was not yet setted
		if self.FoundHdfIsBool==False:

			#debug
			'''
			self.debug(
				[
					'FoundHdfRowDictsList was not yet setted',
				]
			)
			'''

			#Check
			if self.ModelingHdfBool:

				#Take the first one in the list
				self.FoundHdfRowDictsList=Rower.getRowedDictsListWithTable(
					#self.TabularedHdfGroupVariable._f_getChild(
					#	self.TabularedHdfKeyStrsList[0]
					#)
					self.TabledHdfTable
				)

				#set
				self.FoundHdfIsBool=True

				#debug
				'''
				self.debug(
								[
									("self.",self,['FoundHdfRowDictsList'])
								]
						)
				'''

				#Now we find with a condition Tuples list 
				self.FoundHdfRowDictsList=SYS.filterNone(
					SYS.where(
						self.FoundHdfRowDictsList,
						self.FindingWhereVariable
					)
				)

		#debug
		'''
		self.debug(
					[
						'The where is over now',
						("self.",self,['FoundFilterRowDictsList'])
					]

				)
		'''

		#/##################/#
		# Maybe recover
		#

		#Check
		if self.FindingRecoverBool:

			#Check
			if len(self.FoundMongoRowDictsList)==1:

				#get
				self.FoundRecoverDict=self.FoundMongoRowDictsList[0]

			elif len(self.FoundHdfRowDictsList)==1:

				#get
				self.FoundRecoverDict=self.FoundHdfRowDictsList[0]

			#debug
			'''
			self.debug(
						[
							'Now we update with the self.RecoveredDict',
							'self.RecoveredDict is '+str(self.RecoveredDict)
						]
					)
			'''

			#set the RetrievingIndexesList and retrieve
			self.RetrievingIndexesList=(
											0,
											self.FoundRecoverDict['RowInt']
										)
		
			#Now we can retrieve
			self.retrieve()

#</DefineClass>

#</DefinePrint>
FindoerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'FindingWhereVariable',
		'FindingRecoverBool',
		#'FoundMongoRowDictsList',	
		#'FoundHdfRowDictsList',			
		'FoundFilterRowDictsList',
		'FoundMongoIsBool',
		'FoundHdfIsBool',
		'FoundRecoverDict'
	]
)
#<DefinePrint>
