#/######################/#
# Import
#

#ImportModules
import ShareYourSystem as SYS

#/######################/#
# Define you hierarchic objects
#

#addDo
SYS.Doer.addDo('Recorder','Record','Recording','Recorded')

#Define a Moduler class
@SYS.ClasserClass()
class RecorderClass(SYS.NetworkerClass):
								
	def default_init(self,
						**_KwargVariablesDict
					):

		#Call the parent init method
		SYS.NetworkerClass.__init__(self,**_KwargVariablesDict)

#setNetwork		
SYS.Networker.setNetwork(
		RecorderClass,
		[
			('Trace','Traces'),
			('Sample','Samples')
		]
	)

#/######################/#
# Define one instance
#

MyRecorder=RecorderClass(
	).get(
		'/-Traces/|*v/-Samples/|Default'
	)

#/######################/#
# Print
#

#print
print('MyRecorder is ')
SYS._print(MyRecorder)

