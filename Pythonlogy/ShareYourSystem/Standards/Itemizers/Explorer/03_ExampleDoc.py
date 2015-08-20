#ImportModules
import ShareYourSystem as SYS
import scipy.stats

#Define
@SYS.ClasserClass(**{
	'ClassingStructureVariable':[
		('Point','Points')
	]
})
class MakerClass(SYS.ExplorerClass):

	def default_init(
					self,
					_MakingCoordinateFloat = 0.,	
					_MadeDistanceFloat = 0., 													
					**_KwargVariablesDict
				):

		#Call the parent __init__ method
		SYS.ExplorerClass.__init__(self,**_KwargVariablesDict)

			
	def makeTop(self):
		
		#/################/#
		# Way to compute things
		#

		#compute
		self.MadeDistanceFloat = SYS.numpy.sqrt(
			sum(
				SYS.numpy.array(
					map(
						lambda __Variable:
						__Variable.MadeDistanceFloat,
						self.TeamDict['Points'].ManagementDict.values()
					)
				)**2
			)
		)

	def makePoint(self):
		
		#abs
		self.MadeDistanceFloat = abs(self.MakingCoordinateFloat)

	def exploreTop(self):

		#set
		return self.MadeDistanceFloat > self.MakingCoordinateFloat

	def explorePoint(self):

		#/################/#
		# Way to define the check
		#

		#set
		return self.MakingCoordinateFloat < self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable.MakingCoordinateFloat


#Definition 
ConeMaker=SYS.MakerClass(
	).mapSet(
		{
			"ExploringRangeVariable":{
				"MakingCoordinateFloat":lambda self:1.*scipy.stats.uniform.rvs()
			},
			"-Points":{
				"ManagingAfterSetVariable":{
					"ExploringRangeVariable":{
						"MakingCoordinateFloat":lambda self:-2.+4.*scipy.stats.uniform.rvs()
					}
				},
				"|X":{
				},
				"|Y":{
				}
			}
		}
	).explore(
		_MethodStr = 'make',
		_SuccessesInt = 1
	)

#print
print('ConeMaker is ')
SYS._print(ConeMaker)

"""
#show
map(
	lambda __TuplesList:
	SYS.plot(*list(dict(__TuplesList).values()),marker='o'),
	ConeMaker.ExploredStoreTuplesListsList
)
SYS.show()
"""