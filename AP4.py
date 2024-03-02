# -*- coding: utf-8 -*-
"""
@author: Nithish Vengadesan

        	    1       2   	3	     4	  Production
Demand	    45000	80000	65000	155000	      109000
Cost	       20	1.8			
Holdings	4000			          6000	

cost of producing Hard Drive = 20 rs/unit
Inventory cost of Storing hard drive per Quater = 1.8 rs/unit

Variables:
    x1-> Amount of production in 1st Quater
    x2-> Amount of Production in 2nd Quater
    x3-> Amount of Production in 3rd Quater
    x4-> Amount of Production in 4th Quater

Objective:Min(Cost)= Min(Cost of production + cost of inventory)
    Min(25.40*x1 + 23.6*x2 + 21.8*x3 + 20.0*x4 + -626400)

Constraints:
    x1>= 45000-(Previous Year Last Quater Inventory Stored) : x1>=41000
    x2+(x1-45000)>= 80000
    x3+(x2+x1-45000-80000)>= 65000
    x4+(x3+x2+x1-45000-80000-65000)>=155000+(Hard Drive to be hold for 1st quater of next year)
    x1,x2,x3,x4<=109000
    x1,x2,x3,x4>=0

"""

import pandas as pd  # pandas is used to work with data frames
import pulp as pl  # library with an LP Solver is named as pl
import numpy as np

# ********************   INPUT; prepare data***********************************

file_name='Problem.xlsx'
df = pd.read_excel(file_name, "Sheet4", index_col=0)
df

# ******************** MODEL **************************************************
# A "Linear Program" Model with "Minimisation" objective
model1 = pl.LpProblem("Hard_Drive_Production", pl.LpMinimize)

#Variable Declaration
x1 = pl.LpVariable("x1",lowBound=0, upBound = df.iloc[0]['Production'])
x2 = pl.LpVariable("x2",lowBound=0, upBound = df.iloc[0]['Production'])
x3 = pl.LpVariable("x3",lowBound=0, upBound = df.iloc[0]['Production'])
x4 = pl.LpVariable("x4",lowBound=0, upBound = df.iloc[0]['Production'])


#Objective
model1 += ((df.iloc[1][1]*(x1+x2+x3+x4)) +df.iloc[1][2]*(x1+df.iloc[2][1]-df.iloc[0][1]) 
           + df.iloc[1][2]*(x2+x1+df.iloc[2][1]-df.iloc[0][1]-df.iloc[0][2])
           +df.iloc[1][2]*(x2+x1+x3+df.iloc[2][1]-df.iloc[0][1]-df.iloc[0][2]-df.iloc[0][3]))


# Constraints
model1 += x1 >= df.iloc[0][1]-df.iloc[2][1]
model1 += x2+x1+df.iloc[2][1]-df.iloc[0][1] >= df.iloc[0][2]
model1 += x3+x2+x1+df.iloc[2][1]-df.iloc[0][1]-df.iloc[0][2] >= df.iloc[0][3]
model1 += x4+x3+x2+x1+df.iloc[2][1]-df.iloc[0][1]-df.iloc[0][2]-df.iloc[0][3] >= df.iloc[0][4]+df.iloc[2][4]
model1 += x1>=x4
model1 += x2>=x4
model1 += x3>=x4



model1.solve()  # solve the problem with the default solver



# The status of the solution is printed to the screen
print("Status:", pl.LpStatus[model1.status])

# The optimised objective function value is printed to the screen
print("Total cost spent = ", pl.value(model1.objective))

if (pl.LpStatus[model1.status] == 'Optimal'):
# Each of the variables is printed with it's resolved optimum value
    for v in model1.variables():
        print(v.name, "=", v.varValue)

#model1.writeLP("Hard_Drive_Production.lp")
