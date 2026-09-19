
Ex1.
a)
    yes, bid is a key

b)
    yes, as bid is key, any combination with other values should hold, although that dependency have any meagning as an active constraint to maintain.

c)
    ...

d)
    bid is all distinct, therefore all dependencies from it holds, including bid->age,size

e)
    a. b. c.

f)
    a.

g)
    40,60,90,170
    because bid is key, the constraint bid->name,age,size produce no invalid rows.
    therefore, we are answering the query directly: "DISTINCT cost" 

h), i) : study later

Ex2.

a)
    1A, 2C, 3D, 4B, 5C

b)
    P = {"Fl", "lo", "ow", "we", "er"}
    Q = {"Fl", "lw", "we", "er"}

c)
    |P\cap Q| = |{"Fl", "we", "er"}| = 3

d)
    |P\cup Q| = |{"Fl", "lo", "ow", "we", "er", "lw"}| = 6

e)
    Jaccard(P,Q) = 3/6 = 1/2

f)
    certain duplicates: AD
    certain non-duplicates: AB, AC, BD, BE, CD, CE
    uncertain: AE, BC, DE
    \therefore
    all partitions should contain AD as a pair.
    BD is an independent cluster that can or cannot happen.
    E either connect with AD cluster and respect both AE,DE, or do not.
    \therefore
    {AD, B, C, E}
    {AD, BC, E}
    {ADE, B, C}
    {ADE, BC}

g)
$$
    P({ADE,BC}) = 
        0.90 * 0.7 * 0.75
        * 0.6
        * (1-0.10) * (1-0.15)
        * (1-0.20) * (1-0.05)
        * (1-0.10) * (1-0.10)
        = ...
$$

Ex3.
a)
    a., b., e., f.

b)
    b.

c)
    (a) IT department usually lacks domain expertise knowledge and also are unaware of HOW the data will be used. 
    Therefore they can only correct for one quadrant of data quality: (b) they are able to correct information that are context independent
    and application independent. One example can be parsing of dates or standarization of proper names. 
    (c) However they are not able to correct information that are user dependent (e.g. if the data are suitable for some application),
    or information that are context dependent (e.g. if the dates in 'collected time' actually represent the timestamp of the time it was collected).

d)
    in Hospitals, suppose an computer vision application is trained on patient data to predict skin cancer. Any potential data quality issue in the training set,
    either if it is a suitable set, robust, comprehensive etc, can lead to poor decisions over treatment, costing the patient life!


