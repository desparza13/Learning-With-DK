#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:59:11 2020

@author: danielaesparza
"""

import xlrd
import random
import config as c
import Score as ap
import basicFunctions as bf

path  = "BancoPreguntas.xlsx"
inputWorkbook = xlrd.open_workbook(path)
inputWorksheet = inputWorkbook.sheet_by_index(0)

#print(inputWorksheet.nrows)
#print(inputWorksheet.ncols)

def loadQuestionBank(): #uploads all data in excel file into lists, one for each column
    for i in range(1,inputWorksheet.nrows):
        c.cathegories.append(inputWorksheet.cell_value(i,0))
        c.questions.append(inputWorksheet.cell_value(i,1))
        c.optionA.append(inputWorksheet.cell_value(i,2))
        c.optionB.append(inputWorksheet.cell_value(i,3))
        c.optionC.append(inputWorksheet.cell_value(i,4))
        c.correctAnswer.append(int(inputWorksheet.cell_value(i,5)))

def tryPrinting(): #function only used in order to print the lists and visually check their upload
    print("cathegories: ",c.cathegories)
    print("\n\n\n")
    print("questions: ",c.questions)
    print("\n\n\n")
    print("Option A: ",c.optionA)
    print("\n\n\n")
    print("Option B: ",c.optionB)
    print("\n\n\n")
    print("Option C: ",c.optionC)
    print("\n\n\n")
    print("Correct answer: ",c.correctAnswer)

def chooseRandomQuestion():
    qNum = random.randint(0,inputWorksheet.nrows-2)
    return qNum

def checkAnswer(qNum):
    answer=int(input("R: "))
    if (answer==c.correctAnswer[qNum]):
        c.currentGamePoints += 5
        return True
    else:
        ap.addPoints("Puntajes.txt", c.currentGamePoints)
        ap.graphScore("Puntajes.txt")
        bf.quitGame()
        return False
        
def printChosenQuestion(qNum):
    print(c.cathegories[qNum],"\n",c.questions[qNum],"\n1)",c.optionA[qNum],
          "\n2)",c.optionB[qNum],"\n3)",c.optionC[qNum])


def question():
    qNum=chooseRandomQuestion()
    printChosenQuestion(qNum)
    return checkAnswer(qNum)
    

loadQuestionBank()
#tryPrinting()
#print(question())

