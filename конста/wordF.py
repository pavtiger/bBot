import pymorphy2
morph = pymorphy2.MorphAnalyzer()

f = open("Конституция_РФ.txt", "r")
file1 = open("наша_F_конституция.txt","w")

if f.mode == 'r':
    contents = f.read()

for word in f:
    file1.wrile(str(morph.parse(word)[0].normal_form.capitalize()))
    
'''r = list(set(morph.parse(nm)[0].normal_form.capitalize() for nm in str(f).split(' ')))
for elem in r:
    file1.write(elem)'''
    
f.close()
# print(contents)
