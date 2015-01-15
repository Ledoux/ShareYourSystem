# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Databasers defines the Noders that take the role of 
the client-side "Model" in the MVC architecture of SYS. 
Here the databasing process relies on a hdf5 
pytable wrapping, going from simple encapsulations
of the create_table,flush methods to 'sophisticated'
routines that facilitate the joins between tables and 
the automatic shaping of the rowed datas.


"""

#<DefineConcept>
import ShareYourSystem as SYS
SYS.setConceptModule(globals())
#</DefineConcept>
