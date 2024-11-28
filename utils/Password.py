import  os
import  hashlib
import  base64
def password_encrypt(password, salt=None, iterations=10000):
    """
    密码加密:PBKDF2_SHA256加密
    加密格式：pbkdf2_sha256$迭代次数$盐$哈希值
    admin可能的结果:pbkdf2_sha256$10000$yzsusUJwrGfonw+ZzVxlnA==$vgf/OgLf5C4wtQLtfNY9d68H+hxgv8eqZ0mwfxCqqeU=
    """
    # 生成随机盐
    # 生成 16 字节的随机盐，并编码为 Base64 字符串
    salt = salt or base64.b64encode(os.urandom(16)).decode('utf-8')
    # 使用 PBKDF2-SHA256 算法生成哈希值
    hash_object = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), iterations)
    # 将哈希值编码为 Base64 字符串
    hash_value_b64 = base64.b64encode(hash_object).decode('utf-8')
    # 构造加密字符串
    encrypted_string = f'pbkdf2_sha256${iterations}${salt}${hash_value_b64}'
    return encrypted_string

def password_verify(password, encrypted_string):
    """
    密码验证:PBKDF2_SHA256加密
    """
    iterations,salt, hash_value_b64 = encrypted_string.split('$')[-3:]
    return password_encrypt(password, salt,int(iterations)) == encrypted_string