#Definition Python Modules
from distutils.core import setup
import os

#Execute a Setup
setup(
		author='Erwan Ledoux',
		author_email='erwan.ledoux@ens.fr',
		name='ShareYourSystem',
		packages=[
					'ShareYourSystem',
			 		'ShareYourSystem.Objects.Object',
			 		'ShareYourSystem.Objects.Initiator',
			 		'ShareYourSystem.Classors.Classor',
			 		'ShareYourSystem.Classors.Defaultor',
			 		'ShareYourSystem.Classors.Doer',
			 		'ShareYourSystem.Classors.Deriver',
			 		'ShareYourSystem.Classors.Propertiser',
			 		'ShareYourSystem.Classors.Inspecter',
			 		'ShareYourSystem.Classors.Representer',
			 		'ShareYourSystem.Objects.Printer',
			 		'ShareYourSystem.Objects.Debugger',
			 		'ShareYourSystem.Functers.Functer',
			 		'ShareYourSystem.Objects.Packager',
			 		'ShareYourSystem.Classors.Attester',
			 		'ShareYourSystem.Classors.Tester',
			 		'ShareYourSystem.Functers.Functer',
			 		'ShareYourSystem.Functers.Hooker',
			 		'ShareYourSystem.Functers.Triggerer',
			 		'ShareYourSystem.Objects.Conditioner',
			 		'ShareYourSystem.Objects.Concluder',
			 		'ShareYourSystem.Classors.Observer',
			 		'ShareYourSystem.Classors.Binder',
			 		'ShareYourSystem.Classors.Watcher',
			 		'ShareYourSystem.Classors.Resetter',
			 		'ShareYourSystem.Classors.Switcher',
			 		'ShareYourSystem.Classors.Mimicker',
			 		'ShareYourSystem.Objects.Caller',
			 		'ShareYourSystem.Objects.Cloner',
			 		'ShareYourSystem.Classors.Classer',
			 		'ShareYourSystem.Objects.Rebooter',
			 		'ShareYourSystem.Functers.Argumenter',
			 		'ShareYourSystem.Functers.Imitater',
			 		'ShareYourSystem.Functers.Alerter',
			 		'ShareYourSystem.Interfacers.Interfacer',
			 		'ShareYourSystem.Interfacers.Folderer',
			 		'ShareYourSystem.Interfacers.Filer',
			 		'ShareYourSystem.Interfacers.Closer',
			 		'ShareYourSystem.Interfacers.Loader',
			 		'ShareYourSystem.Interfacers.Writer',
			 		'ShareYourSystem.Interfacers.Deployer',
			 		'ShareYourSystem.Interfacers.Hdformater',
			 		'ShareYourSystem.Interfacers.Capturer',
			 		'ShareYourSystem.Interfacers.Processer',
			 		'ShareYourSystem.Interfacers.Statuser',
			 		'ShareYourSystem.Interfacers.Killer',
			 		'ShareYourSystem.Interfacers.Directer',
			 		'ShareYourSystem.Guiders.Guider',
			 		'ShareYourSystem.Guiders.Scriptbooker',
			 		'ShareYourSystem.Guiders.Celler',
			 		'ShareYourSystem.Guiders.Notebooker',
			 		'ShareYourSystem.Guiders.Nbconverter',
			 		'ShareYourSystem.Guiders.Installer',
			 		'ShareYourSystem.Guiders.Informer',
			 		'ShareYourSystem.Guiders.Documenter',
			 		'ShareYourSystem.Itemizers.Itemizer',
			 		'ShareYourSystem.Itemizers.Getter',
			 		'ShareYourSystem.Itemizers.Setter',
			 		'ShareYourSystem.Itemizers.Deleter',
			 		'ShareYourSystem.Itemizers.Attributer',
			 		'ShareYourSystem.Itemizers.Restricter',
			 		'ShareYourSystem.Itemizers.Pather',
			 		'ShareYourSystem.Itemizers.Grasper',
			 		'ShareYourSystem.Itemizers.Sharer',
			 		'ShareYourSystem.Itemizers.Executer',
			 		'ShareYourSystem.Applyiers.Applyier',
			 		'ShareYourSystem.Applyiers.Mapper',
			 		'ShareYourSystem.Applyiers.Picker',
			 		'ShareYourSystem.Applyiers.Gatherer',
			 		'ShareYourSystem.Applyiers.Updater',
			 		'ShareYourSystem.Itemizers.Pointer',
			 		'ShareYourSystem.Applyiers.Linker',
			 		'ShareYourSystem.Applyiers.Weaver',
			 		'ShareYourSystem.Applyiers.Filterer',
			 		'ShareYourSystem.Noders.Noder',
			 		'ShareYourSystem.Functers.Outputer',
			 		'ShareYourSystem.Noders.Appender',
			 		'ShareYourSystem.Noders.Instancer',
			 		'ShareYourSystem.Noders.Adder',
			 		'ShareYourSystem.Noders.Distinguisher',
			 		'ShareYourSystem.Noders.Parenter',
			 		'ShareYourSystem.Noders.Collecter',
			 		'ShareYourSystem.Applyiers.Pusher',
			 		'ShareYourSystem.Applyiers.Producer',
			 		'ShareYourSystem.Noders.Catcher',
			 		'ShareYourSystem.Noders.Attentioner',
			 		'ShareYourSystem.Noders.Coupler',
			 		'ShareYourSystem.Noders.Settler',
			 		'ShareYourSystem.Applyiers.Commander',
			 		'ShareYourSystem.Walkers.Walker',
			 		'ShareYourSystem.Walkers.Cumulater',
			 		'ShareYourSystem.Walkers.Visiter',
			 		'ShareYourSystem.Walkers.Recruiter',
			 		'ShareYourSystem.Walkers.Mobilizer',
			 		'ShareYourSystem.Walkers.Router',
			 		'ShareYourSystem.Walkers.Grabber',
			 		'ShareYourSystem.Applyiers.Poker',
			 		'ShareYourSystem.Noders.Connecter',
			 		'ShareYourSystem.Noders.Networker',
			 		'ShareYourSystem.Noders.Transmitter',
			 		'ShareYourSystem.Noders.Grouper',
			 		'ShareYourSystem.Noders.Structurer',
			 		'ShareYourSystem.Noders.Organizer',
			 		'ShareYourSystem.Storers.Storer',
			 		'ShareYourSystem.Databasers',
			 		'ShareYourSystem.Databasers.Databaser',
			 		'ShareYourSystem.Databasers.Modeler',
			 		'ShareYourSystem.Databasers.Tabularer',
			 		'ShareYourSystem.Databasers.Tabler',
			 		'ShareYourSystem.Databasers.Rower',
			 		'ShareYourSystem.Databasers.Flusher',
			 		'ShareYourSystem.Databasers.Retriever',
			 		'ShareYourSystem.Databasers.Findoer',
			 		'ShareYourSystem.Databasers.Recoverer',
			 		'ShareYourSystem.Databasers.Shaper',
			 		'ShareYourSystem.Databasers.Merger',
			 		'ShareYourSystem.Databasers.Scanner',
			 		'ShareYourSystem.Databasers.Joiner',
			 		'ShareYourSystem.Databasers.Hierarchizer',
			 		'ShareYourSystem.Storers.Grider',
			 		'ShareYourSystem.Storers.Controller',
			 		'ShareYourSystem.Databasers.Featurer',
			 		'ShareYourSystem.Databasers.Recuperater',
			 		'ShareYourSystem.Ploters.Ploter',
			 		'ShareYourSystem.Ploters.Axer',
			 		'ShareYourSystem.Ploters.Paneler',
			 		'ShareYourSystem.Ploters.Figurer',
			 		'ShareYourSystem.Ploters.Pyploter',
			 		'ShareYourSystem.Tutorials.Incrementer',
			 		'ShareYourSystem.Tutorials.Decrementer',
			 		'ShareYourSystem.Tutorials.Multiplier',
			 		'ShareYourSystem.Tutorials.Sumer',
			 		'ShareYourSystem.Tutorials.Modulizer',
			 		'ShareYourSystem.Simulaters.Simulater',
			 		'ShareYourSystem.Simulaters.Runner',
			 		'ShareYourSystem.Simulaters.Moniter',
			 		'ShareYourSystem.Simulaters.Populater',
			 		'ShareYourSystem.Simulaters.Dynamizer',
			 		'ShareYourSystem.Simulaters.Lifer',
			 		'ShareYourSystem.Simulaters.Rater',
			 		'ShareYourSystem.Simulaters.Brianer',
			 		'ShareYourSystem.Simulaters.Pydelayer',
			 		'ShareYourSystem.Muzikers.Muziker',
			 		'ShareYourSystem.Muzikers.Vexflower',
			 		'ShareYourSystem.Muzikers.Permuter',
			 		'ShareYourSystem.Muzikers.Differenciater',
			 		'ShareYourSystem.Muzikers.Pooler',
			 		'ShareYourSystem.Muzikers.Harmonizer',
			 		'ShareYourSystem.Objects',
			 		'ShareYourSystem.Classors',
			 		'ShareYourSystem.Functers',
			 		'ShareYourSystem.Interfacers',
			 		'ShareYourSystem.Guiders',
			 		'ShareYourSystem.Itemizers',
			 		'ShareYourSystem.Applyiers',
			 		'ShareYourSystem.Walkers',
			 		'ShareYourSystem.Noders',
			 		'ShareYourSystem.Storers',
			 		'ShareYourSystem.Databasers',
			 		'ShareYourSystem.Ploters',
			 		'ShareYourSystem.Tutorials',
			 		'ShareYourSystem.Simulaters',
			 		'ShareYourSystem.Muzikers'
			 	]
			 ,
      	package_data={
          'ShareYourSystem':[
          		'Package.json'
          ]
		},
		url='http://shareyoursystem.ouvaton.org',
		version='1.0',
    )

