import os 

nucleo_to_bits = {'A': 0b00, 'C': 0b01, 'G': 0b10, 'T': 0b11}
bits_to_nucleo = {0b00: 'A', 0b01: 'C', 0b10: 'G', 0b11: 'T'}

def compactar_sequencia_bitwise(sequencia_dna):
    bits = 0
    for nucleotideo in sequencia_dna:
        bits = (bits << 2) | nucleo_to_bits[nucleotideo]
    return bits, len(sequencia_dna) * 2 

def salvar_sequencia_binaria(bits, num_bits, filename="dna_compactado.bin"):
    with open(filename, "wb") as file: 
        file.write(bits.to_bytes((num_bits + 7) // 8, byteorder='big'))
    print(f'\nSequência compactada salva em: {filename}')

def descompactar_sequencia_bitwise(bits, num_bits):
    sequencia_dna = ""
    for _ in range(num_bits // 2):
        sequencia_dna = bits_to_nucleo[bits & 0b11] + sequencia_dna 
        bits >>= 2
    return sequencia_dna

def compactar_e_salvar_bitwise(dna_sequence, filename="dna_compactado.bin"):
    bits, num_bits = compactar_sequencia_bitwise(dna_sequence)  
    salvar_sequencia_binaria(bits, num_bits, filename)
    return bits, num_bits 

def ler_e_descompactar(filename="dna_compactado.bin", num_bits=16):
    with open(filename, "rb") as file:
        bits = int.from_bytes(file.read(), byteorder='big')
    dna_sequence = descompactar_sequencia_bitwise(bits, num_bits)
    return dna_sequence

def comparar_tamanho_arquivos(original_file, compacted_file):
    original_size = os.path.getsize(original_file)
    compacted_size = os.path.getsize(compacted_file)

    print('\nResultado dos tamanhos:\n')
    print(f'Tamanho do arquivo original: {original_size} bytes')
    print(f'Tamanho do arquivo compactado: {compacted_size} bytes')
    print(f'Economia de espaço: {original_size - compacted_size} bytes')

# Exemplo de uso
dna_sequence = "ACGTAGCT"
bits, num_bits = compactar_e_salvar_bitwise(dna_sequence)

dna_descompactada = ler_e_descompactar(num_bits=num_bits)
print(f'Sequência descompactada: {dna_descompactada}')

with open("dna_original.txt", "w") as f:
    f.write(dna_sequence)

comparar_tamanho_arquivos("dna_original.txt", "dna_compactado.bin")