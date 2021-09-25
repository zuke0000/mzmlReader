import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring

file_name = 'small.pwiz.1.1.mzML'
full_file = os.path.abspath(os.path.join(file_name))

# dom = ET.parse(full_file)
# tree = ET.parse('small.pwiz.1.1.mzML')
#iter = tree.iter('chromatogramList')
#print(iter[0])


tree1 = ET.parse('small.pwiz.1.1.mzML')
root1 = tree1.getroot()

print ('test')

for stuff in root1.findall(".//chromatogramList"):
    print(stuff)