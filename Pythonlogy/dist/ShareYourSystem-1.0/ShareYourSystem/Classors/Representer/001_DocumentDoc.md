
<!--
FrozenIsBool False
-->

#Representer

##Doc
----


> 
> The Representer is an important module for beginning to visualize 
> the structures of the instanced variables in the environnment.
> The idea is to use the indenting representation like in the json.dump
> function but with a more suitable (but maybe dirty) access to the 
> AlineaStr of each lines of the output, depending on the state 
> of the variables. Instances that are created from the decorated class have
> a __repr__ method, helping for mentionning for the represented attributes where
> do they come from : <Spe> (resp. <Base>) is they were defined at the level of the \_\_class\_\_ 
> and <Instance> (resp. <Class>) if they are getted from the <InstanceVariable>.__dict__ 
> (resp. <InstanceVariable>.__class__.__dict__)
> 
> 

----

<small>
View the Representer notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyoursystem.ouvaton.org/Representer.ipynb)
</small>

