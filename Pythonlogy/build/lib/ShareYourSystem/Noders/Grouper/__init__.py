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
BaseModuleStr="ShareYourSystem.Noders.Transmitter"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import functools

from ShareYourSystem.Classors import Doer
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

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
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
		self.parent()
		
		#Check
		if len(self.ParentedDeriveParentersList)>0:
			UppestParentPointer=self.ParentedDeriveParentersList[-1]
		else:
			UppestParentPointer=self

		#Then get also from the UppestParentPointer its UppestGroupedParentVariable
		if hasattr(UppestParentPointer,'GroupedDeriveParentersList'):
			if len(UppestParentPointer.GroupedDeriveParentersList)>0:
				UppestGroupedParentVariable=UppestParentPointer.GroupedDeriveParentersList.GroupedDeriveParentersList[-1]
			else:
				UppestGroupedParentVariable=UppestParentPointer

		#Link
		self.HdformatedFileVariable=UppestGroupedParentVariable.HdformatedFileVariable

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
			if UppestParentPointer==self:
				self.GroupedPathStr="/"
			else:
				self.GroupedPathStr=getGroupedPathStrWithPathStrsList(
					[
						UppestGroupedParentVariable.GroupedPathStr,
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

		#Return self
		#return self

#</DefineClass>
