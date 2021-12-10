import numpy as np
from pymoo.core.problem import ElementwiseProblem


class Towers(ElementwiseProblem):

    def __init__(self, matrPob, rango, precio):
        self.M = len(matrPob)
        self.N = len(matrPob[0])
        super().__init__(n_var=self.N*self.M,
                         n_obj=2,
                         n_constr=0,
                         xl=0,
                         xu=1,
                         type_var=int)

    def __costo(self, x):
        pass

    def __poblacion(self, x):
        return 0

    def _evaluate(self, x, out, *args, **kwargs):
        out["F"] = [self.costo(x), - self.poblacion(x)]


problem = Towers(5, 8)
