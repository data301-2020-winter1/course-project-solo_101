import pandas as p
import numpy as np
import seaborn as sns
def Procces(path):
    data_chain_1 = (p.read_csv(path,encoding = 'ANSI')
     .rename(columns={'wgi_glacier_id':'Glacier ID','political_unit':'Country'})
     .dropna(subset = ['tongue_activity','mean_elev'])
     .reset_index()
    )
    data_chain_2 = (data_chain_1
                   .loc[:,['tongue_activity','Glacier ID','Country','continent_code','lat','lon','orientation_acc','orientation_abl','source_nourish','mean_elev']]
                   .reset_index()
                   )

    return data_chain_2 
