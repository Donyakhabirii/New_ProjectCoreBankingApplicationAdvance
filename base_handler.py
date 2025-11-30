from BusinessLogic.Validators.ihandler import IHandler

class BaseHandler(IHandler):
    def __init__(self):
        self.next_handler = None
    def set_next(self,next_handler):
        self.next_handler = next_handler
    def handler(self,request):
        pass