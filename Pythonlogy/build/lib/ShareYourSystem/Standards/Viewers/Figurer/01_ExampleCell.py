
#ImportModules
import ShareYourSystem as SYS
from matplotlib import pyplot
import pandas as pd
import numpy as np
import mpld3

#figure
MyFigurer=SYS.FigurerClass(
	).figure(
	)

# Define some CSS to control our custom labels
css = """
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
"""

#Define a sub axis in the figure
MyAxes=pyplot.gca()
MyAxes._figure=MyFigurer.FiguredPyplotVariable
MyAxes.grid(True, alpha=0.3)

#Define data to plot
N = 50
df = pd.DataFrame(index=range(N))
df['x'] = np.random.randn(N)
df['y'] = np.random.randn(N)
df['z'] = np.random.randn(N)
labels = []
for i in range(N):
	label = df.ix[[i], :].T
	label.columns = ['Row {0}'.format(i)]
	# .to_html() is unicode; so make leading 'u' go away with str()
	labels.append(str(label.to_html()))

#Define a Plot
Plot = MyAxes.plot(df.x, df.y, 'o', color='b',
                 mec='k', ms=15, mew=1, alpha=.6)
MyAxes.set_xlabel('x')
MyAxes.set_ylabel('y')
MyAxes.set_title('HTML tooltips', size=20)

#mpl3d plugins, connect and show
MyTooltip = mpld3.plugins.PointHTMLTooltip(
		Plot[0],labels,voffset=10, hoffset=10, css=css
)
mpld3.plugins.connect(MyFigurer.FiguredPyplotVariable,MyTooltip)
mpld3.show()
