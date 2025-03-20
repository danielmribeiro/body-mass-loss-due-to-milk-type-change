#GanhoDeMassaCorporal_Leite.py
# Permite calcular a massa corporal aquando do consumo de uma certa quantidade e qualidade de leite.

def GanhoDeMassaCorporal_Leite():
    KcalPorMl_M = 0.39
    KcalPorMl_MG =0.48
    KcalPorMl_G =0.64
    KgPorKcal =0.00013


    Q1=0
    while((Q1<=0)or (Q1>99999.99)):
        Q1=eval(input("Qual a quantidade de leite que costuma beber de uma só vez [ml]?"))

    V1=0
    while((V1<=0)or (V1>999)):
        V1=eval(input("Quantas vezes toma leite por dia?"))

    V2=0
    while( (V2<=0) or (V2>99999) ):
        V2=eval(input("Quer calcular o ganho de massa para quantos dias?"))

    TL="x"
    # TL = "M" OU TL = "MG" OU TL = "G"
    while((TL != "M" )and (TL != "MG")and (TL != "G")):
        # Introduza o caractere que corresponde ao tipo de leite singular para o qual pretende calcular a massa ganha [M-Magro, Mg-MeioGordo, G-Gordo?
        TL=input("Tipo de leite [M-Magro, MG-MeioGordo, G-Gordo?")
    Q2=V1*Q1
    Q3=V2*Q2
    if (TL=="M"):
        c= Q3*KcalPorMl_M
    else:
          if(TL=="MG"):
              c= Q3*KcalPorMl_MG
          else:
              c= Q3*KcalPorMl_G

    massa=c*KgPorKcal
    print("Massa Ganha: ", massa, "Kg")
          

GanhoDeMassaCorporal_Leite()
