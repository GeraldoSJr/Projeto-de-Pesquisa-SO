def calculate_latency(current_block, target_block, was_seek=False):
    rotational_latency = 4  # 4ms de tempo de rotação
    transfer_time = 4 / 400  # Tempo de transferência de 4KB a 400MB/s
    
    if was_seek or current_block // 4 != target_block // 4:
        seek_time = 4  # 4ms de tempo de busca
    else:
        seek_time = 0  # Não há tempo de busca se estiver na mesma trilha
    
    total_latency = seek_time + rotational_latency + transfer_time
    return total_latency

def sstf_with_latency(requests, start_block):
    current_block = start_block
    total_seeks = 0
    total_latency = 0
    sequence = []

    while requests:
        closest_block = min(requests, key=lambda x: abs(x - current_block))
        was_seek = current_block // 4 != closest_block // 4  # Verifica se houve um seek
        total_seeks += 1 if was_seek else 0
        total_latency += calculate_latency(current_block, closest_block, was_seek)
        current_block = closest_block
        sequence.append(current_block)

        # Verifica se há outros valores na mesma trilha antes de retornar para o mesmo valor
        if any(x // 4 == current_block // 4 and x != current_block for x in requests):
            # Remove apenas o bloco acessado
            requests.remove(current_block)
        else:
            # Remove todos os valores na mesma trilha
            requests = [x for x in requests if x // 4 != current_block // 4]

    return sequence, total_seeks, total_latency

# Teste com uma lista de solicitações de exemplo
request_list = [3, 9, 12, 2, 16, 17, 11, 8]
request_list2 = [3, 4, 5, 13, 11, 17, 0, 10, 11, 7]
request_list3 = [7, 11, 10, 0, 17, 11, 13]
start = 6  # Bloco inicial

sequence, total_seeks, total_latency = sstf_with_latency(request_list, start)
sequence2, total_seeks2, total_latency2 = sstf_with_latency(request_list2, start)
sequence3, total_seeks3, total_latency3 = sstf_with_latency(request_list3, start)

print("Exemplo 1:")
print("Lista de requests:", request_list)
print("Ordem dos blocos acessados:", sequence)
print("Número total de seeks:", total_seeks)
print("Tempo total de latência:", total_latency, "ms")

print("\nExemplo 2:")
print("Lista de requests:", request_list2)
print("Ordem dos blocos acessados:", sequence2)
print("Número total de seeks:", total_seeks2)
print("Tempo total de latência:", total_latency2, "ms")

print("\nExemplo 3:")
print("Lista de requests:", request_list3)
print("Ordem dos blocos acessados:", sequence3)
print("Número total de seeks:", total_seeks3)
print("Tempo total de latência:", total_latency3, "ms")
