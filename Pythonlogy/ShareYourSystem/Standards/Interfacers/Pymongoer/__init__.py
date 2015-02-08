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
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Hdformater"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from pymongo import MongoClient
import os
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass(**{
	'ClassingSwitchMethodStrsList':['pymongo']
})
class PymongoerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
			'PymongoingUrlStr',
			'PymongoingDatabaseKeyStr',
			'PymongoneFolderPathStr',
			'PymongonePopenVariable',
			'PymongoneClientVariable',
			'PymongoneDatabaseVariable'
		]

	def default_init(self,		
			_PymongoingUrlStr='mongodb://localhost:27017/',
			_PymongoingDatabaseKeyStr='Default',
			_PymongoneFolderPathStr="",
			_PymongonePopenVariable=None,
			_PymongoneClientVariable=None,
			_PymongoneDatabaseVariable=None,
			**_KwargVariablesDict
		):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_pymongo(self):

		#debug
		self.debug(('self.',self,[
							'PymongoingUrlStr'
								]))
		

		#folder
		self.folder()

		#connect
		try:

			#init
			self.PymongoneClientVariable=MongoClient(self.PymongoingUrlStr)
		except:

			#debug
			self.debug('No connection maybe to pymongo')

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
			self.debug(
				('self.',self,['PymongonePopenVariable'])
			)

			#wait for connect
			import time
			PymongoneConnectBool=False
			while PymongoneConnectBool==False:
				try:
					self.PymongoneClientVariable=MongoClient(self.PymongoingUrlStr)
					if self.PymongoneClientVariable!=None:
						PymongoneConnectBool=True
				except:
					PymongoneConnectBool=False
					time.sleep(0.2)

			#debug
			self.debug(
				[
					'after connection',
					('self.',self,['PymongoneClientVariable'])
				]
			)

		#get
		self.PymongoneDatabaseVariable=getattr(
				self.PymongoneClientVariable,
				self.PymongoingDatabaseKeyStr
			) 

		#give a parent pointer
		self.PymongoneDatabaseVariable.ParentDerivePymongoer=self

		#

	def pymongoview(self):

		#debug
		'''
		self.debug(
			[
				('self.',self,['PymongoneDatabaseVariable']),
				'self.PymongoneDatabaseVariable.collection_names is \n',
				self.PymongoneDatabaseVariable.collection_names()
			]
		)
		'''

		#map
		self.PymongoneViewStr='\n'.join(
			map(
				lambda __CollectionStr:
				'In '+__CollectionStr+' : \n'+SYS._str(
					list(self.PymongoneDatabaseVariable[__CollectionStr].find())
				),
				self.PymongoneDatabaseVariable.collection_names()
			)
		)

		#return self
		return self
		
	def mongoclose(self):

		#kill the process
		if self.PymongonePopenVariable!=None:

			#debug
			self.debug('kill the mongod popen variable')

			#kill
			self.PymongonePopenVariable.kill()

		#return self
		return self

#</DefineClass>

