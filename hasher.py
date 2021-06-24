import base64

def encode_password(password):
    password_ascii = password.encode("ascii")
    
    base64_bytes = base64.b64encode(password_ascii)
    base64_string = base64_bytes.decode("ascii")
    
    return base64_string

def decode_password(base64_string):
    base64_bytes = base64_string.encode("ascii")
    
    password_ascii = base64.b64decode(base64_bytes)
    password = password_ascii.decode("ascii")
    
    return password
