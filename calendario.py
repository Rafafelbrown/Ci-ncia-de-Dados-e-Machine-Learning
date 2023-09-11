import calendar
yy = int( input ("qual ano\n"))
mm = int( input (" qual mes\n"))
conteudo = print(calendar . month (yy, mm))
filename = (f'resultado{mm}{yy}.txt')

with open(f'{filename}', 'w') as f:
    f.write(calendar.month(yy, mm))
with open(filename, 'r') as f:
    conteudo = f .read(f"{f}")
    if f != conteudo:
      print(f"{conteudo}")