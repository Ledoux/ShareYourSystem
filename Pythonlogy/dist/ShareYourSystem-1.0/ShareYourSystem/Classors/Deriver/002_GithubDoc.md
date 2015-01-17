
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


The Deriver helps for building a base-derive relationships between the classes.
Once a <Class> with based classes is defined, a decorating DeriverClass instance
append to these corresponding BaseClasses the <Class> as a derived class.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Classors.Doer"
DecorationModuleStr=BaseModuleStr
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import sys
#</ImportSpecificModules>

#<DefineFunctions>
def getIsDerivedBoolWithParentClassAndDeriveClass(_ParentClass,_DeriveClass):

	#Debug
	'''
	print('Deriver l.37')
	print('_ParentClass is ',_ParentClass)
	print('_DeriveClass is ',_DeriveClass)
	print('')
	'''
	
	#Return
	return _DeriveClass in _ParentClass.__mro__
#</DefineFunctions>

#<DefineClass>
@DecorationClass()
class DeriverClass(BaseClass):

	def default_init(self,
						_DerivedModule=None,
						**_KwargVariablesDict
					):


		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Class):

		#debug
		'''
		print('Deriver l.30 __call__ method')
		print('_Class is ',_Class)
		print('')
		'''

		#Call the parent __call__ method
		BaseClass.__call__(self,_Class)

		#Debug
		'''
		print('Deriver l.54 We are going to derive')
		print('self.derive is ',self.derive)
		print('')
		'''

		#Derive
		self.derive()

		#Debug
		'''
		print('derive is done')
		print('')
		'''

		#Return 
		return _Class

	def do_derive(self):

		#Debug
		'''
		print('self.DoClass is ',self.DoClass)
		print('')
		'''

		#alias
		DoClass=self.DoClass

		#Link
		self.DerivedModule=sys.modules[DoClass.__module__]

		#set
		if len(DoClass.__bases__)>0:

			#set the DerivedBaseClas
			DerivedBaseClass=DoClass.__bases__[0]

			#Debug
			'''
			print('l. 83 Deriver')
			print('We can set derived bases for the parent')
			print('DerivedBaseClass is ',DerivedBaseClass)
			print('')
			'''
			
			#Append to the parent class 
			if hasattr(DerivedBaseClass,'DerivedClassesList'):
				DerivedBaseClass.DerivedClassesList.append(DoClass)
			else:
				DerivedBaseClass.DerivedClassesList=[DoClass]

			#Add to the KeyStrsList
			DoClass.KeyStrsList+=SYS.getKeyStrsListWithClass(DoClass)

#</DefineClass>

```

<small>
View the Deriver sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Classors/Deriver" target="_blank">Github</a>
</small>

