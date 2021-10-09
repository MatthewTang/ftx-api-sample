#!/usr/bin/env python3.9
# This is a sample Python script.

from ccxt.base.exchange import Exchange
from dotenv import dotenv_values
import time
import hmac
import urllib.parse
from requests import Request, Session, Response
from typing import Tuple

basestring = str  # ccxt

URL = "https://ftx.com/api"


def auth(_session: Session, _key: str, _secret: str, _subaccount_name: str = None) -> None:
    ts = int(time.time() * 1000)
    request = Request('GET', f'{URL}/account')
    prepared = request.prepare()
    signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode()
    signature = hmac.new(_secret.encode(), signature_payload, 'sha256').hexdigest()
    request.headers['FTX-KEY'] = _key
    request.headers['FTX-SIGN'] = signature
    request.headers['FTX-TS'] = str(ts)
    if _subaccount_name:
        request.headers['FTX-SUBACCOUNT'] = urllib.parse.quote(_subaccount_name)
    response = _session.send(request.prepare())
    data = response.json()
    print(response.status_code)


def process_response(response: Response):
    try:
        data = response.json()
    except ValueError:
        response.raise_for_status()
        raise
    else:
        if not data['success']:
            raise Exception(data['error'])
        return data['result']


def get_key() -> Tuple[str, str]:
    config = dotenv_values(".env")
    return config['API_KEY'], config['API_SECRET']


if __name__ == '__main__':
    s = Session()
    key, secret = get_key()
    auth(s, key, secret, dotenv_values(".env")['SUBACCOUNT_NAME'])
