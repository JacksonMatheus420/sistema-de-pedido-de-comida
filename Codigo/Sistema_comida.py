# --- FUNÇÃO AUXILIAR PARA LIMPAR O TEXTO ---
def normalizar_texto(texto):
    # Transforma tudo em minúsculo
    texto = texto.lower()
    # Substitui letras com acentos por letras normais
    texto = texto.replace("ú", "u").replace("ú", "u")
    texto = texto.replace("á", "a").replace("ã", "a").replace("â", "a")
    texto = texto.replace("é", "e").replace("ê", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o").replace("ô", "o").replace("õ", "o")
    # Remove espaços extras que o usuário possa ter digitado sem querer
    return texto.strip()


# --- BANCO DE DADOS DO RESTAURANTE ---
menu = {
    "Hambúrguer": 15.00,
    "Batata Frita": 8.00,
    "Refrigerante": 5.00,
    "Sobremesa": 7.50
}

def exibir_menu():
    print("\n--- MENU DO RESTAURANTE ---")
    for prato, preco in menu.items():
        print(f"- {prato}: R$ {preco:.2f}")
    print("---------------------------\n")

def calcular_taxa_entrega(distancia_km):
    return distancia_km * 1.50


# --- EXECUÇÃO INTERATIVA COM CARRINHO DE COMPRAS ---

exibir_menu()
carrinho = []

while True:
    entrada_usuario = input("Digite o nome do item (or digite 'FIM' para fechar): ")
    
    # Se digitar fim, FIM, Fim, etc., o sistema aceita do mesmo jeito
    if entrada_usuario.upper() == "FIM":
        break
        
    # Variável para controlar se encontramos o item ou não
    item_encontrado = False
    
    # Passamos por cada prato real do menu para comparar com o que o usuário digitou
    for prato_real in menu.keys():
        # Comparamos os dois textos "limpos" (sem acento e minúsculos)
        if normalizar_texto(entrada_usuario) == normalizar_texto(prato_real):
            item_encontrado = True
            qtd = int(input(f"Quantas unidades de {prato_real} você quer? "))
            
            preco_total_item = menu[prato_real] * qtd
            carrinho.append({"nome": prato_real, "quantidade": qtd, "subtotal": preco_total_item})
            print(f"✓ {qtd}x {prato_real} adicionado ao carrinho!\n")
            break # Para o loop 'for' pois já achamos o item correto
            
    if not item_encontrado:
        print("✕ Item não encontrado. Tente digitar novamente.\n")


# --- FECHAMENTO DO PEDIDO ---
if len(carrinho) > 0:
    distancia = float(input("\nQual a distância para entrega em KM? "))
    taxa_entrega = calcular_taxa_entrega(distancia)
    
    subtotal_restaurante = 0
    print("\n====== RECIBO DO PEDIDO ======")
    for pedido in carrinho:
        print(f"- {pedido['nome']} (x{pedido['quantidade']}): R$ {pedido['subtotal']:.2f}")
        subtotal_restaurante += pedido['subtotal']
        
    total_geral = subtotal_restaurante + taxa_entrega
    print("------------------------------")
    print(f"Subtotal Comidas: R$ {subtotal_restaurante:.2f}")
    print(f"Taxa de Entrega:  R$ {taxa_entrega:.2f}")
    print("------------------------------")
    print(f"TOTAL A PAGAR:    R$ {total_geral:.2f}")
    print("==============================")
else:
    print("\nNenhum item foi adicionado. Pedido cancelado.")

input("\nPressione Enter para fechar o terminal...")