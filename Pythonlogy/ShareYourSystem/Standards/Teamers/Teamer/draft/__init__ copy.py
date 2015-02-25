#<ImportSpecificModules>
import collections
,Doer,Representer
from ShareYourSystem.Functers import Argumenter
BaseModuleStr="ShareYourSystem.Standards.Objects.Pather"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer")
#</ImportSpecificModules>

#<DefineLocals>
SYS.setSubModule(globals())

Pather=BaseModule
NodingPrefixGetStr='<'
NodingSuffixGetStr='>'
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class NoderClass(BaseClass):

	def default_init(self,**_KwargVariablesDict):

		#<DefineSpecificDo>
		self.NodingCollectionStr=""						#<NotRepresented>	
		self.NodedOrderedDict=None 					#<NotRepresented>
		self.NodedPrefixStr=""					#<NotRepresented>
		self.NodedKeyStrKeyStr="" 			#<NotRepresented>
		#self.NodedDoerStr=""					
		#self.NodedDoStr=""					
		#self.NodedDoneStr=""				
		#self.NodedDoingStr=""				
		self.NodePointDeriveNoder=None 			 	#<NotRepresented>
		self.NodedInt=-1 							#<NotRepresented>
		#self.NodedPathStr="" 					#<NotRepresented>
		#self.NodedGrandParentPointersList=[]		#<NotRepresented>
		#</DefineSpecificDo>

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	@Argumenter.ArgumenterClass()
	def node(self,_KeyStr=None,**_KwargVariablesDict):

		#debug
		self.debug(("self.",self,['NodingCollectionStr']))

		#Get the NodedStr
		if self.NodingCollectionStr!="":
			#self.NodedDoerStr=Doer.getDoerStrWithKeyStr(self.NodingCollectionStr)
			#self.NodedDoStr=Doer.getDoStrWithDoerStr(self.NodedDoerStr)
			#self.NodedDoneStr=Doer.getDoneStrWithDoStr(self.NodedDoStr)
			#self.NodedDoingStr=Doer.getDoingStrWithDoneStr(self.NodedDoneStr)

			#debug
			'''
			self.debug(("self.",self,[
										'NodedDoerStr',
										'NodedDoStr',
										'NodedDoneStr',
										'NodedDoingStr'
									]))
			'''
		

			#set the NodedPrefixStr
			self.NodedPrefixStr='Noded'+self.NodingCollectionStr

			#set the Noded OrderedDict and KeyStr
			NodedOrderedSetTagStr=self.NodedPrefixStr+'OrderedDict'
			self.NodedKeyStrKeyStr=self.NodedPrefixStr+'KeyStr'

			try:
				self.NodedOrderedDict=getattr(self,NodedOrderedSetTagStr)
			except AttributeError:
				self.__setattr__(NodedOrderedSetTagStr,collections.OrderedDict())
				self.NodedOrderedDict=getattr(self,NodedOrderedSetTagStr)

			try:
				self.NodingCollectionStr=getattr(self,self.NodedKeyStrKeyStr)
			except AttributeError:
				self.__setattr__(self.NodedKeyStrKeyStr,"")
				self.NodingCollectionStr=getattr(self,self.NodedKeyStrKeyStr)

			#If this is a set of a tree of nodes then also init the nodifying attributes	
			if 'IsNoderBool' not in _KwargVariablesDict or _KwargVariablesDict['IsNoderBool']:

				NodePointDeriveNoderKeyStr=self.NodedPrefixStr+'ParentPointer'
				NodedIntKeyStr=self.NodedPrefixStr+'Int'
				NodedPathStrKeyStr=self.NodedPrefixStr+'PathStr'
				NodedGrandParentPointersListKeyStr=self.NodedPrefixStr+'GrandParentPointersList'

				try:
					self.NodedInt=getattr(self,NodedIntKeyStr)
				except AttributeError:
					self.__setattr__(NodedIntKeyStr,-1)
					self.NodedInt=getattr(self,NodedIntKeyStr)

				try:
					self.NodePointDeriveNoder=getattr(self,NodePointDeriveNoderKeyStr)
				except AttributeError:
					self.__setattr__(NodePointDeriveNoderKeyStr,None)
					self.NodePointDeriveNoder=getattr(self,NodePointDeriveNoderKeyStr)

				#debug
				'''
				self.debug(
							[
								('vars ',vars(),['NodePointDeriveNoderKeyStr']),
								('self.',self,[NodePointDeriveNoderKeyStr])
							]
						)
				'''

				'''
				try:
					self.NodedPathStr=getattr(self,NodedPathStrKeyStr)
				except AttributeError:
					self.__setattr__(NodedPathStrKeyStr,"/")
					self.NodedPathStr=getattr(self,NodedPathStrKeyStr)
				'''

				'''
				try:
					self.NodedGrandParentPointersList=getattr(self,NodedGrandParentPointersListKeyStr)
				except AttributeError:
					self.__setattr__(NodedGrandParentPointersListKeyStr,[])
					self.NodedGrandParentPointersList=getattr(self,NodedGrandParentPointersListKeyStr)
				'''

	#<Hook>@Hooker.HookerClass(**{'HookingAfterVariablesList':[BaseClass.get]})
	def get(self,**_KwargVariablesDict):

		#debug
		'''
		self.debug(("self.",self,['GettingKeyVariable']))
		'''

		#Definition
		OutputDict={'HookingIsBool':True}

		#Appending set
		if self.GettingKeyVariable.startswith(NodingPrefixGetStr):

			#Definition the SplittedStrsList
			SplittedStrsList=self.GettingKeyVariable.split(NodingSuffixGetStr)

			#Definition the NodingCollectionStr
			NodingCollectionStr=NodingPrefixGetStr.join(
				SplittedStrsList[0].split(NodingPrefixGetStr)[1:])
			
			#debug
			'''
			self.debug(
						[
							'NodingCollectionStr is '+NodingCollectionStr,
							'We are going to node'
						]
					)
			'''

			#Nodify
			self.node(NodingCollectionStr,**{'IsNoderBool':False})

			#Definition the KeyStr
			KeyStr=NodingSuffixGetStr.join(SplittedStrsList[1:])

			#debug
			'''
			self.debug(
							[
								'node is done',
								'KeyStr is '+KeyStr
							]
				)
			'''

			#Get with a digited KeyStr case
			if KeyStr.isdigit():

				#Definition the GettingInt
				GettingInt=(int)(KeyStr)

				#Check if the size is ok
				if GettingInt<len(self.NodedOrderedDict):

					#Get the GettedVariable 
					self.GettedValueVariable=SYS.get(self.NodedOrderedDict,'values',GettingInt)

					#Return
					OutputDict['HookingIsBool']=False
					#<Hook>return OutputDict

			#Get in the ValueVariablesList
			elif KeyStr=="":

				#Get the GettedVariable
				self.GettedValueVariable=self.NodedOrderedDict.values()

				#Return 
				OutputDict['HookingIsBool']=False
				#<Hook>return OutputDict

			elif KeyStr in self.NodedOrderedDict:
				
				#Get the GettedVariable
				self.GettedValueVariable=self.NodedOrderedDict[KeyStr]

				#Return 
				OutputDict['HookingIsBool']=False
				#<Hook>return OutputDict

		#Call the parent get method
		if OutputDict['HookingIsBool']:
			BaseClass.get(self,**_KwargVariablesDict)

		#debug
		'''
		self.debug('End of the method')
		'''

	#<Hook>@Hooker.HookerClass(**{'HookingAfterVariablesList':[BaseClass.set]})
	def set(self,**_KwargVariablesDict):
		""" """

		#debug
		'''
		self.debug('Start of the method')
		'''

		#Definition
		OutputDict={'HookingIsBool':True}

		#Appending set
		if self.SettingKeyVariable.startswith(NodingPrefixGetStr):

			#Definition the SplittedStrsList
			SplittedStrsList=self.SettingKeyVariable.split(NodingSuffixGetStr)

			#Definition the NodingCollectionStr
			NodingCollectionStr=NodingPrefixGetStr.join(
				SplittedStrsList[0].split(NodingPrefixGetStr)[1:])

			#Check if it is an append of Nodes
			IsNoderBool='NoderClass' in map(
											lambda __Class:
											__Class.__name__,
											type(self.SettingValueVariable).__mro__
											)

			#debug
			self.debug(('vars ',vars(),['NodingCollectionStr','IsNoderBool']))

			#Nodify
			self.node(NodingCollectionStr,**{'IsNoderBool':IsNoderBool})

			#Definition the KeyStr
			SettedKeyStr=NodingSuffixGetStr.join(SplittedStrsList[1:])

			#debug
			'''
			self.debug('KeyStr is '+KeyStr)
			'''

			#Append (or set if it is already in)
			Pather.setWithPathVariableAndKeyVariable(
				self.NodedOrderedDict,
				Pather.PathPrefixStr+SettedKeyStr,
				self.SettingValueVariable
			)

			#If it is an object
			if IsNoderBool:

				#Int and Set Child attributes
				self.SettingValueVariable.__setattr__(self.NodedPrefixStr+'Int',len(self.NodedOrderedDict)-1)
				NodedStrKeyStr=self.NodedPrefixStr+'KeyStr'
				self.SettingValueVariable.__setitem__(NodedStrKeyStr,SettedKeyStr)
				self.SettingValueVariable.__setattr__(self.NodedPrefixStr+'ParentPointer',self)

				#Init GrandChild attributes
				'''
				self.SettingValueVariable.__setattr__(self.NodedPrefixStr+'PathStr',"")
				self.SettingValueVariable.__setattr__(self.NodedPrefixStr+'GrandParentPointersList',[])
				'''

			#Return 
			OutputDict['HookingIsBool']=False
			#<Hook>return OutputDict

		#Call the parent get method
		if OutputDict['HookingIsBool']:
			BaseClass.set(self,**_KwargVariablesDict)

#</DefineClass>

#<DefineAttestingFunctions>
import ShareYourSystem as SYS

def attest_node():

	#Definition a Noder
	MyNoder=NoderClass()

	#Short expression for setting in the appended manner a structured object
	MyNoder['<Group>FirstChildNoder']=NoderClass()

	#Short expression for setting in the appended manner a structured object
	MyNoder['<Group>SecondChildNoder']=NoderClass()
	
	#set with a deep short Str and append Str
	MyNoder['<Group>FirstChildNoder/MyStr']="bonjour"
	
	#set with a deep deep short Str and append Str
	MyNoder['/<Group>FirstChildNoder/<Group>GrandChildNoder']=NoderClass()
	
	#Short expression and set in the appended manner
	MyNoder.__setitem__('<Sort>MyInt',1)

	#Short expression for setting in the append without binding
	MyNoder['<Sort>MyInt']+=1

	#Return
	return Attester.getAttestedStrWithStrsList(
			[
				MyNoder,
				Representer.represent(MyNoder['<Group>'],**{'RepresentingAlineaIsBool':False})
			]
		)
#</DefineAttestingFunctions>

