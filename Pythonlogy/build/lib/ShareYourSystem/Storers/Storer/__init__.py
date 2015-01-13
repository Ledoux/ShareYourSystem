# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Storer instances

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Structurer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class StorerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'StoringCollectionStr',
								'StoringTopDeriveDatabaserVariable'
							]

	def default_init(self,
						_StoringCollectionStr="",
						_StoringTopDeriveDatabaserVariable=None,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_store(self):

		#check
		if self.StoringCollectionStr=="":
			self.StoringCollectionStr=self.NodingCollectionStr
			self.StoringTopDeriveDatabaserVariable=getattr(
				self,
				self.NodingCollectionStr+'CollectionOrderedDict'
			).values()[-1]

		#flush
		self.StoringTopDeriveDatabaserVariable.flush()


		
#</DefineClass>

