import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring
from operator  import itemgetter
from bs4 import BeautifulSoup

with open("small.pwiz.1.1.mzML") as fp:
    soup = BeautifulSoup(fp, 'lxml-xml')

soup = BeautifulSoup("<mzML></mzML>", 'lxml-xml')
print('what is soup', soup)
print('soup tag:', soup.tag)

# TODO: Extract binary data
# TODO: We'll also need other values such as zlib compression and base 64 decode

# file_name = 'small.pwiz.1.1.mzML'
# full_file = os.path.abspath(os.path.join(file_name))

#iter = tree.iter('chromatogramList')

# s=tree1.findall('.//{http://psi.hupo.org/ms/mzml}chromatogramList')

