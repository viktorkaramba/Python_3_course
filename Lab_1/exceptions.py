class MyException(BaseException):
    pass


class AlreadySectionError(MyException):
    def __str__(self):
        self.msg = 'Section with this id is already there!'
        return self.msg


class AlreadyGoodsError(MyException):
    def __str__(self):
        self.msg = 'Goods with this id is already there!'
        return self.msg


class NonSectionError(MyException):
    def __str__(self):
        self.msg = 'There no section with this id!'
        return self.msg


class NonGoodsError(MyException):
    def __str__(self):
        self.msg = 'There no goods with this id!'
        return self.msg


class NonInStoreError(MyException):
    def __init__(self, is_section, is_goods):
        super(NonInStoreError, self).__init__()
        if not is_section:
            self.msg = 'There no section with this id!'
        elif is_section and not is_goods:
            self.msg = 'There no goods with this id!'


class MyIndexError(MyException):
    def __str__(self):
        self.msg = 'List index out of range!'
        return self.msg


class InputError(MyException):
    pass
