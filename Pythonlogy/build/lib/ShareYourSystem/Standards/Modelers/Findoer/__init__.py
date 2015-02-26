# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Findoer (sorry Finder is already an important module in python standards, so just to be sure to not override...)
instances helps to find in a hdf5 table RowedVariablesList corresponding to the FindingWhereTuplesList.

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
	
	#Definition
	RepresentingKeyStrsList=[
								'FindingMongoDict',
								'FindingWhereTuplesList',
								'FoundMongoRowDictsList',	
								'FoundHdfRowDictsList',			
								'FoundFilterRowDictsList',
								'FoundMongoIsBool',
								'FoundHdfIsBool'
							]

	def default_init(self,
					_FindingMongoDict=None,
					_FindingWhereTuplesList=None,
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
		self.debug(("self.",self,['ModeledKeyStr','FindingWhereTuplesList']))
		'''

		#table first
		self.table()

		#If the FoundRowedTuplesList was not yet setted
		if self.FoundHdfIsBool==False:

			#debug
			'''
			self.debug('FoundHdfRowDictsList was not yet setted')
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


			if self.ModelingMongoBool:

				#Take the first one in the list
				self.FoundMongoRowDictsList=list(
					self.TabledMongoCollection.find(
						self.FindingMongoDict
					)
				)
				
				#set
				self.FoundMongoIsBool=True

				#debug
				self.debug(
								[
									("self.",self,['FoundMongoRowDictsList'])
								]
						)

			
		#Now we find with a condition Tuples list 
		self.FoundFilterRowDictsList=SYS.filterNone(
			SYS.where(
				self.FoundHdfRowDictsList,
				self.FindingWhereTuplesList
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

#</DefineClass>

