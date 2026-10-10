nivel = [ "Nível 1",  "Nível 2",  "Nível 3",  "Nível 4",  "Nível 5" ]

print("Níveis de água:")
for niveis in nivel:
    print("->", niveis)

Informe_nivel = int(input("Informe o nível atual (de 1 a 5): "))

from colorama import Fore, Style

if Informe_nivel == 1:
    print(Fore.GREEN + "Nível muito baixo (crítico)")

elif Informe_nivel == 2:
    print(Fore.YELLOW + "Nível baixo")
 
elif Informe_nivel == 3:
    print(Fore.RED + "Nível médio")

elif Informe_nivel == 4:
    print(Fore.CYAN + "Nível alto")

elif Informe_nivel == 5:
    print(Fore.BLUE + "Nível muito alto (alerta)")

else:
    print("Digite um valor válido entre 1 e 5:")
 

print(Style.RESET_ALL)