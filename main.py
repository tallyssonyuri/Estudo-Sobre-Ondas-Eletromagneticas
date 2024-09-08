from functions import (
    calcular_bm_a_partir_de_em, calcular_i_a_partir_de_em,
    calcular_em_a_partir_de_bm, calcular_i_a_partir_de_bm,
    calcular_parametros_onda, calcular_em_a_partir_de_i,
    calcular_bm_a_partir_de_i, menu
)

def main():
    print("\nPrograma de Estudo das Ondas Eletromagnéticas")
    print("Descrição: Este programa calcula parâmetros de ondas eletromagnéticas.\n")
    print("Autores: Cecilia, Tallysson, Carlos")


    while True:
        menu()
        escolha = input("Escolha uma opção: ")

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

if __name__ == "__main__":
    main()
