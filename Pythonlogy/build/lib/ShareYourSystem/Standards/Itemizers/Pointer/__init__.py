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
PointToPrefixStr=">"
PointBackPreifxStr="Back"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class PointerClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'PointingToGetKeyVariable',
								'PointingToSetKeyVariable',
								'PointingBackSetKeyVariable',
								'PointingBackBool',
								'PointedToGetValueVariable'
							]

	def default_init(
					self,		
					_PointingToGetKeyVariable=None,
					_PointingToSetKeyVariable=None,
					_PointingBackSetKeyVariable=None,
					_PointingBackBool=False,
					_PointedToGetValueVariable=None,
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
									'PointingToGetKeyVariable',
									'PointingToSetKeyVariable'None								'PointingFromGetVariable',
								])
					)
		'''

		#get
		PointedToGetValueVariable=self[self.PointingToGetKeyVariable]

		#/####################/#
		# Check for the SetKeyVariable
		#

		#Check
		if self.PointingToSetKeyVariable==None:
			PointedToSetKeyVariable=str(
					self.PointingToGetKeyVariable
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
				PointedToGetValueVariable
			)

		#debug
		'''
		self.debug(
					[
						'After getting',
						('locals()["',locals(),[
										'PointedToGetValueVariable',
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

			#debug
			self.debug(
					[
						'We point back',
						('self.',self,['PointingBackSetKeyVariable'])
					]
				)

			#Check
			if self.PointingBackSetKeyVariable==None:
				
				#debug
				self.debug(
					'PointedToSetKeyVariable is '+str(PointedToSetKeyVariable)
				)

				#/###################/#
				# Case where the PointedToSetKeyVariable is derived from a pathsetstr
				#

				#split
				PointedKeyStrsList=PointedToSetKeyVariable.split('_')
				if len(PointedKeyStrsList)>1:

					#remove the last
					PointedKeyStrsList=PointedKeyStrsList[1:]

					#reverse
					PointedKeyStrsList.reverse()

					#join
					PointedBackSetKeyVariable='_'.join(PointedKeyStrsList)

				#/###################/#
				# else just take the id
				#

				else:

					#set default
					PointedBackSetKeyVariable=str(self.IdInt)

				#add
				PointedBackSetKeyVariable=PointedBackSetKeyVariable+self.NameStr

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
							PointedToGetValueVariable
						)
					]
				)

			#set
			PointedToGetValueVariable.set(
					PointedBackSetKeyVariable,
					self
				)

		#alias
		self.PointedToGetValueVariable=PointedToGetValueVariable

	def mimic_get(self):

		#debug
		'''
		self.debug(
				('self.',self,[
						'GettingKeyVariable',
					])
			)
		'''

		#Check
		if type(self.GettingKeyVariable)==str and self.GettingKeyVariable.startswith(
			PointToPrefixStr
		):

			#debug
			self.debug(
					'we point here'
				)

			#point
			self.point(
					SYS.deprefix(self.GettingKeyVariable,PointToPrefixStr)
				)

			#alias
			self.GettedValueVariable=self.PointedToGetValueVariable

			#return
			return {'HookingIsBool':False}


		else:

			#call the base method
			return BaseClass.get(self)

	def mimic_set(self):

		#debug
		'''
		self.debug(
				('self.',self,[
						'SettingKeyVariable',
						'SettingValueVariable',
					])
			)
		'''

		#Check
		if type(self.SettingKeyVariable)==str and self.SettingKeyVariable.startswith(
			PointToPrefixStr
		):

			#debug
			self.debug(
					'we point here'
				)

			#point
			self.point(
					SYS.deprefix(self.SettingKeyVariable,PointToPrefixStr),
					self.SettingValueVariable
				)

			#return
			return {'HookingIsBool':False}


		else:

			#call the base method
			return BaseClass.set(self)

#</DefineClass>

