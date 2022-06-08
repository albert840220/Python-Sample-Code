# /myproject/converter.py
import mapping as mp

print(mp.name)
print(hasattr(mp, "name"))
print(getattr(mp, "name")["01"])
print(getattr(mp, "add")(3, 4))

# output
# {'01': 'Allen', '02': 'Jack', '03': 'Jessie'}
# True
# Allen
# 7
