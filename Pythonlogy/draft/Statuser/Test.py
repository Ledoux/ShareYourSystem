#<ImportSpecificModules>
from ShareYourSystem.Standards.Classors.Representer import _print
from ShareYourSystem.Standards.Objects import Markdowner
#</ImportSpecificModules>

#Print a version of the class
_print(dict(Markdowner.MarkdownerClass.__dict__.items()))

#Print a version of this object
_print(Markdowner.MarkdownerClass())

#Print a version of his __dict__
_print(Markdowner.MarkdownerClass().__dict__)

#Test
_print(Markdowner.attest_markdown(),**{'RepresentingAlineaIsBool':False})
