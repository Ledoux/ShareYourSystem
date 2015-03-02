#ImportModules
import ShareYourSystem as SYS

#Define
@SYS.DoerClass()
class MakerClass(object):

	def default_init(self,
				_MakingMyFloat=1.,
				_MakingMyList=None,
				_MakingFirstInt={'DefaultValueType':int},
				_MakingSecondInt=0,
				_MadeMyInt=0,
				_MadeMyList=None,
				):
		object.__init__(self)

	def do_make(self):

		#print
		print('Maker : I am going to make')
		print('self.MakingMyFloat is ',self.MakingMyFloat)
		print('')

		#set
		self.MadeMyInt=int(self.MakingMyFloat)
	
#Definition of an instance and make
MyMaker=MakerClass(
	_MakingMyList=['hello'],
	**{'MakingFirstInt':3}
	).superDo_make(
		3.,
		_SecondInt=5
	)

#print
print('MyMaker.getDo() is ')
print(SYS.indent(MyMaker.getDo()))
print('')

#print
print('we reset doing')
MyMaker.setDoing(MakerClass)
print('')

#print
print('MyMaker.getDo() after set doing is ')
print(SYS.indent(MyMaker.getDo()))
print('')

#Add
print('MyMaker.__dict__ is '+SYS.indent(MyMaker.__dict__))


