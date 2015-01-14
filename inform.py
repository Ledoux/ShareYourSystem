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
		SYS.LocalPythonlogyFolderPathStr+'ShareYourSystem/'+__ConceptStr,
		[
			#'Objects',
			#'Classors',
			#'Interfacers',
			#'Itemizers',
			'Applyiers',
			#'Walkers',
			#'Noders',
			#'Savers',
			#'Databasers',
			#'Ploters',
			#'Tutorials',
			#'Simulaters',
			#'Muzikers',
			#'Guiders',
		]
	)
)
