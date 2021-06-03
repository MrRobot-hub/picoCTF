import hashlib
import base64

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

username_trial = b"FREEMAN"

digest_positions = [4,5,3,6,2,7,1,8]

key = ""

for pos in digest_positions:
	key += hashlib.sha256(username_trial).hexdigest()[pos]
get_key = key_part_static1_trial + key + key_part_static2_trial

print(get_key)
