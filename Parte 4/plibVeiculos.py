#!/usr/bin/python3

#Matemática Computacional - Avaliação Prática (Parte 4)
#Feito por Pedro Gabriel de Morais Ribeiro (471550)

from mip import Model, xsum, minimize, BINARY, LinExpr
import numpy as np

#PARÂMETROS
Componentes = [1, 2, 3, 4]
Maquinas = ['A', 'B', 'C', 'D', 'E', 'F']
HorasFab = [[0.04, 0.02, 0.02, 0.0, 0.03, 0.06], [0.0, 0.01, 0.05, 0.15, 0.09, 0.06], [0.02, 0.06, 0.0, 0.06, 0.2, 0.2], [0.06, 0.04, 0.15, 0.0, 0.0, 0.05]]
CustoFabr = [2.55, 2.47, 4.4, 1.9]
CustoCompra = [3.1, 2.6, 4.5, 2.25]
Disponibilidade = 40
Demanda = 150

#MODELO
mod = Model("Avaliação Prática - Parte 4")

x = [mod.add_var(name = 'x', var_type = BINARY) for i in range(len(Componentes))]
y = [mod.add_var(name = 'y', var_type = BINARY) for i in range(len(Componentes))]

mod.objective = minimize(Demanda * xsum(CustoFabr[i] * x[i] + CustoCompra[i] * y[i] for i in range(len(Componentes))))

#RESTRIÇÕES
for i in range(len(Componentes)):
    mod += x[i] + y[i] == 1

for j in range(len(Maquinas)):
    mod += 150 * xsum(x[i] * HorasFab[i][j] for i in range(len(Componentes))) <= Disponibilidade

mod.optimize()

selected = [x[i].x for i in range(len(Componentes)) if x[i].x >= 0]

for i in range(len(Componentes)):
    print("Componente", Componentes[i], "foi", "fabricado." if selected[i] == 1 else "comprado.")

print("Valor ótimo: {}".format(mod.objective_value))

input()
