file = open(r'C:\Users\Talyson Negrao\OneDrive\Documentos\Dev\Estudos\Python\Manipulação de Arquivos/teste.txt', 'w')#/teste.txt ceria novo arquivo

#digita exatamente oque eu mandar 
file.write('Ola mundo!')

#escrve varias strings como lista 
file.writelines(['\n', 'Python ', '\n' , 'Delicia '])
file.close()