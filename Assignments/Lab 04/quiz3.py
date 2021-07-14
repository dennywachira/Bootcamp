 #NameError: name 'stdarray' is not defined     
a= stdarray.createID(10,0)
for i in range(10):
    a[i]=9-1
for i in range(10):
         a[i]=a[a[i]]
for v in a:
     stdio.writeln(v)