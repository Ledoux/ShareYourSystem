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
			'PymongoneFolderPathStr',
			'PymongonePopenVariabe',
			'PymongoneClientVariable'
		]

	def default_init(self,		
			_PymongoingUrlStr='mongodb://localhost:27017/',
			_PymongoneFolderPathStr="",
			_PymongonePopenVariabe=None,
			_PymongoneClientVariable=None,
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

			#wait
			import time
			time.sleep(0.2)

			#init
			self.PymongoneClientVariable=MongoClient(self.PymongoingUrlStr)

#</DefineClass>

