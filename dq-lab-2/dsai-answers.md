

# Exercise 1


my try + questions

a)
    t
    f
    t
    f
    t
    f

note: inclusion dependency is a subsetequal relation: $A[X] \subseteq B[Y]$ means that all values of $A[X]$ exist inside the values of $B[Y]$.

b)
    f : (cid[1] = cid[5] (1=1) but fnm[1] \neq fnm[5] (John \neq Jon)
    f : (rd[1] = rid[2] (1=1) but plane[1] \neq plane[2] (A380 \neq A300)
    t
    f : (tcode[1] = tcode[6] but tcity[1] \neq tcity[6])

c) 
    c
    note: c represents the definition of functional dependency between a->d,g ; which translate to rid->lmn, time. as rid is key, if we have two rows with same rid everything else is the same, including d and g columns.


d)
    d
    note: "Pattern Tableau".

e)
    f : a constraint of the form A -> B can be violated, but we don't know if B is wrong, or A is wrong.

f)
    what is a "consistent query answering approach?"
    it would appear:
        Mary Lawson
        Peter Blanks
        Floor Dessing

g) 
    Mary Lawson
    Peter Banks
    




Exercise 2





Exercise 3

a)
Jaccard(P,Q) = |P \cap Q| / |P \cup Q|

Jon John
|P \cap Q| = |set(Jon)| = 3
|P \cup Q| = |set(John)| = 4

    R: 3/4

b)
N_{Levenshtein}(A,B) = 1 - L(A,B)/max(length(A), length(B))
L(A,B)

L("Jon", "John") = 1
max(length("Jon"),length("John")) = max(3,4) = 4

N_{Lev}("Jon", "John") = 1 - 1/4 = 3/4

    R: 3/4

what this "L(A,B)" really means for a more complex example?

c)

tl = 0.4
tu = 0.9

definitive duplicates:
AA = BB = CC = DD = EE = 1.00
AB = 0.95

definitive non-duplicates:
AD = 0.20
AE = 0.25
BD = 0.20
BE = 0.25
CD = 0.25
CE = 0.20

uncertainty pairs:
AC = 0.45
BC = 0.50
ED = 0.45

{A,B},{C},{D},{E}
{A,B},{C},{D,E}
{A,B,C},{D},{E}
{A,B,C},{D,E}


d)
consider {A,B,C},{D,E}

AB  = 0.95     = 0.95
AC  = 0.45     = 0.45
AnD = (1-0.20) = 0.80
AnE = (1-0.25) = 0.75
BC  = 0.50     = 0.50
BnD = (1-0.20) = 0.80
BnE = (1-0.25) = 0.75
CnD = (1-0.25) = 0.75
CnE = (1-0.20) = 0.80
DE  = 0.45     = 0.45

p(partition) = 0.02077


e)





Exercise 4

a)
    This represents a problem design issue, not a data quality issue. The model will predict using Reservation table, therefore it will give a single prediction per reservation. By the model perspective, the fact that the same user have two rows in the dataset is not an issue, because the model can use other features such as destination, day of the week and time of travel to infer whether that particular reservation is a business or a leisure one. However, if our problem is to classify CUSTOMERs, for those that engage in more than one reservation, we can aggregate the binary predictions into a probability of leisure vs business travel. Therefore, we still would require a second threshold decision in order to fully classify a customer as leisure traveler or business traveler.

b) 
    f : assuming that the couple Lawson traveled together, probably the plane attribute have its inconsistencies.
    t : probably that is the name of it. teach me about the indicator method
    t : data is never perfect
    f : even if the data is accurate, the features can be uninformative to the prediction task


c)
    lets study those concepts again MCAR, MAR, NMAR, etc


Exercise 5

a)
    For sure, the quality of the dataset, specially for prediction purposes, depends on the objective and target. 
Consider for example an image dataset produced by various MRI scans of patient bones. The dataset can be extremely high-quality to predict the brand of the machine that produces the image, because it contains the watermarks of the scan, but rather poor to predict the actual bone structure of patience, because a vision model trained on the data can "cheat" over the MRI watermarkers.

b) 
