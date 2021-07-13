from math import *
from keyword import kwlist

__all__ = ("check_expression", "calc_expression")

sings = ["+", "-", "/", "//", "*",  "**", "%"]
charactors = ["_", "$", "@", "!", "(", ")", "=", "|", "\\", "'", '"', "?", "<", ">", "[", "]", "{", "}"]

def check_expression(expression: str, checker_list: list, check_word: bool = True):
    for _ in expression.split() if check_word else list(expression):

        if _ in checker_list:
            return True 
        
    else:
        return False 



def calc_expresion(expression: str):
    """ Calculate the Mathematical Expression using Python"""
    
    if check_expression(expression, kwlist):
        return None
    
    elif "  " in expression:
        return None
    
    elif "print" in expression:
        return None
    
    elif "input" in expression:
        return None
    
    elif check_expression(expression, charactors):
        return None

    elif check_expression(expression, sings, check_word=False):
        try:
            ouput = eval(expression)
        except Exception:
            return None
        else:
            return ouput

    else:
        print("this")
        return None
    
        

