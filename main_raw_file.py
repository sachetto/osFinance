import pandas as pd
import numpy as np
from os.path import exists
import datetime
import sqlite3
from pandas.api.types import is_numeric_dtype
from Minhas_Classes_temp import *
from Classe_Banco_De_Dados_temp import *

arquivo_ordens = '2019.csv'

def OpenCSV(arquivo):
  try:
    df = pd.read_csv(arquivo)
    # remove possíveis linhas em branco do csv
    df = df.dropna(how = 'any')
    return df

  except FileNotFoundError:
    print("Arquivo não encontrado.")

    
def RemoveRSDoPreco(df_ord):
  try:
    df_ord["Preco"] = df_ord["Preco"].str.replace("R$","")
    return df_ord
    
  except:
    print("Erro ao remover R$ da coluna valor")
    

def ConvertePrecoParaFloat(df_ord):
  try:
    
    if not is_numeric_dtype(df_ord["Preco"]):
        df_ord["Preco"] = pd.to_numeric(df_ord["Preco"])
    
    return df_ord
    
  except:
    print("Erro ao converter")


def ConverteIndiceParaInteiro(df_ord):
  try:
    df_ord["Indice"] = df_ord["Indice"].astype(int)
    return df_ord
    
  except:
    print("Erro ao converter")


def ConvertDataToISOFormat(df_ord):
  # Change the format of the strings in 'Data' column
  df_ord['Data'] = df_ord['Data'].str.split('/').apply(lambda x: f"{x[2]}/{x[1]}/{x[0]}")
  
  # Replace '/' with '-'
  df_ord['Data'] = df_ord['Data'].str.replace('/', '-')
  
  return df_ord


def CriaUmaTabelaDeOrdensNoBancoComBaseNoDataframe(conexao_banco, nome_da_tabela, dr_ord):
  try:
    dr_ord.to_sql(nome_da_tabela, conexao_banco, if_exists="replace", index=False)
  
  except:
    print("Erro ao criar a tabela")
 

def DefineChavePrimariaNoDaTabela(conexao, tabela, chave):
  try:
    cursor = conexao.cursor()
  
    # Create a new table with the desired primary key
    cursor.execute(f"CREATE TABLE {tabela}_new ({chave} INTEGER PRIMARY KEY AUTOINCREMENT, Data TEXT, Tipo TEXT, Titulo TEXT, Ticker TEXT, Qnt REAL, Preco REAL)")

    # Copy the data from the original table to the new table
    cursor.execute(f"INSERT INTO {tabela}_new SELECT * FROM {tabela}")

    # Rename the original table to a backup table
    cursor.execute(f"ALTER TABLE {tabela} RENAME TO {tabela}_old")

    # Rename the new table to the original table name
    cursor.execute(f"ALTER TABLE {tabela}_new RENAME TO {tabela}")

    # Drop the backup table
    cursor.execute(f"DROP TABLE {tabela}_old")

    conexao.commit()

  except:
    print("Erro ao criar chave primária")

def CriaTabelaDeStock(conexao):
  try:
    cursor = conexao.cursor()
    cursor.execute(f"CREATE TABLE stock (Id INTEGER PRIMARY KEY AUTOINCREMENT, Ticker TEXT, Company TEXT, Price REAL, Category TEXT)")
    conexao.commit()
  except:
    print("Erro ao criar a tabela de ações")

# ****************************************************************************
# ****************************************************************************
# ****************************************************************************
def SetupDoBanco():
  df_ordens = OpenCSV(arquivo_ordens)
  print(df_ordens.head())

  print("\n\nOrdens editadas\n")
  df_ordens = RemoveRSDoPreco(df_ordens)
  df_ordens = ConvertePrecoParaFloat(df_ordens)
  df_ordens = ConverteIndiceParaInteiro(df_ordens)
  df_ordens = ConvertDataToISOFormat(df_ordens)

  print(df_ordens.head())

  conn = sqlite3.connect("bancodedados.db")

  CriaUmaTabelaDeOrdensNoBancoComBaseNoDataframe(conn, "ordens", df_ordens)
  DefineChavePrimariaNoDaTabela(conn, "ordens", "Indice")
  CriaTabelaDeStock(conn)

  conn.close()

# ********************************************
#               Execução:
# ********************************************
# SetupDoBanco()






conn = sqlite3.connect("bancodedados.db")
CriaTabelaDeStock(conn)
conn.close()

# cursor = conn.cursor()
# cursor.execute("SELECT DISTINCT Ticker FROM ordens")
# companies = cursor.fetchall()

# for company in companies:
#     print(company[0])

# # # conn.commit()
# conn.close()


# ********************************************
#               Alguns Testes:
# ********************************************
# Test_Stock().Test_Print()
# Test_Database().Test_GetDistinctValues()
# Test_Database().Test_QueryWhithWhere()