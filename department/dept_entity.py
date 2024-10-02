class Dept():

    def __init__(self, dept_name, doct_names, price):

        self.dept_name = dept_name
        self.doct_names = doct_names
        self.price = price

    # def dept_name(self):
    #     return self.dept_name
    #
    # def doct_names(self):
    #     return self.doct_names



    def __repr__(self):
        return f'Dept{{dept_name = {self.dept_name}, doct_names = {self.doct_names}, price = {self.price}}}'