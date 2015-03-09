
#ImportModules
import ShareYourSystem as SYS
from matplotlib import pyplot
import pandas as pd
import numpy as np
import mpld3

#set the size
N=50
MyDataFrame=SYS.update(
        pd.DataFrame(index=range(N)),
        {
          'x':np.random.randn(N),
          'y':np.random.randn(N),
          'z':np.random.randn(N)
        }
      )

#figure
MyFigurer=SYS.FigurerClass(
  )['#map@set'](
    {
        'MyDataFrame':MyDataFrame,
        'FiguringDrawVariable':
        [
          (
            '#plot',
            {
              '#liarg:#map@get':['MyDataFrame.x','MyDataFrame.y'],
              '#kwarg':{
                'linestyle':"",
                'marker':'o',
                'color':'b',
                'mec':'k',
                'ms':15,
                'mew':1,
                'alpha':.6
              }
            }
          ),
          (
            '#axes',
            {
              'grid':{
                '#liarg':[True],
                '#kwarg':{'alpha':0.3}
              },
              'set_xlabel':'x',
              'set_ylabel':'y',
              'set_title':{
                '#liarg':['HTML tooltips'],
                '#kwarg':{'size':20}
              }
            }
          ),
          (
            '#mpld3.plugins.PointHTMLTooltip',
            {
              '#liarg':[
                        map(
                          lambda __IndexInt:
                          str(
                              SYS.set(
                                MyDataFrame.ix[[__IndexInt], :].T,
                                'columns',
                                ['Row {0}'.format(__IndexInt)]).to_html()
                              ),
                          xrange(N)
                        )
                      ],
              '#kwarg':{
                'voffset':10,
                'hoffset':10,
                'css':'''
                        table
                        {
                          border-collapse: collapse;
                        }
                        th
                        {
                          color: #ffffff;
                          background-color: #000000;
                        }
                        td
                        {
                          background-color: #cccccc;
                        }
                        table, th, td
                        {
                          font-family:Arial, Helvetica, sans-serif;
                          border: 1px solid black;
                          text-align: right;
                        }
                      '''
              }
            }
          )
        ]
    }
  )['?v']

#print
#print('MyFigurer.ViewedHtmlStr is ')
#print(MyFigurer.view().ViewedHtmlStr)
mpld3.show()
