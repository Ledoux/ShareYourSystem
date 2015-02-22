# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


An Pymongoer 

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Killer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import os
#</ImportSpecificModules>

#<DefineFunctions>
def getRepresentedCollectionItemTuple(_CollectionItemTuple):

	#Debug
	'''
	print('_CollectionItemTuple[0] is ')
	print(_CollectionItemTuple[0])
	print('')
	'''

	#filter
	RepresentedCollectionList=filter(
		lambda __PymongoviewDict:
		len(__PymongoviewDict)>0,
		SYS.filterNone(
				map(
					lambda __NoderItemTuple:
					__NoderItemTuple[1].pymongoview()
					if hasattr(
							__NoderItemTuple[1],
							'pymongoview'
						) 
					else None,
					_CollectionItemTuple[1].items()
				)
			)
	)


	#Debug
	'''
	print('RepresentedCollectionList is ')
	print(RepresentedCollectionList)
	print('')
	'''

	#Check
	if len(RepresentedCollectionList)>0:
		return (
			_CollectionItemTuple[0],
			RepresentedCollectionList
		)
	else:
		return None

def getRepresentedDatabaseOrderedDict(_Database):

	#map
	RepresentedDatabaseDict=collections.OrderedDict(
		SYS.filterNone
		(
			map(
				lambda __CollectionStr:
				(
					__CollectionStr,
					list(_Database[__CollectionStr].find())
				)
				if __CollectionStr not in ['system.indexes']
				else None,
				_Database.collection_names()
			)
		)
	)

	#Debug
	'''
	print('_Database is ')
	print(_Database)
	print('id(_Database) is')
	print(id(_Database))
	print("'ParentDerivePymongoer' in _Database.__dict__")
	print('ParentDerivePymongoer' in _Database.__dict__)
	print('')
	'''
	
	#Get the childs database dicts
	if 'ParentDerivePymongoer' in _Database.__dict__:

		#Debug
		print('_Database.ParentDerivePymongoer is '+SYS._str(_Database.__dict__[
			'ParentDerivePymongoer']))
		print('')

		#update
		RepresentedDatabaseDict.update(
			collections.OrderedDict(
				filter(
					lambda __ItemTuple:
					len(__ItemTuple[1])>0,
					SYS.filterNone(	
						map(
							lambda __CollectionItemTuple:
							getRepresentedCollectionItemTuple(__CollectionItemTuple),
							_Database.__dict__[
								'ParentDerivePymongoer'
							].CollectionsOrderedDict.items()
						)
					)
				)
			)
		)

	#return 
	return {_Database._Database__name:RepresentedDatabaseDict}


#</DefineFunctions>

#<DefineClass>
@DecorationClass(**{
	'ClassingSwitchMethodStrsList':['pymongo']
})
class PymongoerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
			'PymongoingUrlStr',
			'PymongoingKillBool',
			'PymongoneFolderPathStr',
			'PymongonePopenVariable',
			'PymongoneClientVariable',
			'PymongoneDatabaseVariable'
		]

	def default_init(self,		
			_PymongoingUrlStr='mongodb://localhost:27017/',
			_PymongoingKillBool=True,
			_PymongoneFolderPathStr="",
			_PymongonePopenVariable=None,
			_PymongoneClientVariable=None,
			_PymongoneDatabaseVariable=None,
			**_KwargVariablesDict
		):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#set
		self.StatusingProcessStr="mongod"

	def do_pymongo(self):

		#debug
		'''
		self.debug(('self.',self,[
							'PymongoingUrlStr'
								]))
		'''

		#folder
		self.folder()

		#kill all a possible old mongod process
		if self.PymongoingKillBool:
			self.kill()

		#connect
		try:

			#import
			from pymongo import MongoClient

			#init
			self.PymongoneClientVariable=MongoClient(self.PymongoingUrlStr)
			
		except:

			#debug
			'''
			self.debug('No connection maybe to pymongo')
			'''

			#set
			self.PymongoneFolderPathStr=self.FolderingPathStr+'data/db/'

			#Check
			if os.path.isdir(self.PymongoneFolderPathStr)==False:
				os.popen('mkdir '+self.FolderingPathStr+'data')
				os.popen('mkdir '+self.FolderingPathStr+'data/db')

			#popen
			import subprocess
			self.PymongonePopenVariable = subprocess.Popen(
					[
						'/usr/local/bin/mongod',
						'--dbpath',
						self.PymongoneFolderPathStr
					], 
					shell=False,
                   	stdout=subprocess.PIPE,
                   	stdin=subprocess.PIPE
            )

			#debug
			'''
			self.debug(
				('self.',self,['PymongonePopenVariable'])
			)
			'''

			#wait for connect
			import time
			PymongoneConnectBool=False
			PymongoneCountInt=0
			while PymongoneConnectBool==False and PymongoneCountInt<20:
				try:

					#connect
					self.PymongoneClientVariable=MongoClient(self.PymongoingUrlStr)

					#Check
					if self.PymongoneClientVariable!=None:
						PymongoneConnectBool=True

				except:

					#say that it is not setted
					PymongoneConnectBool=False
					PymongoneCountInt+=1
					time.sleep(0.2)


			#debug
			'''
			self.debug(
				[
					'after connection',
					('self.',self,['PymongoneClientVariable'])
				]
			)
			'''

	def getDatabaseKeyStr(self):

		#get
		_DatabaseKeyStr=(
				self.ParentedNodePathStr+'/'+self.NodeKeyStr
			).replace('/','_')

		#remove
		if _DatabaseKeyStr[0]=='_':
			_DatabaseKeyStr=_DatabaseKeyStr[1:]

		#return 
		return _DatabaseKeyStr

	def pymongoview(self,_DatabaseKeyStr=""):

		#debug
		'''
		self.debug(
			[
				('self.',self,[
								'PymongoneClientVariable',
								'PymongoingDatabaseKeyStr'
							]),
				'self.PymongoneClientVariable.database_names is \n',
				self.PymongoneClientVariable.database_names()
			]
		)
		'''

		#debug
		'''
		self.debug('_DatabaseKeyStr is '+_DatabaseKeyStr)
		'''

		#init
		Database=None

		#Check
		if _DatabaseKeyStr!='':

			#_DatabaseKeyStr=self.getDatabaseKeyStr()
			Database=self.PymongoneClientVariable[
							_DatabaseKeyStr
						]
		else:

			#Check
			if hasattr(self,'Database'):
				#get the local one
				Database=self.Database

		#Check
		if Database!=None:

			#debug
			'''
			self.debug(
				[
					'_DatabaseKeyStr is '+_DatabaseKeyStr,
					"_DatabaseKeyStr in self.PymongoneClientVariable.database_names()",
					_DatabaseKeyStr in self.PymongoneClientVariable.database_names(),
					'self.PymongoneClientVariable.__dict__.keys() is ',
					str(self.PymongoneClientVariable.__dict__.keys())
				]
			)
			'''

			#return
			return getRepresentedDatabaseOrderedDict(
							Database
						)

		else:

			#return empty
			return {}
		
	def mimic_close(self):

		#kill the process
		if self.PymongonePopenVariable!=None:

			#debug
			'''
			self.debug('kill the mongod popen variable')
			'''
			
			#kill but before wait a bit to be sure that the db has time to refresh
			import time
			time.sleep(5)
			self.PymongonePopenVariable.kill()

#</DefineClass>

