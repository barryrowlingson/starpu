# STAR-PU
Some python scripts to generate STAR-PU values per practice from official sources.

## Data
I've included the hard-coded files in the git repo. Other wise they're found as below
* Demographic data - http://fingertips.phe.org.uk/profile/general-practice/data
* STAR-PU weightings - http://www.hscic.gov.uk/prescribing/measures
Assuming they keep roughly the same formats in future releases it should be pretty trivial to change.

## Usage
Either you can look inside the guts - There aren't many comments (yet) but it's pretty simple what it's doing
Or you can use the simple version and use the starpu.py module.

```
import starpu
starpu.gen_starpu(save=True)
```
This will generate a list of `Practice` objects and save it as `starpu.p` using `pickle`. Setting `save=False` will cause the function to return the list instead.

### The `Practice` Object
It's intended to be bog standard simple, each object has a `self.starpu` field, which is a dict, the key of which is the BNF code (e.g. `'1.3'`) as a string.
The values will return the starpu for that section.

### `Weights` and `Demographics`
These arent custom objects, just formats for dicts. The general format for each of them is the same
```
{ Code: { Age-Bracket: Value } }
```
* `Code` is the organisation code of the practice.
* `Age-Bracket` is self explanatory - formatted as a string ('0-4', '5-14', 15-24' ... '65-74', '75+')
* `Value` is either the starpu weighting or a tuple of population (male, female) for that age-bracket

***
Final things - If people do actually want to use this fantastic go ahead, knocked this up in an evening after trying to compare some presribing data on openprescribing.net.
Oh yeah, and leave a comment/message me etc if you have anything to input!
