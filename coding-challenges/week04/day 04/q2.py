import math 
def check( m, n): 
      
    # m^n  
    RHS = m * math.log(n); 
    LHS = n * math.log(m);  
      
    if (LHS > RHS): 
        print("m^n > n^m"); 
          
    elif (LHS < RHS): 
        print("m^n < n^m"); 
          
    else: 
        print("m^n = n^m"); 
  
m = 987654321;  
n = 123456987; 
check(m, n)