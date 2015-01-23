# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Mimicker...

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Classors.Switcher"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Classors import Doer
import six
#</ImportSpecificModules>

#<DefineLocals>
MimickingPrefixStr="mimic_"
MimickingDecoratioStr="_MiM_"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class MimickerClass(BaseClass):
	
	#Definition 
	RepresentingKeyStrsList=[
					'MimickingDoMethodStr',
					'MimickedMethodStr'
	]

	def default_init(self,	
					_MimickingDoMethodStr="",
					_MimickedMethodStr="",	   			
					**_KwargVariablesDict
				):

		#Call the init parent method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Class):

		#Call the parent init method
		BaseClass.__call__(self,_Class)

		#mimic
		self.mimic()

		#Return
		return _Class

	def do_mimic(self):
				
		#set
		self.MimickedMethodStr=MimickingPrefixStr+self.MimickingDoMethodStr

		#Debug
		'''
		print('l 75 Mimicker ')
		print('self.MimickedMethodStr is ',self.MimickedMethodStr)
		print('')
		'''

		#Define
		MimickedDoStr=self.MimickingDoMethodStr[0].upper()+self.MimickingDoMethodStr[1:]
		MimickedDoerStr=Doer.DoStrToDoerStrOrderedDict[MimickedDoStr]

		#Debug
		'''
		print('l 84 Mimicker ')
		print('MimickedDoStr is ',MimickedDoStr)
		print('MimickedDoerStr is ',MimickedDoerStr)
		print('')
		'''

		#Definitions
		MimickedModule=getattr(SYS,MimickedDoerStr)
		MimickedClass=getattr(MimickedModule,SYS.getClassStrWithNameStr(MimickedDoerStr))
		MimickedDoneExecStr=getattr(
			MimickedClass,
			MimickedClass.NameStr+'DoneExecStr'
		).replace('def DoerFunction','def MimickerFunction')

		#Debug
		'''
		print('l 99 Mimicker')
		print('MimickedDoneExecStr is ')
		print(MimickedDoneExecStr)
		print('')
		'''

		#Define
		def MimickedNewFunction(_InstanceVariable,*_LiargVariablesList,**_KwargVariablesDict):
			
			#Set
			MimicMethodStr=_KwargVariablesDict['MimicMethodStr']
			del _KwargVariablesDict['MimicMethodStr']
			MimicDoStr=MimickingPrefixStr.join(MimicMethodStr.split(MimickingPrefixStr)[1:])
			MimicDoStr=MimicDoStr[0].upper()+MimicDoStr[1:] if MimicDoStr[0]!='_' else MimicDoStr[1].upper()+MimicDoStr[2:]
			MimicNameStr=Doer.DoStrToDoerStrOrderedDict[MimicDoStr]
			MimicClass=getattr(SYS,SYS.getClassStrWithNameStr(MimicNameStr))
			DoClassStr=_KwargVariablesDict['DoClassStr']
			del _KwargVariablesDict['DoClassStr']
			DoClass=getattr(SYS,DoClassStr)

			#Debug
			'''
			print('Mimicker l.119 inside of the function MimickedNewFunction')
			#print('_InstanceVariable is ',_InstanceVariable)
			print('_LiargVariablesList is ',_LiargVariablesList)
			print('_KwargVariablesDict is ',_KwargVariablesDict)
			print('MimicMethodStr is ',MimicMethodStr)
			print('')
			'''

			if len(_KwargVariablesDict)>0:

				#group by
				[
					MimicItemTuplesList,
					MimicNotItemTuplesList
				]=SYS.groupby(
					lambda __ItemTuple:
					hasattr(_InstanceVariable,__ItemTuple[0]),
					_KwargVariablesDict.items()
				)

				#Debug
				'''
				print('MimicItemTuplesList is ',MimicItemTuplesList)
				print('MimicNotItemTuplesList is ',MimicNotItemTuplesList)
				print('')
				'''

				#set in the instance the corresponding kwarged arguments
				map(	
						lambda __ItemTuple:
						#set direct explicit attributes
						_InstanceVariable.__setattr__(*__ItemTuple),
						MimicItemTuplesList
					)

				#Define
				MimicKwargDict=dict(MimicNotItemTuplesList)

			else:

				#Define
				MimicKwargDict={}

			#Init
			MimicOutputVariable=None

			#Debug
			'''
			print('Mimicker l.167 inside of the function MimickedNewFunction')
			print('DoClass is ',DoClass)
			print('MimicMethodStr is ',MimicMethodStr)
			print('')
			'''

			#Get the method
			MimicUnBoundMethod=getattr(
				DoClass,
				MimicMethodStr
			)

			#Debug
			'''
			print('Mimicker l.181 inside of the function MimickedNewFunction')
			print('MimicUnBoundMethod is ',MimicUnBoundMethod)
			print('MimicKwargDict is ',MimicKwargDict)
			print('')
			'''
			
			#call the Mimicked function
			if len(MimicKwargDict)>0:
				MimicOutputVariable=MimicUnBoundMethod(
									_InstanceVariable,
									*_LiargVariablesList,
									**MimicKwargDict
								)
			else:
				MimicOutputVariable=MimicUnBoundMethod(
						_InstanceVariable,
						*_LiargVariablesList
					)

			#Debug
			'''
			print('Mimicker l.178 inside of the function MimickedNewFunction')
			print('MimicClass is ',MimicClass)
			print('MimicClass.DoingGetBool is ',MimicClass.DoingGetBool)
			print('MimicOutputVariable is ',MimicOutputVariable)
			print('')
			'''

			#Check
			if MimicClass.DoingGetBool==False:

				#Return 
				return _InstanceVariable
			
			else:

				#Return the 
				return MimicOutputVariable

		#Rename
		MimickedNewFunction.__name__='mimic'+MimickedDoStr+'With'+self.DoClass.NameStr

		#Debug
		'''
		print('l.225 Mimicker')
		print('MimickedNewFunction is ',MimickedNewFunction)
		print('MimickedNewFunction.__name__ is ',MimickedNewFunction.__name__)
		print('')
		'''

		#Set in the class
		setattr(
				self.DoClass,
				MimickedNewFunction.__name__,
				MimickedNewFunction
			)

		#Add to the ImitatedDoneExecStr
		MimickedDoneExecStr+='\n\treturn _InstanceVariable.'+MimickedNewFunction.__name__+'(*_LiargVariablesList,**dict({\'MimicMethodStr\':\''+self.MimickedMethodStr+'\',\'DoClassStr\':\''+self.DoClass.__name__+'\'},**_KwargVariablesDict))'

		#Debug
		'''
		print('MimickedDoneExecStr is ')
		print(MimickedDoneExecStr)
		print('')
		'''
		
		#exec
		six.exec_(MimickedDoneExecStr)

		#set the name
		locals()[
			'MimickerFunction'
		].__name__=self.__class__.NameStr+Doer.DoingDecorationStr+MimickingDecoratioStr+self.MimickingDoMethodStr

		#set in the __class__
		setattr(
					self.DoClass,
					self.MimickingDoMethodStr,
					locals()['MimickerFunction']
				)
	
		#Return self
		#return self

#</DefineClass>

