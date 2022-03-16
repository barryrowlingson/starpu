
class Practice:

    def __init__(self, code, demo):
        self.demographic = demo
        self.code = code
        self.starpu = {}
        print(f" init {demo} with {code}")
    
    def add_starpu(self, section, weights):
#        print(f" adding weights {weights} for {section} to {self.code}")
        cum = 0
        for k, v in self.demographic.items():
            cum += weights[k][0] * v[0]
            cum += weights[k][1] * v[1]
        self.starpu[section] =  cum
