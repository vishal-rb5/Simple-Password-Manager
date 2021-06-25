import base64
import hashlib

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


def hash_master_password(master_password):
    encode_master_password_ascii = master_password.encode("ascii")
    base64_bytes = base64.b64encode(encode_master_password_ascii)
    encode_master_password = base64_bytes.decode("ascii")
    
    result = hashlib.sha256(encode_master_password.encode())

    # returning the equivalent hexadecimal value.
    hex_result = result.hexdigest()
    return hex_result