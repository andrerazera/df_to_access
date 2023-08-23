import pandas as pd
import urllib
from sqlalchemy import create_engine
import pyodbc
import time
from datetime import datetime


d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
df

local_banco = r"C:\Users\andre.razera\Desktop\teste df to access\df_acc.accdb"


def df_to_access(df,local_banco,nome_da_tabela):

    # função para jogar um dataframe em um banco de dados access

    print([x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')])

    # string de conexao ao db
    cnn_str = (
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
        r"DBQ="+local_banco
    )

    # construção da url de conexao com o pyodbc
    cnn_url = f"access+pyodbc:///?odbc_connect={urllib.parse.quote_plus(cnn_str)}"


    #criação do engine do sqlalchemy
    acc_engine = create_engine(cnn_url)

    print('Writing to access table...')

    #função do pandas para copiar valores para tabela sql, atencao pro if_exists
    df.to_sql(nome_da_tabela, acc_engine, if_exists='replace')
    print('write complete.')
    acc_engine.dispose()


df_to_access(df,local_banco,"teste4")