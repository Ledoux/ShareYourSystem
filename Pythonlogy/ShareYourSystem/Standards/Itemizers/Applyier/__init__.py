# -*- coding: utf-8 -*-
"""

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


An Applyier apply a function thanks to a ApplyingMethodStr and an ApplyingArgDict.
This property is going to be useful to begin to establish mappping methods and 
commanding calls in deep structures.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Executer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
import collections
#</ImportSpecificModules>

#<DefineLocals>
class ApplyDictClass(collections.OrderedDict):
	def __init__(self,_Dict=None):

		#Check
		if _Dict==None:
			_Dict={}

		#call the parent init method
		collections.OrderedDict.__init__(self,_Dict)

		#define 
		self.update(
			{
				'LiargVariablesList':[],
				'KwargVariablesDict':{}
			}
		)

		#update
		self.update(_Dict)
SYS.ApplyDictClass=ApplyDictClass
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class ApplyierClass(BaseClass):
		
	#Definition
	RepresentingKeyStrsList=[
								#'ApplyingMethodStr',
								#'ApplyingArgDict',
								#'ApplyingIsBool',
								#'AppliedMethod',
								#'AppliedOutputVariable'
							]

	def default_init(self,
				_ApplyingMethodStr="",
				_ApplyingArgDict=None,
				_ApplyingIsBool=False,
				_AppliedMethod=None,
				_AppliedOutputVariable=None,
				**_KwargVariablesDict
			):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_apply(self):
		""" """

		#debug
		'''
		self.debug(
					('self.',self,[
									'ApplyingMethodStr',
									'ApplyingArgDict'
								])
		)
		'''
		
		#set
		self.AppliedMethod=getattr(self,self.ApplyingMethodStr)

		#debug
		''''
		self.debug(
					('self.',self,[
									'AppliedMethod'
								])
			)
		'''

		#Check
		if self.AppliedMethod!=None:

			#debug
			'''
			self.debug(
						[
							'AppliedMethod is good, We are going to apply',
							('self.',self,['AppliedMethod','ApplyingArgDict'])
						]
					)
			'''
			
			if 'KwargVariablesDict' in self.ApplyingArgDict:

				#debug
				'''
				self.debug('We apply with a KwargVariablesDict')
				'''

				#Call the AppliedMethod
				self.AppliedOutputVariable=self.AppliedMethod(
								*self.ApplyingArgDict['LiargVariablesList'],
								**self.ApplyingArgDict['KwargVariablesDict']
								) 
			else:

				#debug
				'''
				self.debug('We apply without a KwargVariablesDict')
				'''



				#Call
				self.AppliedOutputVariable=self.AppliedMethod(
					*self.ApplyingArgDict['LiargVariablesList']
					)

	def mimic_set(self):

		#debug
		'''
		self.debug(('self.',self,['SettingKeyVariable','SettingValueVariable']))
		'''
		
		#Definition
		OutputDict={'HookingIsBool':True}

		#Check
		if self.SettingKeyVariable!="":

			#Call for a hook
			#if (self.SettingKeyVariable[0].isalpha() or self.SettingKeyVariable[:2]=="__"
			#	) and self.SettingKeyVariable[0].lower()==self.SettingKeyVariable[0]:
			if type(self.SettingValueVariable)==ApplyDictClass:

				#debug
				'''
				self.debug(
							[
								('This is a set that calls a method so this is an apply...'),
								('self.',self,[
												'SettingKeyVariable',
												'SettingValueVariable'
												]
								)
							]
						)
				'''
				
				#Apply
				self.ApplyingIsBool=False
				self.apply(
								self.SettingKeyVariable,
								self.SettingValueVariable
							)

				#Return
				OutputDict['HookingIsBool']=False
				#<Hook>return OutputDict

		if OutputDict['HookingIsBool']:
			BaseClass.set(self)

#</DefineClass>

