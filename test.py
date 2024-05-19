unique_chars = set()
line ='all_imgs/37703.jpg	Vẫn'
_, label = line.strip().split('\t')
unique_chars.update(label)
print(unique_chars)