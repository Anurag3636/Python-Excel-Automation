import pandas as pd
import numpy as np
# praaactical of python with excel
data={
    'OrderID':range(101,151),
    'Date':pd.date_range(start='2026-01-01',periods=50),
    'Product':np.random.choice(['Laptop','Mouse','Keyboard','Monitor','CPU'],50),
    'Category':np.random.choice(['Hardware','Accessory'],50),
    'Unit_Sold':np.random.randint(1,20,50).astype(float),
    'Unit_Price':np.random.choice([1200,500,800,400,200],50),
    'Region':np.random.choice(['North','South','East','West'],50),
    'Tax_Rate':[18]*50
    }
df=pd.DataFrame(data)
df.loc[5,'Unit_Sold']=np.nan
df.loc[15,'Unit_Sold']=np.nan
df.loc[10,'Product']=np.nan
df.to_excel('Anurag_sales.xlsx',index=False)
df['Unit_Sold']=df['Unit_Sold'].fillna(0)
df['Total_price']=df['Unit_Sold']*df['Unit_Price']
df['Totalprice_GST']=df['Total_price']*(1+df['Tax_Rate'])
df.to_csv('Anurag.csv')
                                    


    
    
    
