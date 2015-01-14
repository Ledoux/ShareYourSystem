

<!--
FrozenIsBool False
-->

#Tester

##Doc
----


>
> The Tester helps for defining asserts between
> attested Strs stored in the Attests Folder and
> new calls of the attest functions. Thanks here
> to a wrap of the unitest python module :
> https://docs.python.org/2/library/unittest.html
>
>

----

<small>
View the Tester notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyour
system.ouvaton.org/Tester.ipynb)
</small>




<!---
FrozenIsBool True
-->

##Example

The Incrementer from the previous Attester Module is now tested from its
corresponding attesting function
attest_increment. Here a test_increment method is implicitely defined in a
unittest class and when we call
the test method, a unittest.run is done.

```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Tester
from ShareYourSystem.Tutorials import Decrementer

#Attest the module
Decrementer.DecrementerClass().setAttest(
    Tester.TesterClass.DeriveClassor.AttestingFolderPathStr
)
Decrementer.test()

#Print



```


```console
>>>


```

