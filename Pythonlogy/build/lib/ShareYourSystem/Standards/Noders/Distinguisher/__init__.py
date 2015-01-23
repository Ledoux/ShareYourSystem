# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Distinguisher is a bit the opposite of a Commander, it updates
for every child nodes with a distinguished tuples list.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Noders.Noder"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Noders import Noder
#</ImportSpecificModules>

#<DefineLocals>
DistinguishingPrefixStr="Dis_"
#</DefineLocals

#<DefineClass>
@DecorationClass()
class DistinguisherClass(BaseClass):

	#Definition 
	RepresentingKeyStrsList=[
								'DistinguishingNodeStr',
								'DistinguishingUpdatesList',
								'DistinguishedCollectionOrderedDict'
							]

	def default_init(self,
				_DistinguishingNodeStr="",
				_DistinguishingUpdatesList=None,	
				_DistinguishedCollectionOrderedDict=None,						
				**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def mimic_set(self):
		""" """

		#debug
		'''
		self.debug(('self.',self,['SettingKeyVariable','SettingValueVariable']))
		'''

		#Definition
		OutputDict={'HookingIsBool':True}

		#Deep set
		if self.SettingKeyVariable.startswith(DistinguishingPrefixStr):

			#debug
			'''
			self.debug('We are going to distinguish')
			'''

			
			#set arguments
			self.DistinguishingNodeStr=Noder.NodingSuffixGetStr.join(
					(
						Noder.NodingPrefixGetStr.join(
							self.SettingKeyVariable.split(
								Noder.NodingPrefixGetStr
							)[1:]
						)
					).split(Noder.NodingSuffixGetStr)[:-1]
				)

			self.DistinguishingUpdatesList=self.SettingValueVariable

			#debug
			'''
			self.debug(('self.',self,[
					'DistinguishingNodeStr',
					'DistinguishingUpdatesList'
					]))
			'''
			
			#distinguish
			self.distinguish()

			#Stop the setting
			OutputDict["HookingIsBool"]=False
			#<Hook>return OutputDict

		#Call the parent get method
		if OutputDict['HookingIsBool']:
			BaseClass.set(self)

	def do_distinguish(self):
		""" """

		#Check
		if self.DistinguishingNodeStr!="":

			#debug
			'''
			self.debug(('self.',self,['DistinguishingNodeStr']))
			'''

			#get
			self.DistinguishedCollectionOrderedDict=getattr(
				self,
				self.DistinguishingNodeStr+'CollectionOrderedDict'
			)

			#Map the distinguished updates
			map(
				lambda __NodeVariable,__UpdateTuplesList:
				__NodeVariable.update(__UpdateTuplesList),
				self.DistinguishedCollectionOrderedDict.values(),
				self.DistinguishingUpdatesList
			)

#</DefineClass>
