from django.shortcuts import render
from services.models import Service, Category

import json
import requests
import os

#Load varibles from .env
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#Function for connect with Crown Wallets
def instruct_wallet(method, params):

    #Set data for login
    RPC_USER = os.getenv("RPC_USER")
    RPC_PHRASE = os.getenv("RPC_PHRASE")
    RPC_URL = os.getenv("RPC_URL")

    #Check crownd for info
    payload = json.dumps({"method": method, "params": params})
    headers = {'content-type': "application/json", 'cache-control': "no-cache"}
    try:
        response = requests.request("POST", RPC_URL, data=payload, headers=headers, auth=(RPC_USER, RPC_PHRASE))
        result = json.loads(response.text)
        return result
    except requests.exceptions.RequestException as e:
        print (e)
    except:
        print ('No response from Wallet, check Bitcoin is running on this machine')


# Update all info on home.
def home(request):
    x = instruct_wallet("getinfo", [])
    print(x)


    """
    services = Service.objects.all()

    #Check Balance for each service
    for service in services:

        balance = instruct_wallet('getbalance', [service.title])["result"]
        PHRASE = os.getenv("PHRASE")
        #Check crown needed
        needed = service.crw_donate - balance

        #Calculate the progress
        progress = int(balance / service.crw_donate * 100)
        finish = str(progress)+"%" 

        #Check for finish project
        if balance >= service.crw_donate:

            #Set True on completed and save
            service.completed = True
            service.save()

            #Unblock wallet, settxfee and send the tx at wallet shop.
            answer = instruct_wallet('walletpassphrase', [PHRASE, 5])
            set_txfee = instruct_wallet('settxfee', [0.00000007])
            send_tx = instruct_wallet("sendfrom", [str(service.title), str(service.wallet_shop), 1]) #Cambiar ammount
            print(send_tx)

        else:
            #Update balance for project
            if service.wallet_donate == None:
                address = instruct_wallet("getnewaddress", [str(service.title)])["result"]
                service.wallet_donate = address
                service.save()
                print("This is title: {} and this is address: {} ".format(service.title, address))
            else:   
                service.amount_needed = needed
                service.amount_donate = balance
                service.progress = finish
                service.save()
    """

    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

#def store(request):
    #return render(request, "core/store.html")






