# Exercise 1

my try + questions

a)
    t
    f
    t
    f
    t
    f

Note: Inclusion dependency is a subset relation ($A[X] \subseteq B[Y]$), meaning that all values present in $A[X]$ must also exist in $B[Y]$.

b)
    f : (cid[1] = cid[5] (1=1) but fnm[1] \neq fnm[5] (John \neq Jon))
    f : (rid[1] = rid[2] (1=1) but plane[1] \neq plane[2] (A380 \neq A300))
    t
    f : (tcode[1] = tcode[6] but tcity[1] \neq tcity[6] (Vienna \neq Wenen))

c) 
    c
    Note: Option 'c' represents the exact mathematical definition of the functional dependency fid -> fcode, tcode. It states that if two rows have the same 'fid' (a), regardless of other values, they must have the same 'fcode' (d) and 'tcode' (g).

d)
    d
    Note: The correct technical term is "Pattern Tableau".

e)
    f : If a constraint of the form A -> B is violated, we know there is an error, but we cannot deduce whether A is wrong, B is wrong, or both.

f)
    what is a "consistent query answering approach?"
    it would appear:
        Mary Lawson
        Peter Blanks
        Floor Dessing

g) 
    Mary Lawson
    

Exercise 2

a)
Functional dependency violations for 'album, year -> genre':
Number of violations found: 3

Violation details:
Violation 1:
  Row 0: Billie Jean - Album: Thriller, Year: 1982, Genre: Pop
  Row 1: Beat It - Album: Thriller, Year: 1982, Genre: Rock

Violation 2:
  Row 1: Beat It - Album: Thriller, Year: 1982, Genre: Rock
  Row 4: Human Nature - Album: Thriller, Year: 1982, Genre: Pop

Violation 3:
  Row 13: Starboy - Album: Starboy, Year: 2016, Genre: Pop
  Row 14: I Feel It Coming - Album: Starboy, Year: 2016, Genre: R&B

b)
there is 64 possible repair tables

c)

The song "Beat it" is a common denominator: it is a single song that causes conflict with both "Billie Jean" and "Human Nature". By updating this song (Genre from Rock to Pop), we can solve two violations at once.


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

Note: L(A,B) represents the Levenshtein distance, which is the minimum number of single-character edits (insertions, deletions, or substitutions) required to change word A into word B (e.g., transforming "kitten" to "sitting" requires 3 edits).

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

Unnormalized P(partition) = 0.02077


e)
They do not remain as alternatives forever. We use probabilistic databases to quickly integrate all available evidence into a single place, achieving a fast initial integration. As we start using the system and gathering more evidence (e.g., human feedback or new data rules), we can continuously improve the database's quality by progressively collapsing the uncertainty into a single correct answer.


Exercise 4

a)
    This represents a problem design issue, not a data quality issue. The model predicts at the reservation level, yielding a single prediction per reservation. From the model's perspective, the fact that the same user has two rows with different 'bl' values accurately reflects reality and is not an issue. The model can use other features, such as destination, day of the week, and time of travel, to infer whether a particular reservation is for business or leisure. However, if our goal is to classify customers globally, we would need to aggregate these binary reservation predictions into a probability and apply a secondary threshold to classify the customer as a leisure or business traveler.

b) 
    f : Assuming that the couple Lawson traveled together on the same flight, the 'plane' attribute has inconsistencies (A380 vs A300).
    f : Deleting rows is called "listwise deletion". The "indicator method" involves keeping the row but adding a new binary variable to indicate whether the value was missing.
    t : Data is never perfect.
    f : Even if the data is 100% accurate, the features themselves might lack the predictive power needed to achieve 100% accuracy.


c)
    Data can be missing for a variety of reasons. Stating that the missing pattern is MCAR means that the data is independently and randomly dropped from the database, with no relationship to its underlying value or to any other observed values. To assess this, we can use the indicator method to create a "missingness flag" and try to predict it using the other features with a model like logistic regression. If all coefficients are statistically insignificant, we rule out the MAR hypothesis, making it more likely to be MCAR (assuming we can also rule out MNAR based on domain knowledge).


Exercise 5

a)
    Absolutely. The quality of a dataset, especially for prediction purposes, heavily depends on the objective and target ("Fitness for Use"). Consider an image dataset produced by various MRI scans of patient bones. The dataset might be of extremely high quality for predicting the brand of the MRI machine, because it contains clear watermarks. However, it would be of poor quality for predicting actual bone structures, as a vision model trained on this data could "cheat" by learning to identify the watermarks instead.

b)
    Yes, a dataset can be perfectly accurate, complete, and have sufficient rows and columns, yet still be of bad quality. For example, the data might have been collected 15 years ago, making it untimely and of poor quality for predicting current trends. Additionally, the entries could suffer from bad formatting or inconsistency, such as unstandardized date formats, making it difficult to use.

c)
    Yes. Modern Data Quality frameworks define quality as "fitness for use". If a dataset contains highly sensitive records (e.g., perfectly accurate and complete patient data) but is saved without anonymization or proper security, it cannot be safely used by the doctors who need it without violating privacy laws. Thus, poor security destroys its fitness for use.

d)
    Symbolic reasoning.

e)
    Symbolic reasoning can be mathematically traceable but not practically interpretable if the input features lack interpretation. For example, assume a feature extractor collects a highly non-linear feature map from images. The entries of this feature map are numerical values without clear human meaning. If we develop symbolic reasoning over these entries, we might conclude traceable logic steps such as: "if f[1] > f[2] then class A". Although a human can easily compute and trace this rule, the underlying meaning remains uninterpretable because f[1] and f[2] lack semantic meaning.

f)
    The PhD student likely decided not to drop the incomplete mammograms because the missingness could be related to the actual outcome of the exam (MNAR). For example, if patients with severe, malignant cancers are in too much pain to complete all four pictures, dropping these records would eliminate critical information from the dataset and heavily bias the model.
