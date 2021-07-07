from math import *

__all__ = ("calc_expression", )

sings = ["+", "-", "/", "//", "*",  "**", "%"]

def check_expression(expression):
    for _ in expression:
        if _ in sings:
            return True 
    
    else:
        return False 



def calc_expresion(expression: str):
    """ Calculate the Mathematical Expression using Python"""
    
    if "import" in expression:
        return None
    
    elif "  " in expression:
        return None
    
    elif "print" in expression:
        return None
    
    elif check_expression(expression):
        ouput = eval(expression)
        return ouput
    
    else:
        return None
    
        

