#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Classer
from ShareYourSystem.Storers import Grider
import numpy as np

#Define a Sumer class
@Classer.ClasserClass()
class SumerClass(Grider.GriderClass):

	#Definition
	RepresentingKeyStrsList=[
								'SumingFirstInt',
								'SumingSecondInt',
								'SumedTotalInt'
							]
								
	def default_init(self,
						_SumingFirstInt=0,
						_SumingSecondInt=0,
						_SumedTotalInt=0
					):

		#Call the parent init method
		self.__class__.__bases__[0].__init__(self)
		
	def do_sum(self):
		
		#set the SumedTotalInt
		self.SumedTotalInt=self.SumingFirstInt+self.SumingSecondInt

#Define a Factorizer class
@Classer.ClasserClass()
class FactorizerClass(Grider.GriderClass):

	#Definition
	RepresentingKeyStrsList=[
								'FactorizingPowerFloat',
								'FactorizedTotalFloat'
							]
								
	def default_init(self,
						_FactorizingPowerFloat=1.,
						_FactorizedTotalFloat=0.
					):

		#Call the parent init method
		self.__class__.__bases__[0].__init__(self)

		#Build the output hierarchy
		self.produce(
				['X','Y'],
				SumerClass,
				**{'CollectingCollectionStr':self.OrganizingComponentCollectionStr}
			)

	def do_factorize(self):

		#debug
		'''
		self.debug('We factorize here')
		'''

		#set the FactorizedTotalFloat
		self.FactorizedTotalFloat=np.power(
			sum(
				map(
					lambda __DeriveSumer:
					__DeriveSumer.SumedTotalInt,
					self[self.OrganizedComponentGetStr]
				)
			),
			self.FactorizingPowerFloat
		)

#Definition of a Factorizer 
MyFactorizer=FactorizerClass().__setitem__(
	"Dis_<Component>",
	[
		[
			(
				'GridingScanTuplesList',
				[
					('SumingFirstInt',[1]),
					('SumingSecondInt',[2,4])
				]
			),
		],
		[
			(
				'GridingScanTuplesList',
				[
					('SumingFirstInt',[0,1]),
					('SumingSecondInt',[3])
				]
			),
		],
	]
)

#grid
MyFactorizer.grid([('FactorizingPowerFloat',[1,2])])

#Definition the AttestedStr
SYS._attest(
	[
		'MyFactorizer is '+SYS._str(
		MyFactorizer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
		'hdf5 file is : '+MyFactorizer.hdfview().hdfclose().HdformatedStr
	]
) 

#Print