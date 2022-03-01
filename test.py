import pandas as pd
from pymysql import *
import pandas.io.sql as sql
import numpy as np
con=connect(user="cron",password="MTdkOTJhOGEw",host="136.243.37.207",database="asterisk")

# df_tra_dnc=sql.read_sql("""SELECT phone_number as Phone FROM vicidial_list WHERE `status`='TRA' OR `status` = 'DNC';""",con)

# print(df_tra_dnc)

df = pd.DataFrame(['2676673099','2176343088'])

df2 = pd.DataFrame(['2176343088'])

# print(df2)

ar_1 = df.to_numpy().flatten()
ar_2 = df2.to_numpy().flatten()


print(ar_1, ar_2)

array_difference = np.setdiff1d(ar_1, ar_2).reshape(-1)

print(array_difference)