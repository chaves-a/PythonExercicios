for n in range(2, 51, 2):
    print(n, end=' ')
print('Acabou')


# tem a forma abaixo de implementar... mas essa forma faz iterações desnecessárias
# ele itera mais vezes sem necessidade e ocupa mais o processador

'''
for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=' ')
print('Acabou')
'''