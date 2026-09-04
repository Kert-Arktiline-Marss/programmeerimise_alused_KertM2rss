print("Hello World!")

nimi = input("sisesta enda nimi : ")
print(f"Tere {nimi}")
print("")

'''test arvutamine
print(f"5+5 = {5+5}")
print(f"5-2 = {5-2}")
print(f"2-5 = {2-5}")
print(f"10*2 = {10*2}")
'''

#Väga kergelt kasutatav kalkulaator
#E_arv = esimene arv. T_arv = teine arv
#F_arv = "First" arv. S_arv = "Second" arv
E_arv = input("sisesta esimene arv: ")
operator = input("sisesta operaator (+, -, /, *): ")
T_arv = input("sisesta teine arv: ")

if operator == "+":
    F_arv = int(E_arv)
    S_arv = int(T_arv)
    print(f"{E_arv} + {T_arv} = {F_arv + S_arv}")
elif operator == "-":
    F_arv = int(E_arv)
    S_arv = int(T_arv)
    print(f"{E_arv} - {T_arv} = {F_arv - S_arv}")
elif operator == "*":
    F_arv = int(E_arv)
    S_arv = int(T_arv)
    print(f"{E_arv} * {T_arv} = {F_arv * S_arv}")
elif operator == "/":
    F_arv = int(E_arv)
    S_arv = int(T_arv)
    print(f"{E_arv} / {T_arv} = {F_arv / S_arv}")