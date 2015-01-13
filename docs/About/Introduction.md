# ShareYourSystem 

What is the thing here :
ShareYourSystem would like to make deeper thinkings about :

1. what should be a good human readable syntax in Python for
sharing scientific objects. Hoping even for a mathematical 
demonstration like logic when rules of writing are clearly defined.
Here the syntax of "Doers" is chosen. The arguments for a certain scope of a class that will maybe then derived into an other class have a prefix string <Doing><VariableString>,
and controls the methods applications that set then instances <Done><VariableString> variables. Then a framework for decorating class (like a Propertizer for enhancing automatic binding in a process), methods (like a Hooker for calling synchronously a suite of hooked methods) and defining effective objects, is logically derived from this base of concept.

3. how can we build an object oriented frameworks leading to a LabView or MaxMsp ontology like helping for wrapping any kind of complex and specialized already developped python modules, like brian (for network simulations), music21 for music analysing, scikit...

3.	what should be the first way of sharing static files on 
repositories that automatically propose attests and tests and readme, thanks 
to the nb converter in ipython that can markdowns and deploy code,latex cells.

4. how to facilitate the scientific templating result attestations (following the pypet philosophy) with a hierarching model view controller framework based on client side "db like", like hdf5 and deploy data on django, 
mySQL more robust server side db. 
 
5.	how would participate to the work of annotating webs scientific proofs
mediated in public journals (and even scientific journals for which peer-review system exists 
but only at the lookup of the text and the figures, not at the code level), when blogs feedbacks systems straightforwardly
are quickly dived in the 'soup discussion problem'.
And avoiding also at the same time the spaghetti code problem if proofs
requires code writings, so here is a proposition : annotations like hypothesis and climate feedback project 
http://climatefeedback.org/ claimes to be could be decorated by direct Javacript API - Python mediated :
thanks to new js frameworks like Meteor for quickly settings reactive templates
of SVG or html objects that can helps for representing abstractions coded in python, a proof of a scientific result can be joined to a meteor web page where Client side Python processes can directly tests the attests.
But then comes the tricky question on how synchronizes python processes with js web pages... And here is not the expert place for deciding. For now, all the propositions are in the prototype process even waiting for the framework to be devleopped by other hackers.

	1.	The first simplest solution is thinking on a server side python tester, when statging on the meteor web page. In such a way :
	Meteor with the meteorite npm package for loading a python shell and a zerorpc TCP communication should be adapted. But here it gees for a sharing project at the level of a small team... Making crashing the server if too much python processes are running.

	2. Then comes more the idea of relieving the server by making the client running by itself the test codes...But here therefore special modules for testing should be installed by everyone. In that case, even the way to implement that is still tricky as long as a js page session cannot talk with a running python on the same computer for safety. 
	
		* But still, a ddp communication through our python or ipython notebook to set things on the server that will then callbacks for setting our session is possible thanks to pyddp (and possibly python-meteor but it's still apparently under development). 
		* Also, directly implementing a skulpt shell in the meteor page can possibly bring nice interactions.


