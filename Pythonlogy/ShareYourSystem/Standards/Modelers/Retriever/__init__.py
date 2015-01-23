# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Retriever instances can retrieve FlushedVariablesList given their 
IndexInt of their corresponding table and their RowInt 
(ie their index of their flushed line).

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Modelers.Flusher"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class RetrieverClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'RetrievingIndexesList',
									'RetrievedColumnStrToGetStrOrderedDict',
									'RetrievedModelInt',			
									'RetrievedTable', 			
									'RetrievedPickOrderedDict'
								]

	def default_init(self,
						_RetrievingIndexesList=None,
						_RetrievedColumnStrToGetStrOrderedDict=None,
						_RetrievedModelInt=-1,			
						_RetrievedTable=None, 			
						_RetrievedPickOrderedDict=None,		
						**_KwargVariablesDict
			):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def setDatabasingSealTuplesList(self,_SettingValueVariable):

		#debug
		'''
		self.debug('Before we call the parent setDatabasingSealTuplesList method ')
		'''

		#Hook
		BaseClass.setDatabasingSealTuplesList(self,_SettingValueVariable)

		#Bind with RetrievedColumnStrToGetStrOrderedDict setting
		if self.RetrievedColumnStrToGetStrOrderedDict==None:
			self.RetrievedColumnStrToGetStrOrderedDict=collections.OrderedDict()
		map(
			lambda __DatabasingColumnTuple:
			self.RetrievedColumnStrToGetStrOrderedDict.__setitem__(
				__DatabasingColumnTuple[1],
				__DatabasingColumnTuple[0]
			),
			self.DatabasingSealTuplesList
		)

		#Init
		if self.RetrievedPickOrderedDict==None:
			self.RetrievedPickOrderedDict=collections.OrderedDict()

		#debug
		'''
		self.debug(('self.',self,['RetrievedColumnStrToGetStrOrderedDict']))
		'''
		
	DatabasingSealTuplesList=property(
									BaseClass.DatabasingSealTuplesList.fget,
									setDatabasingSealTuplesList,
									BaseClass.DatabasingSealTuplesList.fdel,
									BaseClass.DatabasingSealTuplesList.__doc__
								)
	
	def do_retrieve(self):

		#debug
		'''
		self.debug(
					[
						('self.',self,[
										'TabularedKeyStrsList',
										'RetrievingIndexesList'
									])
					]
				)
		'''

		#<NotHook>
		#table first
		self.table()
		#</NotHook>

		#debug
		'''
		self.debug(
					[
						('Ok table is done'),
						('self.',self,['TabularedOrderedDict','TabularedKeyStrsList'])
					]
				)
		'''

		#set the RetrievedModelInt
		self.RetrievedModelInt=self.RetrievingIndexesList[1]

		#Definition the RetrievedTable
		self.RetrievedTable=self.TabularedOrderedDict[
			self.TabularedKeyStrsList[
				self.RetrievingIndexesList[0]
			]
		]

		#debug
		'''
		self.debug(('self.',self,['RetrievedModelInt','RetrievedTable']))
		'''

		#Definition the RetrievedRowsList
		for __RetrievedRow in self.RetrievedTable.iterrows():
			if __RetrievedRow['RowInt']==self.RetrievedModelInt:

				#debug
				'''
				self.debug('self.RetrievedTable.colnames is '+str(self.RetrievedTable.colnames))
				'''

				#Init
				if self.RetrievedPickOrderedDict==None:
					self.RetrievedPickOrderedDict=collections.OrderedDict()

				#set
				map(
					lambda __ColumnStr:
					self.RetrievedPickOrderedDict.__setitem__(
						self.RetrievedColumnStrToGetStrOrderedDict[__ColumnStr],
						__RetrievedRow[__ColumnStr]
						) if __ColumnStr in self.RetrievedColumnStrToGetStrOrderedDict else None
					,
					self.RetrievedTable.colnames
				)

				#debug
				'''
				self.debug('RetrievedPickOrderedDict is setted')
				'''

		#debug
		'''
		self.debug(
					[
						('self.',self,['RetrievedPickOrderedDict'])
					]
				)
		'''

		#Update
		self.NodePointDeriveNoder.update(
			self.RetrievedPickOrderedDict.items(),
			#**{'RestrictingIsBool':True}
		)
		self.NodePointDeriveNoder.RestrictingIsBool=False


#</DefineClass>
