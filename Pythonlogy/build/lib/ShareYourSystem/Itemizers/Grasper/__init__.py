# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Grasper can get a GraspedGetVariable depending if the GraspingGetVariable
is a PathStr, a GraspDict or directly the Variable itself.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Itemizers.Pather"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
#</ImportSpecificModules>

#<DefineLocals>
class GraspDictClass(collections.OrderedDict):pass
SYS.GraspDictClass=GraspDictClass
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class GrasperClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'GraspingClueVariable',
								'GraspedAnswerVariable',	
								'GraspedClueVariableType'
							]

	def default_init(self,	
				_GraspingClueVariable=None,
				_GraspedAnswerVariable=None,	
				_GraspedClueVariableType=None,	
				**_KwargVariablesDict
				):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_grasp(self):

		#type
		self.GraspedClueVariableType=type(self.GraspingClueVariable)

		#debug
		'''
		self.debug(
					[
						'GraspedClueVariableType is '+str(GraspedClueVariableType),
						('self.',self,[
										'GraspedClueVariableType',
										'GraspingClueVariable'
									])
					]
				)
		'''

		#Check
		if self.GraspedClueVariableType in SYS.StrTypesList:

			#debug
			'''
			self.debug('We get with a pathstr')
			'''

			#It is a get through a PathStr
			self.GraspedAnswerVariable=self[self.GraspingClueVariable]

		elif self.GraspedClueVariableType==GraspDictClass:

			#debug
			'''
			self.debug('We get with a GraspDict')
			'''

			#Check
			if type(self.GraspingClueVariable['HintVariable']) in SYS.StrTypesList:

				#debug
				'''
				self.debug(
							[
								'We get with a pathstr in the GraspDict',
								"self.GraspingClueVariable['HintVariable'] is "+self.GraspingClueVariable['HintVariable']
							]
						)
				'''
				
				#The GraspDict has maybe a path str to get the thing
				self.GraspedAnswerVariable=self[self.GraspingClueVariable['HintVariable']]

			else:

				#debug
				'''
				self.debug('We get direct in the GraspDict')
				'''

				#The GraspDict has maybe a path str to get the thing
				self.GraspedAnswerVariable=self.GraspingClueVariable['HintVariable']

		else:

			#It is already getted
			self.GraspedAnswerVariable=self.GraspingClueVariable


#</DefineClass>

