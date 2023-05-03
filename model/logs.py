class Logs:
    def __init__(self, dir_path='', save=True, content='', name=''):
        self.dir_path = dir_path
        self.save = save
        self.content = content
        self.name = name

    def saveLogs(self):
        if self.save:
            with open(f"{self.dir_path}/{self.name}.txt", "a") as file:
                file.write(f"{self.content}\n")
        else:
            print(self.content)