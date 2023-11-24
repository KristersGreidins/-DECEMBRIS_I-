"""Izveidojiet Python programmu, kas saskaita no 1 līdz lietotāja ievadītam skaitlim, izmantojot for ciklu.
Izmantojiet GIT, lai izsekotu izmaiņas programmas kodā un izveidotu komitus, tos ievietojot arī GITHUB."""

ievaditais_skaitlis=int(input("Ievadiet skaitli: "))
summa=0
for skaitlis in range (ievaditais_skaitlis+1):
    summa+=skaitlis

    print(f'Summa ir: {ievaditais_skaitlis}')

