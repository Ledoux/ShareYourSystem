
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


A Coupler 

"""


#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Noders.Attentioner"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>

from ShareYourSystem.Standards.Itemizers import Pather
from ShareYourSystem.Standards.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class CouplerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'CouplingNodeStr',
								'CouplingGetStr',
								'CoupledGetStr'
							]

	def default_init(self,
						_CouplingNodeStr="",
						_CouplingGetStr="",	
						_CoupledGetStr="",
						**_KwargVariablesDict
					):
	
		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_couple(self):

		#debug
		'''
		self.debug(('self.',self,[
									'CouplingNodeStr',
									'CouplingGetStr',
									'PointingBackBool'
								]))
		'''
		
		#set
		self.CoupledGetStr=Noder.NodingPrefixGetStr+self.CouplingNodeStr+Noder.NodingSuffixGetStr
		self.PointingSetPathStr=self.CoupledGetStr+self.CouplingGetStr.split(
						Noder.NodingSuffixGetStr
					)[-1]

		#debug
		'''
		self.debug(('self.',self,['CoupledGetStr','PointingSetPathStr']))
		'''

		#point
		self.point(
					self.CouplingGetStr,
					self.PointingSetPathStr
				)

		#Return self
		#return self

#</DefineClass>

```

<small>
View the Coupler sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Noders/Coupler" target="_blank">Github</a>
</small>

