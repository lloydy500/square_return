# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 11:30:24 2020

@author: lloyd
"""


def square_returner():
    while True:
        try:
            num = int(input("Please enter an integer to be squared: "))**2
        except:
            print("Try a number!")
            continue
        else:
            print(f'Good job, the answer is {num}.')
            break
            
            