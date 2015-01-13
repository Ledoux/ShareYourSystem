
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Itemizers import Itemizer

class MakerClass(Itemizer.ItemizerClass):
	
	def __getitem__(self,_KeyVariable):

		#Debug
		print('_KeyVariable is ',_KeyVariable)
		print('')

		#return 
		return object.__getattribute__(self,
						'My'+str(_KeyVariable)+'Int'
					)

#Definition of a derive maker itemizer class
MyMaker=MakerClass()
MyMaker.My1Int=1
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyMaker is'+SYS._str(
			MyMaker,
			**{
				'RepresentingAlineaIsBool':False,
			}
		),
		'MyMaker[1] is '+str(MyMaker[1]),
		#'MyMaker.Item_1 is '+str(MyMaker.Item_1),
	]
) 

#Print

