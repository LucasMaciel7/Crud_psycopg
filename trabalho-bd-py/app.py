
import psycopg2 
from psycopg2.extras import DictCursor
conexao = psycopg2.connect(
    dbname='trabalho_db',
    user='postgres',
    password='2707',
    host='localhost',
    port='5555'
)

cursor = conexao.cursor(cursor_factory=DictCursor)
cursor.execute("CREATE TABLE IF NOT EXISTS professor(id_prof integer primary key, nome varchar, salario float, data date)")
cursor.execute("INSERT INTO professor values (1,'Lucas',1500,'11/11/1111')")
cursor.execute("INSERT INTO professor VALUES(2,'Pedro',1300,'11/11/2003')")

cursor.execute("SELECT * FROM professor")
dados = cursor.fetchall()


while True:
    print(80*"-")
    menu=int(input("\nEscolha qual Opção Deseja:\n\n1 - Inserir Professor \n2 - Atualizar Professor\n3 - Deletar um Professor\n4 - Buscar um prosfessor\n5 - Parar Sistema\n\nDigite sua opção:"))
    print(80*"-")
    if menu ==1:
        print("\n Prencha os Dados do Novo professor\n")
        id=int(input("Digite ID:"))
        nome=input("Digite o Nome:")
        salario=float(input("Digite o salario:"))
        data=input("Digite a data:")
        cursor.execute("INSERT INTO professor VALUES (%s, %s, %s, %s)", (id, nome, salario, data))
        cursor.execute("SELECT * FROM professor")
        dados = cursor.fetchall()
        for x in dados:
            print(f"\nProfessor inserido com Sucesso!\nid:{x[0]}\nNome:{x[1]}\nsalario:{x[2]}\ndata:{x[3]} ")
        pass

    if menu ==2:
        cursor.execute("SELECT id_prof,nome FROM professor")
        professores = cursor.fetchall()
        print("Professores Cadastrados\n")
        for linha in professores:
            print(f"id:{linha[0]} / {linha[1]}")

        prof_id=int(input("\nDigite o ID do professor que deseja atualizar:"))
        opcao=int(input("\nOque Você deseja atualizar ?\n1 - ID\n2 - Nome\n3 - Salario\n4 - Data\n\nDigite o numero de sua opção: "))
        if opcao ==1:
            coluna="id_prof"

        elif opcao==2:
            coluna= "Nome"

        elif opcao==3:
             coluna="Salario"

        elif opcao==4:
             coluna="Data"

        novo_valor=input("\nDigite o novo Valor deste campo:")
        query = f"UPDATE professor SET {coluna} = '{novo_valor}' WHERE id_prof = {prof_id}"
        cursor.execute(query)
        print("\nAlteração realizada com sucesso")
        pass
    
    if menu ==3:
        print("Lista e professores")
        cursor.execute("SELECT id_prof,nome FROM professor")
        professores = cursor.fetchall()
        print("Professores Cadastrados\n")
        for linha in professores:
            print(f"id:{linha[0]} / {linha[1]}")
        opcao=int(input("\nDigite o numero do prodfessor que deseja deletar: "))
        query=f"DELETE FROM PROFESSOR WHERE ID_PROF = {opcao}"
        cursor.execute(query)
        print("\nProfessor deletado com sucesso!")

    if menu==4:
            opcao=int(input("Escolha o campo em que deseja buscar o professor\n1 - ID\n2 - Nome\n3 - Salario\n4 - Data\n5 - Todos\n\nDigite sua numero de sua Opção:"))
            if opcao ==1:
                coluna="id_prof"
                id=int(input("Digite a Id do professor que deseja buscar:"))
                query=f"SELECT * FROM PROFESSOR WHERE ID_PROF={id}"
                cursor.execute(query)
                dados = cursor.fetchall()
                for x in dados:
                    print(f"\nResultado da busca\n\nid:{x[0]}\nNome:{x[1]}\nsalario:{x[2]}\ndata:{x[3]} ")
                
            elif opcao==2:
                coluna= "Nome"
                nome=input("Digite o nome do professor que deseja procurar:")
                query=f"SELECT * FROM PROFESSOR WHERE nome={nome}"
                cursor.execute(query)
                dados = cursor.fetchall()
                for x in dados:
                    print(f"\nResultado da busca\n\nid:{x[0]}\nNome:{x[1]}\nsalario:{x[2]}\ndata:{x[3]} ")

            elif opcao==3:  
                coluna="Salario"
                salario=int(input("Digite o nome do professor que deseja procurar:"))
                query=f"SELECT * FROM PROFESSOR WHERE salario={salario}"
                cursor.execute(query)
                dados = cursor.fetchall()
                for x in dados:
                    print(f"\nResultado da busca\n\nid:{x[0]}\nNome:{x[1]}\nsalario:{x[2]}\ndata:{x[3]} ")

            elif opcao==4:
                coluna="Data"
                data=int(input("Digite a data do professor que deseja procurar:"))
                query=f"SELECT * FROM PROFESSOR WHERE salario={data}"
                cursor.execute(query)
                dados = cursor.fetchall()
                for x in dados:
                    print(f"\nResultado da busca\n\nid:{x[0]}\nNome:{x[1]}\nsalario:{x[2]}\ndata:{x[3]} ")

            elif opcao == 5:
                query = "SELECT id_prof,nome FROM PROFESSOR"
                cursor.execute(query)
                dados = cursor.fetchall()
                print("\n")
                for linha in dados:
                    print(f"Id: {linha[0]} {linha[1]}")
    if menu==5:
        print("Fim do Programa")
        break





