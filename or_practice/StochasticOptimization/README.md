# 随机优化项目（Stochastic Optimization with SCIP）

## 项目简介
本项目旨在通过调用 SCIP 求解器，解决带有不确定性的数据下的随机优化问题。项目结构清晰，便于扩展和复现，适合科研与教学使用。

## 代码结构
```
@StochasticOptmization/
├── README.md                # 项目说明文档
├── data/                    # 存放带有不确定性的数据文件
├── src/                     # 主要代码实现
│   ├── main.py              # 项目主入口，读取数据并调用优化模型
│   ├── stochastic_model.py  # 随机优化建模与SCIP接口
│   └── utils.py             # 工具函数（如数据处理、结果分析等）
├── requirements.txt         # Python依赖包列表
└── examples/                # 示例与测试脚本
```

## data 文件夹说明
- 用于存放所有带有不确定性的数据文件（如 CSV、Excel、JSON 等）。
- 示例：`data/uncertain_params.csv`，每列为一个参数，每行为一次采样或场景。

## 依赖环境
- Python 3.8+
- [SCIP](https://www.scipopt.org/)（需提前安装并配置好 Python 接口，如 `pyscipopt`）
- 其他依赖见 `requirements.txt`

## 安装依赖
```bash
pip install -r requirements.txt
```

## 运行方法
1. 准备好不确定性数据，放入 `data/` 文件夹。
2. 配置好 SCIP 求解器及其 Python 接口（如 `pyscipopt`）。
3. 运行主程序：
   ```bash
   python src/main.py --data data/uncertain_params.csv
   ```
4. 可在 `examples/` 文件夹中查看和运行示例脚本。

## 主要功能
- 支持多种不确定性数据格式的读取与处理。
- 基于 SCIP 的随机优化建模与求解。
- 结果分析与可视化（可选）。

## 参考资料
- [SCIP 官方文档](https://www.scipopt.org/doc/html/)
- [PySCIPOpt 文档](https://github.com/SCIP-Interfaces/PySCIPOpt)

---
如需扩展其他随机优化算法或数据类型，请在 `src/` 目录下添加相应模块。 