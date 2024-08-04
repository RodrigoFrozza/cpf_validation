import os

# 123.456.789
# 10 - 1

def cpf_validation_1(cpf):
    nove_digitos = cpf[:9]
    primeiro_digito = cpf[10]
    contador_regressivo = 10
    digito_1 = 0

    for digito in nove_digitos:
        digito_1 += int(digito) * contador_regressivo
        contador_regressivo -= 1
    
    digito_1 = (digito_1 * 10) % 11
    print(digito_1)


def main():

    while True:
        cpf = input('Digite um cpf (Apenas Números): ')

        if len(cpf) > 11 or len(cpf) <= 0:
            print('CPF precisa conter 11 Digitos.')
            continue
        else:
            cpf_validation_1(cpf)

if __name__ == '__main__':
    main()

