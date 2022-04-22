# Programa que vai classificar a categoria de um atléta de natação pela sua idade.

from datetime import date
print('-='*20)
print('\033[0;0;36mCLASSIFICAÇÃO DE ATLÉTAS PARA NATAÇÃO\033[m')
print('-='*20)
atual = date.today().year
ano = int(input('Digite o ano de nascimento do atléta: '))
idade = (atual - ano)
if idade <= 9:
    print('''Este atléta nasceu em \033[1;0;0m{}\033[m.
    Está na categoria \033[0;0;33mMIRIM.\033[m.'''.format(ano))
elif idade <= 14:
    print('''Este atléta nasceu em \033[1;0;0m{}\033[m.
    Está na categoria \033[0;0;33mINFANTIL.\033[m.'''.format(ano))
elif idade <= 19:
    print('''Este atléta nasceu em \033[1;0;0m{}\033[m.
    Está na categoria \033[0;0;33mJUNIOR.\033[m.'''.format(ano))
elif idade <= 25:
    print('''Este atléta nasceu em \033[1;0;0m{}\033[m.
    Está na categoria \033[0;0;33mSÊNIOR.\033[m.'''.format(ano))
else:
    print('''Este atléta nasceu em \033[1;0;0m{}\033[m.
    Está na categoria \033[0;0;33mMASTER.\033[m.'''.format(ano))
print('-='*20)


