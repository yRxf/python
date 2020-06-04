class file():
    def __init__(self,filename):
        self.filename = filename
        self.file_ = ''
    def file_write(self):
        try:
            with open(self.filename) as self.file_:
                pass
        except FileNotFoundError:
            self.file_ = open(self.filename,'w')
            return self.file_
        else:
            flag = input("存在文件是否需要清空内容(Y/N)")
            if 'N' == flag:
                self.file_ = open(self.filename,'a')
                return self.file_
            else:
                self.file_ = open(self.filename,'w')
                return self.file_
    def __del__(self):
        self.file_.close()
        print("文件已关闭！")

file_ = file("test1.txt")
file_f = file_.file_write()
file_f.write("123")

            