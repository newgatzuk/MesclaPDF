# Como estou aprendendo, vou pegar boa pratica do ";"
#PyPDF2 é uma biblioteca de manipulação PDF
import PyPDF2;
#Verificar e ler arquivos do PC
import os;

#aviso para quem usar
print("Lembrando que os pdf que você quer mesclar tem que está nessa pasta.");
#input para dizer onde vai ser o local
caminho = input("digite o caminho da pasta que vai querer mesclar: ");


#declaração variavel do manipulador de pdf
mesclar = PyPDF2.PdfMerger();

#Aqui é a variavel que vai "listar os arquivos para você."
lista_arquivo = os.listdir(caminho);

#Aqui vai ordenar arquivos de como vai aparecer EX: 1 2 3...
lista_arquivo.sort();

#aqui vai mostrar na tela quais arquivos estão na pasta da variável "lista_arquivo"
print(lista_arquivo);

#criado um loop para "arquivo" que sempre que iniciado
#Vai verificar se "lista_arquivo" vai está em .pdf, se tiver, vai
#mesclar.append que no caso vai "adicionar"
for arquivo in lista_arquivo:
    if ".pdf" in arquivo: 
        mesclar.append(f"PDFs/{arquivo}");
    else:
        print("O arquivo não é um PDF, verifique seus arquivos.");


#Pedir nome do PDF
nome_do_pdf = input("Digite Nome do PDF Mesclado: ")
#salvar o PDF
mesclar.write(nome_do_pdf);
print(f"O PDF {nome_do_pdf} foi criado com sucesso!")