# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 09:03:48 2021

@author: Moon
"""
while(True):
    number=input("Integer: ")
    
    if len(number)<=3:
        if (len(str(number)))==3:
            r1=int(str(number)[0])*100
            r2=int(str(number)[1])*10
            r3=int(str(number)[2])*1
        if (len(str(number)))==2:
            r1=None
            r1s=""
            r2=int(str(number)[0])*10
            r3=int(str(number)[1])*1
        if (len(str(number)))==1:
            r1=None
            r1s=""
            r2=None
            r2s=""
            r3=int(str(number)[0])*1
        
        
        if r1!=None:
            if(r1>=500):
                diff1=abs(r1-500)
                if diff1/100<4:
                    r1s="D"+"C"*int(diff1/100)
                else:
                    r1s="CM"
            
            if(r1>=100 and r1<500):
                diff1=abs(r1-100)
                if diff1/100<3:
                    r1s="C"+"C"*int(diff1/100)
                else:
                    r1s="CD"
        
        if r2!=None:
            if(r2>=50):
                diff1=abs(r2-50)
                if diff1/10<4:
                    r2s="L"+"X"*int(diff1/10)
                else:
                    r2s="XC"
            
            if(r2>=10 and r2<50):
                diff1=abs(r2-10)
                if diff1/10<3:
                    r2s="X"+"X"*int(diff1/10)
                else:
                    r2s="XL"
            if r2==0:
                r2s=""
                    
        
        if(r3>=5):
            diff1=abs(r3-5)
            if diff1/1<4:
                r3s="V"+"I"*int(diff1/1)
            else:
                r3s="IX"
        
        if(r3>=1 and r3<5):
            diff1=abs(r3-1)
            if diff1/1<3:
                r3s="I"+"I"*int(diff1/1)
            else:
                r3s="IV"
        if r3==0:
            r3s=""        
            
        print(r1s+r2s+r3s)
    
    else:
        print("Give maximum 3 digits")


     
    