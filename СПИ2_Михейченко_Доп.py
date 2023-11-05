
#задание 1, сотрите 2 и 3. запустите код.
vc = int(input()) 
ff = int(input()) 
vv = int(input()) 

for i in range(vc,ff+ vv,vv ): 
    for k in range(vc,ff+ vv,vv ): 
        print(f'{i} + {k} = {i + k}', end='\t') 
print()
#задание 2. ctrl+z верните всё назат и сотрите код 1 и 3.
aaad = []
while True:
    vvv= input()
    if not vvv: 
        break
    if len (vvv) ==len (set(vvv)) : 
        aaad.append (vvv)
print(aaad, sep='\n')

# ctrl+z и сотрите код 1,2 запустите код 3.
fds=int(input())
for i in range(1,fds +1):
    if i % 7:
        print (f'Пройдена!! {i % 7} миля.')
    else:
        print ('Крюк!!!!!!!!!!!!)')
