"""
    IDPay Python Package 
    docs: https://idpay.ir/web-service/v1.1/#8614460e98
"""

import requests
import json
from .logger import GetLogger


GLOBAL_LOGGER = GetLogger()


class HttpRequest:
    """
    Base Class For adding get and post request to IDpay Class
    """
    def post(self, *args, **kwargs):
        return requests.post(args, kwargs)

    def get(self, *args, **kwargs):
        return requests.post(args, kwargs)




class IDpayBase:
    
    endpoint = 'https://api.idpay.ir/v1.1/'
    


class IDPay(HttpRequest, IDpayBase):
    """ 
    IDPay Class
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        usage:
            Interface =  IDPay(...)
            interface.payment(...)
            interface.get_status(...)
            interface.inquiry(...)
            interface.verify(...)
        
    """

    def __init__(self, api_key, domain, sandbox = False):
        self.api_key = api_key
        self.domain = domain
        self.sandbox = sandbox
        self.log = GLOBAL_LOGGER

        self.headers = {
            'Content-Type': 'application/json',
            'X-API-KEY': self.api_key,
            'X-SANDBOX': '1' if self.sandbox else '0'
        }


    def payment(self, order_id, amount, callback_page, payer = {}):
        data = {
            'order_id': order_id,
            'amount': amount,
            'callback': self.domain + callback_page,
            'name': payer.get('name'),
            'phone': payer.get('phone'),
            'mail': payer.get('mail'),
            'desc': payer.get('desc'),
        }

        url = self.endpoint + "/payment"
        self.log(f"SEND POST REQUEST TO {url}")
        request = self.post(url, data=json.dumps(data), headers=self.headers)

        if request.status_code == 201:
            return request.json()

        else:
            response = request.json()
            message = "Http status Code : " + str(request.status_code) + "   |   " + "Error Code : " + str(response['error_code']) + "   |   " + "Description : " + str(response['error_message'])

        return {'message': message}


    def verify(self, id, order_id):
        """ Verify a Payment Transaction"""
        data = {
            'id': id,
            'order_id': order_id,
        }
        url = self.endpoint + "payment/verify"
        self.log(f"SEND POST REQUEST TO {url}")
        request = self.post(url, data=json.dumps(data), headers=self.headers)

        if request.status_code == 200:
            response = request.json()
            response['message'] = "Status: " + str(response['status']) + " (" + self.get_status(response['status']) + ")"

            return response

        else:
            response = request.json()
            message = "Http status Code : " + str(request.status_code) + "   |   " + "Error Code : " + str(response['error_code']) + "   |   " + "Description : " + str(response['error_message'])

        return {'message': message}


    def inquiry(self, id, order_id):
        """ Check Status of a Transaction """

        data = {
            'id': id,
            'order_id': order_id,
        }

        url = self.endpoint + "payment/inquiry"
        self.log(f"SEND POST REQUEST TO {url}")
        request = self.post(url, data=json.dumps(data), headers=self.headers)
        
        if request.status_code == 200:
            response = request.json()
            response['message'] = "Status: " + str(response['status']) + " (" + self.get_status(response['status']) + ")"

            return response

        else:
            response = request.json()
            message = "Http status Code : " + str(request.status_code) + "   |   " + "Error Code : " + str(response['error_code']) + "   |   " + "Description : " + str(response['error_message'])

        return {'message': message}


    def get_status(self, status:int) -> str:

        states = {
            1: 'Transaction created',
            2: 'Transaction failed',
            3: 'An error has occurred',
            4: 'Transaction blocked',
            5: 'Transaction rejected to payer',
            6: 'Transaction rejected',
            7: 'Transaction canceled',
            8: 'Redirected to IPG',
            10: 'Verify pending',
            100: 'Transaction verified',
            101: 'Verified again',
            200: 'Transaction settled',
        }
        if type(states) == type(int):
            return states.get(status, "Invalid Status Number")
        
        return False