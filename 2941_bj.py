alb = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in alb:
    word = word.replace(i, '*')

print(len(word))