 
FDECL = """
int {name}(State initial_state) {{
	State state = initial_state;
	while (true) {{
		switch(state) {{
"""

def iprint(level, *args, **kwargs):
	print("  " * level, end="")
	print(*args, **kwargs)

class Edge(object):
	def __init__(self, event, next_state, action):
		self.event = event
		self.next_state = next_state
		self.action = action

	def emit(self):
		iprint(5, f"case e_{self.event}:")
		iprint(6, self.action)
		iprint(6, f"state = s_{self.next_state};")
		iprint(5, "break;")

class Machine(object):
	def __init__(self, name):
		self.name = name
		self._header = ""
		self._footer = ""
		self.states = {}
		self.event_names = set()

	def header(self, text):
		self._header = text

	def footer(self, text):
		self._footer = text

	def state(self, name, action, edges=None):
		if not edges:
			edges = []
		self.states[name] = (action, edges)

	def edge(self, event, next_state, action=""):
		self.event_names.add(event)
		return Edge(event, next_state, action)

	def edges(self, *args):
		pass

	def gen(self):
		# header stuff
		print(self._header)
		print("using namespace std;")
		iprint(1, "enum State {")
		for s in self.states.keys():
			iprint(2, f"s_{s},")
		iprint(1, "};")

		iprint(1, "enum Event {")
		for e in self.event_names:
			iprint(2, f"e_{e},")
		iprint(1, "};")

		print()

		print('const char * Event_NAMES[] = {')
		for e in self.event_names:
			print(f'	"{e}"')
		print("};")

		print('Event get_next_event();\n')

		# String to Event Method
		print('Event string_to_event(string event_string) {')
		for e in self.event_names:
			print('	if (event_string == "{0}") {{return "{0}_EVENT";}}'.format(e))
		print("	return INVALID_EVENT;\n}")
        
		print(FDECL.format(name=self.name))
		for s, (action, edges) in self.states.items():
			iprint(3, f"case s_{s}:")
			iprint(4, action)
			iprint(4, "event = get_next_event();")
			iprint(4, "switch (event) {")
			for e in edges:
				e.emit()
			iprint(4, "}")
			iprint(4, "break;")
		iprint(2, "}")
		iprint(1, "}")
		iprint(0, "}")
		print(self._footer)