import pandas as pd
import matplotlib.pyplot as plt

data = [
    ("2025/06", 1218),
    ("2024/11", 1280),
    ("2023/09", 1244),
    ("2023/01", 1278),
    ("2022/07", 1301),
    ("2021/07", 1276),
    ("2020/07", 1201),
    ("2019/07", 1160),
    ("2018/08", 1118),
    ("2017/07", 1077),
    ("2016/07", 1030),
    ("2015/07", 974)
]

df = pd.DataFrame(data, columns=["Date", "Number of Journals"])
df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m')
df = df.sort_values("Date")

plt.rcParams['font.family'] = 'serif'
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Number of Journals'], marker='o', linestyle='-', color='k')
plt.xlabel('Year', labelpad=15)
plt.ylabel('Number of Journals Indexed by ERIC', labelpad=15)
plt.grid(False)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('figure1.png', dpi=1200, format='png')
