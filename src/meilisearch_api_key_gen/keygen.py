from request import make_request 

def key_gen(masterKey: str, address: str, actions: list, indexes: list):
    response = make_request(masterKey, address, actions, indexes)
    return response['key']