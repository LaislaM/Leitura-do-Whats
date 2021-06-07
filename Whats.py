#encoding=utf
#bibliotca para formatar data.
import datetime

#
from collections import Counter

#
import collections

#
import pandas as pd

#
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

msg1 = "[23/03/2021 11:19:24] Laisla Souza 💕: Com certeza!
msg1[22:].split(":")

ref_arquivo = open('chat.txt', 'r', encoding='utf-8')
linha = ref_arquivo.readline()


list_datas = []
list_erros_formatacao = []
list_pessoas = []
list_msgs = []

while linha:
    linha = ref_arquivo.readline()
    
    try:
        date_time_obj = datetime.datetime.strptime(linha[1:20], '%d/%m/%Y %H:%M:%S')
        list_datas.append(date_time_obj)
        msg = linha[22:]
        if(len(msg.split(':')) >= 2):
            list_pessoas.append(msg.split(':')[0])
            list_msgs.append(msg.split(':')[1])
    except ValueError:
        list_erros_formatacao.append('Errors de formatação de data')
ref_arquivo.close()

type(Counter(list_pessoas))

p = dict(Counter(list_pessoas))

p

dict_pessoas = dict(Counter(list_pessoas))
pessoas_df = pd.DataFrame(dict_pessoas.items(), columns=['Pessoa', 'Qnt Mensagem'])
pessoas_df = pessoas_df.sort_values(by=['Qnt Mensagem'])
pessoas_df['Pessoa'] = pessoas_df['Pessoa'].replace(['\u202a+55\xa011\xa095765‑5550\u202c','\u202a+55\xa081\xa09957‑6999\u202c','\u202a+55\xa011\xa098793‑6843\u202c','\u202a+55\xa011\xa097301‑7387\u202c','\u202a+55\xa013\xa099785‑0435\u202c','\u202a+55\xa011\xa095980‑8745\u202c','\u202a+55\xa011\xa099122‑8956\u202c'])
print(pessoas_df)
pessoas_df.plot(kind='barh', x = 'Pessoa', y = 'Qnt Mensagem', figsize=(13,7), color=['#D4A29C', '#E8B298', '#EDCC8B', '#BDD1C5', '#9DAAA2'])

pessoas_df
def contador_palavras(msgs):
    palavras = []
    for frases in msgs:
        for palavra in frases.split():
            palavras.append(palavra)
    return Counter(palavras)

palavras_dict = dict(contador_palavras(list_msgs))

#palavras_df = pd.DataFrame(palavras_dict.items(), columns=['Palavra', 'Frequencia'])
#palavras_df = palavras_df.sort_values(by=['Frequencia'], ascending=False)
#palavras_df.head(10).plot(kind='bar', x = 'Palavra', y='Frequencia', title='Palavras mais faladas')dict_pessoas = dict(Counter(list_pessoas))
pessoas_df = pd.DataFrame(dict_pessoas.items(), columns=['Pessoa', 'Qnt Mensagem'])
pessoas_df = pessoas_df.sort_values(by=['Qnt Mensagem'], ascending=False)
#palavras_df.head(10).plot(kind='bar', x = 'Palavra', y='Frequencia', title='Palavras mais faladas')dict_pessoas = dict(Counter(list_pessoas))

print(pessoas_df)
pessoas_df.plot(kind='barh', x = 'Pessoa', y = 'Qnt Mensagem', figsize=(13,7), color=['#D4A29C', '#E8B298', '#EDCC8B', '#BDD1C5', '#9DAAA2'])

dia_da_semana = {
  0: "Domingo",
  1: "Segunda",
  2: "Terça"
 
}
list_horas = []
list_dia_semana = []
for data in list_datas:
    list_horas.append(data.time().hour)
    
    list_dia_semana.append(dia_da_semana.get(data.weekday()))
    
    if(data.weekday() == 1):
        list_dia_semana.append('segunda')
    elif(data.weekday() == 2):
        list_dia_semana.append('terca')
    elif(data.weekday() == 3):
        list_dia_semana.append('quarta')
    elif(data.weekday() == 4):
        list_dia_semana.append('quinta')
    elif(data.weekday() == 5):
        list_dia_semana.append('sexta')
    elif(data.weekday() == 6):
        list_dia_semana.append('sabado')
    elif(data.weekday() == 0):
        list_dia_semana.append('domingo')
        
    dict_dia_semana = dict(Counter(list_dia_semana))
        
    semana_df = pd.DataFrame(dict_dia_semana.items(), columns=['Dia_Semana', 'Frequencia'])
semana_df.plot(kind='bar', x = 'Dia_Semana', y='Frequencia', title='Dia da Semana que tem conversa', color=['#D4A29C', '#E8B298', '#EDCC8B', '#BDD1C5', '#9DAAA2'])

dict_horas = dict(Counter(list_horas))
horas_df = pd.DataFrame(dict_horas.items(), columns=['Hora', 'Frequencia'])
horas_df.plot(kind='bar', x = 'Hora', y='Frequencia', title='Horario das Conversas',color=['#D4A29C', '#E8B298', '#EDCC8B', '#BDD1C5', '#9DAAA2'])


ax = sns.lineplot(x="Hora", y="Frequencia", data=horas_df, ci=68)
        
        
        


