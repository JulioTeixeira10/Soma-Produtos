#Cria um dicionário com os produtos e suas devidas quantidades da primeira lista
with open("C:\\Users\\Usefr\\Desktop\\Soma-Produtos\\Listas\\t1.txt") as t1:
    file2 = open("C:\\Users\\Usefr\\Desktop\\Soma-Produtos\\Produtos Únicos\\Produtos_Únicos1.txt", "w+")
    produtos1 = {}
    n = 0
    for row in t1:
        if (n % 2) == 0:
            nomeproduto = row.strip()
            n += 1
        else:
            stripquantidade = row[0:2].strip()
            quantidade = int(stripquantidade)
            produtos1[nomeproduto] = quantidade
            n += 1

#Cria um dicionário com os produtos e suas devidas quantidades da segunda lista
with open("C:\\Users\\Usefr\\Desktop\\Soma-Produtos\\Listas\\t2.txt") as t2:
    file3 = open("C:\\Users\\Usefr\\Desktop\\Soma-Produtos\\Produtos Únicos\\Produtos_Únicos2.txt", "w+")
    produtos2 = {}
    n2 = 0
    for row in t2:
        if (n2 % 2) == 0:
            nomeproduto = row.strip()
            n2 += 1
        else:
            stripquantidade = row[0:2].strip()
            quantidade = int(stripquantidade)
            if nomeproduto in produtos2:
                produtos2[nomeproduto] += quantidade
            else:
                produtos2[nomeproduto] = quantidade
            n2 += 1

#Cria um dicionário com os produtos e suas devidas quantidades da teceira lista
with open("C:\\Users\\Usefr\\Desktop\\Soma-Produtos\\Listas\\t3.txt") as t3:
    produtos3 = {}
    n = 0
    for row in t3:
        if (n % 2) == 0:
            nomeproduto = row.strip()
            n += 1
        else:
            stripquantidade = row[0:2].strip()
            quantidade = int(stripquantidade)
            if nomeproduto in produtos3:
                produtos3[nomeproduto] += quantidade
            else:
                produtos3[nomeproduto] = quantidade
            n += 1
    file3 = open("C:\\Users\\Usefr\\Desktop\\Soma-Produtos\\Produtos Únicos\\Produtos_Únicos3.txt", "w+")

#Cria um arquivo que soma os produtos em comúm entre os arquivos t1 - t2 e t1 - t3
file = open("C:\\Users\\Usefr\\Desktop\\Soma-Produtos\\Pedido.txt", "w+")
for produto in produtos1:
    if (produto in produtos2) and (produto in produtos3):
        resquantidade = produtos1[produto] + produtos2[produto] + produtos3[produto]
        strquantidade = str(resquantidade)
        file = open("C:\\Users\\Usefr\\Desktop\\Soma-Produtos\\Pedido.txt", "a")
        file.write(produto)
        file.write(" ------- Quantidade: ")
        file.write(strquantidade)
        file.write("\n\n")
    elif produto in produtos2:
        resquantidade = produtos1[produto] + produtos2[produto]
        strquantidade = str(resquantidade)
        file = open("C:\\Users\\Usefr\\Desktop\\Soma-Produtos\\Pedido.txt", "a")
        file.write(produto)
        file.write(" ------- Quantidade: ")
        file.write(strquantidade)
        file.write("\n\n")
    elif produto in produtos3:
        resquantidade = produtos1[produto] + produtos3[produto]
        strquantidade = str(resquantidade)
        file = open("C:\\Users\\Usefr\\Desktop\\Soma-Produtos\\Pedido.txt", "a")
        file.write(produto)
        file.write(" ------- Quantidade: ")
        file.write(strquantidade)
        file.write("\n\n")
    #Cria um arquivo com os produtos únicos do arquivo t1
    else:
        file2 = open("C:\\Users\\Usefr\\Desktop\\Soma-Produtos\\Produtos Únicos\\Produtos_Únicos1.txt", "a")
        file2.write(produto)
        file2.write(" ------- Quantidade: ")
        file2.write(str(produtos1[produto]))
        file2.write("\n\n")

#Cria um arquivo que soma os produtos em comúm entre os arquivos t2 - t3
for produto in produtos2:
    if produto in produtos1:
        pass
    elif produto in produtos3:
        resquantidade = produtos2[produto] + produtos3[produto]
        strquantidade = str(resquantidade)
        file = open("C:\\Users\\Usefr\\Desktop\\Soma-Produtos\\Pedido.txt", "a")
        file.write(produto)
        file.write(" ------- Quantidade: ")
        file.write(strquantidade)
        file.write("\n\n")


#Cria um arquivo com os produtos únicos do arquivo t2
for produto in produtos2:
    if produto in produtos1:
        pass
    elif produto in produtos3:
        pass
    else:
        file3 = open("C:\\Users\\Usefr\\Desktop\\Soma-Produtos\\Produtos Únicos\\Produtos_Únicos2.txt", "a")
        file3.write(produto)
        file3.write(" ------- Quantidade: ")
        file3.write(str(produtos2[produto]))
        file3.write("\n\n")

#Cria um arquivo com os produtos únicos do arquivo t3
for produto in produtos3:
    if produto in produtos1:
        pass
    elif produto in produtos2:
        pass
    else:
        file3 = open("C:\\Users\\Usefr\\Desktop\\Soma-Produtos\\Produtos Únicos\\Produtos_Únicos3.txt", "a")
        file3.write(produto)
        file3.write(" ------- Quantidade: ")
        file3.write(str(produtos3[produto]))
        file3.write("\n\n")

file.close()
file2.close()
file3.close()