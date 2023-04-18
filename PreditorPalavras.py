import nltk

#Importando a base de dados emma
nltk.corpus.gutenberg.fileids()
emma = list(nltk.corpus.gutenberg.words( 'austen-emma.txt' ))#Transformo em lista para poder lidar melhor com os dados


dictWords = {}
#Para esse problema eu irei adotar o 2-gram para poder gerar a próxima palavra
def generateNextWord(listWords, word):
    splitted = word.split()
    for i in range(len(listWords) - 2):
        #Como estou adotando 2-gram o if abaixo irá garantir que a análise será feita através das 2 últimas palavras da frase sugerida
        if listWords[i].lower() == splitted[len(splitted)-2].lower() and listWords[i+1].lower() == splitted[len(splitted)-1].lower():
            if listWords[i + 2] in dictWords:
                dictWords[emma[i+2]] = dictWords.get(emma[i + 2]) + 1
            else:
                dictWords[emma[i+2]] = 1
    return max(dictWords)


#Retorna uma lista contendo as 10 palavras mais frequentes
def mostCommon():
    reverseDict = {k: v for k, v in sorted(dictWords.items(), key=lambda item: item[1], reverse=True)}
    print("Palavras mais frequentes:")

    if len(reverseDict) < 10:
        print(reverseDict)
    else:
        aux = 0

    for i in reverseDict:
        if aux == 10:
            break
        print(i)
        aux += 1

fraseEntrada = "she was"
print("Palavra sugerida: ",generateNextWord(emma, fraseEntrada))
mostCommon()