import math

# Constantes
c = 3.00e8  # velocidade da luz no vácuo (m/s)
mu_0 = 4 * math.pi * 1e-7  # permeabilidade magnética do vácuo (H/m)
epsilon_0 = 8.85e-12  # permissividade elétrica do vácuo (frequencia/m)

def intro():
    print("\nSeja bem vindo ao Programa de Estudo das Ondas Eletromagnéticas!\n")
    print("Este programa calcula parâmetros de ondas eletromagnéticas, incluindo frequência, comprimento de onda, número de onda, frequência angular, campo magnético, campo elétrico e intensidade.\nO usuário pode fornecer diferentes entradas e obter os parâmetros correspondentes como saída.\nO algoritimo é útil para compreender e calcular características de ondas eletromagnéticas com base em diferentes variáveis de entrada. As unidades de medida são rigorosamente aplicadas para garantir precisão nos cálculos.\n")
    print("Autores: Carlos, Tallysson e Cecilia\n")

def exibeMenu():
    print("\nMenu:\n")

    print("1. Entrada: f (frequência);\n   Saída: λ (comprimento de onda), k (número de onda), ω (frequência angular)\n\n")

    print("2. Entrada: λ (comprimento de onda);\n   Saída: f (frequência), k (número de onda), ω (frequência angular)\n\n")

    print("3. Entrada: k (número de onda);\n   Saída: f (frequência), λ (comprimento de onda), ω (frequência angular)\n\n")
    
    print("4. Entrada: ω (frequência angular);\n   Saída: f (frequência), λ (comprimento de onda), k (número de onda)\n\n")
    
    print("5. Entrada: Bm (campo magnético);\n   Saída: Em (campo elétrico) e I (intensidade)\n\n")

    print("6. Entrada: Em (campo elétrico);\n   Saída: Bm (campo magnético) e I (intensidade)\n\n")
    
    print("7. Entrada: I (intensidade)\n   Saída: Em (campo elétrico) e Bm (campo magnético)\n\n")

    print("8. Sair\n")

def menu():
    while True:
        exibeMenu()

        escolha = input("\nDigite o número correspondente à opção desejada: ")

        if escolha == "1":
            # Questão 1 - Uma onda eletromagnética tem frequência igual a 4.48×e8 Hz. Determine:
            frequencia = eval(input("\nDigite a frequência f (Hz): "))

            # Função: calcular_parametros_onda
            frequencia, comprimento_onda, k, omega = calcular_parametros_onda(frequencia=frequencia)

            # (a) O comprimento de onda em [m]:
            print(f"\nComprimento de onda λ (m): {comprimento_onda:.3e}")

            # (b) O número de onda em [rad/m]: )
            print(f"Número de onda k (rad/m): {k:.3e}")

            # (c) A frequência angular da onda em [rad/s]: 
            print(f"Frequência angular ω (rad/s): {omega:.3e}")

        elif escolha == "2":
            # Questão 2 - Uma onda eletromagnética tem comprimento de onda igual a 4.91×10-4 m. Determine:
            comprimento_onda = eval(input("\nDigite o comprimento de onda λ (m): "))

            # Função: calcular_parametros_onda
            frequencia, comprimento_onda, k, omega = calcular_parametros_onda(comprimento_onda=comprimento_onda)

            # (a) A frequência da onda em [Hz]:
            print(f"\nFrequência f (Hz): {frequencia:.3e}")

            # (b) O número de onda em [rad/m]: 
            print(f"Número de onda k (rad/m): {k:.3e}")

            # (c) A frequência angular da onda em [rad/s]: 
            print(f"Frequência angular ω (rad/s): {omega:.3e}")
        
        elif escolha == "3":
            # Questão 3 - Uma onda eletromagnética tem número de onda igual a 2.6×10-6 rad/m. Determine:
            k = float(input("\nDigite o número de onda k (rad/m): "))
            
            # Função: calcular_parametros_onda
            frequencia, comprimento_onda, k, omega = calcular_parametros_onda(k=k)
        
            # (a) A frequência da onda em [Hz]: 
            print(f"\nFrequência f (Hz): {frequencia:.3e}")
            
            # (b) O comprimento de onda em [m]: 
            print(f"Comprimento de onda λ (m): {comprimento_onda:.3e}")

            # (c) A frequência angular da onda em [rad/s]: 
            print(f"Frequência angular ω (rad/s): {omega:.3e}")
        
        elif escolha == "4":
            # Questão 4 - Uma onda eletromagnética tem frequência angular igual a 8.74×1013 rad/s. Determine:
            omega = float(input("\nDigite a frequência angular ω (rad/s): "))

            # Função: calcular_parametros_onda
            frequencia, comprimento_onda, k, omega = calcular_parametros_onda(omega=omega)
            
            # (a) O comprimento de onda em [m]: 
            print(f"\nComprimento de onda λ (m): {comprimento_onda:.3e}")

            # b) O número de onda em [rad/m]: 
            print(f"Número de onda k (rad/m): {k:.3e}")

            # (c) A frequência da onda em [Hz]: 
            print(f"Frequência f (Hz): {frequencia:.3e}")

        elif escolha == "5":
            # Questão 5 - Uma onda eletromagnética possui amplitude do campo magnético igual a 8 μT. Determine:
            bm = float(input("\nDigite a amplitude do campo magnético Bm (T): "))

            em = calcular_em_a_partir_de_bm(bm)
            i = calcular_i_a_partir_de_bm(bm)

            # (a) A amplitude do campo elétrico: 
            print(f"\nAmplitude do campo elétrico Em (V/m): {em:.3e}")
            
            # (b) A intensidade da onda: 
            print(f"Intensidade I (W/m²): {i:.3e}")

        elif escolha == "6":
            # Questão 6 - Uma onda eletromagnética possui amplitude do campo elétrico igual a 200 V/m. Determine:
            em = float(input("\nDigite a amplitude do campo elétrico Em (V/m): "))

            bm = calcular_bm_a_partir_de_em(em)
            i = calcular_i_a_partir_de_em(em)
            # (a) A amplitude do campo magnético: 
            print(f"\nAmplitude do campo magnético Bm (T): {bm:.3e}")

            # (b) A intensidade da onda:
            print(f"Intensidade I (W/m²): {i:.3e}")

        elif escolha == "7":
            # Questão 7 -Uma onda eletromagnética possui intensidade igual a 160 W/m2. Determine:
            i = float(input("\nDigite a intensidade I (W/m²): "))

            em = calcular_em_a_partir_de_i(i)
            bm = calcular_bm_a_partir_de_i(i)

            # (a) A amplitude do campo elétrico:
            print(f"\nAmplitude do campo elétrico Em (V/m): {em:.3e}")

            # (b) A amplitude do campo magnético:
            print(f"Amplitude do campo magnético Bm (T): {bm:.3e}")

        elif escolha == "8":
            print("\nSaindo do programa.\n")
            break
       
        else:
            print("\nOpção inválida! Tente novamente.")
            
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

def main():
    intro()

    while True:
        acessa = input("Deseja acessar o programa? 1 (Sim) e 2 (não): ")

        if acessa == "1":
            menu()
            break
        elif acessa == "2":
            break
        else:
            print("\nOpção inválida!\n")    

if __name__ == "__main__":
    main()
