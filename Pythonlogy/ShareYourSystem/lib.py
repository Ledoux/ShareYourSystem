#Definition Python Modules
from distutils.core import setup
from distutils.command.install import install
import os
import sys
import importlib

RequirePackageDict={
	#'inflect':'sudo pip install inflect',
	#'yaml':'sudo pip install pyyaml',
	#'pymongo':'sudo pip install pymongo',
	#'tables':'sudo pip install tables',
	#'brian2':'sudo pip install brian2'
}

#Define
class InstallClass(install):

	def run(self):

		#for
		for __RequirePackageModuleStr,__RequirePackagePipStr in RequirePackageDict.items():

			try:

				#import
				importlib.import_module(__RequirePackageModuleStr)
				
			except:

				#print
				print(__RequirePackageModuleStr+' is not installed...')
				print('... so we try to pip install it')

				#system
				os.system(__RequirePackagePipStr)

		#call the base method
		install.run(self)

#Execute a Setup
setup(

		#Author properties
		author='Erwan Ledoux',
		author_email='erwan.ledoux@ens.fr',

		#Application properties
		name='ShareYourSystem',
		version='0.0.0',
		url='http://shareyoursystem.ouvaton.org',

		#Commnd
		cmdclass={'install': InstallClass},

		#Packages properties
		packages=[
					'ShareYourSystem',
			 		'ShareYourSystem.Standards.Classors.Classor',
			 		'ShareYourSystem.Standards.Classors.Defaultor',
			 		'ShareYourSystem.Standards.Classors.Doer',
			 		'ShareYourSystem.Standards.Interfacers.Interfacer',
			 		'ShareYourSystem.Standards.Interfacers.Printer',
			 		'ShareYourSystem.Standards.Interfacers.Debugger',
			 		'ShareYourSystem.Standards.Classors.Deriver',
			 		'ShareYourSystem.Standards.Classors.Inspecter',
			 		'ShareYourSystem.Standards.Classors.Propertiser',
			 		'ShareYourSystem.Standards.Tutorials.Incrementer',
			 		'ShareYourSystem.Standards.Classors.Attester',
			 		'ShareYourSystem.Standards.Tutorials.Decrementer',
			 		'ShareYourSystem.Standards.Classors.Tester',
			 		'ShareYourSystem.Standards.Classors.Observer',
			 		'ShareYourSystem.Standards.Classors.Binder',
			 		'ShareYourSystem.Standards.Classors.Watcher',
			 		'ShareYourSystem.Standards.Classors.Switcher',
			 		'ShareYourSystem.Standards.Classors.Mimicker',
			 		'ShareYourSystem.Standards.Classors.Classer',
			 		'ShareYourSystem.Standards.Itemizers.Itemizer',
			 		'ShareYourSystem.Standards.Itemizers.Getter',
			 		'ShareYourSystem.Standards.Itemizers.Setter',
			 		'ShareYourSystem.Standards.Itemizers.Executer',
			 		'ShareYourSystem.Standards.Itemizers.Conditioner',
			 		'ShareYourSystem.Standards.Itemizers.Arrayer',
			 		'ShareYourSystem.Standards.Itemizers.Pather',
			 		'ShareYourSystem.Standards.Itemizers.Commander',
			 		'ShareYourSystem.Standards.Itemizers.Pointer',
			 		'ShareYourSystem.Standards.Itemizers.Teamer',
			 		'ShareYourSystem.Standards.Itemizers.Manager',
			 		'ShareYourSystem.Standards.Itemizers.Parenter',
			 		'ShareYourSystem.Standards.Interfacers.Folderer',
			 		'ShareYourSystem.Standards.Interfacers.Filer',
			 		'ShareYourSystem.Standards.Interfacers.Processer',
			 		'ShareYourSystem.Standards.Interfacers.Pymongoer',
			 		'ShareYourSystem.Standards.Interfacers.Hdformater',
			 		'ShareYourSystem.Standards.Controllers.Controller',
			 		'ShareYourSystem.Standards.Modelers.Modeler',
			 		'ShareYourSystem.Standards.Modelers.Tabularer',
			 		'ShareYourSystem.Standards.Modelers.Tabler',
			 		'ShareYourSystem.Standards.Modelers.Rower',
			 		'ShareYourSystem.Standards.Modelers.Inserter',
			 		#'ShareYourSystem.Standards.Controllers.Organizer',
			 		#'ShareYourSystem.Standards.Controllers.Storer',
			 		'ShareYourSystem.Standards.Classors',
			 		'ShareYourSystem.Standards.Interfacers',
			 		'ShareYourSystem.Standards.Tutorials',
			 		'ShareYourSystem.Standards.Itemizers',
			 		'ShareYourSystem.Standards.Controllers',
			 		'ShareYourSystem.Standards.Modelers',
			 		'ShareYourSystem.Standards',
			 		
			 		
			 	]
			 ,

      	package_data={
          'ShareYourSystem':[
          		'Package.json'
          ]
		},

    )

"""
			 		'ShareYourSystem.Standards.Interfacers.Packager',
			 		'ShareYourSystem.Standards.Interfacers.Consoler',
			 		'ShareYourSystem.Standards.Interfacers.Deployer',
			 		'ShareYourSystem.Standards.Interfacers.Capturer',
			 		'ShareYourSystem.Standards.Interfacers.Processer',
			 		'ShareYourSystem.Standards.Interfacers.Directer',
			 		'ShareYourSystem.Standards.Interfacers.Swiger',
			 		'ShareYourSystem.Standards.Guiders.Guider',
			 		'ShareYourSystem.Standards.Guiders.Scriptbooker',
			 		'ShareYourSystem.Standards.Guiders.Celler',
			 		'ShareYourSystem.Standards.Guiders.Notebooker',
			 		'ShareYourSystem.Standards.Guiders.Nbconverter',
			 		'ShareYourSystem.Standards.Guiders.Installer',
			 		'ShareYourSystem.Standards.Guiders.Documenter',



			 		'ShareYourSystem.Standards.Controllers.Controller',
			 		'ShareYourSystem.Standards.Controllers.Organizer',
			 		'ShareYourSystem.Standards.Controllers.Storer',
			 		'ShareYourSystem.Standards.Modelers.Modeler',
			 		'ShareYourSystem.Standards.Modelers.Tabularer',
			 		'ShareYourSystem.Standards.Modelers.Tabler',
			 		'ShareYourSystem.Standards.Modelers.Rower',
			 		'ShareYourSystem.Standards.Modelers.Inserter',
			 		'ShareYourSystem.Standards.Modelers.Retriever',
			 		'ShareYourSystem.Standards.Modelers.Findoer',
			 		'ShareYourSystem.Standards.Modelers.Recoverer',
			 		'ShareYourSystem.Standards.Modelers.Shaper',
			 		'ShareYourSystem.Standards.Modelers.Merger',
			 		'ShareYourSystem.Standards.Modelers.Joiner',
			 		'ShareYourSystem.Standards.Modelers.Hierarchizer',
			 		'ShareYourSystem.Standards.Interfacers',
			 		'ShareYourSystem.Standards.Classors',
			 		'ShareYourSystem.Standards.Tutorials',
			 		'ShareYourSystem.Standards.Functers',
			 		'ShareYourSystem.Standards.Interfacers',
			 		'ShareYourSystem.Standards.Guiders',
			 		'ShareYourSystem.Standards.Itemizers',
			 		'ShareYourSystem.Standards.Teamers',
			 		'ShareYourSystem.Standards.Controllers',
			 		'ShareYourSystem.Standards.Modelers',
			 		'ShareYourSystem.Standards'
			 		#'ShareYourSystem.Specials.Simulaters.Simulater',
			 		#'ShareYourSystem.Standards.Simulaters'
			 		#'ShareYourSystem.Standards'
"""

"""
			 		
			 		'ShareYourSystem.Standards.Modelers.Databaser',
			 		'ShareYourSystem.Standards.Modelers.Modeler',
			 		'ShareYourSystem.Standards.Modelers.Tabularer',
			 		'ShareYourSystem.Standards.Modelers.Tabler',
			 		'ShareYourSystem.Standards.Modelers.Rower',
			 		'ShareYourSystem.Standards.Modelers.Inserter',
			 		'ShareYourSystem.Standards.Modelers.Retriever',
			 		'ShareYourSystem.Standards.Modelers.Findoer',
			 		'ShareYourSystem.Standards.Modelers.Recoverer',
			 		'ShareYourSystem.Standards.Modelers.Shaper',
			 		'ShareYourSystem.Standards.Modelers.Merger',
			 		'ShareYourSystem.Standards.Modelers.Joiner',
			 		'ShareYourSystem.Standards.Modelers.Hierarchizer',
			 		'ShareYourSystem.Standards.Viewers.Viewer',
			 		'ShareYourSystem.Standards.Viewers.Texter',
			 		'ShareYourSystem.Standards.Viewers.Boxer',
			 		'ShareYourSystem.Standards.Viewers.Pyploter',
			 		'ShareYourSystem.Standards.Viewers.Ploter',
			 		'ShareYourSystem.Standards.Viewers.Axer',
			 		'ShareYourSystem.Standards.Viewers.Paneler',
			 		'ShareYourSystem.Standards.Viewers.Figurer',
			 		'ShareYourSystem.Standards.Controllers.Grider',
			 		'ShareYourSystem.Standards.Controllers.Explorer',
			 		'ShareYourSystem.Standards.Controllers.Meteorer',
			 		'ShareYourSystem.Standards.Controllers.Patcher',
			 		'ShareYourSystem.Standards.Controllers.Systemer',
			 		'ShareYourSystem.Standards.Tutorials.Incrementer',
			 		'ShareYourSystem.Standards.Tutorials.Decrementer',
			 		'ShareYourSystem.Standards.Tutorials.Multiplier',
			 		'ShareYourSystem.Standards.Tutorials.Sumer',
			 		'ShareYourSystem.Standards.Tutorials.Modulizer',
			 		'ShareYourSystem.Specials.Neuroners.Neuroner',
			 		'ShareYourSystem.Specials.Simulaters.Simulater',
			 		'ShareYourSystem.Specials.Simulaters.Matrixer',
			 		#'ShareYourSystem.Specials.Simulaters.Expresser',
			 		#'ShareYourSystem.Specials.Simulaters.Eulerer',
			 		#'ShareYourSystem.Specials.Simulaters.Integrater',
			 		'ShareYourSystem.Specials.Simulaters.Runner',
			 		'ShareYourSystem.Specials.Simulaters.Moniter',
			 		'ShareYourSystem.Specials.Simulaters.Populater',
			 		#'ShareYourSystem.Specials.Simulaters.Dynamizer',
			 		'ShareYourSystem.Specials.Simulaters.Rater',
			 		'ShareYourSystem.Specials.Simulaters.Brianer',
			 		'ShareYourSystem.Specials.Simulaters.Neurongrouper',
			 		'ShareYourSystem.Specials.Simulaters.Lifer',
			 		'ShareYourSystem.Specials.Simulaters.Synapser',
			 		#'ShareYourSystem.Specials.Simulaters.Pydelayer',
			 		#'ShareYourSystem.Specials.Simulaters.Equationer',
			 		#'ShareYourSystem.Specials.Simulaters.Leaker',
			 		'ShareYourSystem.Specials.Predicters.Predicter',
			 		'ShareYourSystem.Specials.Predicters.Predispiker',
			 		'ShareYourSystem.Specials.Muzikers.Muziker',
			 		'ShareYourSystem.Specials.Muzikers.Streamer',
			 		'ShareYourSystem.Specials.Muzikers.Vexflower',
			 		'ShareYourSystem.Specials.Muzikers.Permuter',
			 		'ShareYourSystem.Specials.Muzikers.Differenciater',
			 		'ShareYourSystem.Specials.Muzikers.Pooler',
			 		'ShareYourSystem.Specials.Muzikers.Scaler',
			 		'ShareYourSystem.Specials.Muzikers.Harmonizer',
			 		'ShareYourSystem.Standards.Interfacers',
			 		'ShareYourSystem.Standards.Classors',
			 		'ShareYourSystem.Standards.Functers',
			 		'ShareYourSystem.Standards.Interfacers',
			 		'ShareYourSystem.Standards.Guiders',
			 		'ShareYourSystem.Standards.Itemizers',
			 		'ShareYourSystem.Standards.Walkers',
			 		'ShareYourSystem.Standards.Noders',
			 		'ShareYourSystem.Standards.Parenters',
			 		'ShareYourSystem.Standards.Modelers',
			 		'ShareYourSystem.Standards.Viewers',
			 		'ShareYourSystem.Standards.Controllers',
			 		'ShareYourSystem.Standards',
			 		'ShareYourSystem.Specials.Neuroners',
			 		'ShareYourSystem.Specials.Simulaters',
			 		'ShareYourSystem.Specials.Muzikers',
			 		'ShareYourSystem.Specials.Diffusers',
			 		'ShareYourSystem.Specials'
"""