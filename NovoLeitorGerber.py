import matplotlib.patches as mpatches
# import ClasseFerramentas as dFerramentas

"""Configurações do arquivo"""

# 1. Carregar o arquivo que deseja fazer a leitura:
Arquivo = open("Bottom.txt", "r")

# 2. Separar cada linha do arquivo em uma string. (Linhas é uma lista de string)
Linhas = Arquivo.readlines()

# 3. Fechar o arquivo:
Arquivo.close()

# 4. Determinar File Specification = número de casas decimais
def FormatSpecification():
    for i in range(len(Linhas)):
        if 'FS' in Linhas[i]:
            LinhaFS = Linhas[i]
    iX = int(LinhaFS[LinhaFS.find('X')+1])
    iY = int(LinhaFS[LinhaFS.find('Y')+1])
    dX = int(LinhaFS[LinhaFS.find('X')+2])
    dY = int(LinhaFS[LinhaFS.find('Y')+2])
    return iX, iY, dX, dY

# 5. Determinar a unidade de medida:
def Medida():
    for i in range(len(Linhas)):
        if 'MO' in Linhas[i]:
            Unidade = Linhas[i]
    UnidadeMedida = Unidade[Unidade.find('MO')+2:Unidade.find('*')]
    if UnidadeMedida == 'IN':
            pol = 25.4
    else:
            pol = 1
    return pol

# 6. Carregar a lista de ferramentas do Gerber:
ListaFerramentas = []
dic_tools = {}
newtoollist = []
def Ferramentas():
    for i in range(len(Linhas)):
        Linha = Linhas[i]
        if Linha.startswith('%ADD'):
            ListaFerramentas.append(Linha)
            
            
    for j in range(len(ListaFerramentas)):
        tool = ListaFerramentas[j]
        toolname = tool[tool.find('ADD')+2:tool.find(',')-1]
        toolshape = tool[tool.find('ADD')+5:tool.find(',')]
        if (toolshape == 'C'):
            raio = tool[tool.find(',') + 1 : tool.find('*')]
            toolshaperadius = [toolshape,raio]
            dic_tools = {toolname:toolshaperadius}
            newtoollist.append(dic_tools)
        elif (toolshape == 'R'):
            n = tool[tool.find(',') + 1 : tool.find('X')]
            m = tool[tool.find('X') + 1 : tool.find('*')]
            toolshaperadius = [toolshape, m, n]
            dic_tools = {toolname : toolshaperadius}
            newtoollist.append(dic_tools)
    return newtoollist

# 7. Selecionar a ferramenta:   
def SelecionarFerramenta(LinhaAtual):
    tool = LinhaAtual[LinhaAtual.find('*')-3:LinhaAtual.find('*')]
    return tool
    
# 8. Determinar as coordendas:
def Coordenadas(LinhaAtual):
    x_new = float(LinhaAtual[LinhaAtual.find('X')+1:LinhaAtual.find('Y')])/(10**dX)
    y_new = float(LinhaAtual[LinhaAtual.find('Y')+1:LinhaAtual.find('*')-3])/(10**dY)
    return x_new, y_new

# 9. Determinar operação (Desenhar D01, mover D02 e carimbar D03):
def Operacao(LinhaAtual):
    op = LinhaAtual[LinhaAtual.find('*')-2:LinhaAtual.find('*')]
    return op
    
# x = Ferramentas()

# tool = 'D11'
# for i in x:
#     if tool in i:
#         y = i[tool]
#         s = y[0]
#         m = y[1]
#         n = y[2]


# INÍCIO DO ALGORITMO:
    
iX, iY, dX, dY = FormatSpecification()

pol = Medida()

for i in range(len(Linhas)):
    if Linhas[i].startswith("G"):
        tool = SelecionarFerramenta(Linhas[i])
        
    if Linhas[i].startswith("X"):
        x, y = Coordenadas(Linhas[i])
        op = Operacao(Linhas[i])
        print(op)        
        print(tool)
        print(x*pol)
        # print(float(x))
        # print(y)
    
    