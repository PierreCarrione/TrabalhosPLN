from builtins import range, print, len

import PyPDF2
import tweepy as tw
import re

with open('twitter-tokens.txt', 'r') as file:
    consumer_key = file.readline().strip('\n')
    consumer_secret = file.readline().strip('\n')
    bearer_token = file.readline().strip('\n')
    acess_token = file.readline().strip('\n')
    acess_token_secret = file.readline().strip('\n')

cliente = tw.Client(bearer_token,consumer_key,consumer_secret,acess_token,acess_token_secret)

keywords = ["rs", "rS", "Rs", "RS"]
tweets = cliente.search_recent_tweets(query = keywords, max_results = 100).data

twts_rs = []
twts_kk = []
results_rs = []
results_kk = []

for i in range(len(tweets)):
    twts_rs.append(tweets[i].text)
    results_rs.append(re.findall("((rs|Rs|rS|RS)+)", twts_rs[i]))

keywords = ['k', 'K', "KK","kk"]
tweets = cliente.search_recent_tweets(query = keywords, max_results = 100).data

for i in range(len(tweets)):
    twts_kk.append(tweets[i].text)
    results_kk.append(re.findall("(\sk+)", twts_kk[i]))

print("Tweets encontrados com pelo menos um 'rs'")
for i in range(len(twts_rs)):
    print(twts_rs[i])
    print("//---------------------------------------------------------------\\\\")

print("\n\nTweets encontrados com pelo menos um 'k'")
for i in range(len(twts_kk)):
    print(twts_kk[i])
    print("//---------------------------------------------------------------\\\\")

print("\nTotal de tweets encontrados com pelo menos um 'k' :",len(twts_kk))
print("Total de tweets encontrados com pelo menos um 'rs' :",len(twts_rs))

#Busca em um pdf de uma base de dados de livros digitais
#https://projectoadamastor.org/base-de-dados-de-livros-digitais/
#A busca será feita para encontrar datas

pdf_file = open('bn000163.pdf','rb')

read_pdf = PyPDF2.PdfFileReader(pdf_file)

number_of_pages = read_pdf.getNumPages()

results = []

for i in range(number_of_pages):
    results.append(re.findall("(\(?\d{4}\-?\d{4}\)?|\d{4}\s?|\s\w+\s?\-?\s?\d{4}|\w+\s?\–?\s?\d{2}\s?\-?\s?\w{2}\s?\–?\w+\s?\–?\s?\d{4}|\s\w+\s?\–+?\s?\d{4})",
                              read_pdf.getPage(i).extractText()))

total = 0
for i in range(len(results)):
    if len(results[i]) == 0:
        print("Não foram encontrado ocorrências de datas na página ",i+1)
        print("//---------------------------------------------------------------\\\\")
    else:
        print("Registros encontrados na página ", i+1)
        print(results[i])
        print("//---------------------------------------------------------------\\\\")
        total = total + len(results[i])

print("\nO total de datas encontradas foi de:" , total)