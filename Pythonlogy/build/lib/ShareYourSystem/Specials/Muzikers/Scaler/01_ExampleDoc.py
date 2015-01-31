
#ImportModules
import ShareYourSystem as SYS
import os

#Definition a Scaler
MyScaler=SYS.ScalerClass().scale()

'''
MyScaler.write(
	music21.vexflow.fromObject(
		MyScaler.ScaledOrderedDict.values()[5]['Stream'],
		mode="html"
	),
	**{
		'FolderingPathStr':'/Users/ledoux/Documents/MampLocalhost/vexflow/',
		'FilingKeyStr':"Scale.html"
	}
).close()
'''