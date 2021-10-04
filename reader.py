import os
from bs4 import BeautifulSoup

file_name = 'small.pwiz.1.1.mzML'

with open('small.pwiz.1.1.mzML', 'r', ) as mzml_file:
  content = mzml_file.read() # Entire file at this point

  soup = BeautifulSoup(content, 'lxml') 
  chromatogram = soup.find_all("chromatogram") # This seems to work for now. Idk why stuff like 'indexedmzML' or 'chromatogramList' dont work
  
  for entry in chromatogram:
    print('test')
  mzml_file.close
    