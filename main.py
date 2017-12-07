#!/usr/bin/env python3

import os
import json

import hvac

# Using plaintext
client = hvac.Client(url='http://192.168.90.2:8200')
# root
#client.token = '89000ce5-92be-8a79-58e4xxx'


try:
    # Auth with token java-example
    client.token = '5b0b68d7-9c38-3524-5b8b-89dfeacc3xx'
    values = client.read('secret/hello')
    print(values['data'])

    # Auth with token jenkins
    client.token = '713ce28e-770b-f20f-3358-e70c2dcd93xx'
    assert client.is_authenticated() # => True

    role_id = 'bba51b2c-7191-c29b-39d9-65d0fc9e0462'
    secret_id = client.write('auth/approle/role/java-example/secret-id')['data']['secret_id']
    auth_token = client.write('auth/approle/login', role_id=role_id, secret_id=secret_id)['auth']['client_token']
    print("auth_token: ", auth_token)
    print("role_id: ", role_id)
    print("secret_id: ", secret_id)

    client.token = auth_token
    values = client.read('secret/hello')
    print(values['data'])





except Exception as e:
    print(e.__dict__)

