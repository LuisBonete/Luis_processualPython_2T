import random

lista_nomes = []

for i in range(1, 7):
    nome = input(f"Insira o {i}º nome aqui: ")
    lista_nomes.append(nome)

# Inicializa as variáveis de ação para garantir que existam, mesmo que não haja alvos
assassinato = None
salvo = None
investigado = None

if len(lista_nomes) >= 6:
    # Escolhe 3 nomes diferentes para as funções principais
    nomes_para_funcoes = random.sample(lista_nomes, 3)

    impostor = nomes_para_funcoes[0]
    detetive = nomes_para_funcoes[1]
    anjo = nomes_para_funcoes[2]

    # Identifica os inocentes (nomes que não foram atribuídos a funções)
    inocentes = [nome for nome in lista_nomes if nome not in nomes_para_funcoes]

    print(f"\n--- Atribuição de Funções ---")
    print(f"O {impostor} será o Impostor!")
    print(f"O {detetive} será o Detetive!")
    print(f"O {anjo} será o Anjo!")
    print(f"O resto é Inocente: {inocentes}")
    print(f"---------------------------\n")

    print("\nCidade dorme!")
    print("\nNa primeira noite o Impostor escolheu alguém para matar, o Detetive escolheu alguém para investigar, e o Anjo escolheu alguém para salvar!")

    # Impostor escolhe alguém para matar (não pode ser ele mesmo)
    alvos_impostor = [nome for nome in lista_nomes if nome != impostor]
    if alvos_impostor:
        assassinato = random.choice(alvos_impostor)
        print(f"\nO Impostor ({impostor}) escolheu {assassinato} para assassinar.")
    else:
        print(f"\nO Impostor ({impostor}) não tem ninguém para assassinar (lista de alvos vazia).")

    # Detetive escolhe alguém para investigar (não pode ser ele mesmo)
    alvos_detetive = [nome for nome in lista_nomes if nome != detetive]
    if alvos_detetive:
        investigado = random.choice(alvos_detetive)
        print(f"\nO Detetive ({detetive}) escolheu {investigado} para investigar.")
    else:
        print(f"\nO Detetive ({detetive}) não tem ninguém para investigar (lista de alvos vazia).")

    # Anjo escolhe alguém para salvar (não pode ser ele mesmo)
    alvos_anjo = [nome for nome in lista_nomes if nome != anjo]
    if alvos_anjo:
        salvo = random.choice(alvos_anjo)
        print(f"\nO Anjo ({anjo}) escolheu {salvo} para salvar.")
    else:
        print(f"\nO Anjo ({anjo}) não tem ninguém para salvar (lista de alvos vazia).")

    print("\nResponda com 'sim' ou 'não' para as próximas perguntas.")
    pergunta1 = input("O Anjo salvou a mesma pessoa que o Impostor matou? ")
    pergunta2 = input("O Detetive escolheu o Impostor? ")

    # Lógica para a pergunta 1: A vítima do Impostor foi salva pelo Anjo?
    if assassinato is not None: # Verifica se houve um assassinato
        if pergunta1.lower() == 'não':
            # Se a resposta for 'não', a pessoa assassinada é removida da lista
            if assassinato in lista_nomes:
                lista_nomes.remove(assassinato)
                print(f"\n{assassinato} foi eliminado(a) do jogo!")
            else:
                print(f"\n{assassinato} já não estava na lista (ou não foi assassinado).")
        elif pergunta1.lower() == 'sim':
            # Se a resposta for 'sim', a pessoa assassinada permanece na lista
            print(f"\n{assassinato} foi salvo(a) pelo Anjo e permanece no jogo!")
        else:
            print("\nResposta inválida para a pergunta do Anjo. Nenhuma ação de eliminação foi tomada.")
    else:
        print("\nNinguém foi assassinado nesta noite.")

    # Lógica para a pergunta 2: O Detetive encontrou o Impostor?
    if pergunta2.lower() == 'sim':
        print("\nFim de jogo! O Detetive encontrou o Impostor!")
    elif pergunta2.lower() == 'não':
        print("\nO jogo continua...")
    else:
        print("\nResposta inválida para a pergunta do Detetive. O jogo continua.")

    # Mostra a lista de nomes atualizada após a noite (se houver eliminação)
    print(f"\nParticipantes restantes: {lista_nomes}")


 print("\nCidade dorme!")
    print("\nNa primeira noite o Impostor escolheu alguém para matar, o Detetive escolheu alguém para investigar, e o Anjo escolheu alguém para salvar!")

    # Impostor escolhe alguém para matar (não pode ser ele mesmo)
    alvos_impostor = [nome for nome in lista_nomes if nome != impostor]
    if alvos_impostor:
        assassinato = random.choice(alvos_impostor)
        print(f"\nO Impostor ({impostor}) escolheu {assassinato} para assassinar.")
    else:
        print(f"\nO Impostor ({impostor}) não tem ninguém para assassinar (lista de alvos vazia).")

    # Detetive escolhe alguém para investigar (não pode ser ele mesmo)
    alvos_detetive = [nome for nome in lista_nomes if nome != detetive]
    if alvos_detetive:
        investigado = random.choice(alvos_detetive)
        print(f"\nO Detetive ({detetive}) escolheu {investigado} para investigar.")
    else:
        print(f"\nO Detetive ({detetive}) não tem ninguém para investigar (lista de alvos vazia).")

    # Anjo escolhe alguém para salvar (não pode ser ele mesmo)
    alvos_anjo = [nome for nome in lista_nomes if nome != anjo]
    if alvos_anjo:
        salvo = random.choice(alvos_anjo)
        print(f"\nO Anjo ({anjo}) escolheu {salvo} para salvar.")
    else:
        print(f"\nO Anjo ({anjo}) não tem ninguém para salvar (lista de alvos vazia).")

    print("\nResponda com 'sim' ou 'não' para as próximas perguntas.")
    pergunta1 = input("O Anjo salvou a mesma pessoa que o Impostor matou? ")
    pergunta2 = input("O Detetive escolheu o Impostor? ")

    # Lógica para a pergunta 1: A vítima do Impostor foi salva pelo Anjo?
    if assassinato is not None: # Verifica se houve um assassinato
        if pergunta1.lower() == 'não':
            # Se a resposta for 'não', a pessoa assassinada é removida da lista
            if assassinato in lista_nomes:
                lista_nomes.remove(assassinato)
                print(f"\n{assassinato} foi eliminado(a) do jogo!")
            else:
                print(f"\n{assassinato} já não estava na lista (ou não foi assassinado).")
        elif pergunta1.lower() == 'sim':
            # Se a resposta for 'sim', a pessoa assassinada permanece na lista
            print(f"\n{assassinato} foi salvo(a) pelo Anjo e permanece no jogo!")
        else:
            print("\nResposta inválida para a pergunta do Anjo. Nenhuma ação de eliminação foi tomada.")
    else:
        print("\nNinguém foi assassinado nesta noite.")

    # Lógica para a pergunta 2: O Detetive encontrou o Impostor?
    if pergunta2.lower() == 'sim':
        print("\nFim de jogo! O Detetive encontrou o Impostor!")
    elif pergunta2.lower() == 'não':
        print("\nO jogo continua...")
    else:
        print("\nResposta inválida para a pergunta do Detetive. O jogo continua.")

    # Mostra a lista de nomes atualizada após a noite (se houver eliminação)
    print(f"\nParticipantes restantes: {lista_nomes}")


else:
    print(f"A lista de nomes precisa ter 6 participantes para este jogo. Você inseriu apenas {len(lista_nomes)}.")
