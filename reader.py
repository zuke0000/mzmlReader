import os
from bs4 import BeautifulSoup

file_name = 'small.pwiz.1.1.mzML'

with open('small.pwiz.1.1.mzML', 'r', ) as mzml_file:
  content = mzml_file.read() # Entire file at this point

  soup = BeautifulSoup(content, 'lxml') 
  tags = soup.find('mzML') # For some reason these tags don't seem to work. Do we need to do something extra for mzML?
  print(tags)

