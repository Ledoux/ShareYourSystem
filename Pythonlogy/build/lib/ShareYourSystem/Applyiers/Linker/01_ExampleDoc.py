#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Itemizers import Pather
from ShareYourSystem.Applyiers import Linker

#Update several things
MyLinker=Linker.LinkerClass().update(
	map(
			lambda __Int:
			(str(__Int)+'Pather',Pather.PatherClass()),
			xrange(3)
		)
)

#link
MyLinker.link(
		map(
				lambda __Int:
				(str(__Int)+'Pather','/'+str(__Int-1)+'Pather/'+str(__Int)+'Pather') 
				if __Int>0
				else
				(str(0)+'Pather','/2Pather/0Pather'),
				xrange(3)
			)
		)

#Definition the AttestedStr
SYS._attest(
	[
		'MyLinker is '+SYS._str(
		MyLinker,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
)  

#Print

