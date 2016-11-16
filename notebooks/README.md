README on ipython notebooks
============================


# Notebooks
---------------

## First tests to read CTIO images


- ViewfirstImage.ipynb : View file of the first ilage
- FirstSpectrum_fileno016.ipynb : Extract spectrum for the first image	
- Slide_FirstSpectrum.ipynb : Example of slides in ipython notebook

## Work on several images of the same object

- TestAugustinScripts.ipynb : test python tools from Augustin Guyonnet

- ViewDarkAndMaster.ipynb : View master file and flats

- OverscanAllImages.ipynb : Use overscan and trim tool from augustin G to generate trim images.

- ViewTrimImages.ipynb : View the trim images that were produced above
- MakeLogBook.ipynb : Build a logfile from header		


## Analysis

- ProcessTrimImages.ipynb : will work on produced trim images



## tool example for 2D histogram
- Histo2D.ipynb


## tool for using Hitran
- HitranData.ipynb		




# python tool libraries

## tools provided by Augustin Guyonnet
-----------------------------------


- used tool to find overscan, make subtraction of overscan and trimming 
of the images
			
overscan_subtract_andTrim.py

- utility tool used
skylev.py

- not used
compute.py


## tool provided by HITRAN
---------------------------

- very usefull interface to Hitran provided by hitran
hapi.py