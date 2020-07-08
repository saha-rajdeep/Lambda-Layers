import json
import account_validation as validationlayer

def lambda_handler(event, context):
    if validationlayer.validateAcct(event['AcctNo']) =='PASS':
        createAccount()
        return 'Account created'
    else:
        return 'Bad Account Number'
        
def createAccount():
    #Actual Account creation logic will go here
    print()