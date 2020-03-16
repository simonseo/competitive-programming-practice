import hashlib

S = input().encode('utf-8')
h = hashlib.sha256()
h.update(S)
print(h.hexdigest())