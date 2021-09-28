import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring
from operator  import itemgetter

# Here's some weird documentation:
# https://www.coder.work/article/1004003
# Some more
# https://www.kite.com/python/examples/3506/xml-find-all-children-of-an-xml-element-that-match-a-tag

file_name = 'small.pwiz.1.1.mzML'
full_file = os.path.abspath(os.path.join(file_name))

# dom = ET.parse(full_file)
# tree = ET.parse('small.pwiz.1.1.mzML')
#iter = tree.iter('chromatogramList')
#print(iter[0])


tree1 = ET.parse('small.pwiz.1.1.mzML')
root1 = tree1.getroot()
s=tree1.findall('.//{http://psi.hupo.org/ms/mzml}chromatogramList')

print('what is my element', s)
for item in s:
    ET.dump(item)
# TODO: From here we need to grab specific element values and binary data.



#for stuff in range(len(s)):
  #   attribs = s[stuff].attrib
   # print(attribs)
