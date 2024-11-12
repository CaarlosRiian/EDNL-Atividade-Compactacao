import time
import os
import psutil

def measure_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024 

def measure_performance(func, *args):
    start_time = time.time() 
    memory_before = measure_memory() 
    result = func(*args)  
    memory_after = measure_memory() 
    end_time = time.time() 
    execution_time = end_time - start_time  
    memory_used = memory_after - memory_before  
    return execution_time, memory_used, result

def compactar_sequencia_string(sequencia_dna):
    nucleo_to_bits = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}
    return ''.join([nucleo_to_bits[nucleotideo] for nucleotideo in sequencia_dna])

def descompactar_sequencia_string(bits):
    bits_to_nucleo = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
    return ''.join([bits_to_nucleo[bits[i:i+2]] for i in range(0, len(bits), 2)])

def compactar_sequencia_bitwise(sequencia_dna):
    bits = 0
    for nucleotideo in sequencia_dna:
        bits = (bits << 2) | {'A': 0b00, 'C': 0b01, 'G': 0b10, 'T': 0b11}[nucleotideo]
    return bits

def descompactar_sequencia_bitwise(bits, num_bits):
    sequencia_dna = ""
    for _ in range(num_bits // 2):
        sequencia_dna = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}[bin(bits & 0b11)[2:].zfill(2)] + sequencia_dna
        bits >>= 2
    return sequencia_dna

def gerar_sequencia_dna(tamanho):
    import random
    return ''.join(random.choice('ACGT') for _ in range(tamanho))

def comparar_tamanho_arquivos(original_file, compacted_file):
    original_size = os.path.getsize(original_file)
    compacted_size = os.path.getsize(compacted_file)
    print(f'Tamanho do arquivo original: {original_size} bytes')
    print(f'Tamanho do arquivo compactado: {compacted_size} bytes')
    print(f'Economia de espaço: {original_size - compacted_size} bytes')

tamanhos = [100, 1000, 2500, 5000, 7500, 10000]

print(f'\nResultados Esperados: \n')

for tamanho in tamanhos:
    print(f'\nTamanho da sequência: {tamanho} nucleotídeos')
    dna_sequence = gerar_sequencia_dna(tamanho)

    print('Analisando compactação/descompactação com String...')
    execution_time, memory_used, _ = measure_performance(compactar_sequencia_string, dna_sequence)
    print(f'Tempo de execução (compactação): {execution_time:.6f} segundos')
    print(f'Memória usada (compactação): {memory_used:.2f} MB')

    execution_time, memory_used, _ = measure_performance(descompactar_sequencia_string, compactar_sequencia_string(dna_sequence))
    print(f'Tempo de execução (descompactação): {execution_time:.6f} segundos')
    print(f'Memória usada (descompactação): {memory_used:.2f} MB')

    print('Analisando compactação/descompactação com Bitwise...')
    execution_time, memory_used, _ = measure_performance(compactar_sequencia_bitwise, dna_sequence)
    print(f'Tempo de execução (compactação): {execution_time:.6f} segundos')
    print(f'Memória usada (compactação): {memory_used:.2f} MB')

    execution_time, memory_used, _ = measure_performance(descompactar_sequencia_bitwise, compactar_sequencia_bitwise(dna_sequence), tamanho * 2)
    print(f'Tempo de execução (descompactação): {execution_time:.6f} segundos')
    print(f'Memória usada (descompactação): {memory_used:.2f} MB')

    with open("dna_original.txt", "w") as f:
        f.write(dna_sequence)

    with open("dna_compactado.bin", "wb") as f:
        f.write(compactar_sequencia_bitwise(dna_sequence).to_bytes((tamanho * 2 + 7) // 8, byteorder='big'))
    
    comparar_tamanho_arquivos("dna_original.txt", "dna_compactado.bin")
