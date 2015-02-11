# -*- coding: utf-8 -*-
"""

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


An Applyier apply a function thanks to a ApplyingMethodVariable and an ApplyingArgVariable.
This property is going to be useful to begin to establish mappping methods and 
commanding calls in deep structures.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Setter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
import collections
#</ImportSpecificModules>

#<DefineLocals>
ApplyMapPrefixStr="map*"
ApplySetPrefixStr="apply*"
class ApplyDictClass(collections.OrderedDict):
	def __init__(self,_DictVariable=None):

		#Check
		if _DictVariable==None:
			_DictVariable={}
		elif type(_DictVariable)==list:
			_DictVariable={
				'LiargVariablesList':_DictVariable
			}
		elif hasattr(_DictVariable,'items')==False:
			_DictVariable={
				'LiargVariablesList':[_DictVariable]
			}

		#call the parent init method
		collections.OrderedDict.__init__(self,_DictVariable)

		#define 
		self.update(
			{
				'LiargVariablesList':[],
				'KwargVariablesDict':{}
			}
		)

		#update
		self.update(_DictVariable)

SYS.ApplyDictClass=ApplyDictClass
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class ApplyierClass(BaseClass):
		
	#Definition
	RepresentingKeyStrsList=[
								#'ApplyingMethodVariable',
								#'ApplyingArgVariable',
								#'AppliedMethod',
								#'AppliedOutputVariable'
							]

	def default_init(self,
				_ApplyingMethodVariable="",
				_ApplyingArgVariable=None,
				_AppliedMethod=None,
				_AppliedOutputVariable=None,
				_AppliedMapVariablesList=None,
				**_KwargVariablesDict
			):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_apply(self):
		""" """

		#debug
		self.debug(
					('self.',self,[
									'ApplyingMethodVariable',
									'ApplyingArgVariable'
								])
		)
	
		#Check
		if type(self.ApplyingArgVariable)!=SYS.ApplyDictClass:

			#Check
			if self.ApplyingMethodVariable in ['get','__getitem__']:

				#Check
				if type(self.ApplyingArgVariable)!=list:
					self.ApplyingArgVariable=[self.ApplyingArgVariable]

			#init
			self.ApplyingArgVariable=SYS.ApplyDictClass(
					{
						'LiargVariablesList':self.ApplyingArgVariable
					}
				)

		#Check
		if type(self.ApplyingMethodVariable)!=str:

			#Check
			if type(self.ApplyingMethodVariable)==SYS.ApplyDictClass:

				#apply
				self.apply(
						self.ApplyingMethodVariable['MethodStr'],
						self.ApplyingMethodVariable
					)

				#return
				return

			elif hasattr(self.ApplyingMethodVariable,'items'):

				#map 
				map(
						lambda __ItemTuple:
						self.apply(
							__ItemTuple[0],
							__ItemTuple[1]
						),
						self.ApplyingMethodVariable.items()
					)

				#return
				return

			elif type(self.ApplyingMethodVariable)==list:

				#debug
				self.debug(
						[
							'we do a map top map',
							('self.',self,[
									'ApplyingMethodVariable',
									'ApplyingArgVariable'
								])
						]
					)

				#map
				self.AppliedMapVariablesList=map(
						lambda __MethodVariable,__ArgVariable:
						self.apply(
							__MethodVariable,
							__ArgVariable
						),
						self.ApplyingMethodVariable,
						self.ApplyingArgVariable['LiargVariablesList']
					)

				#return
				return 

		else:

			#Check
			if self.ApplyingMethodVariable.startswith(ApplyMapPrefixStr):

				#apply a map to map
				self.apply(
						[
							SYS.deprefix(
								self.ApplyingMethodVariable,
								ApplyMapPrefixStr
							)
						]*len(self.ApplyingArgVariable),
						self.ApplyingArgVariable['LiargVariablesList']
					)

				#return 
				return 

			else:

				#set
				self.AppliedMethod=getattr(
					self,
					self.ApplyingMethodVariable
				)

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
					self.debug(
								[
									'AppliedMethod is good, We are going to apply',
									('self.',self,[
										'AppliedMethod',
										'ApplyingArgVariable'
									])
								]
							)
					
					#Check
					if len(self.ApplyingArgVariable['KwargVariablesDict'])>0:

						#debug
						'''
						self.debug('We apply with a KwargVariablesDict')
						'''

						#Call the AppliedMethod
						self.AppliedOutputVariable=self.AppliedMethod(
							*self.ApplyingArgVariable['LiargVariablesList'],
							**self.ApplyingArgVariable['KwargVariablesDict']
						) 
					else:

						#debug
						'''
						self.debug('We apply without a KwargVariablesDict')
						'''
						
						#Call
						self.AppliedOutputVariable=self.AppliedMethod(
							*self.ApplyingArgVariable['LiargVariablesList']
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
				self.apply(
								self.SettingKeyVariable,
								self.SettingValueVariable
							)

				#Return
				OutputDict['HookingIsBool']=False
				#<Hook>return OutputDict

			elif type(
				self.SettingKeyVariable
				)==str and self.SettingKeyVariable.startswith(
					ApplySetPrefixStr
				):

				#apply
				self.apply(
						SYS.deprefix(
							self.SettingKeyVariable,
							ApplySetPrefixStr
						),
						self.SettingValueVariable
					)

				#Return
				OutputDict['HookingIsBool']=False
				#<Hook>return OutputDict

		if OutputDict['HookingIsBool']:
			BaseClass.set(self)

#</DefineClass>

