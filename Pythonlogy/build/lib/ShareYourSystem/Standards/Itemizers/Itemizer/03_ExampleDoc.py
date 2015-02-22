
#ImportModules
import ShareYourSystem as SYS

@SYS.ClasserClass()
class MakerClass(SYS.ItemizerClass):
	
	def default_init(self,
			_MakingMyFloat=0.,
			_MadeMyInt=0
		):

		#call the init base method
		SYS.ItemizerClass.__init__(self)

	def do_make(self):

		#set
		self.MadeMyInt=(int)(self.MakingMyFloat)

#Define how to map the make
def getMapList(_LiargVariablesList):
	return map(
		lambda __Variable:
		[__Variable],
		_LiargVariablesList[0]
	)

#define and itemize just like a get
MyMaker=MakerClass(
	).itemize(
		#ItemizingKeyVariable
		'map*make',
		#ItemizingMapGetVariable
		_MapGetVariable='MadeMyInt'
	)

#show the map
print("MyMaker.ItemizedValueMethod([3.,6.]).ItemizedMapVariablesList is ")
print(MyMaker.ItemizedValueMethod([3.,6.]).ItemizedMapVariablesList)

#define and itemize just like a get but with a map query
MyMaker=MakerClass(
	).itemize(
		#ItemizingKeyVariable
		'map*make',
		#ItemizingMapGetVariable
		_MapGetVariable=['MadeMyInt','MakingMyFloat']
	)

#show the map
print("MyMaker.ItemizedValueMethod([3.,6.]).ItemizedMapVariablesList is ")
print(MyMaker.ItemizedValueMethod([3.,6.]).ItemizedMapVariablesList)

