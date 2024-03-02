# -*- coding: utf-8 -*-
"""
@author: Nithish Vengadesan

	x1r1	x1r2	x1l	x2r1	x2r2	x2l	x3r1	x3r2	x3l	x4r1	x4r2	x4l	RHS
Objective	5.5	2.5	2.5	9	6	6	6	3	3	9	6	6	
Production_Regular_Constarint1	-1	0	0	-1	0	0	-1	0	0	-1	0	0	-1500
Production_Regular_Constarint2	0	-1	0	0	-1	0	0	-1	0	0	-1	0	-1500
Production_Regular_Constarint3	0	0	-1	0	0	-1	0	0	-1	0	0	-1	-1500
Barrel_Constraint1	1	1	1	0	0	0	0	0	0	0	0	0	3000
Barrel_Constraint2	0	0	0	1	1	1	0	0	0	0	0	0	4000
Barrel_Constraint3	0	0	0	0	0	0	1	1	1	0	0	0	2000
Barrel_Constraint4	0	0	0	0	0	0	0	0	0	1	1	1	2500
Blending_Constraint1	-0.87	0	0	0.13	0	0	0.13	0	0	0.13	0	0	0
Blending_Constraint2	-0.07	0	0	0.93	0	0	-0.07	0	0	-0.07	0	0	0
Blending_Constraint3	0.07	0	0	0.07	0	0	-0.93	0	0	0.07	0	0	0
Blending_Constraint4	0	0.04	0	0	-0.96	0	0	0.04	0	0	0.04	0	0
Blending_Constraint5	0	-0.04	0	0	-0.04	0	0	0.96	0	0	-0.04	0	0
Blending_Constraint6	0	0.1	0	0	0.1	0	0	0.1	0	0	-0.9	0	0
Blending_Constraint7	0	0	0.06	0	0	0.06	0	0	-0.94	0	0	0.06	0
Blending_Constraint8	0	0	-0.04	0	0	-0.04	0	0	-0.04	0	0	0.96	0
Blending_Constraint9	0	0	-0.91	0	0	0.09	0	0	0.09	0	0	0.09	0


Varables:
    x1r1-> Amount of component 1 used in Regular Grade 1 petrol
    x1r2-> Amount of component 1 used in Regular Grade 2 petrol
    x1l -> Amount of component 1 used in Low Grade petrol
    x2r1-> Amount of component 2 used in Regular Grade 1 petrol
    x2r2-> Amount of component 2 used in Regular Grade 2 petrol
    x2l -> Amount of component 2 used in Low Grade petrol
    x3r1-> Amount of component 3 used in Regular Grade 1 petrol
    x3r2-> Amount of component 3 used in Regular Grade 2 petrol
    x3l -> Amount of component 3 used in low Grade  petrol
    x4r1-> Amount of component 4 used in Regular Grade 1 petrol
    x4r2-> Amount of component 4 used in Regular Grade 2 petrol
    x4l -> Amount of component 4 used in Low Grade  petrol
    
Objective:Max(Selling Price - cost Price)
    Max(5.5x1r1+9x2r1+6x3r11+9x4r1
        +2.5x1r1+6x2r2+3x3r2+6x4r2
        +2.5x1l+6x2l+3x3l+6x4l)

Constarints:
    Production Constrain:
        x1r1+x2r1+x3r1+x4r1 >= 1500
        x1r2+x2r2+x3r2+x4r2 >= 1500
        x1l+x2l+x3l+x4l >= 1500
    Barrel Constrain:
        x1r1+x1r2+x1l <= 3000
        x2r1+x2r2+x2l <= 4000
        x3r1+x3r2+x3l <= 2000
        x4r1+x4r2+x4l <= 2500
    Blending Constraint:
        0.87x1r1-0.13(x2r1+x3r1+x4r1)>=0
        0.93x2r1-0.07(x1r1+x3r1+x4r1)<=0
        0.93x3r1-0.13(x2r1+x1r1+x4r1)>=0
        0.96x2r2-0.04(x1r2+x3r2+x4r2)>=0
        0.96x3r2-0.04(x1r2+x2r2+x4r2)<=0
        0.90x4r2-0.04(x1r2+x3r2+x2r2)>=0
        0.94x3l-0.06(x1l+x2l+x4l)>=0
        0.96x4l-0.04(x1l+x2l+x3l)<=0
        0.91x1l-0.09(x3l+x2l+x4l)>=0
   
"""
#Library Required
import pandas as pd  
import pulp as pl  

# ********************   INPUT; prepare data***********************************


file_name='Problem.xlsx'
df = pd.read_excel(file_name, "Sheet5", index_col=0) # by default header=0, i.e. no need to create


product = df.loc[df.index[0], df.columns[0:-1]].to_dict()
product

constraint_matrix = pd.DataFrame(df, index=df.index[1:],
                                 columns=df.columns[0:-1]).to_dict('index')
constraint_matrix

rhs_coefficients = df.loc[df.index[1:], df.columns[-1]].to_dict()
rhs_coefficients


# ******************** MODEL **************************************************
# "Linear Program" Model with "Maximisation" objective

model1 = pl.LpProblem("Blending_Problem", pl.LpMaximize)
model1

#Variable Declaration
variables = pl.LpVariable.dicts('amount', product, lowBound=0)
variables

#Objective Function
model1 += pl.lpSum([product[i]*variables[i] for i in product])

# Constratint Declaration
for c in rhs_coefficients:
    model1 += pl.lpSum(constraint_matrix[c][u]*variables[u]for u in product
                       ) <= rhs_coefficients[c], c  # c is constraint name

model1.solve()  # solve the problem with the default solver

# The status of the solution is printed to the screen
print("Status:", pl.LpStatus[model1.status])

# The optimised objective function value is printed to the screen
print("Total Revenue = ", pl.value(model1.objective))
# Each of the variables is printed with it's resolved optimum value
if (pl.LpStatus[model1.status] == 'Optimal'):
    for v in model1.variables():
        print(v.name, "=", v.varValue)

## advanced; no need to use it in the assignment
# # #see https://realpython.com/linear-programming-python/
print('\n ADVANCED: Info about the constraints for the solution found')
for name, constraint in model1.constraints.items():
    print(f"{name}: {constraint.value():.2f}")

# The model is written to an .lp file
model1.writeLP("Blending_Problem.lp")
