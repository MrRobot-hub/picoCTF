
file = open("enc", "r").read()
shifted = "" #pcCF1_isis3do__1107
for i in file:
    shifted += chr(ord(i) >> 8)

shifted2 = "" #ioT{6bt_nt4_f8e4af}
for j in range(len(file)):
    shifted2 += chr(ord(file[j])-(ord(shifted[j]) << 8))

for i in range(len(shifted)):
    print(shifted[i], end="")
    print(shifted2[i], end="")
