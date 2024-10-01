#criar uma lista 
cidades = ["Sobradinho","Plano Piloto","Taguatinga","Grande Colorado","Vicente Pires","Aquas Claras",
           "Planaltina","Cruzeiro","Gama","Plano Piloto","Valparaiso","Sudoeste","Samambaia","Asa Sul","Asa Norte","Sobradinho","Varjão","Recanto das Emas","Santa Maria","Cruzeiro","Plano Piloto"]

#usuário informa o nome que deseja procurar
cidade = input("Informe o nome da cidade que desaja procurar: ")

#informa a quantidade de vezes que o termo foi achado 
quantidade = cidades.count(cidade)

#exibe o resultado na 
if cidade in cidades:
   print(f"{cidade} Foi encontrado na lista {quantidade} vezes.")
else:
   print(f"{cidade} Não foi encontrado.")