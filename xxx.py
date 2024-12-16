import random
import string
 
# 定义一个函数来生成密钥
def generate_key(length=8):
    # 使用random和string模块生成一个指定长度的随机字符串作为密钥
    key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    return key
 
# 生成一个密钥
key = generate_key()
print(f"生成的密钥是: {key}")
