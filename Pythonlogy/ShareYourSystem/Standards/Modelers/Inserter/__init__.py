# -*- coding: utf-8 -*-
"""

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Inserter instances can insert a RowedVariablesList into a table
checking maybe before if this line is new in the table or not
depending on identifying items.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
import collections
BaseModuleStr="ShareYourSystem.Standards.Modelers.Rower"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class InserterClass(
					BaseClass,
				):
	
	#Definition
	RepresentingKeyStrsList=[										
								'InsertedNotRowGetStrsList',
								'InsertedNotRowColumnStrsList',
								'InsertedMongoNotRowPickOrderedDict',
								'InsertedHdfNotRowPickOrderedDict',
								'InsertedIndexInt'
							]

	def default_init(self,
					_InsertedNotRowGetStrsList=None,
					_InsertedNotRowColumnStrsList=None,
					_InsertedMongoNotRowPickOrderedDict=None,
					_InsertedHdfNotRowPickOrderedDict=None,
					_InsertedIndexInt=-1,		
					**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)
			
	def setRowingGetStrsList(self,_SettingValueVariable):
		
		#Hook
		BaseClass.setRowingGetStrsList(self,_SettingValueVariable)

		#Bind 
		self.InsertedNotRowGetStrsList=list(
				set(
					SYS.unzip(
					self.DatabasingSealTuplesList,[0]
				)
			)-set(
				self.RowingGetStrsList
			)
		)

		#set
		if self.DatabasingHdfBool:
			self.InsertedNotRowColumnStrsList=map(
				lambda __NotRowGetStr:
				self.RowedGetStrToColumnStrOrderedDict[__NotRowGetStr],
				self.InsertedNotRowGetStrsList
			)

	RowingGetStrsList=property(
		BaseClass.RowingGetStrsList.fget,
		setRowingGetStrsList,
		BaseClass.RowingGetStrsList.fdel,
		BaseClass.RowingGetStrsList.__doc__
	)

	def do_insert(self):
		""" """

		#debug
		'''
		self.debug('row maybe before...')
		'''

		#row first
		self.row()

		#debug
		'''
		self.debug(
					('self.',self,['RowedIsBool'])
				)
		self.NodePointDeriveNoder.debug([
				('NOTE : ...ParentSpeaking...')
			])
		'''

		"""
		map(
				lambda __InitVariable:
				setattr(
					self,
					__KeyStr,
					SYS.getInitiatedVariableWithKeyStr(__KeyStr)	
				) if __InitVariable==None else None,
				map(
						lambda __KeyStr:
						(
							__KeyStr,
							getattr(self,__KeyStr)
						),
						[
							'InsertedNotRowPickOrderedDict',
							'InsertedNotRowGetStrsList',
							'InsertedNotRowGetStrsList',
							'InsertedNotRowPickOrderedDict'
						]
					)
			)
		"""

		#debug
		'''
		self.debug(('self.',self,['InsertedNotRowPickOrderedDict']))
		'''
		
		#Check
		if self.DatabasingMongoBool:

			#Append and row if it is new
			if self.RowedMongoIsBool==False:

				#Check
				if self.TabledMongoCollection!=None:

					#debug
					self.debug(
						[
							'This is a new collection row',
							('self.',self,[
										'RowingGetStrsList',
										'InsertedNotRowGetStrsList'
									])
						]
					)

					#debug
					self.debug(
						[
							'Before update',
							('self.',self,['InsertedMongoNotRowPickOrderedDict'])
						]
					)

					#Pick and update				
					self.InsertedMongoNotRowPickOrderedDict.update(
					zip(
						self.InsertedNotRowGetStrsList,
						self.ModeledPointDeriveControllerVariable.pick(
							self.InsertedNotRowGetStrsList
							)
						)
					)

					#debug
					self.debug(
						[
							'After update',
							('self.',self,['InsertedMongoNotRowPickOrderedDict'])
						]
					)

					#Definition the InsertedItemTuplesList
					InsertedItemTuplesList=[
											('RowInt',self.RowedMongoIndexInt)
										]+self.RowedMongoPickOrderedDict.items(
					)+self.InsertedMongoNotRowPickOrderedDict.items()

					#insert
					self.TabledMongoCollection.insert(
						dict(InsertedItemTuplesList)
					)

		#Check
		if self.DatabasingHdfBool:

			#Append and row if it is new
			if self.RowedHdfIsBool==False:

				#Check
				if self.TabledHdfTable!=None:

					#debug
					'''
					self.debug('This is a new hdf row')
					'''

					#Get the row
					Row=None
					Row=self.TabledHdfTable.row

					#debug
					'''
					self.debug(('self.',self,['InsertedNotRowPickOrderedDict']))
					'''
					
					#Pick and update				
					self.InsertedHdfNotRowPickOrderedDict.update(
					zip(
						self.InsertedNotRowGetStrsList,
						self.ModeledPointDeriveControllerVariable.pick(
							self.InsertedNotRowGetStrsList
							)
						)
					)

					#debug
					'''
					self.debug(('self.',self,[
												'RowedPickOrderedDict',
												'InsertedNotRowPickOrderedDict'
											]))
					'''

					#Definition the InsertedItemTuplesList
					InsertedItemTuplesList=[
											('RowInt',self.RowedHdfIndexInt)
										]+self.RowedHdfPickOrderedDict.items(
					)+self.InsertedHdfNotRowPickOrderedDict.items()
						
					#import tables
					#print(tables.tableextension.Row)

					#debug
					'''
					self.debug(
						[
							'This is a new row',
							'Colnames are : '+str(self.TabledHdfTable.colnames),
							'InsertedItemTuplesList is '+str(InsertedItemTuplesList),
							'self.TabledHdfTable is '+str(dir(self.TabledHdfTable)),
							'self.DatabasedModelClass is '+(str(self.DatabasedModelClass.columns) if hasattr(self.DatabasedModelClass,'columns') else ""),
							'Row is '+str(dir(Row)),
							'Row.table is '+str(Row.table),
							'TabularedHdfTablesOrderedDict is '+str(self.TabularedHdfTablesOrderedDict)
						]
					)
					'''

					#set
					map(
							lambda __InsertingTuple:
							Row.__setitem__(*__InsertingTuple),
							InsertedItemTuplesList
						)

					#debug
					'''
					self.debug('The Row setting was good, so append insert')
					'''

					#Append and Flush
					Row.append()
					self.TabledHdfTable.flush()
					
			else:

				#debug
				'''
				self.debug(
							[
								'This is maybe not an IdentifyingInserter',
								'Or it is already rowed',
								'self.InsertedIsBoolsList is '+str(self.InsertedIsBoolsList)
							]
						)
				'''
				pass
				
		

#</DefineClass>
