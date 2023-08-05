# AcrePointSite 

Mock Site for Diego

# Color Scheme

Colors:
--dark-purple: #0d0221ff;
--dark-slate-gray: #2c514cff;
--taupe-gray: #857885ff;
--ghost-white: #fafaffff;
--seal-brown: #6a381fff;

# Django Apps

Apps:
Gallery -- photo gallery of jobs
Landing Page -- description of business
Consultation -- Forms for setting up Consultation

# ToDo
- Get Gallery working (see dg-README.md)
- Add footer

# Post-MVP
- Ensure that files exist b4 sending to client
- optimize querys (in Gallery IndexView, a better should be made to get all the data needed)
- Alter (in some way) the Gallery models s.t. the model fields accurately reflect the models' relationships
- improve JS efficency: run tests to see if it is better to query the dom, or to loop over small number of elements

# Notes

- loading in scripts after all other scripts (of the base.html file) may cause conflicts 
  you may want to load in jquery on a per app basis (by default) but, you may be able to use logic to prevent scripts from loading twice