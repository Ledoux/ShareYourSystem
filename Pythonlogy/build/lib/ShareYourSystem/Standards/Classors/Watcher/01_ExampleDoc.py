#ImportModules
import ShareYourSystem as SYS

#Definition a MakerClass with decorated make by a Watcher
@SYS.WatcherClass(**{
	'WatchingIsBool':True,
	#'ObservingWrapMethodStr':'do_make'
	#'ObservingWrapMethodStr':'superDo_make'
	'ObservingWrapMethodStr':'make'
	})
class MakerClass(SYS.InitiatorClass):

	#Definition
	RepresentingKeyStrsList=[
								'MakingMyFloat',
								'MadeMyInt'
							]

	def default_init(self,
				_MakingMyFloat=1.,
				_MadeMyInt=0
				):
		SYS.InitiatorClass.__init__(self)

	def do_make(self):

		#print
		print('self.MakingMyFloat is '+str(self.MakingMyFloat))
		print('self.MadeMyInt is '+str(self.MadeMyInt))
		print('')

		#Cast
		self.MadeMyInt=int(self.MakingMyFloat)


#Definition an instance
MyMaker=MakerClass()

#Print
print('Before make, MyMaker is ')
SYS._print(MyMaker)

#make once
MyMaker.make(3.)

#Print
print('After the first make, MyMaker is ')
SYS._print(MyMaker)

#Definition the AttestedStr
SYS._attest(
	[
		'MakerClass.make is '+str(MakerClass.make),
		'MyMaker is '+SYS._str(
			MyMaker,**{'RepresentingAlineaIsBool':False}
		)
	]
) 

#Print
