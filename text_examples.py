from itertools import chain
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
#nltk.download()
from tokenize import generate_tokens

class TextExamples(object):

    def quitarSigno(texto):
        prohibidos = {"?", "¿", ".", ",", ";", ":", "!", "¡", "'"}
        return ("".join(c for c in texto.lower() if c not in prohibidos)).split()

    #def listaDePalabras(texto):
       # return quitarSigno(texto).split()

    def contar(lista):
        frecuencia = []
        for w in lista:
            frecuencia.append(lista.count(w))
        listavistos = []
        listaFinal = []
        contador = 0
        for k in lista:
            listaAux = []
            if k not in listavistos:
                listaAux.append(k)
                listavistos.append(k)
                listaAux.append(frecuencia[contador])
                listaFinal.append(listaAux)
                contador += 1
            else:
                contador += 1

        listaSoloConNumeros=[]
        listaOrdenada=[]
        for m in range(0,len(listaFinal)):
            arrayA= listaFinal[m]
            listaSoloConNumeros.append(arrayA[1])
        listaSoloConNumeros.sort(reverse=True)

        for x in range(0,len(listaSoloConNumeros)):
            mAux=0
            for m in range(0, len(listaFinal)):
                if listaFinal[m][1] is listaSoloConNumeros[x]:
                    mAux=m
            listaOrdenada.insert(x,listaFinal[mAux])

        return listaOrdenada


if __name__ == '__main__':
    my_text = "Lorem ipsum; dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut. labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    text = "This is an example text. Let us use two sentences, so that it is more logical."

    tes = "hola ma hola que tal ma ma ma ma"
    l = TextExamples.quitarSigno(tes)
    print(TextExamples.contar(l))
    l2= TextExamples.quitarSigno(my_text)
    print(TextExamples.contar(l2))