# -*- coding: utf-8 -*-

# Hangman Game (Jogo da Forca)

from colorama import init, Fore
import random

# Define os prints do bonequinho
board = [
    '''
                            + - - - - - +
                            |           |
                            |
                            |
                            |
                            |
                            |
                            =======================
    ''',
    '''
                            + - - - - - +
                            |           |
                            |           O
                            |
                            |
                            |
                            |
                            =======================
    ''',
    '''
                            + - - - - - +
                            |           |
                            |           O
                            |           |
                            |
                            |
                            |
                            =======================
    ''',
    '''
                            + - - - - - +
                            |           |
                            |           O
                            |          /|
                            |
                            |
                            |
                            =======================
    ''',
    '''
                            + - - - - - +
                            |           |
                            |           O
                            |          /|\\
                            |
                            |
                            |
                            =======================
    ''',
    '''
                            + - - - - - +
                            |           |
                            |           O
                            |          /|\\
                            |          /
                            |
                            |
                            =======================
    ''',
    '''
                            + - - - - - +
                            |           |
                            |           O
                            |          /|\\
                            |          / \\
                            |
                            |       GAME OVER
                            =======================
    '''
]

class Hangman:

    def __init__(self, word = ''):
        self.word = word
        self.failures = 0
        self.hits = 0
        self.gamefinished = 0
        self.knownWords = []
        self.wrongWords = []

    def startgame(self):
        init(convert=True)
        print (Fore.GREEN + "\n>>> Jogo da Forca (Hangman) desenvolvido por Guilherme Semissatto (semissatto@gmail.com) - fev/2019 <<<")
        while not self.gamefinished:
            self.printstatus()
            self.printwrongwords()
            self.printknownwords()
            self.guess(word = self.askword())
            self.lost()
            self.won()

    def printstatus(self):
        print(board[self.failures])
        temp = ""
        for word in self.word:
            if word.upper() in self.knownWords or word.lower() in self.knownWords:
                temp += word + " "
            else:
                temp += "_ "
        print ("                            "+ temp + "\n")

    def askword(self):
        while True:
            instantword = str(input('Digite uma letra: '))
            if instantword.upper() in self.knownWords or instantword.upper() in self.wrongWords \
                or instantword.lower() in self.knownWords or instantword.lower() in self.wrongWords:
                print("Você já digitou esta letra. Digite outra: ")
            else:
                return instantword

    def guess(self, word):
        if word in self.word or word.lower() in self.word:
            self.knownWords.append(word)
            for item in self.word:
                if word.upper() == item or word.lower() == item:
                    self.hits += 1

            
        else:
            self.failures += 1
            self.wrongWords.append(word)            

    def printknownwords(self):
        temp = ""
        for i in self.knownWords:
            temp += i + " "
        print("Letras corretas: " + temp)

    def printwrongwords(self):
        temp = ""
        for i in self.wrongWords:
            temp += i + " "
        print ("Letras erradas:" + temp)

    def won(self):
        if self.hits == len(self.word):
            self.gamefinished = 1
            print ("Parabéns! Você venceu. A palavra é %s." % self.word.upper())

    def lost(self):
        if self.failures == len(board)-1:
            print (board[6])
            self.gamefinished = 1
            print ("Game over. Você perdeu. A palavra era %s." % self.word.upper())

    def showword(self):
        print (self.word)



# Main program
def choseword(file_path):
    file = open(file_path, 'r', encoding = 'UTF-8')
    words = file.readlines()
    filtered_words = list(map(lambda x: x[:len(x) - 1], words)) # Remove o \n de cada palavra
    return random.choice(filtered_words)

Hangman1 = Hangman(word = choseword('palavras.txt'))
Hangman1.startgame()