from conexao_orm import Base, engine, session
from User import User
from Post import Post

#Cria as tabelas
Base.metadata.create_all(engine)

#função para  exibir o menu de opçoes
def show_menu():
    print("Menu de Opções:")
    print("1. Add Usuários")
    print("2. Adicionar Post")
    print("3. Consultar Usuários e seus Posts")
    print("4. Sair")


#Função para adicionar Usuario
def add_user():
    print("Adicionar novo usuário")
    name = input("Nome\n")
    email= input("Email\n")
    user= User(name, email)
    session.add(user)
    session.commit()
    print("Usuário adicionado com sucesso")

#Função para adicionar um novo post    
def add_post():
    print("Adicionar novo post:")
    title = input("Título:\n")
    content = input("Conteúdo:\n")
    author_id = input("Id do Author:\n")
    user = session.query(User).filter_by(id=author_id).first()
    if user:
        post = Post(title=title, content=content, author=user)
        session.add(post)
        session.commit()
        print("Post adicionado com sucesso")
    else:
        print("Usuário não encontrado")



#Função para consultar usuários e posts
def query_users_posts():
    users = session.query(User).join(User.posts).order_by(User.name).all()
    for user in users:
        print(f"User: {user.name}, Email: {user.email} ")
        for post in user.posts:
            print(f"Post: {post.title}, Conteúdo: {post.content}")


