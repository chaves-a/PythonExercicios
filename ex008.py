m = float(input('Uma distância em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('A medida de {}m corresponde a: '.format(m))
print('{}km \n{}hm \n{}dam'.format(km, hm, dam))
print('{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(dm, cm, mm))
