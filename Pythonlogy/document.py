#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Guiders import Documenter

#Definition an Documenter instance
MyDocumenter=Documenter.DocumenterClass(
	_DocumentingSubReadmeIsBool=True,
	_DocumentingConceptReadmeIsBool=True,
	_DocumentingDocumentIsBool=True,
	_DocumentingConceptSlideIsBool=True,
	**{}
)

#map
map(
	MyDocumenter.inform,
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
			'Controllers',
			'Modelers',
			'Viewers',
			'Simulaters',
			#'Ploters',
			#'Tutorials',
			#'Muzikers',
			
		]
	)
)
