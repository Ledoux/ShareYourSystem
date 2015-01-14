
<!--
FrozenIsBool False
-->

##Code

----

<ClassDocStr>

----

```python
# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Restricter object sets only in the __dict__ only if hasattr(self,self.SettingKeyVariable)
returns True before.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Itemizers.Attributer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class RestricterClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'RestrictingIsBool',
								'RestrictingKeyStr',
								'RestrictedSetIsBool'
							]

	def default_init(self,
				_RestrictingIsBool=False, 
				_RestrictingKeyStr=None,					
				_RestrictedSetIsBool=True,			
				**_KwargVariablesDict
				):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_restrict(self):

		#Init
		self.RestrictedSetIsBool=True

		#debug
		'''
		self.debug(('self.',self,['RestrictingIsBool','RestrictingKeyStr']))
		'''

		#Check
		if self.RestrictingIsBool:

			#Check
			if hasattr(self,self.RestrictingKeyStr):
				self.RestrictedSetIsBool=False

		else:

			#set to False
			self.RestrictedSetIsBool=False

	#<Hook>@Hooker.HookerClass(**{'HookingAfterVariablesList':[BaseClass.set]})
	#@Imitater.ImitaterClass()
	def mimic_set(self):
		""" """

		#debug
		'''
		self.debug(('self.',self,['SettingKeyVariable','SettingValueVariable']))
		'''

		#Definition
		OutputDict={'HookingIsBool':True}

		#debug
		'''
		self.debug('We are going to restrict')
		'''

		#restrict
		self.restrict(_KeyStr=self.SettingKeyVariable)

		#<Hook>
		#Stop the setting
		if self.RestrictedSetIsBool:
			OutputDict["HookingIsBool"]=False
			return OutputDict
		#</Hook>

		#Debug
		'''
		self.debug(
					[
						'BaseClass is '+str(BaseClass),
						'BaseClass.set is '+str(BaseClass.set),
					]
				)
		'''
		
		#Call the parent set method
		return BaseClass.set(self)

#</DefineClass>


```

<small>
View the Restricter sources on [Github](https://github.com/Ledoux/ShareYourSystem/tree/master/ShareYourSystem/Itemizers/Restricter)
</small>

