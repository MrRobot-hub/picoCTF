"""
Author: Umer Farid
Rot-13 decryptor in Python

"""

class Rot_13:
    def __init__(self, string, shift_value) -> None:
        self.string = string
        self.shift_value = shift_value
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        self.decrypted_txt = ''

    def decryptor(self):
        for i in self.string:
            if i in self.letters:
                if i.isupper():
                    self.decrypted_txt += self.letters[self.letters.index(i) + self.shift_value].capitalize()
                else:
                    self.decrypted_txt += self.letters[self.letters.index(i) + self.shift_value]
            else:
                self.decrypted_txt += i 
        return self.decrypted_txt

enc_text = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}"

dec_rot_13 = Rot_13(string = enc_text, shift_value = 13).decryptor()
print(dec_rot_13)
