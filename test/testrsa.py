import rsa

(pub_key,pri_key) = rsa.newkeys(512)

message = "hello".encode("utf-8")

cry = rsa.encrypt(message,pub_key)

print(cry)

me = rsa.decrypt(cry,pri_key)

print(me)