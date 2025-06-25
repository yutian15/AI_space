import argparse
from stochastic_model import NewsvendorStochasticModel
from utils import load_demand_samples

def main():
    parser = argparse.ArgumentParser(description="Stochastic Newsvendor Problem")
    parser.add_argument('--data', type=str, required=True, help='需求数据CSV文件路径')
    parser.add_argument('--c', type=float, default=1.0, help='进货成本价')
    parser.add_argument('--p', type=float, default=2.0, help='销售价')
    parser.add_argument('--s', type=float, default=0.5, help='回收价')
    args = parser.parse_args()

    demand_samples = load_demand_samples(args.data)
    model = NewsvendorStochasticModel(demand_samples, args.c, args.p, args.s)
    q_opt = model.solve()
    if q_opt is not None:
        print(f"最优订购量: {q_opt:.2f}")
    else:
        print("未找到最优解")

if __name__ == "__main__":
    main() 