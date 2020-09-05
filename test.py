import csv
import dask.dataframe as ddf
import dask.multiprocessing

df_dask = ddf.read_csv('bpitool/score_data/playerdata_dpoverjoy.csv',parse_dates=True) 
df_dask = df_dask.compute()
display(df_dask.tail())
print(df_dask.info())