class Book:
    def __init__(self, T, A, P):
        self.title = T
        self.author = A
        self.pages = P

    def summary(self):
        print(f"輸出： {self.title} 作者為 {self.author}，共{self.pages}頁")


book = Book("Python", "Jerry", 180)
book.summary()