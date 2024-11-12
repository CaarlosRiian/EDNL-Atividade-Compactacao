nucleo_to_bits = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}
bits_to_nucleo = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}

# Compactar
def compactar_sequencia(sequencia_dna):
    sequencia_bits = ""
    for nucletideo in sequencia_dna:
        sequencia_bits += nucleo_to_bits[nucletideo]
    return sequencia_bits
    
def salvar_sequencia_compactada(sequencia_bits, filename="dna_compactado.txt"):
    with open(filename, "w") as file:
        file.write(sequencia_bits)
    print(f'A Sequência compactada foi salva em: {filename}')

def compactar_e_salvar(sequencia_dna, filename="dna_compactado.txt"):
    sequencia_bits = compactar_sequencia(sequencia_dna)
    salvar_sequencia_compactada(sequencia_bits, filename) 

# Descompactar

def descompactar_sequencia(sequencia_bits):
    sequencia_dna = ""
    for i in range(0, len(sequencia_bits), 2):
        bits = sequencia_bits[i:i + 2]
        sequencia_dna += bits_to_nucleo[bits]
    return sequencia_dna

def leitura_descompactacao(filename="dna_compactado.txt"):
    with open(filename, "r") as file:
        sequencia_bits = file.read()
    sequencia_dna = descompactar_sequencia(sequencia_bits)
    return sequencia_dna


# Exemplos de uso ( Compactado ): 
sequencia_dna = "ACGTACT"
compactar_e_salvar(sequencia_dna)

# Exemplos de uso ( Descompactado ):
print(f'Resultado Descompactado\n')
dna_recuperado = leitura_descompactacao()
print(f'Sequência descompactada: {dna_recuperado}')