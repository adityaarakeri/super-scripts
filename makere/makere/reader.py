import os
class Reader:

    def __init__(self, source):
        if type(source) in [list, set, tuple, str]:
            pass
        elif hasattr(source, 'read'):
            pass
        else:
            raise (ValueError("Source type {0} not supported ".format(type(source))))
        if type(source) == str and not os.path.exists(source):
            #print os.path.join(os.getcwd() , 'makere\\tests', source)
            raise (IOError("File does not exists"))
        if type(source) == str or hasattr(source, 'read'):
            source = self._gen_source(source)
        self.source = source

    # Returns the source in iterable form
    def read(self):
        return self.source

    def _gen_source(self, source):
        if hasattr(source, 'read'):
            input_file = source
        else:
            #source = os.path.join(os.getcwd(),'makere\\tests', source)
            input_file = open(source, 'r')
            lst = [line.strip() for line in input_file]
            input_file.close()
            return lst

    
