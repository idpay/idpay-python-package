# -*- coding: utf-8 -*-

from validators import domain as DomainValidator


def validate_api_key(api_key:str) -> None:
    """
    validate api key check api length equal to 36 characters
    this function does not return any return value if api key is not valid
     its just raise an exception
    """
    doc_url = "https://idpay.ir/web-service/v1.1/#cee8b80267"
    if type(api_key) != type(""):
        raise ValueError("API key must be a string.")

    if len(api_key) != 36:
        raise ValueError(f"API key must be a string and have length of 36 characters.\n see the docs: {doc_url}.")



def validate_domain(domain:str) -> None:
    """
    validate a domain name
    """
    doc_url = "https://idpay.ir/web-service/v1.1/#972fadbc1d"
    if not DomainValidator(domain):
        raise ValueError(f"Invalid domain name: {domain}. see the docs: {doc_url}")
