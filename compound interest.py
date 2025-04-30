
#program to find compound interest

def compund_interest(p, r, t):
    # Compound Interest = Principal * ((1 + Rate/100) ** Time) - Principal
    
    return p*((1+r/100)**t)-p 
#returns the compound interest 

p , r ,t= 32 , 6 , 2

print(compund_interest(p , r ,t))            



  

