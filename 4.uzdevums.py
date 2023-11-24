"""Izveidojiet Python programmu, kas aprēķina lietotāja ievadīta skaitļa faktoriālu, izmantojot for ciklu.
Izmantojiet GIT, lai izsekotu kodu un veidotu komitus."""

ievaditais_skaitlis = int(input("Ievadiet skaitli: "))

if ievaditais_skaitlis<0:
    print("Faktoriāls nepieder negatīviem skaitļiem")
else:
    faktorials=1

for skaitlis in range(1,ievaditais_skaitlis +1):
    faktorials*=skaitlis

    print(f'{ievaditais_skaitlis}! = {faktorials}')
