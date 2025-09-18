def imprimir_tabuleiro(tabuleiro):
    for i in range(0, 9, 3):
        print(f" {tabuleiro[i]} | {tabuleiro[i+1]} | {tabuleiro[i+2]} ")
        if i < 6:
            print("-----------")

def verificar_vitoria(tabuleiro):
    combinacoes = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for combo in combinacoes:
        if tabuleiro[combo[0]] == tabuleiro[combo[1]] == tabuleiro[combo[2]] != ' ':
            return tabuleiro[combo[0]]
    return None

def jogo_da_velha():
    tabuleiro = [' '] * 9
    jogador_atual = 'X'
    
    print("Jogo da Velha!")
    print("Posições: 1-9")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print()
    
    for jogada in range(9):
        imprimir_tabuleiro(tabuleiro)
        
        try:
            posicao = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): \n")) - 1
            if posicao < 0 or posicao > 8 or tabuleiro[posicao] != ' ':
                print("Posição inválida! Tente novamente.")
                continue
        except ValueError:
            print("Digite um número válido!")
            continue
        
        tabuleiro[posicao] = jogador_atual
        
        vencedor = verificar_vitoria(tabuleiro)
        if vencedor:
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {vencedor} venceu!")
            return
        
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'
    
    imprimir_tabuleiro(tabuleiro)
    print("Empate!")

if __name__ == "__main__":
    jogo_da_velha()
