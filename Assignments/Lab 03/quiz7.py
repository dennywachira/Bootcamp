#results to an Error (NameError: name 'stdio' is not defined)

f=0
g=1

for i in range(0,16):
    f=f+g
    g=f-g
    stdio.writeln(f)