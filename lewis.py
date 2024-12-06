'''
Tom Goldberg
Jack Robarge
CS 1210
The Most Amazing Lewis Structure Generator
'''

import turtle
import math

#dictionary of element with valence electrons and electronegativity 
valence_electrons = {
    "H": [1, 2.20],
    "He": [2, None],
    "Li": [1, 0.98],
    "Be": [2, 1.57],
    "B": [3, 2.04],
    "C": [4, 2.55],
    "N": [5, 3.04],
    "O": [6, 3.44],
    "F": [7, 3.98],
    "Ne": [8, None],
    "Na": [1, 0.93],
    "Mg": [2, 1.31],
    "Al": [3, 1.61],
    "Si": [4, 1.90],
    "P": [5, 2.19],
    "S": [6, 2.58],
    "Cl": [7, 3.16],
    "Ar": [8, None],
    "K": [1, 0.82],
    "Ca": [2, 1.00],
    "Sc": [2, 1.36],
    "Ti": [2, 1.54],
    "V": [2, 1.63],
    "Cr": [1, 1.66],
    "Mn": [2, 1.55],
    "Fe": [2, 1.83],
    "Co": [2, 1.88],
    "Ni": [2, 1.91],
    "Cu": [1, 1.90],
    "Zn": [2, 1.65],
    "Ga": [3, 1.81],
    "Ge": [4, 2.01],
    "As": [5, 2.18],
    "Se": [6, 2.55],
    "Br": [7, 2.96],
    "Kr": [8, 3.00],
    "Rb": [1, 0.82],
    "Sr": [2, 0.95],
    "Y": [2, 1.22],
    "Zr": [2, 1.33],
    "Nb": [2, 1.60],
    "Mo": [2, 2.16],
    "Tc": [2, 1.90],
    "Ru": [2, 2.20],
    "Rh": [2, 2.28],
    "Pd": [0, 2.20],
    "Ag": [1, 1.93],
    "Cd": [2, 1.69],
    "In": [3, 1.78],
    "Sn": [4, 1.96],
    "Sb": [5, 2.05],
    "Te": [6, 2.10],
    "I": [7, 2.66],
    "Xe": [8, 2.60],
    "Cs": [1, 0.79],
    "Ba": [2, 0.89],
    "La": [3, 1.10],
    "Ce": [3, 1.12],
    "Pr": [3, 1.13],
    "Nd": [3, 1.14],
    "Pm": [3, 1.13],
    "Sm": [3, 1.17],
    "Eu": [2, 1.20],
    "Gd": [3, 1.20],
    "Tb": [3, 1.10],
    "Dy": [3, 1.22],
    "Ho": [3, 1.23],
    "Er": [3, 1.24],
    "Tm": [3, 1.25],
    "Yb": [2, 1.10],
    "Lu": [3, 1.27],
    "Hf": [4, 1.30],
    "Ta": [5, 1.50],
    "W": [6, 2.36],
    "Re": [7, 1.90],
    "Os": [6, 2.20],
    "Ir": [6, 2.20],
    "Pt": [6, 2.28],
    "Au": [1, 2.54],
    "Hg": [2, 2.00],
    "Tl": [3, 1.62],
    "Pb": [4, 2.33],
    "Bi": [5, 2.02],
    "Po": [6, 2.00],
    "At": [7, 2.20],
    "Rn": [8, None],
    "Fr": [1, 0.70],
    "Ra": [2, 0.90],
    "Ac": [3, 1.10],
    "Th": [4, 1.30],
    "Pa": [5, 1.50],
    "U": [6, 1.38],
    "Np": [6, 1.36],
    "Pu": [6, 1.28],
    "Am": [6, 1.13],
    "Cm": [6, 1.28],
    "Bk": [6, 1.30],
    "Cf": [6, 1.30],
    "Es": [6, None],
    "Fm": [6, None],
    "Md": [6, None],
    "No": [6, None],
    "Lr": [6, None]
}

    
# generates dictionary of the seperate elements from string
def ele(molecule):
    n = ""
    lst = []
    cap = 'HLNKGRICTFMCBSPAYWZOVUX'
    for c in molecule:
        if c in cap:
            if n:
                lst.append(n)
                n = c
            else:
                n += c
        else:
            n += c    
    if n:
        lst.append(n)
    
    return lst

#generates dictionary of moles of elements
def oxi(mo):
    l = ele(mo)
    elec_num = {}
    for i in l:
        y = ""
        g = 0
        for x in i:
            if x not in "123456789":
                y += x
            else:
                g = int(x)
               
        elec_num[y] = g
        for key in elec_num.keys():
            if elec_num[key] == 0:
                elec_num[key] = 1

    return elec_num

# generates dictionary of valence electrons present
def val(e):
    formula = oxi(e)
    electrons = {}
    for key in formula.keys():
        x = formula[key]
        electrons[key] = x
        
    return electrons

# calculates central atom        
def central(v):
    valence = val(v)
    lew = []
    x = ""
    px = 10
    for key in valence.keys():
            if key != "H":
                y = valence_electrons[key][1]
                if y < px:
                    x = key
                    px = y
                    
    return x

# calculates number of electron domains 
def edom(a):
    d = oxi(a)
    x = 0
    for value in d.values():
        x += value
    return x - 1

# calculates actual max of electrons
def total(x):
    l = val(x)
    a = 0
    for key in l.keys():
        a += l[key] * valence_electrons[key][0]
    
    return a

#calculates theoretical max of electrons
def need(x):
    a = oxi(x)
    y = 0
    for key in a.keys():
        if key == "H":
            y += a[key] * 2
        else:
            y += a[key] * 8
    
    return y

#caculates number of bonds        
def bonds(x):
    v = total(x) 
    needed = need(x)
    bonds = (needed - v)/2
    lone = v - (bonds * 2)
   
    return [bonds, lone]

# calculates formal charge   
def fc(atom,n,b):
    return valence_electrons[atom][0] - n - b

#calculate sum of formal charges
def tot(x):
    y = 0
    for i in range(len(x)):
      a = fc(x[i][0], x[i][2] * 2, x[i][1])
      #x.append(a)
      y += a
      
    return y

# calculates current number of electrons being used 
def current_e(x):
    a = 0
    c = x[0][0]
    for i in range(len(x)):
        if x[i][0] == c:
            pass
        else:
            a += x[i][1]
        if x[i][2] < 0:
            pass
        else:
            a += x[i][2]
    
    return a

# figures out molecule shape and generates molecule data
def placer(x):
    a = oxi(x)
    n = []
    c = central(x)
    n.append([c])
    q = 1
    p = 10
    count = 0
    pab = abs(p)
# everything below this is chemistry magic, in short its a minimzation function but using chemistry rules
    for key in a.keys(): 
        if key != c:
            if valence_electrons[key][0] == 7:
                y = [key,1,3]
                n.append(y)
                q = 2
            else:
                for i in range(a[key]):
                    if key == "H":
                        y = [key,1,0]
                        n.append(y)
                    else:
                        y = [key,1,3]
                        n.append(y)
# start of minimazation section secondary stage    
    j = (len(n) - 1) * n[1][1]
    n[0].append(j)
    n[0].append(4 - j)
    while q == 1:
        if count < 5:
            if tot(n) != 0:
                if abs(tot(n)) < pab:
                    for t in range(len(n)):
                        n[t][1] += 1
                        n[t][2] += - 1
                    n[0][1] = n[1][1] * (len(n) -1)
                    n[0][2] = 4 - (n[1][1] * (len(n) -1))
                    p = tot(n)
                    pab = abs(p)
                    if bonds(x)[0] + (bonds(x)[1] / 2) == current_e(n):
                        pass
                    else:
                        pab += 1
                else:
                    q = 2
            else:
                q = 2
            count += 1
        else:
#             print("Molecule ouside of scope or does not exist")
#             inp = input("molecule formula:")
#             idiot(inp)
            n = 1
            q = 2
                
    return n

# generates list of data to give to draw function    
def info(a):
    x = placer(a)
    if x[0] == 1:
        lst = 1
    else:
        lst = [edom(a), x[0][2], central(a), x[1]]
    return lst

# draws single bond        
def single_bond():
    t.hideturtle()
    t.forward(5)
    
# draws double bond
def double_bond():
    t.hideturtle()
    t.forward(5)
    t.pu()
    t.right(90)
    t.forward(0.25)
    t.right(90)
    t.pd()
    t.forward(5)
    
# draws triple bond    
def triple_bond():
    t.hideturtle()
    t.forward(5)
    t.pu()
    t.right(90)
    t.forward(0.25)
    t.right(90)
    t.pd()
    t.forward(5)
    t.pu()
    t.right(90)
    t.forward(0.5)
    t.right(90)
    t.pd()
    t.forward(5)
    
# calculates the position of the outer elements
def coord(r,a):
# jimbo = x coord, also the reason jack understands CS
    jimbo = ((r * math.cos(math.radians(a))) + (math.cos((math.radians(a))) * 0.75)) - 0.2
    y = ((r * math.sin(math.radians(a))) + (math.sin((math.radians(a))) * 0.75)) - 0.5
    return jimbo, y

# draws the letter elements     
def element_draw(a):
    t.hideturtle()
    t.write(a)
    
# draws the full molecule    
def molecule_draw(x):
    if x == 1:
        turtle.close()
    else:
        angle = 360 / x[0]
        current_angle = 0
        t.pu()
        t.goto(-.2, -.5) 
        element_draw(x[2])
        t.goto(0.75, 0)
        r = 5.75
        if x[3][1] == 1:
            for i in range(x[0]):
                t.pd()
                single_bond()
                t.pu()
                t.goto(coord(r,current_angle)[0], coord(r,current_angle)[1])
                current_angle += angle
                element_draw(x[3][0])
                t.goto(0, 0)
                t.right(angle)
                t.forward(0.75)
                
        elif x[3][1] == 2:
            t.goto(0.75, 0.25)
            for i in range(x[0]):
                t.pd()
                double_bond()
                t.pu()
                t.right(180)
                t.forward(6)
                t.goto(coord(r,current_angle)[0], coord(r,current_angle)[1])
                current_angle += angle
                element_draw(x[3][0])
                t.goto(0, 0)
                t.right(angle)
                t.forward(0.75)
                
        elif x[3][1] == 3:
            for i in range(x[0]):
                t.pd()
                triple_bond()
                t.pu()
                t.goto(coord(r,current_angle)[0], coord(r,current_angle)[1])
                current_angle += angle
                element_draw(x[3][0])
                t.goto(0, 0)
                t.right(angle)
                t.forward(0.75)
        print("Structure Generated")
        turtle.done()
    
# Exception handling   
def idiot(x):
    fg = x
    b = 1
    while b == 1:
        try:
            a = 0
            formula = oxi(fg)
            electrons = {}
            for key in formula.keys():
                a += 1
                s = formula[key]
                electrons[key] = s
                
            assert a > 1 and a < 3
            
            for i in fg:
                assert i not in "67890"
            assert placer(fg) != 1
            b = 2
        except KeyError:
            print("Not a Valid Molecule")
            fg = input("molecule formula:")
            b = 1
        except AssertionError:
            print("Not a Valid Molecule for project scope")
            fg = input("molecule formula:")
            b = 1
#         turtle.setworldcoordinates(-30, -30, 30, 30)
#         t = turtle.Turtle()
#         turtle.delay(0)
#         print(molecule_draw(info((fg))))
    return fg
        
    
if __name__ == "__main__":
    intro = """Welcome to our Amazing Lewis Structure Generator(ALSG)!!

Here you will enter a valid molecular formula, and we will return the Lewis structure.

Keep in mind:
- Elements entered must be real elements.
- Must be two elements only (not one, for example, H2 or CNO would not work).
- The central element cannot have more than one atom (for example, C2H6 would not work).
- The second element cannot have more than 6 atoms (for example, CH12 would not work).
- The molecule cannot be an ion (for example, SO4 would not work).
- Must be in proper chemical notation, with the first letter uppercase and the second lowercase 
  (for example, Cl is correct, but cL or cl will not work).

"""
    print(intro)

    mole = input("Enter Valid Molecular Formula:")
    m = idiot(mole)
    turtle.setworldcoordinates(-30, -30, 30, 30)
    t = turtle.Turtle()
    turtle.delay(0)
    molecule_draw(info((m)))
    