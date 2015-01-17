LilypondPathString="/Applications/LilyPond.app/Contents/MacOS/LilyPond"

LilypondString="""
\version "2.12.3"
{
  c' e' g' a'
}
"""

import os
os.popen(LilypondPathString+' '+LilypondString)





