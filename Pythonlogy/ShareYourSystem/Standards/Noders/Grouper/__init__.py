# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Grouper establishes a group of parenting nodes for which 
each level is setted in equivalent hdf5 structure.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Noders.Transmitter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import functools
from ShareYourSystem.Standards.Classors import Doer
#</ImportSpecificModules>

#<DefineFunctions>
def getGroupedPathStrWithPathStrsList(_PathStrsList):

	#Reduce
	PathStr=functools.reduce(
			lambda _TotalPathStr,_PathStr:
			_TotalPathStr+_PathStr 
			if (len(_TotalPathStr)>0 and _TotalPathStr[-1]=='/') and (len(_PathStr)>0 and _PathStr[0]!='/'
				) or (len(_TotalPathStr)>0 and _TotalPathStr[-1]!='/') and (len(_PathStr)>0 and _PathStr[0]=='/')
			else 
			_TotalPathStr[:-1]+_PathStr 
			if (len(_TotalPathStr)>0 and _TotalPathStr[-1]=='/') and (len(_PathStr)>0 and _PathStr[0]=='/'
				)
			else _TotalPathStr+'/'+_PathStr 
			if '/' not in [_PathStr,_TotalPathStr]
			else "",
			_PathStrsList
			)

	#Maybe add / at the beginning
	if (len(PathStr)>0 and PathStr[0]!='/') or PathStr=="":
		PathStr='/'+PathStr

	#Return
	return PathStr
#</DefineFunctions>

#<DefineClass>
@DecorationClass()
class GrouperClass(BaseClass):
		
	#Definition
	RepresentingKeyStrsList=[
									'GroupedParentVariable',
									'GroupedInt',
									'GroupedKeyStr',
									'GroupedDeriveParentersList',
									'GroupedPathStrsList',
									'GroupedPathStr'
								]

	def default_init(
				self,
				_GroupedParentVariable=None,
				_GroupedInt=-1,
				_GroupedKeyStr="",
				_GroupedDeriveParentersList=None,
				_GroupedPathStrsList=None,
				_GroupedPathStr="/",
				**_KwargVariablesDict
			):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#set
		if self.HdformatingFileKeyStr=="":
			self.HdformatingFileKeyStr=SYS.InflectEngine.plural(
				Doer.DoerStrToDoStrOrderedDict[
					self.__class__.NameStr
					]
				)+'.hdf5'

	def do_group(self):

		#debug
		'''
		self.debug(('self.',self,['ParentingNodeStr']))
		'''
	
		#Parent
		self.parent(_PickVariablesList=['HdformatedFileVariable'])
		
		#debug
		#print('self.HdformatedFileVariable is ',self.HdformatedFileVariable)

		#Create a group in the hdf5 file
		if self.HdformatedFileVariable!=None:

			#debug
			'''
			self.debug(
						[
							'UppestGroupedParentVariable.GroupedPathStr is '+UppestGroupedParentVariable.GroupedPathStr,
							('self.',self,[
										'ParentedPathStr',
										'NodedKeyStr'
									])
						]
					)
			'''

			#set the GroupedPathStr
			if self.ParentedTopDeriveParenterVariable==self:
				self.GroupedPathStr="/"
			else:
				self.GroupedPathStr=getGroupedPathStrWithPathStrsList(
					[
						self.ParentedTopDeriveParenterVariable.GroupedPathStr,
						self.ParentedPathStr,
						self.NodeKeyStr
					]
				)

			#debug
			'''
			self.debug(('self.',self,['GroupedPathStr']))
			'''
			
			#Check if the Path exists
			if self.GroupedPathStr not in self.HdformatedFileVariable:

				#set all the intermediate Paths before
				PathStrsList=self.GroupedPathStr.split('/')[1:]
				ParsingChildPathStr="/"

				#set the PathStr from the top to the down (integrativ loop)
				for ChildPathStr in PathStrsList:

					#Go deeper
					NewParsingChildPathStr=ParsingChildPathStr+ChildPathStr

					#Create the group if not already
					if NewParsingChildPathStr not in self.HdformatedFileVariable:
						if self.HdformatingModuleStr=="tables":
							self.HdformatedFileVariable.create_group(ParsingChildPathStr,ChildPathStr)
						elif self.HdformatingModuleStr=="h5py":
							Group=self.HdformatedFileVariable[ParsingChildPathStr]
							Group.create_group(ChildPathStr)
					
					#Prepare the next group	
					ParsingChildPathStr=NewParsingChildPathStr+'/'

#</DefineClass>
