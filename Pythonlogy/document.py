
#ImportModules
import ShareYourSystem as SYS

#Definition an Documenter instance
MyDocumenter=SYS.DocumenterClass(
	_DocumentingSubReadmeIsBool=True,
	_DocumentingConceptReadmeIsBool=True,
	_DocumentingDocumentIsBool=True,
	_DocumentingConceptSlideIsBool=True,
	**{}
)

#map
map(
	MyDocumenter.document,
	[
		'Classors',
		#'Guiders',
		#'Interfacers',
		#'Itemizers',
		#'Modelers',
		#'Viewers',
		#'Simulaters',
		#'Ploters',
		#'Tutorials',
		#'Muzikers',
		
	]
)