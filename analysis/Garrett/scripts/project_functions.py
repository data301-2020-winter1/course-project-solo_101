import pandas as p
import numpy as np
import seaborn as sns

def Procces(path):
    #Renames a few columns and drops na valuesin tongue activity nad mean elevation
    data_chain_1 = (p.read_csv(path,encoding = 'ANSI')
     .rename(columns={'wgi_glacier_id':'Glacier ID','political_unit':'Country'})
     .dropna(subset = ['tongue_activity','mean_elev'])
     .reset_index()
    )
    #removes unwanted columns
    data_chain_2 = (data_chain_1
                   .loc[:,['tongue_activity','Glacier ID','Country','continent_code','lat','lon','orientation_acc','orientation_abl','source_nourish','mean_elev']]
                   .reset_index()
                   .drop(columns=['index'])
                   )
    #replaces country code with country name
    dat = data_chain_2.replace(['AF','AQ','AR','AT','BO','BT','CA','CH','CL','CN','CO','DE','EC','ES','FR','GL','GS','HM','ID','IN','IS','IT','KE','MX','NO','NP','NZ','PE','PK','SE','SU',
                              'TF','TZ','UG',
              'US','VE','ZA','ZR'],['Afghanistan','Antarctica','Argentina','Austria','Bolivia','Bhutan','Canada','Switzerland','Chile','China','Colombia','Germany','Ecuador','Spain',
              'France','Greenland','South georgia','Heard Island','Indonesia','India','Iceland','Italy','Kenya','Mexico','Norway','Nepal','New Zeland','Peru','Pakistan','Sweden','USSR',
              'French territ.','Tanzania','Uganda','United States','Venezuala', 'South Africa','Zaire'])
    return dat
