from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def hutool_encrypt(content, key):
    """
    ECB 模式 和 PKCS7 填充 和 gbk编码
    :param content:
    :param key:
    :return:
    """
    # 将密钥转换为字节，并确保长度为 16、24 或 32 字节（AES 要求）
    key_bytes = key.encode('gbk')[:32].ljust(32, b'\0')  # 补齐到 32 字节
    cipher = AES.new(key_bytes, AES.MODE_ECB)  # 使用 ECB 模式
    # 对内容进行填充（PKCS7 填充）
    content_bytes = content.encode('gbk')
    padded_content = pad(content_bytes, AES.block_size)
    # 加密
    encrypted_bytes = cipher.encrypt(padded_content)
    # 返回 Hex 字符串
    return encrypted_bytes.hex()

# 解密函数
def hutool_decrypt(encrypted_content, key):
    # 将密钥转换为字节，并确保长度为 16、24 或 32 字节
    key_bytes = key.encode('gbk')[:32].ljust(32, b'\0')  # 补齐到 32 字节
    cipher = AES.new(key_bytes, AES.MODE_ECB)  # 使用 ECB 模式
    # 将 Hex 字符串转换为字节
    encrypted_bytes = bytes.fromhex(encrypted_content)
    # 解密
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    # 去除填充
    unpadded_bytes = unpad(decrypted_bytes, AES.block_size)
    # 返回 GBK 解码后的字符串
    return unpadded_bytes.decode('gbk')