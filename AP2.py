# -*- coding: utf-8 -*-
"""
@author: Nithish Vengadesan

Problem:
                    	TV	Radio	Magazine	Prize_Promotion	    Total 
Invested            	x1	x2	      x3	      x4	           210000
Return	                27	9          9	      11	
Spent_Constraints	70000	0.25(x1) 24000	    28000	
                	Max 	Min 	Min     	Max	
					
Variables: 
    x1-> Amount Spent on TV Advertising
    x2-> Amount Spent on Radio Advertising
    x3-> Amount Spent on Magazine Advertising
    x4-> Amount Spent on Prize

Objective: Max(27x1 + 9x2 + 9x3 + 11x4)

Constraints:
    x1+x2+x3+x4 <= 210000
    x1<=70000
    x2>= 0.25(x1)
    x3>= 24000
    x4<= 21000

"""
#Library Required
import pandas as pd  
import pulp as pl  

# ********************   INPUT; prepare data***********************************

file_name='Problem.xlsx'
df = pd.read_excel(file_name, "Sheet2", index_col=0)
df

# ******************** MODEL **************************************************
# A "Linear Program" Model with "Maximisation" objective

x1 = pl.LpVariable("x1",lowBound=0)
x2 = pl.LpVariable("x2",lowBound=0)
x3 = pl.LpVariable("x3",lowBound=0)
x4 = pl.LpVariable("x4",lowBound=0)

model1 = pl.LpProblem("Advertisment_Problem", pl.LpMaximize)

#objective
model1 += (df.iloc[1][0]*x1) + (df.iloc[1][1]*x2) + (df.iloc[1][2]*x3)  + (df.iloc[1][3]*x4)

#Constraints
model1 += x1+x2+x3+x4 <= df.iloc[0][4]
model1 += x1 <= df.iloc[2][0]
model1 += x2 >= df.iloc[2][1]*x1
model1 += x3 >= df.iloc[2][2]
model1 += x4 <= df.iloc[2][3]

model1.solve()



# The status of the solution 
print("Status:", pl.LpStatus[model1.status])

# The optimised objective function value is printed to the screen
print("Total Investment = ", pl.value(x1)+pl.value(x2)+pl.value(x3)+pl.value(x4))
print("Total Sales Increased = ", pl.value(model1.objective))

if (pl.LpStatus[model1.status] == 'Optimal'):
# Each of the variables is printed with it's resolved optimum value
    for v in model1.variables():
        print(v.name, "=", v.varValue)
        
# The model is written to an .lp file
model1.writeLP("Advertisment_Problem.lp")