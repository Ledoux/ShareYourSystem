
#ImportModules
import ShareYourSystem as SYS

#Definition an instance
MyNeuronGrouper=SYS.NeuronGrouperClass().run()
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyNeuronGrouper is '+SYS._str(
		MyNeuronGrouper,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 

#Print


"""
# Make a plot of x(t) vs x(t-tau):
# Sample the solution twice with a stepsize of dt=0.1:

# once in the interval [515, 1000]
sol1 = dde.sample(515, 1000, 0.1)
x1 = sol1['x']

# and once between [500, 1000-15]
sol2 = dde.sample(500, 1000-15, 0.1)
x2 = sol2['x']

pl.plot(x1, x2)
pl.xlabel('$x(t)$')
pl.ylabel('$x(t - 15)$')
pl.show()
"""