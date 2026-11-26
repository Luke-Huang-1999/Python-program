try:
    b'\x04\xeb\x12'.decode('utf-8')

except UnicodeDecodeError:
    print("utf-8解碼錯誤")