import matplotlib.pyplot as plt 
import numpy as np

from math import log2  

def read_book(url):
    file = open(url,"r",encoding='UTF-8')
    content = list()
    if file.mode == 'r':
        content = file.read()
    
    return content


def probability_per_symbol(book,alphabeat):  
 
   size = len(alphabeat)

   bookSize = len(book)

   Probability = np.zeros(size)

   for i in range(size):
       reps = 0
       current_symbol = alphabeat[i]
       for j in range(bookSize):
           symbol = book[j]

           if symbol == current_symbol:
               reps+=1
      
       Probability[i] = reps/bookSize
  
   return Probability


def information_per_symbol(Probability, size_alphabet):

    Information = np.zeros(size_alphabet)
    
    for i in range(size_alphabet):
        p_by_symbol = Probability[i]
        if p_by_symbol != 0:
            Information[i] = log2(1/p_by_symbol)
        else:
            Information[i] = 0

    return Information


def calc_entropy(Probability, Information):
    h = np.zeros(len(Probability))

    for i in range(len(Probability)):
        h[i]=Probability[i]*Information[i]

    H = sum(h)

    return H


def plot_bar_Probabilities(alphabeat,probabilities):
    index = np.arange(len(alphabeat))
    plt.figure(1)
    plt.bar(index, probabilities)
    plt.xlabel('Símbolo', fontsize=12)
    plt.ylabel('Probabilidad', fontsize=12)
    plt.xticks(index, alphabeat, fontsize=10)
    plt.title('Probabilidades por cada símbolo del alfabeto')

def plot_bar_Information(alphabeat,Information):
    plt.figure(2)
    index = np.arange(len(alphabeat))
    plt.bar(index, Information)
    plt.xlabel('Símbolo', fontsize=12)
    plt.ylabel('Información', fontsize=12)
    plt.xticks(index, alphabeat, fontsize=10)
    plt.title('Información por símbolo')

if __name__=='__main__':
    book = read_book("el_principito.txt")

    bookSize = len(book) 

    ABC=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    
    size_alphabet = len(ABC)

    Probability = probability_per_symbol(book, ABC)
    
    Information = information_per_symbol(Probability,size_alphabet)
    
    H = calc_entropy(Probability, Information)
    
    plot_bar_Probabilities(ABC, Probability)
    plot_bar_Information(ABC, Information)
    plt.show()

    print(f"La información promedio de cada símbolo es de (Entropía): {H} bits")
    print(f"La longitud del libro es: {bookSize} símbolos")
    print(f"La información promedio contenida por esta fuente de información es {bookSize*H / 8000} kB")