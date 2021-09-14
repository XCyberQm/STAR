import base64
message ="QnUgaGVzYWJhIGFpdCBtYWlsIGFkcmVzaW5pIGJ1bGFiaWxpciBtaXNpbg=="
base64_bytes = message.encode('ascii')

sample_string_bytes = base64.b64decode(base64_bytes)
sample_string = sample_string_bytes.decode("ascii")

print(f"Decoded string: {sample_string}") 