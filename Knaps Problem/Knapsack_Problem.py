"""
Knaps problem using pyomo
Sajjad Ranjbar Yazdi

you can also see this code on my gitub account!
- https://github.com/Sajjad-s-presentations/Dynamic-Optimization/tree/main/Knaps%20Problem
"""

#liberary
from pyomo.environ import *

#inputs
Capacity = 106
weight = {'Bag1':300, 'Bag2':1, 'Bag3':200, 'Bag4':100, 'Bag5':10, 'Bag6':54}
value = {'Bag1':4000, 'Bag2':5000, 'Bag3':5000, 'Bag4':2000, 'Bag5':1000, 'Bag6':2834}

#set Pyomo:
M = ConcreteModel()
M.ITEMS = Set(initialize=value.keys())
M.x = Var(M.ITEMS, domain=Binary)

#Modeling problem:
M.value = Objective(expr=sum(value[i]*M.x[i] for i in M.ITEMS),sense=maximize)#Eq
M.weight = Constraint(expr=sum(weight[i]*M.x[i] for i in M.ITEMS) <=Capacity)#subject to...

#using GNU Linear Programming Kit solver:
solver = SolverFactory('glpk', executable='/usr/bin/glpsol')
solver.solve(M)

#print ultimate answer:
for i in value.keys():
    print('  ', i, ':', M.x[i]())
print("objective:",M.value())
