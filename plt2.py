import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
holmes = pd.read_csv('./results/Holmes_results.csv')
rf = pd.read_csv('./results/RF_results.csv')

# 设置横坐标（20, 30, ..., 100）
x = list(range(20, 101, 10))

# 四个指标名称
metrics = ['Accuracy', 'Precision', 'Recall', 'F1-score']

for metric in metrics:
    plt.figure(figsize=(8, 6))
    plt.plot(x, holmes[metric], marker='o', label='Holmes')
    plt.plot(x, rf[metric], marker='s', label='RF')

    # 美化图像
    plt.title(f'Model Comparison: {metric}')
    plt.xlabel('Traffic Percentage (%)')
    plt.ylabel(metric)
    plt.ylim(0.2, 1.0)
    plt.xticks(x)  # 显示每个百分比
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()

    # 保存图像
    plt.savefig(f'compare_{metric}.png', dpi=300)
    plt.show()