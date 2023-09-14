# AcrePointSite 

Django Site for Acre Point Cabinets

# Color Scheme


# Django Apps
Gallery -- photo gallery of jobs
Landing Page -- description of business
Consultation -- Forms for setting up Consultation

# ToDo
- Gallery Branch (see dg-README.md)
- Landing Page (see lp-README.md)

- Setup global theme variables 
- set the navbar to only display the logo and collapse button and a certain width
- use a more sophisticated font 
- Figure out which CSS is needed (remove excess)
- navbar collapse on scroll (or swipe)

# Post-MVP
- Ensure that files exist b4 sending to client
- lower quality of images when loading on small screens
- optimize querys (in Gallery IndexView, a better should be made to get all the data needed)
- Alter (in some way) the Gallery models s.t. the model fields accurately reflect the models' relationships
- improve JS efficency: run tests to see if it is better to query the dom, or to loop over small number of elements
- minify css files

# Notes
- loading in scripts after all other scripts (of the base.html file) may cause conflicts 
  you may want to load in jquery on a per app basis (by default) but, you may be able to use logic to prevent scripts from loading twice

- ALWAYS dump sql database before updating an existing model 
