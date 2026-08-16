from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='whitegrid')
pd.set_option('display.max_columns', None)

FILE_EXCEL = Path('studi_kasus_eda_penjualan.xlsx')
assert FILE_EXCEL.exists(), `File Excel tidak di temukan`
print(`FILE terdeteksi`)

pd.read_excel()

