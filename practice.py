
class Practice:

    def __init__(self, code, demo):
        self.demographic = demo
        self.code = code
        self.starpu = {}
    
    def add_starpu(self, section, weights):
        cum = 0
        for k, v in self.demographic.items():
            cum += weights[k][0] * v[0]
            cum += weights[k][1] * v[1]
        self.starpu[section] =  cum