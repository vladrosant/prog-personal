##################          EXERCÍCIO 18         ##################
print('Programa de velocidade de download.\n')

# Solução #
file_size = int(input('Informe o tamanho do arquivo em MB.\n'))
velocidade_internet = int(input('Agora informe a velocidade da sua conexão em Mbps.\n'))
tempo_download = (file_size*8)/velocidade_internet
print(f'O tempo estimado de download é {int(tempo_download/60)} minutos e {int(tempo_download%60)} segundos.')
print('\n\n')