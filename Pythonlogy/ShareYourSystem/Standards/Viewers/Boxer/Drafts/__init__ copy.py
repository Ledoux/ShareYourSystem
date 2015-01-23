# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Boxer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Viewers.Viewer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class BoxerClass(BaseClass):
	
	#Definition 
	RepresentingKeyStrsList=[
								'BoxingPatchStr',
								'BoxingXaxisInt',
								'BoxingYaxisInt',
								'BoxingWidthInt',
								'BoxingHeigthInt',
								'BoxedWidthInt',
								'BoxedHeigthInt',
								'BoxedDerivePatcherVariable',
								'BoxedCollectionsOrderedDict'
							]

	def default_init(self, 
						_BoxingPatchStr="",
						_BoxingCollectionStr="",
						_BoxingXaxisInt=400,
						_BoxingYaxisInt=100,
						_BoxingWidthInt=50,
						_BoxingHeigthInt=10,
						_BoxedWidthInt=0,
						_BoxedHeigthInt=0,
						_BoxedDerivePatcherVariable=None,
						_BoxedCollectionsOrderedDict=None,
						**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_box(self):
		
		#parent first
		self.parent(['MeteoredConcurrentDDPClientVariable'])

		#Check
		if self.BoxedDerivePatcherVariable==None:
			self.BoxedDerivePatcherVariable=self.NodePointDeriveNoder

		'''
		#debug
		self.debug(('self.',self,[
			#'ParentedDeriveParentersList',
			'ParentedPathStr'
		]))

		#Determine the deep
		self.BoxedDeepInt=len(self.ParentedPathStr.split('/'))
		'''


		"""
		#insert the node box
		self.MeteoredConcurrentDDPClientVariable.call(
				'mongo',
				'boxes',
				'insert',
				{
					'x':self.BoxingWidthInt,
					'y':self.BoxingHeigthInt,
					'IsNoderBool':True,
					'NodeKeyStr':self.NodeKeyStr,
					'CollectionStr':self.NodeCollectionStr,
					'PatchStr':self.BoxingPatchStr
				}
			)
		"""

		#set
		self.BoxedCollectionsOrderedDict=self.BoxedDerivePatcherVariable.CollectionsOrderedDict

		#debug
		'''
		self.debug(('self.',self,['BoxedCollectionsOrderedDict']))
		'''


		'''
		#Check
		if len(self.CollectionsOrderedDict)%2==0:
			BoxedStepXaxisInt=self.BoxingWidthInt/len(self.BoxedCollectionsOrderedDict)
		else:
			BoxedStepXaxisInt=self.BoxingWidthInt/(len(self.BoxedCollectionsOrderedDict)-1)

		#set
		self.BoxedCollectionXaxisIntsArray=BoxedStepXaxisInt*np.array(
			len(self.BoxedCollectionsOrderedDict)
		)+self.BoxingXaxisInt-(self.BoxingWidthInt/2.)
		self.BoxesCollectionYaxisInt=self.BoxingYaxisInt+self.BoxingHeigthInt

		#debug
		self.debug(('self.',self,[
						'BoxedCollectionXaxisIntsArray',
						'BoxesCollectionYaxisInt'
						]))
		'''

		#insert the child collections ordered dict
		map(
				lambda __BoxedCollectionStr:
				self.MeteoredConcurrentDDPClientVariable.call(
					'mongo',
					'boxes',
					'insert',
					{
						'IsOrderedDict':True,
						'CollectionStr':__BoxedCollectionStr,
						'SystemStr':self.BoxingSystemStr,
						'PatchStr':self.BoxingPatchStr
					}
				),
				self.BoxedCollectionsOrderedDict.keys()
			)

#</DefineClass>