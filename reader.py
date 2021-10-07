import os
from bs4 import BeautifulSoup

file_name = 'small.pwiz.1.1.mzML'
dictionaryList = [] # This will hold the dictionaries
dictionary = {"timeArray": 0, "intensityArray": 0, "zlibCompression": False}

with open('small.pwiz.1.1.mzML', 'r', ) as mzml_file:
  content = mzml_file.read() # Entire file at this point
  soup = BeautifulSoup(content, 'lxml') 
  chromatogram = soup.find_all("chromatogram")
  
  binaryCounter = 0
  for chromo in chromatogram:
      # For now I will assume the first binary data is time and the second is intensity
      # The way these values are grabbed could be smarter
    for children in chromo.find_all("binary"):
      if (binaryCounter == 0):
        dictionary['timeArray'] = children.text
      else: 
        dictionary['intensityArray'] = children.text
  mzml_file.close
print('dictionary', dictionary)
    