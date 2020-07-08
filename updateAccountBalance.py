import json
import account_validation as validationlayer

def lambda_handler(event, context):
    if validationlayer.validateAcct(event['AcctNo']) =='PASS':
        updateAccountBalance()
        return 'Account balance updated'
    else:
        return 'Bad Account Number'
        
def updateAccountBalance():
    #Actual update Account balance logic will go here
    print()
