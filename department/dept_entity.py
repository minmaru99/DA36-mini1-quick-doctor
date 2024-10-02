class Dept():

    def __init__(self, dept_name, doct_name):

        self.__dept_name = dept_name
        self.__doct_name = doct_name

    def __str__(self):
        return f'str: {self.__dept_name} - {self.__doct_name}'

    def get_dept_name(self):
        return self.__dept_name

    def get_doct_name(self):
        return self.__doct_name

    def set_dept_name(self, dept_name):
        self.__dept_name = dept_name

    def set_doct_name(self, doct_name):
        self.__doct_name = doct_name

    def __repr__(self):
        return f'Dept{{dept_name = {self.__dept_name}, doct_name = {self.__doct_name}}}'