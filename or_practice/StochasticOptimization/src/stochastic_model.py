import numpy as np
from pyscipopt import Model, quicksum

class NewsvendorStochasticModel:
    def __init__(self, demand_samples, c, p, s):
        """
        demand_samples: 历史需求样本（list 或 np.array）
        c: 进货成本价
        p: 售价
        s: 回收价
        """
        self.demand_samples = np.array(demand_samples)
        self.c = c
        self.p = p
        self.s = s
        self.model = Model("Stochastic Newsvendor")
        self._build_model()

    def _build_model(self):
        n = len(self.demand_samples)
        q = self.model.addVar(vtype="C", name="q")
        sold = []  # min(q, d_i)
        left = []  # max(q - d_i, 0)
        for i, d in enumerate(self.demand_samples):
            sold_i = self.model.addVar(vtype="C", name=f"sold_{i}")
            left_i = self.model.addVar(vtype="C", name=f"left_{i}")
            # sold_i <= q
            self.model.addCons(sold_i <= q)
            # sold_i <= d
            self.model.addCons(sold_i <= d)
            # sold_i >= 0
            self.model.addCons(sold_i >= 0)
            # sold_i >= q - left_i
            self.model.addCons(sold_i >= q - left_i)
            # left_i >= q - d
            self.model.addCons(left_i >= q - d)
            # left_i >= 0
            self.model.addCons(left_i >= 0)
            sold.append(sold_i)
            left.append(left_i)
        expected_profit = quicksum(
            self.p * sold[i] - self.c * q + self.s * left[i]
            for i in range(n)
        ) / n
        self.model.setObjective(expected_profit, sense="maximize")
        self.q = q

    def solve(self):
        self.model.optimize()
        if self.model.getStatus() == "optimal":
            return self.model.getVal(self.q)
        else:
            return None 