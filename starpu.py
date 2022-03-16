import parsedemographics as pd
import parseweights as pw
import practice as p
import pickle
import os.path

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

def save_csv(practices, rootname, dst):
    starpu_names = list(practices[0].starpu.keys())
    meta = os.path.join(dst, rootname+"-meta.csv")
    with open(meta, "w") as f:
        f.write("id, name\n")
        for (i, name) in enumerate(starpu_names):
            f.write(f'S{i},"{name.strip()}"\n')
    csv = os.path.join(dst, rootname+".csv")
    with open(csv, "w") as f:
        f.write("PRACTICE,")
        for i,n in enumerate(starpu_names):
            f.write(f"S{i},")
        f.write("\n")
        for p in practices:
            f.write(f"{p.code},")
            for i,name in enumerate(starpu_names):
                f.write(f"{int(p.starpu[name])},")
            f.write("\n")
    
if __name__ == '__main__':
    gen_starpu()

