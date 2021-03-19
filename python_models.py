# Для демонстрации разберём следующие классы: авторы, биография авторов, статья, книга. У автора есть имя и год рождения.
# Биография содержит текст. Статья имеет название, её может написать один автор.
# У книги есть название, её могут написать несколько авторов.
# Этот пример выбран потому, что в нём есть основные виды связей между классами: one-to-one, one-to-many, many-to-many.

class Author:

   def __init__(self, name, birthday_year):
       self.name = name
       self.birthday_year = birthday_year

   def __str__(self):
       return self.name


class Biography:

   def __init__(self, text, author:Author):
       self.author = author
       self.text = text


class Book:

   def __init__(self, name, authors):
       self.name = name
       self.authors = authors


class Article:

   def __init__(self, name, author:Author):
       self.name = name
       self.author = author
