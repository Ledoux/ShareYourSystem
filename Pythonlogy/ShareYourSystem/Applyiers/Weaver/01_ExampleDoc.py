#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Itemizers import Pointer
from ShareYourSystem.Applyiers import Weaver

#Update several things
MyWeaver=Weaver.WeaverClass().update(
	map(
			lambda __Int:
			(
				str(__Int)+'Pointer',
				Pointer.PointerClass()
			),
			xrange(3)
		)
).weave(
		map(
				lambda __Int:
				(
					[
						str(__Int)+'Pointer',
						str(__Int-1)+'Pointer',
					],
					str(__Int)+'-'+str(__Int-1)+'Pointer',
					Pointer.PointerClass()
				)
				if __Int>0
				else
				(
					[
						str(0)+'Pointer',
						str(2)+'Pointer',
					],
					str(0)+'-'+str(2)+'Pointer',
					Pointer.PointerClass()
				),
				xrange(3)
			)
		)
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyWeaver is '+SYS._str(
		MyWeaver,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
)  

#Print

