# Lewis
Lewis Structure Generator for Simple Molecules

Lewis Structure Generator 
The goal of our computer science final project is to take in a simple molecule and draw the 
corresponding Lewis structure.  This was done with a series of functions and the turtle module. 
We split up the project in the following way: - 
Calculation:  Main goal was to create a list containing the elements, the number of elements and the 
bond type.  This list was [Electron domain, number of electron pairs on the central element, 
chemical symbol of central atom, [chemical symbol of second element, type of bond, 
number of electron pairs on the central atom]]. 
Note: The electron pairs were an internal mechanism required for some of the calculations 
on the calulation end. - 
Drawing:  Main goal was to take the list that the calculation section created from his code and use turtle to draw the 
structure of the given molecule.  Bonds were drawn by rotating by an angle each time it 
looped.  The angle was made by dividing 360 by the electron domain.  The elements were 
then drawn at the end of these bonds. 

The input must be a molecule which satisfies the following: - - - - - - 
Elements entered must be real elements 
Must be two elements only (not one, for example, H2 or CNO would not work) 
Central element cannot have more than one atom (for example, C2H6 would not work) 
Second element cannot have more than 6 atoms (for example, CH12 would not work) 
Molecule cannot be an ion (for example, (for example, SO4 would not work) 
Must be in proper chemical notation, first letter uppercase and second lowercase (for 
example Cl, cL or cl will not work) 
Attempting anything else will tell you that the molecule does not exist and will prompt you for a new 
molecule. To test, enter any valid molecule and compare the produced drawing to the real structure 
which can easily be found by googling or using an online Lewis structure generator.  
Note: our model does not include lone pairs, aka the dots 
