import math

# Constantes
c = 3.00e8  # velocidade da luz no vácuo (m/s)
mu_0 = 4 * math.pi * 1e-7  # permeabilidade magnética do vácuo (H/m)
epsilon_0 = 8.85e-12  # permissividade elétrica do vácuo (frequencia/m)

def menu():
    print("\nMenu:\n")

    print("1. Entrada: f (frequência);\n   Saída: λ (comprimento de onda), k (número de onda), ω (frequência angular)\n\n")

    print("2. Entrada: λ (comprimento de onda);\n   Saída: f (frequência), k (número de onda), ω (frequência angular)\n\n")

    print("3. Entrada: k (número de onda);\n   Saída: f (frequência), λ (comprimento de onda), ω (frequência angular)\n\n")
    
    print("4. Entrada: ω (frequência angular);\n   Saída: f (frequência), λ (comprimento de onda), k (número de onda)\n\n")
    
    print("5. Entrada: Bm (campo magnético);\n   Saída: Em (campo elétrico) e I (intensidade)\n\n")

    print("6. Entrada: Em (campo elétrico);\n   Saída: Bm (campo magnético) e I (intensidade)\n\n")
    
    print("7. Entrada: I (intensidade)\n   Saída: Em (campo elétrico) e Bm (campo magnético)\n\n")

    print("8. Sair\n")

# Questão 1 - Uma onda eletromagnética tem frequência igual a 4.48×e8 Hz. 
# Questão 2 - Uma onda eletromagnética tem comprimento de onda igual a 4.91×10-4 m. Determine:
# Questão 3 - Uma onda eletromagnética tem número de onda igual a 2.6×10-6 rad/m. Determine:
# Questão 4 - Uma onda eletromagnética tem frequência angular igual a 8.74×1013 rad/s. Determine:
def calcular_parametros_onda(frequencia=None, comprimento_onda=None, k=None, omega=None):

    # Questão 1 - Uma onda eletromagnética tem frequência igual a 4.48×e8 Hz. 
    if frequencia is not None:
        comprimento_onda = c / frequencia
        k = 2 * math.pi / comprimento_onda
        omega = 2 * math.pi * frequencia
    
    # Questão 2 - Uma onda eletromagnética tem comprimento de onda igual a 4.91×10-4 m. Determine:
    elif comprimento_onda is not None:
        frequencia = c / comprimento_onda
        k = 2 * math.pi / comprimento_onda
        omega = 2 * math.pi * frequencia
    
    # Questão 3 - Uma onda eletromagnética tem número de onda igual a 2.6×10-6 rad/m. Determine:
    elif k is not None:
        comprimento_onda = 2 * math.pi / k
        frequencia = c / comprimento_onda
        omega = c * k

    # Questão 4 - Uma onda eletromagnética tem frequência angular igual a 8.74×1013 rad/s. Determine:
    elif omega is not None:
        frequencia = omega / (2 * math.pi)
        comprimento_onda = c / frequencia
        k = 2 * math.pi / comprimento_onda

    return frequencia, comprimento_onda, k, omega

# Questão 5 - Uma onda eletromagnética possui amplitude do campo magnético igual a 8 μT. Determine:
def calcular_em_a_partir_de_bm(bm):
    return bm * c

# Questão 5 - Uma onda eletromagnética possui amplitude do campo magnético igual a 8 μT. Determine:
def calcular_i_a_partir_de_bm(bm):
    return ((bm**2) * c) / (2 * mu_0)

# Questão 6 - Uma onda eletromagnética possui amplitude do campo elétrico igual a 200 V/m. Determine:
def calcular_bm_a_partir_de_em(em):
    return em / c

# Questão 6 - Uma onda eletromagnética possui amplitude do campo elétrico igual a 200 V/m. Determine:
def calcular_i_a_partir_de_em(em):
    return 0.5 * em**2 / (mu_0 * c)

# Questão 7 -Uma onda eletromagnética possui intensidade igual a 160 W/m2. Determine:
def calcular_em_a_partir_de_i(i):
    return math.sqrt(2 * i / (c * epsilon_0))

# Questão 7 -Uma onda eletromagnética possui intensidade igual a 160 W/m2. Determine:""
def calcular_bm_a_partir_de_i(i):
    em = calcular_em_a_partir_de_i(i)
    return em / c
