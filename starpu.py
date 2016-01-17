import parsedemographics as pd
import parseweights as pw
import practice as p
import pickle

def gen_starpu(save=True):
    demogs = pd.get_demographics('PublicHealthEngland-Data.xlsx')
    weights = pw.get_weights('PrescribingUnits2013.xlsx')
    
    practices = []
    for k,v in demogs.items():
        practices.append(p.Practice(k, v))
    for prac in practices:
        for k, v in weights.items():
            prac.add_starpu(k, v)
    if save:
        pickle.dump( practices, open( "starpu.p", "wb" ) )
    else:
        return practices
        
if __name__ == '__main__':
    gen_starpu()