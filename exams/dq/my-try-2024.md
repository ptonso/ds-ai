Exercise 1

a)
    c.

b)
    a.

c)
    c.

d)
    a.

e)
    c.

f)
    I dont understand this notation. lets study it

g)
    

h)


i)
    b.


Exercise 2

a)
    3 -> 4 -> 2 -> 1 -> 5

note: what is "attribute value matching"?; what does "search space reduction" does?

b)
    b.
    
reason: one window matching = 100*100 = 10.000. we need to compute that 10 times, therefore 100,000.
note: I assume that slide=100, but in my mental model that is not a requirement

c)
    b.

d)
    P = {"Pl", "ay", "-D", "oh"}
e)
    |P\cap Q| = |{"Pl", "ay"}| = 2

f) |P \cup Q| = |{"Pl", "ay", "-D", "oh", " D", "oo"}| = 6

g) Jac(P,Q) = 2/6 = 1/3 = 0.33


h)
    {A, BC, DE}
    {A, BCDE}
    sure duplicates: BC, DE
    sure non-duplicates: AB, AC, AD, AE
    not-sure duplicates: BD, BE, CD, CE
    
    as BC and DE are sure duplicates, we start with the most granular partition {A,BC,DE} (assuming all not-sure duplicates are not duplicates.    
    we know for sure that A is a standalone cluster, because it is sure not duplicate with all others.
    because we are sure that BC and DE are clusters, the only possible move we have by considering any possible "not-sure duplicates" is to consider the full bound (BCDE), because we cannot split BC and DE.

i)
    P({A, BC, DE}) = 
        (1-0.15) * (1-0.20) * (1-0.35) * (1-0.25)
        * 0.9 * (1-0.60) * (1-0.70)
        * (1-0.75) * (1-0.55)
        * 0.95
    
    = 0.85 * 0.80 * 0.65 * 0.75 * 0.90 * 0.40 * 0.30 * 0.25 * 0.45 * 0.95
    = 0.00382633875


Exercise 3

a)
    e.

b)
    It is a common practice in database schematization to abbreviate the attributes names to spare visual space while reading the full table. 
    However, if this process is developed without documenting the underlying meagning of the abbreviations, this information lies only on the mind of professions that work on this data. 
    Later in the future, if we want to use this dataset without contacting the professionals that collect the data, one can have no information about the meagning of the abbreviate attributes. That can lead to poor preprocessing decisions, such as normalizing categorical features, or wrongly chose a technique to fill missign data.

c)
    have to study this one.

d)
    f.


e)
    c.
