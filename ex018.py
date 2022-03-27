from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
rad = radians(ang)
print('O ângulo de {} tem o SEN de {:.2f}'.format(ang, sin(rad)))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos(rad)))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ang, tan(rad)))
