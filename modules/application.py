from . import api_engine

class API:
    def __init__(self):
        pass

    def initialize(self, input_arg) -> dict:
        def process_input(valid) -> tuple:
            if len(valid.strip()) >= 5:
                return valid
            
            else:
                return False
            
        input_arg = process_input(input_arg)
        

        if input_arg != False:
        
            return api_engine.SEARCH(input_arg).initialize()
        

        else:
            raise Exception("O input deve ser maior que 3")
    

