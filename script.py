from pybrain.datasets.supervised import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
#from pybrain.supervised.trainers.backprop import Back


D = SupervisedDataet(
	#2 inputs
	2,
	#1 target output
	1
)

D.addSample([0,0],[0])
D.addSample([0,1],[1])
D.addSample([1,0],[1])
D.addSample([1,1],[0])