def valida_cpf(cpf):

    cpf = ''.join(filter(str.isdigit, cpf))


    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0

    if cpf[-2:] == str(digito1) + str(digito2):
        return True
    else:
        return False


 # Coloca aqui o CPF  
cpf = ("13550223472")
if valida_cpf(cpf):
    print('CPF válido')
else:
    print('CPF inválido')


# Criador: Matheus A.
# curso de ciencias da computação 3° período 