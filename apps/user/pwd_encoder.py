import hashlib

# 明文密码md5加密
def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest()
