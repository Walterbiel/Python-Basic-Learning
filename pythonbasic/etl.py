import pandas as pd
import os
import glob

#função extract json
def extrair_json(path:str):
    arquivos_json = glob.glob(os.path.join(path,'*.json'))
    #for arquivo in arquivos_json:
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    dftotal = pd.concat(df_list , ignore_index= True)
    return dftotal

#função que transforma
def calcular_total_vendas(df: pd.DataFrame):
    df["total"] = df['Quantidade'] * df['Venda']
    return df.to_csv(r'C:\Users\walte\Documents\Aquivos_Walter\Engenharia de dados\basic-python\Function\pythonbasic\data\output.csv',index = False)

#uma função que load em csv e parquet
#def load_dados(df: pd.DataFrame , name , path):
 #   df.to_csv(path&name , index = False)

#função final
def etl_completa(pasta):
    df = extrair_json(pasta)
    df_calculado = calcular_total_vendas(df)

##if __name__ == "__main__":
 ##   pasta_argumento = r'C:\Users\walte\Documents\Aquivos_Walter\Engenharia de dados\basic-python\Function\pythonbasic\data'
  #  df = extrair_json(pasta_argumento)
  #  df_calculado = calcular_total_vendas(df)
   # load_dados(df_calculado ,'output.csv',pasta_argumento)
