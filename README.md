<p align="center"><img src="assets/logo.svg" width="400"></p>

## What is it
Pip package for implement API's payment service of [IDPay](https://idpay.ir).

## How to use

Require idpay package in your project by:

```bash
pip install -U idpay 
```

### how to use

```python
from idpay import IDPay

# create an instance of IDPay Class
IDpayManager = IDPay(
    api_key="put your api key here",
    sandbox=True or False,
    domain="yourdomain.ir"
)

# During the application running you can change the api_key and domain and sandbox with the following methods
IDpayManager.SetDomain(domain="domain")
IDpayManager.SetAPIKey(api_key="yourapikey")
IDpayManager.SetSandBox(sandbox=True or False)

# Methods:
IDpayManager.verify()
IDpayManager.payment()
IDpayManager.inquiry()
IDpayManager.get_status()
```

official Documentation: 
https://idpay.ir/web-service/v1.1/


