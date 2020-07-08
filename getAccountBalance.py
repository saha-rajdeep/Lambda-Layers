import json
import account_validation as validationlayer

def lambda_handler(event, context):
    if validationlayer.validateAcct(event['AcctNo']) =='PASS':
        getAccountBalance()
        return 'Account balance returned'
    else:
        return 'Bad Account Number'
        
def getAccountBalance():
    #Actual get Account Balance logic will go here
    print()
