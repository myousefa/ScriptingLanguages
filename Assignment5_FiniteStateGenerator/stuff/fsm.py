
class Edge:

    def __init__(self):
        pass
    pass

class Machine:

    def __init__(self,name):
        self.name = name

        # These are your vertices
        # NOTE: Edges represent the transition of states (vertices)
        self.state_list = {}
        pass

    def header(self,text):
        self.header = text
        pass

    def footer(self,text):
        self.footer = text
        pass

    def state(self,state_name,action_string,edge_list):
        self.state_list[state_name] = (action_string,edge_list)
        pass

    def edge(self,event_name,next_state,optional_action_string):
        pass

    def gen(self):
        self.cpp_text = ""
        self.cpp_text += self.header
        # -- edges here -- 
        self.cpp_text += self.footer
        return self.cpp_text