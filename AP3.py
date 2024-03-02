# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 12:48:35 2022

@author: Nithish Vengadesan

                    	Brown_Sugar	White_Sugar	Powder_Sugar	Treacle	  Rhs
Profit	                  130	      210	      250       	   50	
Brown_Sugar_Constraint  	1        	0	        0	            0	 1280
White_Sugar_Constraint   0.75	        1	        0           	0	  960
Powder_Sugar_Constraint	 0.71	     0.95	        1	            0	  912
Treacle_Constraint	        0	        0	        0	            1	  640
Min_BS_Constraint	       -1	        0	        0	            0	 -100
Min_WS_Constraint	        0	       -1	        0	            0	 -100

1 ton Sugar Syrup Processed to Produces 0.4 tons Brown_Sugar and 0.2 tons treacle
1 tonne of brown sugar Processed to produce 0.75 tonne of white sugar
1 tonne of white sugar processed to produce 0.95 tonne of powdered sugar

Avilability of Sugar Syrup per week 3200 tons

Variables:
    BS -> Brown_Sugar
    WS -> White_Sugar
    PS -> Powder_Sugar
    T  -> Treacle

Objective:
    Max(130BS+210WS+290PS+50T)
    
Constraints:
    BS,WS,PS,T  >= 100
    BS <= 1280
    T  <= 640
    WS <= 960-0.75BS
    PS <= 912-0.71BS-0.95WS

"""
import pandas as pd  # pandas is used to work with data frames
import pulp as pl  # library with an LP Solver is named as pl

# ********************   INPUT; prepare data***********************************

# Read data 
file_name='Problem.xlsx'
df = pd.read_excel(file_name, "Sheet3", index_col=0) # by default header=0, i.e. no need to create

# dictionary  
product = df.loc[df.index[0], df.columns[0:-1]].to_dict()
product
# constraint matrix from dataframe
constraint_matrix = pd.DataFrame(df, index=df.index[1:],
                                 columns=df.columns[0:-1]).to_dict('index')
constraint_matrix
#RHS associated with the constraints
rhs_coefficients = df.loc[df.index[1:], df.columns[-1]].to_dict()
rhs_coefficients


# ******************** MODEL **************************************************
# A "Linear Program" Model with "Maximisation" objective
model = pl.LpProblem("Sugar_Syrup", pl.LpMaximize)
model
# Creates a dictionary of variables. these are continuous varriables (default)

variables = pl.LpVariable.dicts('amount', product, lowBound=0)
variables
#Objective function
model += pl.lpSum([product[i]*variables[i] for i in product])

#Constraints to the model; format like Ax<=b
for c in rhs_coefficients:
    model += pl.lpSum(constraint_matrix[c][u]*variables[u]for u in product
                       ) <= rhs_coefficients[c], c  # c is constraint name

#Default solver
model.solve()  

# The status of the solution is printed to the screen
print("Status:", pl.LpStatus[model.status])

# The optimised objective function value is printed to the screen
print("Total Revenue = ", pl.value(model.objective))
# Each of the variables is printed with it's resolved optimum value
if (pl.LpStatus[model.status] == 'Optimal'):
    for v in model.variables():
        print(v.name, "=", v.varValue)

# The model is written to an .lp file
model.writeLP("Sugar_Syrup.lp")