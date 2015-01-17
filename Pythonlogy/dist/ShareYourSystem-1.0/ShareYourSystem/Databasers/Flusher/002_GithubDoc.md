
<!--
FrozenIsBool False
-->

##Code

----

<ClassDocStr>

----

```python
# -*- coding: utf-8 -*-
"""

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Flusher instances can flush a RowedVariablesList into a table
checking maybe before if this line is new in the table or not
depending on identifying items.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
import collections
BaseModuleStr="ShareYourSystem.Databasers.Rower"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class FlusherClass(
					BaseClass,
				):
	
	#Definition
	RepresentingKeyStrsList=[										
									'FlushedNotRowGetStrsList',
									'FlushedNotRowColumnStrsList',
									'FlushedNotRowPickOrderedDict',
									'FlushedIndexInt'
								]

	def default_init(self,
					_FlushedNotRowGetStrsList=None,
					_FlushedNotRowColumnStrsList=None,
					_FlushedNotRowPickOrderedDict=None,
					_FlushedIndexInt=-1,		
					**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)
			
	def setRowingGetStrsList(self,_SettingValueVariable):
		
		#Hook
		BaseClass.setRowingGetStrsList(self,_SettingValueVariable)

		#Bind 
		self.FlushedNotRowGetStrsList=list(set(SYS.unzip(
			self.ModelingSealTuplesList,[0]
		))-set(self.RowingGetStrsList))

		#set
		self.FlushedNotRowColumnStrsList=map(
			lambda __NotRowGetStr:
			self.RowedGetStrToColumnStrOrderedDict[__NotRowGetStr],
			self.FlushedNotRowGetStrsList
		)
	RowingGetStrsList=property(
									BaseClass.RowingGetStrsList.fget,
									setRowingGetStrsList,
									BaseClass.RowingGetStrsList.fdel,
									BaseClass.RowingGetStrsList.__doc__
								)

	
	def do_flush(self):
		""" """

		#debug
		'''
		self.debug('row maybe before...')
		'''

		#<NotHook>
		#row first
		self.row()
		#</NotHook>

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
							'FlushedNotRowPickOrderedDict',
							'FlushedNotRowGetStrsList',
							'FlushedNotRowGetStrsList',
							'FlushedNotRowPickOrderedDict'
						]
					)
			)
		"""

		#debug
		'''
		self.debug(('self.',self,['FlushedNotRowPickOrderedDict']))
		'''
		
		#Append and row if it is new
		if self.RowedIsBool==False:

			#Check
			if self.TabledTable!=None:

				#debug
				'''
				self.debug('This is a new row')
				'''

				#Get the row
				Row=None
				Row=self.TabledTable.row

				#debug
				'''
				self.debug(('self.',self,['FlushedNotRowPickOrderedDict']))
				'''
				
				#Pick and update				
				self.FlushedNotRowPickOrderedDict.update(
				zip(
					self.FlushedNotRowColumnStrsList,
					self.NodePointDeriveNoder.pick(
						self.FlushedNotRowGetStrsList
						)
					)
				)

				#debug
				'''
				self.debug(('self.',self,[
											'RowedPickOrderedDict',
											'FlushedNotRowPickOrderedDict'
										]))
				'''

				#Definition the FlushedItemTuplesList
				FlushedItemTuplesList=[
										('ModeledInt',self.RowedIndexInt)
									]+self.RowedPickOrderedDict.items(
									)+self.FlushedNotRowPickOrderedDict.items()
					
				#import tables
				#print(tables.tableextension.Row)

				#debug
				'''
				self.debug(
							[
								'This is a new row',
								'Colnames are : '+str(self.TabledTable.colnames),
								'FlushedItemTuplesList is '+str(FlushedItemTuplesList),
								'self.TabledTable is '+str(dir(self.TabledTable)),
								'self.ModeledClass is '+(str(self.ModeledClass.columns) if hasattr(self.ModeledClass,'columns') else ""),
								'Row is '+str(dir(Row)),
								'Row.table is '+str(Row.table),
								'TabularedOrderedDict is '+str(self.TabularedOrderedDict)
							]
						)
				'''

				#set
				map(
						lambda __FlushingTuple:
						Row.__setitem__(*__FlushingTuple),
						FlushedItemTuplesList
					)

				#debug
				'''
				self.debug('The Row setting was good, so append flush')
				'''

				#Append and Flush
				Row.append()
				self.TabledTable.flush()
				
		else:

			#debug
			'''
			self.debug(
						[
							'This is maybe not an IdentifyingFlusher',
							'Or it is already rowed',
							'self.FlushedIsBoolsList is '+str(self.FlushedIsBoolsList)
						]
					)
			'''
			pass
			
		#<NotHook>
		#Return self
		#return self
		#</NotHook>

#</DefineClass>

```

<small>
View the Flusher sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Databasers/Flusher" target="_blank">Github</a>
</small>

