class pyBMPtools:
    def __init__(self, file):
        with open(file, 'rb') as f:
            self.raw = f.read()
            self.hexArr = self.raw.hex(' ',-8).split(' ')
    def __str__(self):
        return "".join(f"{item}\n" for item in self.hexArr)
    
    # HEADER METHODS
    def header(self, style='r') -> bytes:
        '''
        Retorna os primeiros 14 bytes do cabeçalho da estrutura.
        Args:
            style (str): O estilo de retorno/exibição.
                        'r' (raw): Retorna os bytes brutos do cabeçalho.
                        'f' (formatted): Exibe uma versão formatada do cabeçalho no console
                                        e ainda retorna os bytes brutos.
        Returns:
            bytes: Os primeiros 14 bytes do cabeçalho, representando a versão bruta.
        '''
        if style == 'r':
            return self.raw[0:14]
        print(self.raw[0:14].hex(' ',-8))
        return self.raw[0:14]
    
    def fileSize(self) -> int:
        return int.from_bytes(self.raw[2:6], 'little')
    
    def format(self):
        if '424d' in self.hexArr[0]:
            return "Win NT"
        if '4241' in self.hexArr[0]:
            return "OS/2 struct bitmap array"
        if '4349' in self.hexArr[0]:
            return "OS/2 struct color icon"
        if '4350' in self.hexArr[0]:
            return "OS/2 const color pointer"
        if '4349' in self.hexArr[0]:
            return "OS/2 struct icon"
        if '5054' in self.hexArr[0]:
            return "OS/2 pointer"
    
    # (WINDOWS) BITMAPINFOHEADER
    def info_header(self, style='r'):
        if style == 'r':
            return self.raw[14:54]
        return self.raw[14:54].hex(' ',-8)

image = bmptools('img01.bmp')    