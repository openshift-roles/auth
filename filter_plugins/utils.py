import base64

def base64_encode(value):
    encoded_bytes = base64.b64encode(value.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def base64_decode(encoded):
    decoded = base64.b64decode(encoded)
    return decoded('utf-8')

class FilterModule(object):
    '''
    Custom filter for base64 encode and decode text
    '''
    def filters(self):
        return {
            'base64_encode': base64_encode,
            'base64_decode': base64_decode 
        }