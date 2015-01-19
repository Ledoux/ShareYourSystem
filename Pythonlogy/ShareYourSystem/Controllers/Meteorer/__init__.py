# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


An Meteorer maps an append
"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Controllers.Grider"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import ddp
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class MeteorerClass(BaseClass):
	
	#Definition 
	RepresentingKeyStrsList=[
								'MeteoringSocketStr',
								'MeteoringWidthInt',
								'MeteoringHeigthInt',
								'MeteoredConcurrentDDPClientVariable',
								'MeteoredUrlStr'
							]

	def default_init(self,
						_MeteoringSocketStr='ws://127.0.0.1:3000/websocket',
						_MeteoringWidthInt=100,
						_MeteoringHeigthInt=100,
						_MeteoredConcurrentDDPClientVariable=None,
						_MeteoredUrlStr="",
						_MeteoredServerStr="",
						_MeteoredServerHtmlVariable=None,
						**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)
		
	def do_meteor(self):

		#Set the MeteoredUrlStr
		self.MeteoredUrlStr='/websocket'.join(
				self.MeteoringSocketStr.split('/websocket')[:-1]
			).replace('ws','http')

		#Do the connection
		self.MeteoredConcurrentDDPClientVariable = ddp.ConcurrentDDPClient(self.MeteoringSocketStr)
		self.MeteoredConcurrentDDPClientVariable.start()


#</DefineClass>
