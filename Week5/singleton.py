class callManager:
    __instance = None
    @staticmethod
    def getInstance():
        if callManager.__instance == None:
            callManager()
        return callManager.__instance
    def __init__(self):
        if callManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            callManager.__instance = self
c = callManager()
print(c)