# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Tester helps for defining asserts between 
attested Strs stored in the Attests Folder and
new calls of the attest functions. Thanks here 
to a wrap of the unitest python module :
https://docs.python.org/2/library/unittest.html

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Classors.Attester"
DecorationModuleStr=BaseModuleStr
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import copy
import os
import sys
import unittest
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Representer
#</ImportSpecificModules>

#<DefineLocals>
AttestingStr='attest'
#</DefineLocals>

#<DefineFunctions>
def setTestFunctionWithFolderPathStrAndAttestUnboundMethod(
	_FolderPathStr,_AttestUnboundMethod):

	#Definition
	AttestUnboundMethodStr=_AttestUnboundMethod.__name__
	TestUnboundMethodStr='at'.join(AttestUnboundMethodStr.split('at')[1:])
	TestModule=sys.modules[_AttestUnboundMethod.__module__]

	#Debug
	'''
	print('l 50 Tester')
	print('_AttestUnboundMethod is ',_AttestUnboundMethod)
	print('_AttestUnboundMethod.__module__ is ',_AttestUnboundMethod.__module__)
	print('')
	'''

	#Define
	def test(_InstanceVariable):

		#Get the AssertedStr
		File=open(_FolderPathStr+AttestUnboundMethodStr+'.txt','r')
		AttestStr=File.read()
		File.close()

		#Call the attest function to get the TestVariable
		TestVariable=_AttestUnboundMethod(
						getattr(
							SYS,
							SYS.getClassStrWithNameStr(
								TestModule.__name__.split('.')[-1]
								if '.' in TestModule.__name__ else TestModule
							)
						)()
					)

		#Bind with TestStr setting
		Representer.RepresentingIdBool=False
		TestStr=Representer.getRepresentedStrWithVariable(TestVariable)
		Representer.RepresentingIdBool=True

		#Represent maybe
		if TestModule.TestingPrintIsBool:

			#debug
			print("\n###########################################")
			print("")
			print('AttestStr is :')
			print(AttestStr)
			print("")

			#debug
			print('TestStr is :')
			print(TestStr)
			print("")

		#Assert
		#print("a",AssertingStr)
		#print("b",_InstanceVariable.TestedPointer.TestStr)

		#assert
		_InstanceVariable.assertEqual(
				#1,1
				AttestStr,
				TestStr
		)

	#Copy a form of the test function and name it differently
	test.__name__=TestUnboundMethodStr

	#Debug
	'''
	print('l 96 Tester')
	print('TestModule is',TestModule)
	print('')
	'''
	
	#Append in the Test OrderedDict
	TestModule.TestedOrderedDict[test.__name__]=test
#</DefineFunctions>

#<DefineClass>
@DecorationClass()
class TesterClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
							]

	def default_init(self,**_KwargVariablesDict):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Class):

		#Call the parent init method
		BaseClass.__call__(self,_Class)

		#Represent
		self.test()

		#Return
		return _Class

	def do_test(self):
		
		#Init in the classed Module
		if hasattr(self.DerivedModule,'TestingPrintIsBool')==False:
			self.DerivedModule.TestingPrintIsBool=True
		self.DerivedModule.TestedOrderedDict=collections.OrderedDict()

		#set the tests for each asserting function
		map(
				lambda __AttestedUnboundMethod:
				setTestFunctionWithFolderPathStrAndAttestUnboundMethod(
					self.AttestingFolderPathStr,
					__AttestedUnboundMethod
				),
				self.AttestedUnboundMethodsList
			)
			
		#Definition the TestClass
		class TestClass(unittest.TestCase):				

			#Bind with the Tested object
			TestedPointer=self

			#Bound the setUp function
			#locals().__setitem__(setUp.__name__,setUp)
			
			#Bound each testing function
			for __InstanceVariableedKeyStr,__InstanceVariableedMethod in self.DerivedModule.TestedOrderedDict.items():
				locals().__setitem__(__InstanceVariableedKeyStr,__InstanceVariableedMethod)

			try:
				del TestedKeyStr,TestedMethod
			except:
				pass

		#Give a name
		TestClass.__name__=SYS.getClassStrWithNameStr(self.NameStr+'Test')

		#set to the module of the classing class
		self.DerivedModule.TestedClass=TestClass

		#Definition
		def test():

			#Call to the unittest runner
			TestLoader=unittest.TestLoader().loadTestsFromTestCase(
				self.DerivedModule.TestedClass
			)
			unittest.TextTestRunner(verbosity=2).run(TestLoader)

		#Link to the module of the classing class
		self.DerivedModule.test=test
#</DefineClass>

