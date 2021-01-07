# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:34:46 2020

@author: USER
"""

#ask user to enter the total amount for their order
orderTotal = float(input('Please enter the total price of your order'))
#also ask user to enter their country
userCountry = input('Please enter your country you are ordering from').upper()
#if the users country is canada
if userCountry == 'CANADA':
#ask the user to enetr their province
    province = input('Please enter your province').upper()
#if the province ia alberta, charge user .05% GST task    
    if province == 'ALBERTA':  
#here, get .05% of the users input and store in a variable        
        convofPercentage = (0.05/100)*orderTotal
# then add the result from above to the order total inputed by the user
#and store in a variable        
        gstCharge = orderTotal + convofPercentage
#display the result from the above as the users total to pay for their order        
        print('The total charge for your order is {0:.03f}$'.format(gstCharge))
#but if provive is ontario,new brunswick or nova scotia,charge .13% harmony sales task        
    elif province == 'ONTARIO' or province== 'NEW BRUNSWICK' or province=='NOVA SCOTIA':
#here, get .15% of the users input and store in a variable         
        convofPercentage1 = (0.13/100)*orderTotal
 # then add the result from above to the order total inputed by the user
#and store in a variable       
        harmsalesTask = orderTotal + convofPercentage1
#display the result from the above as the users total to pay for their order        
        print('The total charge for your order is {0:.03f}$'.format(harmsalesTask))
# but if users province is the rest of the provinves not mentioned above, as seen listed below
#then charge them .06% other province charge and also the .05% GST CHARGE        
    elif province == 'QUEBEC' or province=='MANITOBA' or province== 'BRITISH COLUMBIA'\
    or province == 'PRINCE EDWARD ISLAND' or province == 'SASKATCHEWAN' or province == 'NEWFOUNDLAND AND LABRADOR':
#here, get .05% of the users input and store in a variable #        
        convofPercentage2 = (0.06/100)*orderTotal
 # then add the result from above to the order total inputed by the user, also adding the gst chharge
#and store in a variable           
        otherprovinceCharge = orderTotal + convofPercentage2 + convofPercentage
#display the result from the above as the users total to pay for their order           
        print('The total charge for your order is {0:.03f}$'.format(otherprovinceCharge))
# but if user is not from canada,the user isnt charged tax hence
#display the order total inputed as the total charge for users order        
else:
    print('The total charge for your order is {0:.03f}$'.format(orderTotal))
    
 
 

    
   
     
    