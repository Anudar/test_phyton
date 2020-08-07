import pandas as pd
import numpy as np 
import re 
df = pd.read_excel('..\Szempontok_v3.xlsm',sheet_name='Szempontok')
df_reg = pd.read_excel('..\Szempontok_v3.xlsm',sheet_name='Regex')

for i in df.index:
    result=str(df['Eredeti szöveg'][i])
    for j in df_reg.index:
        replacing_string=re.search(df_reg['Expression'][j],result)
        if replacing_string is not None:
            result=re.sub(re.escape(replacing_string.group(0)),"",result)
    print(i,"-",result)
   



