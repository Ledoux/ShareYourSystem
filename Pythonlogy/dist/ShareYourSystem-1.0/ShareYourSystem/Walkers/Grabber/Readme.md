
#Grabber
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Grabber




```python

#ImportModules
import ShareYourSystem as SYS

from ShareYourSystem.Walkers import Grabber

#Definition a Grabber instance that has Tree nodes
MyGrabber=Grabber.GrabberClass().update(
        [
            (
                '<Tree>FirstChildGrabber',
                Grabber.GrabberClass().update(
                    [
                        (
                            '<Tree>GrandChildGrabber',
                            Grabber.GrabberClass()
                        )
                    ]
                )
            ),
            (
                '<Tree>SecondChildGrabber',
                Grabber.GrabberClass()
            )
        ]
    )

#Grab
MyGrabber.grab("Tree",['NodedTreeInt','NodedTreeKeyStr'])

#Definition the AttestedStr
SYS._attest(
    [
        'MyGrabber is '+SYS._str(
        MyGrabber,
        **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False
        }
        )
    ]
)

#Print



```


```console
>>>
Doer l.132 : DoerStr is Visiter
DoStr is Visit
DoMethodStr is visit
DoingStr is Visiting
DoneStr is Visited

Doer l.132 : DoerStr is Recruiter
DoStr is Recruit
DoMethodStr is recruit
DoingStr is Recruiting
DoneStr is Recruit

Doer l.132 : DoerStr is Mobilizer
DoStr is Mobilize
DoMethodStr is mobilize
DoingStr is Mobilizing
DoneStr is Mobilized

Doer l.132 : DoerStr is Router
DoStr is Route
DoMethodStr is route
DoingStr is Routing
DoneStr is Routed

Doer l.132 : DoerStr is Grabber
DoStr is Grab
DoMethodStr is grab
DoingStr is Grabbing
DoneStr is Grabbed



*****Start of the Attest *****

MyGrabber is < (GrabberClass), 4559025168>
   /{
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>IdString' : 4559025168
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildGrabber' : < (GrabberClass), 4559027088>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>IdString' : 4559027088
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildGrabber
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (GrabberClass),
4559025168>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4559125176>
   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'GrandChildGrabber' : < (GrabberClass), 4559028048>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /   /   /  '<New><Instance>IdString' : 4559028048
   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /  '<New><Instance>NodeKeyStr' : GrandChildGrabber
   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(GrabberClass), 4559027088>
   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4559124880>
   /   /   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Class>GrabbedVariablesOrderedDict' : None
   /   /   /   /   /  '<Spe><Class>GrabbingNodeStr' : None
   /   /   /   /   /  '<Spe><Class>GrabbingPickVariablesList' : None
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<Spe><Class>GrabbedVariablesOrderedDict' : None
   /   /   /  '<Spe><Class>GrabbingNodeStr' : None
   /   /   /  '<Spe><Class>GrabbingPickVariablesList' : None
   /   /   /}
   /   /  'SecondChildGrabber' : < (GrabberClass), 4559075088>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>IdString' : 4559075088
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildGrabber
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (GrabberClass),
4559025168>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4559125176>
   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Class>GrabbedVariablesOrderedDict' : None
   /   /   /  '<Spe><Class>GrabbingNodeStr' : None
   /   /   /  '<Spe><Class>GrabbingPickVariablesList' : None
   /   /   /}
   /   /}
   /  '<Spe><Instance>GrabbedVariablesOrderedDict' :
   /   /{
   /   /  'NodedTreeInt' : None
   /   /  'NodedTreeKeyStr' : None
   /   /  '0' :
   /   /   /{
   /   /   /  'NodedTreeInt' : None
   /   /   /  'NodedTreeKeyStr' : None
   /   /   /  '1' :
   /   /   /   /{
   /   /   /   /  'NodedTreeInt' : None
   /   /   /   /  'NodedTreeKeyStr' : None
   /   /   /   /}
   /   /   /}
   /   /  '2' :
   /   /   /{
   /   /   /  'NodedTreeInt' : None
   /   /   /  'NodedTreeKeyStr' : None
   /   /   /}
   /   /}
   /  '<Spe><Instance>GrabbingNodeStr' : Tree
   /  '<Spe><Instance>GrabbingPickVariablesList' : ['NodedTreeInt',
'NodedTreeKeyStr']
   /}

*****End of the Attest *****



```

