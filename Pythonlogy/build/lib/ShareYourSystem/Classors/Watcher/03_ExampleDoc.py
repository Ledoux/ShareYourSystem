#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Watcher
from ShareYourSystem.Objects import Initiator

#Definition a MakerClass with decorated make by a Watcher
@Watcher.WatcherClass(**{
	'WatchingIsBool':True,
	#'ObservingWrapMethodStr':'do_make'
	#'ObservingWrapMethodStr':'superDo_make'
	'ObservingWrapMethodStr':'make'
	})
class MakerClass(Initiator.InitiatorClass):

	#Definition
	RepresentingKeyStrsList=[
								'MakingMyFloat',
								'MadeMyInt'
							]

	def default_init(self,
				_MakingMyFloat=1.,
				_MadeMyInt=0
				):
		Initiator.InitiatorClass.__init__(self)

	def do_make(self):

		#print
		print('self.MakingMyFloat is '+str(self.MakingMyFloat))
		print('self.MadeMyInt is '+str(self.MadeMyInt))
		print('')

		#Cast
		self.MadeMyInt=int(self.MakingMyFloat)

#Definition a MakerClass with decorated make by a Watcher
@Watcher.WatcherClass(**{
	'WatchingIsBool':True,
	#'ObservingWrapMethodStr':'do_make'
	#'ObservingWrapMethodStr':'superDo_make'
	'ObservingWrapMethodStr':'make'
	})
class BuilderClass(MakerClass):

	#Definition
	RepresentingKeyStrsList=[
							]

	def default_init(self,
				):
		MakerClass.__init__(self)

	def do_buid(self):
		pass

#Definition an instance
MyBuilder=MakerClass()

#Print
print('Before make, MyBuilder is ')
_print(MyBuilder)

#make once
MyBuilder.make(3.)

#Print
print('After the first make, MyBuilder is ')
_print(MyBuilder)

#Definition the AttestedStr
SYS._attest(
	[
		'BuilderClass.make is '+str(BuilderClass.make),
		'MyBuilder is '+SYS._str(
			MyBuilder,**{'RepresentingAlineaIsBool':False}
		)
	]
) 

#Print
