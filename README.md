#ShareYourSystem

ShareYourSystem is a scientific data-mining application based on a Python-Javascript hierarchic MVCframework (still under construction)

It proposes a meta object syntax for making a source code and classes ontology more directly human-readable, **[http://shareyoursystem.ouvaton.org/site/LibraryReference/Databasers](Model)** objects for synchronising mongo and hdf5 databases client and server-side, Viewer objects for their interactive UML repre-
sentation through a Meteor patch, Controller objects for establishing the inter-
face between models and views, communication between python and js instances and the scope level for defining parameter and result variables characterising your scientific system. Applications to research by wrapping scientific tools like Brian
for python neural networks simulations, vexflow/music21 for music analysis.


##Install the python packages

###Install

On a Terminal :
```bash
$ pip install ShareYourSystem
```

###Uninstall

On a Terminal :
```bash
$ pip uninstall ShareYourSystem
```

##Docs

1. Put yours markdowned files docs/
2. Set the mkdocs.yml to refer to these docs
3. On the ShareYourSystem-master dir, build your site (it updates the the site/ folder)
```bash
$ mkdocs build --clean
```
4. Deploy on your http server (It is Ouvaton for here)

##Meteor GUI

1. Put your meteor js files in Meteor/
2. Deploy your application on the meteor free test server (with your specific name, ie replace shareyoursystem by your app name). On the ShareYourSystem-master dir :
```
$ meteor deploy shareyoursystem.meteor.com
```

##Reveal Slides

1. Go in Convert your modules Docs into reveal html, on the ShareYourSystem-master dir :
```
$ python inform.py
```
2. Then deploy the html slides in the http server that you want. (Ouvaton for here)


