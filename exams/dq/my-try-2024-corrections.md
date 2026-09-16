Corrections and study notes for my-try-2024.md

Graded against the official answer key (2024-10-11-dsai-dq-test.pdf, "Elaboration of the answer" pages) and the DQ lecture slides.

Exercise 1

a) c. — CORRECT. FD "Stock,Weight -> ToyID" does not hold in general: nothing about stock count or weight guarantees uniqueness, so two different toys could coincidentally share both values.

b) a. — CORRECT. Toys 1007 and 1012 share ToyName "Play-Doh Set" and Brand "Hasbro", but their Category differs (Craft vs Education), which is exactly the pattern in option a.

c) c. — CORRECT. Formal notation for "ToyName,Brand -> Category".

d) a. — CORRECT. A deletion-based repair (removing one of the violating tuples) always removes an FD violation.

e) c. — CORRECT. See explanation under f) — under CQA the only certain answers are categories coming from toys whose Material value cannot be blamed for a violation.

f) (unanswered) — Correct answer: the ASP program detects violations of the FD "ToyName, Brand -> Category" (rubric: 0-2pt for recognizing it's an FD, 0-3pt for the specific FD). See "Study notes -> Answer Set Programming" below.

g) (unanswered) — Correct answer: b. (rule 2). See "Study notes -> Answer Set Programming" below.

h) (unanswered) — Correct answer: d. Rule 1 does fire: toys 1007 and 1012 both have annotation t* (they're in the original table), agree on N and B, and have C1≠C2, so the rule body is satisfied and it derives "toys_(...,f)" for one of them.

i) b. — CORRECT.


Exercise 2

a) "3 -> 4 -> 2 -> 1 -> 5" — WRONG. Correct order (referring to the item numbers as listed in the question: 1=Decision model, 2=Search space reduction, 3=Data preparation, 4=Duplicate clustering, 5=Attribute value matching):
3 -> 2 -> 5 -> 1 -> 4
i.e. Data preparation -> Search space reduction -> Attribute value matching -> Decision model -> Duplicate clustering.
See "Study notes -> Record matching process" below for what each step means.

b) b. — CORRECT (100,000 — the exact count from the explanation is 99,001 comparisons, and the exam rounds that to the closest option, 100,000).

c) b. — CORRECT. Using UNION to merge multiple candidate partitionings is not meaningful — you'd need to keep them separate (probabilistically, by human decision, or in a probabilistic DB), not merge them into one set.

d) P = {"Pl", "ay", "-D", "oh"} — marked WRONG against the key, but the question itself is ambiguous/contradictory, see the note below.
The official key gives P = {"Pla","lay","ay-","y-D","-Do","Doh"} (6 overlapping 3-character substrings).
The exam text says: "We define 3-grams as tokens (i.e., a token is a string of 2 subsequent characters)." Taken literally, that parenthetical describes a 2-character token, which is exactly what you did (non-overlapping pairs: "Pl","ay","-D","oh"). But the label "3-gram" and the graded answer both use 3-character overlapping substrings (the standard Q-gram definition from the slides, Q=3). This is a genuine wording error/contradiction in the exam — your answer was a reasonable literal reading of a badly worded question, not a conceptual mistake. Worth flagging to a TA. See "Study notes -> Q-grams" below for the standard definition actually being tested.

e) |P∩Q| = 2 — numerically matches the key's answer (2), but for the wrong reason: computed from the 2-char tokens. With the key's 3-char trigrams, P∩Q = {"Pla","lay"} (2 elements) — coincidentally the same count, different elements.

f) |P∪Q| = 6 — WRONG against the key. Correct: |P∪Q| = 10 (|P|+|Q|-|P∩Q| = 6+6-2 = 10, using the key's trigrams).

g) Jac(P,Q) = 0.33 — WRONG against the key. Correct: Jaccard(P,Q) = 2/10 = 0.2.

h) {A, BC, DE} / {A, BCDE} — CORRECT. Matches the key exactly: { {A,BC,DE}, {A,BCDE} }. Your reasoning (BC and DE are certain matches so never split; A is certainly separate from everyone; the only freedom left is whether BC and DE merge into one cluster) is exactly the intended argument.

i) P({A,BC,DE}) = 0.00382633875 — CORRECT. Same set of factors as the key (on-edges B-C and D-E use P(edge); every other pair uses 1-P(edge)), just in a different multiplication order.


Exercise 3

a) e. — CORRECT. A case-level label doesn't say which of the (usually 4) images actually shows the abnormality, so converting it to an image-level label is ambiguous, not just an "extra step".

b) (documentation/abbreviation example) — plausible / reasonably convincing. This is an open question graded 0-4pt "valid example" + 0-2pt "convincing example", no single correct answer. Your example (undocumented abbreviations leading to preprocessing mistakes) is a valid documentation-as-data-quality-problem case.

c) "have to study this one" — unanswered. See "Study notes -> Business perspective quadrant" below. Needs an example that is simultaneously "information perspective" (an issue with the data/information itself, not with how a user experiences it) AND "context dependent" (needs external/business knowledge to detect, unlike a generic rule like "spelling error").

d) f. — WRONG. Correct: b. (0.2%).
An absolute Z-score of 3.0 means the value could be +3.0 or -3.0 standard deviations away. From the picture, ~0.1% of values lie beyond +3σ and ~0.1% lie below -3σ, so 0.1% + 0.1% = 0.2% of values are at least this extreme in absolute value.

e) c. — CORRECT. Option c describes the autoencoder as learning what is "noise" and flagging noise in the output — that's backwards (it learns what is "normal", and failure to reproduce a value flags it as anomalous), which is why c is the one that is NOT a valid reason.


---

Study notes

Answer Set Programming (repairs), Exercise 1 f/g/h
The ASP program repairs violations of a functional dependency X -> Y. General shape (from the slides, "Students" example, Snum -> Name):
1. Students_(x,y,f) v Students_(x,z,f) <- Students_(x,y,t*) ^ Students_(x,z,t*) ^ y!=z
   Rule to enforce the FD: if two tuples agree on the determinant (x = Snum) but disagree on the dependent attribute (y/z = Name), propose deleting one of them ('f' = delete).
2. Students_(x,y,t*) <- Students(x,y)
   Every original tuple is marked t* ("candidate to be in the repair") — this is what makes original tuples possible members of a possible repair.
3. Students_(x,y,t*) <- Students_(x,y,t)
   Every proposed-insertion tuple is also marked t* — same reasoning, for inserted tuples.
4. Students_(x,y,t**) <- Students_(x,y,t*) ^ not Students_(x,y,f)
   Collects everything that survives (is candidate and not deleted) into the final repaired table.
5. <- Students_(x,y,t) ^ Students_(x,y,f)
   Integrity constraint: discard any solution where the same tuple is both inserted and deleted.

Mapping onto the toy table (I=ToyID, N=ToyName, C=Category, B=Brand, P=Price):
- Rule 1's condition "C1 != C2" while N, B, and t* agree means it is enforcing "ToyName, Brand -> Category". Toys 1007 (Category=Craft) and 1012 (Category=Education) share ToyName="Play-Doh Set" and Brand="Hasbro", so they satisfy the rule body and rule 1 does fire, deriving that one of them must be deleted. That answers both f) (the constraint) and h) (yes, rule 1 produces a derivation, answer d).
- g) asks which rule makes tuples of the original table possible members of a possible repair — that's rule 2 (answer b), the direct analogue of "Students_(x,y,t*) <- Students(x,y)".

Record matching process, Exercise 2a
The slides give one linear pipeline for duplicate detection ("Record Matching Process"):
1. Data preparation — parsing, standardization, encoding fixes, unit conversion, enrichment (e.g. splitting "John A. Doe" into first/middle/last name, or "123,59" -> 123.59).
2. Search space reduction — avoid the full O(n^2) all-pairs comparison, e.g. via the Sorted Neighbourhood Method: sort on a key and only compare records inside a sliding window.
3. Attribute value matching — compute a similarity score per attribute (Jaccard, Levenshtein, Jaro-Winkler, Q-gram, ...) and combine them (often a weighted sum) into one record-pair similarity score.
4. Decision model — turn each pair's similarity score into a decision using thresholds T_lambda (below = certain non-match) and T_mu (above = certain match); in between = possible match / needs review.
5. Duplicate clustering — since "is a duplicate of" should be transitive, take the transitive closure of the certain/possible matches to form clusters (partitions) of records that represent the same real-world entity.

Q-grams / trigrams, Exercise 2 d-g
The standard slide definition: a Q-gram (here Q=3, so "3-gram"/trigram) is an overlapping substring of length 3, sliding one character at a time — not a split into disjoint chunks. For a string of length n you get n-Q+1 trigrams. Example from the slides: "John Doe" (8 chars) -> ["Joh","ohn","hn ","n D"," Do","Doe"] (6 trigrams). Same logic for "Play-Doh" (8 chars, including the hyphen) -> {"Pla","lay","ay-","y-D","-Do","Doh"} (6 trigrams). Jaccard similarity is then |P∩Q| / |P∪Q| over these token sets.
Note: the exam's own phrasing ("a token is a string of 2 subsequent characters") contradicts this and matches your 2-char reading instead — see the note under d) above.

Business perspective quadrant, Exercise 3c
The slides' 2x2 classification of DQ problems (information perspective vs. user perspective) x (context-independent vs. context-dependent):
- Context-independent + information perspective: spelling error, missing data, duplicate data, incorrect value, inconsistent format, outdated data, syntax violation, unique-value violation, integrity-constraint violation.
- Context-independent + user perspective: information is inaccessible/insecure/hard to retrieve or aggregate, errors introduced in transformation.
- Context-dependent + information perspective: violation of a domain constraint, violation of the organization's business rules, violation of laws/regulations, violation of a DBA-defined constraint.
- Context-dependent + user perspective: information not based on fact, of doubtful credibility, irrelevant to the work, inconsistent meaning, hard to manipulate/understand.
So a valid answer for 3c needs an example from the third cell, e.g.: a hospital's "date" field is documented as "date of the activity" but is actually filled with the date the clinician entered the note (which may be days later) — this only becomes a quality problem once you know the hospital's business rule/workflow (context-dependent), and it's a flaw in the data itself, not in how a user experiences it (information perspective).
