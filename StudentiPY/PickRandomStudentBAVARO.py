import random
#####STUDENTI COL PDP: BAVARO, CAPOZZI, QUARTO, SIBILANO, DE GIOSA. Commentarli usando ---> #
                                                                   #accanto al nome. Esempio:
#"Bavaro",


def get_students():
    studenti: list[str] = [
        "1 - Annese",
        "2 - Auriole",
        # "3 - Bavaro",
        # "4 - Capozzi",
        "5 - Casadibari",
        "6 - Cippone",
        "7 - Coppolecchia",
        # "8 - De Giosa",
        "9 - Ficarella",
        "10 - Francabandera",
        "11 - Genchi",
        "12 - Greco",
        "13 - Illiano",
        "14 - Lacolla",
        "15 - Lattanzio",
        "16 - Leone",
        "17 - Linciano",
        "18 - Pugliese",
        # "19 - Quarto",
        "20 - Raudino",
        "21 - Recchimurzi",
        "22 - Rotondo",
        "23 - Sanese",
        # "24 - Sibilano",
        "25 - Tenerelli"
    ]

    #print("-" * 29, "Programma-sorteggio-interrogati-BAVARO", "-" * 29)
    #print("La classe è composta dai seguenti studenti:")
    #for i in range(studenti.__len__()):
    #    print(studenti[i])
    ##Utilizzando random.sample, gli passo la variabile lista "studenti" e la variabile k (2 in questo caso), che rappresenta il numero di elementi
    ##da estrarre dalla lista.
    studenti_interrogati = random.sample(studenti, 2)
    return studenti_interrogati