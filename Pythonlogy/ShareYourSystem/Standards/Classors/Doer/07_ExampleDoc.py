#ImportModules
import ShareYourSystem as SYS

#Define
@SYS.DoerClass()
class MakerClass(SYS.ObjectClass):

	def default_init(self,
				_MakingMyFloat=0.,
				_MadeShareObject=SYS.ObjectClass(),
				_MadeSpecificObject=None
				):
		SYS.ObjectClass.__init__(self)

	def do_make(self):

		#print
		print('Maker : I am going to make')
		print('')

		#set
		self.MadeSpecificObject.MyInt=int(self.MakingMyFloat)

		#Return self
		#return self
	
#Definition of an instance and make
MakerClass.MadeShareObject.MyInt=5
MyMaker=MakerClass().make(3.)

#Add
print("\n".join([
		'After the make ',
		'MakerClass.MadeSpecificObject is '+str(MakerClass.MadeSpecificObject),
		'MyMaker.MadeShareObject.__dict__ is '+str(MyMaker.MadeShareObject.__dict__),
		'MyMaker.MadeSpecificObject.__dict__ is '+str(MyMaker.MadeSpecificObject.__dict__)
	]))


