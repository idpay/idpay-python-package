from idpay import IDPay


# create an instance of idpay class
IDPayManager = IDPay(
    api_key="a"*36,
    sandbox=True,
    domain="domain.ir"
)


# handy methods for changing the api key or domain during the app
IDPayManager.SetAPIKey("a"*36)
IDPayManager.SetDomain("domain.ir")
IDPayManager.SetSandBox(True)


# Mrthods
#       IDPayManager.verify(...)
#       IDPayManager.inquiry(...)
#       IDPayManager.payment(...)


response = IDPayManager.verify(id=1, order_id=1)
# >>>
# [IDPAY - WARNING] [2023-09-14 14:35:01,852] - SENDING POST REQUEST to https://api.idpay.ir/v1.1/payment/verify
# {'message': 'Http status Code : 403   |   Error Code : 12   |   Description : API Key یافت نشد.'}



status = IDPayManager.get_status(2123)
# >>> Invalid Status Number

status = IDPayManager.get_status(4)
# >>> Transaction blocked

