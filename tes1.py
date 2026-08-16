from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='whitegrid')
pd.set_option('display.max_columns', None)

#import fILE              
DATA_TRX = Path('studi_kasus_eda_penjualan.xlsx') 
assert DATA_TRX.exists(), 'File Not Found' 
print('Found!') 

#Read File
rf = pd.read_excel(
    DATA_TRX,
    sheet_name='Data Penjualan'
)

rf.head()

print('Jumlah Baris: ', rf.shape[0])
print('Jumlah Kolom: ', rf.shape[1])
print('Nama Kolom: ')
print(rf.columns.tolist())

# Melihat Type Data
rf.info()

# Melihat Nilai rata-rata
rf.describe().T

#EDA

#jumlah nilai Kosong
rf.isna().sum().to_frame('jumlah_kosong')

#Jumlah Nilai Duplicate
print('Jumlah Baris Duplikat', 
     rf.duplicated().sum(),
     rf[rf.duplicated(keep=False)].sort_values('id_transaksi'))
