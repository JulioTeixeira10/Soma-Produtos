with open("C:\\Users\\Usefr\\Desktop\\somapgit\\Soma-Produtos\\t1.txt") as t1:
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

with open("C:\\Users\\Usefr\\Desktop\\somapgit\\Soma-Produtos\\t2.txt") as t2:
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

for produto in produtos1:
    if produto in produtos2:
        resquantidade = produtos1[produto] + produtos2[produto]
        strquantidade = str(resquantidade)
        file = open("C:\\Users\\Usefr\\Desktop\\somapgit\\Soma-Produtos\\Pedido.txt", "a")
        file.write(produto)
        file.write(" ------- Quantidade: ")
        file.write(strquantidade)
        file.write("\n\n")
    else:
        file2 = open("C:\\Users\\Usefr\\Desktop\\somapgit\\Soma-Produtos\\Produtos_Únicos.txt", "a")
        file2.write(produto)
        file2.write(" ------- Quantidade: ")
        file2.write(str(produtos1[produto]))
        file2.write("\n\n")
file.close()
file2.close()
