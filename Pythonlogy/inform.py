#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Guiders import Informer

#Definition an Informer instance
MyInformer=Informer.InformerClass(
	_InformingSubReadmeIsBool=True,
	_InformingConceptReadmeIsBool=True,
	_InformingDocumentIsBool=True,
	_InformingConceptSlideIsBool=True,
	**{}
)

#map
map(
	MyInformer.inform,
	map(
		lambda __ConceptStr:
		SYS.PythonlogyLocalFolderPathStr+'ShareYourSystem/'+__ConceptStr,
		[
			'Objects',
			'Classors',
			'Guiders',
			'Interfacers',
			'Itemizers',
			'Applyiers',
			'Noders',
			'Walkers',
			'Storers',
			'Databasers',
			'Simulaters',
			
			#'Ploters',
			#'Tutorials',
			#'Muzikers',
			
		]
	)
)
