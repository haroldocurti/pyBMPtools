# PyBMPTools

Uma ferramenta Python simples para inspecionar e trabalhar com arquivos de imagem BMP.

## Visão Geral

**PyBMPTools** é uma biblioteca Python em desenvolvimento focada na leitura e análise da estrutura de arquivos de imagem BMP (Bitmap). Atualmente, ela permite acessar o **cabeçalho do arquivo** e o **cabeçalho de informações da imagem**, além de extrair metadados importantes como o tamanho do arquivo e o formato.

O objetivo principal é fornecer uma interface intuitiva para entender a estrutura interna dos arquivos BMP, sendo uma ferramenta útil para aprendizado, depuração ou pequenas manipulações que exigem acesso direto aos dados brutos do arquivo.

## Recursos

Atualmente, a biblioteca oferece as seguintes funcionalidades:

* **Leitura de Arquivos BMP**: Carrega o conteúdo completo de um arquivo BMP.
* **Acesso ao Cabeçalho do Arquivo (BMP File Header)**: Permite extrair os primeiros 14 bytes do cabeçalho, que contêm informações cruciais sobre o arquivo BMP.
* **Obtenção do Tamanho do Arquivo**: Extrai o tamanho total do arquivo BMP diretamente do cabeçalho.
* **Identificação do Formato BMP**: Tenta identificar o tipo de formato BMP (ex: Windows NT, OS/2) com base nos bytes mágicos.
* **Acesso ao Cabeçalho de Informações (BITMAPINFOHEADER)**: Fornece acesso aos 40 bytes do cabeçalho de informações, que detalham as propriedades da imagem (largura, altura, bits por pixel, etc.).
* **Representação Hexadecimal**: Permite visualizar o conteúdo completo do arquivo em formato hexadecimal.

## Estágio Atual de Desenvolvimento

Esta biblioteca está em **desenvolvimento inicial**. As funcionalidades implementadas focam principalmente na **leitura e interpretação dos cabeçalhos dos arquivos BMP**.

**Funcionalidades já implementadas e testadas:**

* Carregamento de arquivos BMP.
* Extração e exibição do "BMP File Header".
* Obtenção do tamanho do arquivo.
* Tentativa de identificação do formato (limitada aos códigos mágicos presentes).
* Extração e exibição do "BITMAPINFOHEADER".

**Próximos passos planejados:**

* Implementar métodos para extrair e interpretar todos os campos do `BITMAPINFOHEADER` (largura, altura, profundidade de cor, compressão, etc.).
* Adicionar suporte para leitura de dados de pixel.
* Desenvolver funcionalidades para manipulação e escrita de arquivos BMP.
* Melhorar a detecção de formatos BMP e suportar outros tipos de cabeçalhos (ex: `BITMAPV5HEADER`).
* Adicionar tratamento de erros robusto para arquivos BMP inválidos ou corrompidos.

## Como Usar

### Pré-requisitos

* Python 3.x

### Instalação

Como a biblioteca ainda está em desenvolvimento inicial e não está empacotada, você pode usá-la clonando o repositório e importando a classe diretamente.

```bash
git clone [https://github.com/SeuUsuario/PyBMPTools.git](https://github.com/SeuUsuario/PyBMPTools.git)
cd PyBMPTools
```
### Exemplos de Código
```Python

# Suponha que você tenha um arquivo BMP chamado 'img01.bmp' no mesmo diretório

from bmptools import bmptools

# Cria uma instância da ferramenta, carregando o arquivo
image = bmptools('img01.bmp')

# Visualiza o conteúdo completo do arquivo em formato hexadecimal
print("--- Conteúdo Hexadecimal Completo ---")
print(image) # Usa o método __str__ para imprimir o hexArr formatado

# Acessa e exibe o cabeçalho do arquivo (BMP File Header)
print("\n--- BMP File Header (Formatado) ---")
header_bytes = image.header(style='f') # Exibe no console e retorna os bytes
print(f"Bytes Brutos do Header: {header_bytes.hex()}")

# Obtém o tamanho do arquivo
file_size = image.fileSize()
print(f"\nTamanho do Arquivo (bytes): {file_size}")

# Tenta identificar o formato do BMP
file_format = image.format()
print(f"Formato Identificado: {file_format if file_format else 'Desconhecido / Não Suportado'}")

# Acessa o cabeçalho de informações (BITMAPINFOHEADER)
print("\n--- BITMAPINFOHEADER (Hexadecimal) ---")
info_header_hex = image.info_header(style='r').hex(' ',-8) # Retorna os bytes e os formata
print(info_header_hex)
```
