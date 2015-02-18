# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Pointer 

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Walker"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Itemizers import Pather
#</ImportSpecificModules>

#<DefineLocals>
PointPrefixStr=">"
PointSuffixStr=""
PointBackStr="Back"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class PointerClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'PointingToGetVariable',
								'PointingToSetKeyVariable',
								'PointingBackSetKeyVariable',
								'PointingBackBool'
							]

	def default_init(
					self,		
					_PointingToGetVariable=None,
					_PointingToSetKeyVariable=None,
					_PointingBackSetKeyVariable="",
					_PointingBackBool=False,
					**_KwargVariablesDict
				):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_point(self):

		#/###################/#
		# First point TO like a classic set
		#

		#debug
		'''
		self.debug(
					('self.',self,[
									'PointingToGetVariable',
									'PointingToSetKeyVariable'None								'PointingFromGetVariable',
								])
					)
		'''

		#get
		PointedToGetVariable=self[self.PointingToGetVariable]

		#/####################/#
		# Check for the SetKeyVariable
		#

		#Check
		if self.PointingToSetKeyVariable==None:
			PointedToSetKeyVariable=PointPrefixStr+str(
					self.PointingToGetVariable
				).replace('/','_')
		else:
			PointedToSetKeyVariable=self.PointingToSetKeyVariable

		#debug
		self.debug(
				'PointedToSetKeyVariable is '+SYS._str(
					PointedToSetKeyVariable
				)
			)

		#set
		self.set(
				PointedToSetKeyVariable,
				PointedToGetVariable
			)

		#debug
		'''
		self.debug(
					[
						'After getting',
						('locals()["',locals(),[
										'PointedToGetVariable',
										],']
									)
					]
				)
		'''

		#/###################/#
		# Maybe do a back point
		#

		#Check
		if self.PointingBackBool:

			#Check
			if self.PointingBackSetKeyVariable==None:
				
				#get the pathstr
				PointedBackSetKeyVariable="nn"

			else:

				#just alias
				PointedBackSetKeyVariable=self.PointingBackSetKeyVariable


			#debug
			self.debug(
					[
						'we set the back',
						'PointedBackSetKeyVariable is '+SYS._str(
							PointedBackSetKeyVariable
						),
						'PointedToGetVariable is '+SYS._str(
							PointedToGetVariable
						)
					]
				)

			#set
			PointedToGetVariable.set(
					PointedBackSetKeyVariable,
					self
				)


#</DefineClass>

