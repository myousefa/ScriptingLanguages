import sys

class Emitter:
    def __init__(self):
        self.level = 0

    def print(self,value="",sep=' ',end='\n',file=sys.stdout):
        spaces = 4
        file.write(" "*spaces*self.level + value+end)

    def indent(self):
        return self

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self,exc_type, exc_value, exc_traceback):
        self.level -= 1


e = Emitter()
def cases():
    for case in ["THIS", "THAT", "OTHER"]:
        e.print(f"case {case}:")
        with e.indent():
            e.print("// this is the code for", case)
            e.print("// with some boilerplate")
        e.print("break;")
 
def body():
    with e.indent():
        e.print("while (true) {")
        with e.indent():
            e.print("switch(state) {")
            with e.indent():
                cases()
            e.print("}")
        e.print("}")
 
 
def machine():
    e.print("void Machine(enum State initial_state)")
    e.print("{")
    body()
    e.print("}")
 
 
if __name__ == "__main__":
    machine()
