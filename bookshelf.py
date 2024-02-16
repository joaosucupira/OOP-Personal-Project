# CLASSE PARA LIVROS
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.lended = False

# CLASSE PARA BIBLIOTECAS 
class Library:
    def __init__(self):
        self.books = []
    
    # adicionar livro
    def add_book(self, book):
        self.books.append(book)
    
    # listar livros disponíveis
    def list_avlb_books(self):
        # função que vai acrescentando livros à lista de disponíveis SE for conferida FALSA a condição de emprestado
        avlb_books = [book for book in self.books if not book.lended]
        # condicional verificando se há algum livro disponível
        if avlb_books:
            for book in avlb_books:
                print(f'{book.title} - {book.author}')
        else:
            print('No available books.')
    
    # empréstimo de um livro
    def lend_book(self, title):
        for book in self.books:
            if book.title == title and not book.lended:
                book.lended = True
                print("Book lended succefully.")
                return
        print("Unavailable book.")
    
    # devolução de um livro
    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.lended:
                book.lended = False
                print("Book returned succefully.")
                return
        print("Book wasn't lended/Doesn't belong in library.")

# CLASSE PARA USUÁRIOS
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.books_lended = []
        

      
# biblioteca = Library()      
# livro1 = Book("Python for Beginners", "John Smith")
# livro2 = Book("Introduction to Machine Learning", "Jane Doe")
# livro3 = Book("Data Structures and Algorithms in Python", "Alice Johnson")

# biblioteca.add_book(livro1)
# biblioteca.add_book(livro2)
# biblioteca.add_book(livro3)

# biblioteca.lend_book(livro1.title)
# biblioteca.return_book(livro1.title)

# biblioteca.list_avlb_books()