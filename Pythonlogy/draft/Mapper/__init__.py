# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Mapper

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Classors.Mimicker"
DecorationModuleStr=BaseModuleStr
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import sys
#</ImportSpecificModules>

#<DefineLocals>
class MapListClass(list):
	pass

def map(_InstanceVariable,*_LiargVariablesList,**_KwargVariablesDict):

	#Set
	MapMethodStr=_KwargVariablesDict['MapMethodStr']
	MapClassStr=_KwargVariablesDict['MapClassStr']
	MapClass=getattr(SYS,MapClassStr)
	MapUnBoundMethod=getattr(
		MapClass,
		MapMethodStr
	)
	BaseClassStr=_KwargVariablesDict['BaseClassStr']
	BaseClass=getattr(SYS,BaseClassStr)
	del _KwargVariablesDict['MapMethodStr']
	del _KwargVariablesDict['MapClassStr']
	del _KwargVariablesDict['BaseClassStr']

	#Check
	if len(_LiargVariablesList)>0:

		#define
		MapList=_LiargVariablesList[0]

		if type(MapList)==MapListClass:
			
			"""
			#map
			map(
					lambda __ListedVariable:
					MapUnBoundMethod(
						_InstanceVariable,	
					)
					MapList
				)
			"""

#</DefineLocals>

#<DefineClass>
@DecorationClass()
class MapperClass(BaseClass):

	def default_init(self,
						_MappingDoMethodStr="",
						_MappedWrapMethodStr="",
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Class):

		#debug
		'''
		print('Mapper l.30 __call__ method')
		print('_Class is ',_Class)
		print('')
		'''

		#Call the parent __call__ method
		BaseClass.__call__(self,_Class)

		#Debug
		'''
		print('Mapper l.54 We are going to map')
		print('self.map is ',self.map)
		print('')
		'''

		#map
		self.map()

		#Debug
		'''
		print('map is done')
		print('')
		'''

		#Return 
		return _Class

	def do_map(self):

		#Debug
		'''
		print('l 174 Mapper')
		print('self.MappingDoMethodStr is ',self.MappingDoMethodStr)
		print('')
		'''

		#Check
		if self.MappingDoMethodStr!="":

			#observe
			self.observe(True,self.MappingDoMethodStr)

			#set
			self.MappedWrapMethodStr=MappingWrapPrefixStr+self.MappingDoMethodStr

			#Debug
			'''
			print('l 75 Mapper ')
			print('self.MappedWrapMethodStr is ',self.MappedWrapMethodStr)
			print('')
			'''

			#Define
			MappedDoStr=self.MappingDoMethodStr[0].upper()+self.MappingDoMethodStr[1:]
			MappedDoerStr=Doer.DoStrToDoerStrOrderedDict[MappedDoStr]

			#Debug
			'''
			print('l 84 Mapper ')
			print('MappedDoStr is ',MappedDoStr)
			print('MappedDoerStr is ',MappedDoerStr)
			print('MappedBaseModule is ',MappedBaseModule)
			print('')
			'''

			#Definitions
			MappedBaseClass=getattr(
				SYS,
				SYS.getClassStrWithNameStr(MappedDoerStr)
			)

			#get
			MappedDoExecStr=getattr(
				MappedBaseClass,
				'Do'+MappedBaseClass.NameStr+'ExecStr'
			)

			#debug
			'''
			print('l 206 Mapper')
			print('MappedDoExecStr is ')
			print(MappedDoExecStr)
			print('')
			'''

			#replace
			MappedDecorationMethodStr=MappingDecorationPrefixStr+MappingDecorationTagStr+MappingDecorationSuffixStr
			MappedDecorationMethodStr+=self.ObservedWrapMethodStr

			#Debug
			'''
			print('l 232 Mapper')
			print('MappedDecorationMethodStr is '+MappedDecorationMethodStr)
			print('')
			'''
			
			#replace
			MappedExecStr='def '+MappedDecorationMethodStr+'('+'('.join(
				MappedDoExecStr.split('(')[1:]
			)

			#Debug
			'''
			print('l 208 Mapper')
			print('MappedExecStr is ')
			print(MappedExecStr)
			print('')
			'''
			
			#Add to the ImitatedDoneExecStr
			MappedExecStr+='\n\treturn map(_InstanceVariable,*_LiargVariablesList,'
			MappedExecStr+='**dict({\'MapMethodStr\':\''+self.MappedWrapMethodStr+'\','
			MappedExecStr+='\'MapClassStr\':\''+self.DoClass.__name__+'\','
			MappedExecStr+='\'BaseClassStr\':\''+MappedBaseClass.__name__+'\''
			MappedExecStr+='},**_KwargVariablesDict))'
			
			#Debug
			'''
			print('l 223 Mapper')
			print('MappedExecStr is ')
			print(MappedExecStr)
			print('')
			'''
			
			#exec
			six.exec_(MappedExecStr)

			#set
			self.MappedDecorationUnboundMethod=locals()[MappedDecorationMethodStr]

			#set in the __class__
			setattr(
						self.DoClass,
						MappedDecorationMethodStr,
						self.MappedDecorationUnboundMethod
					)

			#make the amalgam
			setattr(
						self.DoClass,
						self.MappingDoMethodStr,
						self.MappedDecorationUnboundMethod
					)


#</DefineClass>
