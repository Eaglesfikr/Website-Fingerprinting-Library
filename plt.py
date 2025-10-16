import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
df = pd.read_csv('results.csv')

# 设置横坐标（例如代表不同阶段或百分比）
x = range(1, len(df) + 1)

# 绘制四个指标
plt.figure(figsize=(8, 6))
plt.plot(x, df['Accuracy'], marker='o', label='Accuracy')
plt.plot(x, df['Precision'], marker='s', label='Precision')
plt.plot(x, df['Recall'], marker='^', label='Recall')
plt.plot(x, df['F1-score'], marker='d', label='F1-score')

# 美化图像
plt.title('Model Performance Metrics')
plt.xlabel('Progress Step')
plt.ylabel('Score')
plt.ylim(0.4, 1.0)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

# 保存或显示图像
plt.savefig('metrics_plot.png', dpi=300)
plt.show()
