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
PointPrefixStr=""
PointSuffixStr=""
PointBackStr="Back"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class PointerClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'PointingGetVariable',
								'PointingSetPathStr',
								'PointingBackSetStr',
								'PointedGetVariable',
								'PointedPathBackVariable',
								'PointedLocalSetStr',
								'PointedBackSetStr'
							]

	def default_init(
					self,		
					_PointingGetVariable=None,
					_PointingSetPathStr="",
					_PointingBackSetStr="",
					_PointedGetVariable=None,
					_PointedPathBackVariable="",
					_PointedPathBackStr="",
					_PointedLocalSetStr="",
					_PointedBackSetStr="",
					**_KwargVariablesDict
				):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_point(self):

		#debug
		'''
		self.debug(('self.',self,[
									'PointingGetVariable',
									'PointingSetPathStr'
								]))
		'''

		#get
		self.PointedGetVariable=self[self.PointingGetVariable]

		#debug
		'''
		self.debug(
					[
						'After getting',
						('self.',self,[
										'PointingGetVariable',
										'PointedGetVariable'
										]
									)
					]
				)
		'''

		#set
		self.PointedPathBackStr=Pather.getPathedBackGetStrWithGetStr(
			self.PointingSetPathStr
		)
		
		#set
		self.PointedLocalSetStr=self.PointingSetPathStr.split(
			self.PointedPathBackStr+Pather.PathPrefixStr
		)[-1]

		#debug
		'''
		self.debug(('self.',self,[
									'PointingSetPathStr',
									'PointedPathBackStr',
									'PointedLocalSetStr'
								]))
		'''
		
		#set
		self.SettingKeyVariable=self.PointedPathBackStr+Pather.PathPrefixStr+PointPrefixStr+self.PointedLocalSetStr+PointSuffixStr

		#debug
		'''
		self.debug(('self.',self,['SettingKeyVariable']))
		'''
		
		#set the point variable
		self[
				self.SettingKeyVariable
			]=self.PointedGetVariable

		#set a back pointer
		if self.PointingBackSetStr!="":

			#debug
			'''
			self.debug(
						[
							'We point back here',
							('self.',self,[
												'PointingSetPathStr',
												'PointingBackSetStr'
										])
						]
					)
			'''
			
			#Get
			self.PointedPathBackVariable=Pather.getPathedBackVariableWithVariableAndGetStr(
				self,
				self.PointingSetPathStr
			)

			#debug
			'''
			self.debug(('self.',self,[
										'PointedGetVariable',
										'PointedPathBackVariable',
										'PointingBackSetStr'
									]))
			'''

			#link
			self.PointedGetVariable[
				self.PointingBackSetStr
			]=self.PointedPathBackVariable


#</DefineClass>

