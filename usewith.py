class MyOpen():
    def __init__(self,filename):
        '''初始化方法'''
        self.filename = filename
        self.filehandler = None
        return
    def __enter__(self):
        '''enter,返回文件操作对象'''
        print("enter:", self.filename)
        self.filehandler = open(self.filename, "r")
        return self.filehandler

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''exit方法，关闭文件并且返回True'''
        print("exit:", exc_type, exc_val, exc_tb)
        if self.filehandler:
            self.filehandler.close()
        if exc_val:
            raise ZeroDivisionError
        else:
            #raise ZeroDivisionError
            return True
        #return True
# 使用实例
with MyOpen("1.txt") as file:
    for line in file:
        print(line)
        raise ZeroDivisionError

