

<!--
FrozenIsBool False
-->

#Attester

##Doc
----


>
> The Attester helps for outputing and writing
> AttestingPrefixStrs that are a succession of well-shaped
> prints in the console from an defined attesting function.
> This environment helps for displaying nicer exampling
> python codes in Readme and also contributing to unittests
> of the modules.
>
>

----

<small>
View the Attester notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyo
ursystem.ouvaton.org/Attester.ipynb)
</small>




<!---
FrozenIsBool True
-->

##Example

Here we just decorate an IncrementerClass with an Attester and define an
attest_increment
function in the module that for which an AttestingStr will be written in a local
Folder
Attests/

```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Attester
from ShareYourSystem.Tutorials import Incrementer

#Attest the module
Incrementer.IncrementerClass().setAttest(
    Attester.AttesterClass.DeriveClassor.AttestingFolderPathStr
)

#Definition the AttestedStr
SYS._attest(
    [
'Attests file is written and is '+open(
    Attester.AttesterClass.DeriveClassor.AttestingFolderPathStr+'attest_incremen
t.txt'
).read()
    ]
)

#Print


```


```console
>>>


*****Start of the Attest *****

Attests file is written and is 1

*****End of the Attest *****



```

