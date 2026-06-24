# CADA ITEM: "chave : valor"

x = {"RN":"Natal", "PB":"João Pessoa", "PE":"Pernambuco"}
y = [1, 2, 3, 4]
z = (1, 2, 3, 4)

X["AM"] = "Manaus" #insere
X["PB"] = "J. Pessoa" #altera
x.pop("PB") #remove

#passar em todos os itens
for item in x.items(): print(item)