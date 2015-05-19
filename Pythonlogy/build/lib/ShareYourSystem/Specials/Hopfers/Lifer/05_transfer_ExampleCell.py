
#/###################/#
# Import modules
#

"""
#import
import ShareYourSystem as SYS

#define
MyLifer=SYS.LiferClass(
	).lif(
		_PerturbFrequencyFloat=10.
	)

#print
print('MyLifer is')
SYS._print(MyLifer)
"""

"""
#import
import ShareYourSystem as SYS

#define
MyLifer=SYS.LiferClass(
        ).lif(
        ).setAttr(
            'LifingStationaryBool',
            False
        )


MyLifer.LifingPerturbMethodStr="Hakim"
print(MyLifer)

#map
PerturbFrequencyFloatsArray=SYS.numpy.array(SYS.numpy.logspace(0,3,10));

#map
LifedPerturbMeanComplexesArray=SYS.numpy.array(
    map(
        lambda __PerturbFrequencyFloat:
        MyLifer.setAttr(
                'LifingPerturbFrequencyFloat',
                __PerturbFrequencyFloat
            ).lif(
            ).LifedPerturbMeanComplexVariable,
        PerturbFrequencyFloatsArray
    )
)

#plot
SYS.plot(
    PerturbFrequencyFloatsArray,
    abs(LifedPerturbMeanComplexesArray)/MyLifer.LifedStationaryRateFloat,
    '.-',linewidth=3,markersize=25
);
SYS.plot(
    [1.,100.],
    [MyLifer.LifedPerturbNullFloat/MyLifer.LifedStationaryRateFloat]*2,
    '--',linewidth=3,markersize=25
);
SYS.Axes.set_xscale('log')
SYS.show()
"""


#import
import ShareYourSystem as SYS


#define
MyLifer=SYS.LiferClass(
        )
MyLifer.LifingVoltageNoiseFloat=1.
MyLifer.LifingTotalStationaryCurrentFloat=-51.
MyLifer.lif(
        ).setAttr(
            'LifingStationaryBool',
            False
        )

#map
PerturbFrequencyFloatsArray=SYS.numpy.array(SYS.numpy.logspace(0,3,100));

#init
SYS.Figure=None

"""
#loop
for __PerturbMethodStr in [
                    #"Brunel",
                    "Hakim"
                ]:

    #map
    LifedPerturbMeanComplexesArray=SYS.numpy.array(
        map(
            lambda __PerturbFrequencyFloat:
            MyLifer.setAttr(
                    'LifingPerturbFrequencyFloat',
                    __PerturbFrequencyFloat
                ).lif(
                    _PerturbMethodStr=__PerturbMethodStr
                ).LifedPerturbMeanComplexVariable,
            PerturbFrequencyFloatsArray
        )
    )

    #plot
    SYS.plot(
        PerturbFrequencyFloatsArray,
        abs(LifedPerturbMeanComplexesArray),
        '.-',linewidth=3,markersize=25
    );
 
#init figure
SYS.plot(
    [1.,100.],
    [MyLifer.LifedPerturbNullFloat]*2,
    '--',linewidth=3,markersize=25
);
SYS.Axes.set_xscale('log')
SYS.show()
"""

MyLifer.LifedSwigVariable.DoubleDict['StationaryRate']=0.
print(MyLifer.LifedSwigVariable.DoubleDict['StationaryRate'])