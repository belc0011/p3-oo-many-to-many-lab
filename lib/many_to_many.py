class Author:
    def __init__(self, name):
        self.name = name
    
    def contracts(self):
        contracts = [contract for contract in Contract.all if contract.author == self]
        return contracts
    
    def books(self):
        books = [contract.book for contract in Contract.all if contract.author == self]
        return books
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        total_royalties = sum(contract.royalties for contract in Contract.all if contract.author == self)
        return total_royalties

class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        contracts = [contract for contract in Contract.all if contract.book == self]
        return contracts
    
    def authors(self):
        authors = [contract.author for contract in Contract.all if contract.book == self]
        return authors

class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if (isinstance(author, Author)):
            self.author = author
        else:
            raise Exception("author must be of class Author")
        if (isinstance(book, Book)):
            self.book = book
        else:
            raise Exception("book must be of class Book")
        if (isinstance(date, str)):
            self.date = date
        else:
            raise Exception("date must be of type string")
        if (isinstance(royalties, int)):
            self.royalties = royalties
        else:
            raise Exception("royalties must be of type integer")
        Contract.all.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        contracts_date = [contract for contract in cls.all if contract.date == date]
        return sorted(contracts_date, key=lambda contract: contract.date)