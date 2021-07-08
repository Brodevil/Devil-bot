from math import *

__all__ = ("check_expression", "calc_expression")

sings = ["+", "-", "/", "//", "*",  "**", "%"]

def check_expression(expression: str):
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
        try:
            ouput = eval(expression)
            return ouput
        except Exception:
            return None
    
    else:
        return None
    
        

