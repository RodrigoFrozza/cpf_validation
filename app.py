import os

def cpf_validation_1(cpf): #valida o primeiro digito do CPF
    nove_digitos = cpf[:9]
    primeiro_digito = int(cpf[9])
    contador_regressivo = 10
    digito_1 = 0

    for digito in nove_digitos:
        digito_1 += int(digito) * contador_regressivo
        contador_regressivo -= 1
    
    digito_1 = (digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    if digito_1 == primeiro_digito:
        return digito_1
    else:
        return None
        
def cpf_validation_2(cpf): #valida o segundo digito do CPF
    dez_digitos = cpf[:10]
    segundo_digito = int(cpf[10])
    contador_regressivo = 11
    digito_2 = 0

    for digito in dez_digitos:
        digito_2 += int(digito) * contador_regressivo
        contador_regressivo -= 1
    
    digito_2 = (digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    if digito_2 == segundo_digito:
        return digito_2
    else:
        return None

def main():
    primeiro_digito = 0
    segundo_digito = 0

    while True:
        os.system('cls')

        cpf = input('Digite um cpf (Apenas Números): ')

        if len(cpf) != 11 or not cpf.isdigit():
            os.system('cls')
            print('CPF precisa conter somente 11 Digitos (sem pontos e traços).')
            input('Aperte ENTER para recomeçar...')
            continue
        else:
            primeiro_digito = cpf_validation_1(cpf)

        if primeiro_digito == None:
            os.system('cls')
            print('CPF Inválido')
            input('Aperte ENTER para recomeçar...')
            continue

        segundo_digito = cpf_validation_2(cpf)

        if segundo_digito == None:
            os.system('cls')            
            print('CPF Inválido')
            input('Aperte ENTER para recomeçar...')
            continue
        
        print(f'O CPF {cpf} é um CPF válido!')
        break
            


if __name__ == '__main__':
    main()

