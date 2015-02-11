# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Cooper defines Child ordered dicts with <DoStr> as KeyStr. 
The items inside are automatically setted with Cooped<DoStr><TypeStr> and have 
a Pointer to the parent InstanceVariable. This is the beginning for buiding high
arborescent and (possibly circular) structures of objects.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Filterer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
from ShareYourSystem.Standards.Itemizers import Pather
#</ImportSpecificModules>

#<DefineLocals>
class CoopClass(collections.OrderedDict):

	def __init__(self,_Dict=None):

		#Check
		if _Dict==None:
			_Dict={}

		#call the parent init method
		collections.OrderedDict.__init__(self,_Dict)

		#define 
		self.update(
			{
				'NameStr':""
			}
		)

		#update
		self.update(_Dict)

	#def __setitem__(self,_KeyVariable,_ValueVariable):
	#	if _KeyVariable


SYS.CoopClass=CoopClass
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class CooperClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'CoopingNameStr',
								'CoopedCoop'
							]

	def default_init(self,
				_CoopingNameStr="",							
				_CoopedCoop=None, 																		
				**_KwargVariablesDict
			):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#init
		self.CoopsOrderedDict=collections.OrderedDict()

	def do_coop(self):

		#debug
		'''
		self.debug(("self.",self,['CoopingNameStr']))
		'''

		#Get the CoopedStr
		if self.CoopingNameStr!="":
		
			#set the Cooped OrderedDict and KeyStr
			CoopedCoopKeyStr=self.CoopingNameStr+'Coop'

			#try to set or get
			try:

				#get
				self.CoopedCoop=getattr(self,CoopedCoopKeyStr)
			
			except AttributeError:

				#set
				self.__setattr__(
									CoopedCoopKeyStr,
									CoopClass()
								)

				#get
				self.CoopedCoop=getattr(self,CoopedCoopKeyStr)

				#set an alias with the namestr
				self.__setattr__(self.CoopingNameStr,self.CoopedCoop)

				#set
				self.CoopsOrderedDict[CoopedCoopKeyStr]=self.CoopedCoop

			

#</DefineClass>

