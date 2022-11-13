msg = "😀😀😀😀😀"

msg_bytes = msg.encode('utf-8')

print(len(msg)) # 5
print(len(msg_bytes)) # 10

print(msg_bytes)

msg_decoded = msg_bytes.decode('utf-8')
print(msg_decoded)
