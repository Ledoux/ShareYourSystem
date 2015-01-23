#<ImportSpecificModules>
from ShareYourSystem.Standards.Classors.Representer import _print
from ShareYourSystem.Standards.Objects import Picker
#</ImportSpecificModules>

#Print a version of the class
_print(dict(Picker.PickerClass.__dict__.items()))

#Print a version of this object
_print(Picker.PickerClass())

#Print a version of his __dict__
_print(Picker.PickerClass().__dict__)

#Test
_print(Picker.attest_pick(),**{'RepresentingAlineaIsBool':False})