# -*- coding: utf-8 -*-
"""
@author: Nithish Vengdesan
    	Machine_1	Machine_2	Machine_3	Profit
Product1	4	       2	       3	     95
Product2	2	       4	       2	     40
Total	   80	      80	     100	

Variables: p1 -> Product1, p2 -> Product2

Objective: max(95p1+40p2)

Constraints:
    4p1+2p2<=80
    2p1+4p2<=80
    3p1+2p2<=100
    p1,p2>=0
"""
# library Required
import pandas as pd  
import pulp as pl  

# ********************   INPUT; prepare data***********************************

file_name='Problem.xlsx'
df = pd.read_excel(file_name, "Sheet1", index_col=0)
df


product = df.loc[df.index[0:-1], df.columns[-1]].to_dict()
product

constraint_matrix = pd.DataFrame(
    df, index=df.index[0:-1], columns=df.columns[0:-1]).to_dict()

rhs_coefficients = df.loc[df.index[-1], df.columns[0:-1]].to_dict()

# ******************** MODEL **************************************************
# A "Linear Program" Model with "Maximisation" objective
model = pl.LpProblem("Factory_Problems", pl.LpMaximize)

#Variable declaration
variables = pl.LpVariable.dicts('Number_of', product, lowBound=0)

#Objective
model += pl.lpSum([product[i]*variables[i] for i in product])

#Constraints
for c in rhs_coefficients:  
    model += (pl.lpSum([constraint_matrix[c][u]*variables[u] for u in product]) 
        <= rhs_coefficients[c], c)

#Solve using Simple Solve
model.solve()

# The status of the solution is printed to the screen
print("Status:", pl.LpStatus[model.status])

# The optimised objective function value is printed to the screen
print("Total Revenue = ", pl.value(model.objective))

if (pl.LpStatus[model.status] == 'Optimal'):
# Each of the variables is printed with it's resolved optimum value
    for v in model.variables():
        print(v.name, "=", v.varValue)

# The model is written to an .lp file
model.writeLP("Advertisment_Problem.lp")