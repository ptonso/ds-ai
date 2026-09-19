Corrections and study notes for my-try-2023.md

Graded against the official "Correctiemodel" (2023-10-13 example exam) and the DQ lecture slides.
Case: GreatBuildings(bid, name, age, level, cost, bonus, size, descr) — bid is auto-generated/unique.
Columns, precisely: bid=id, name=building name, age="Bronze"/"Iron"/"Progressive" (an era label, not a number!), level=1/2/3, cost, bonus, size (grid dims), descr.


Exercise 1

a) "yes, bid is a key" — CORRECT. bid is auto-generated and therefore unique, so it's (at least) a superkey; any FD "bid -> anything" holds trivially, independent of what the data actually looks like.

b) "yes, as bid is key, any combination with other values should hold..." — CORRECT, same reasoning: {bid,level} is a superset of the key {bid}, so it's also a superkey, and any FD from a superkey holds trivially (even though, as you noted, it's not a meaningful constraint to actively maintain).

c) "..." (unanswered) — This question was officially CANCELLED by the course staff ("none of the answers is perfectly correct"), so it doesn't cost you anything either way. For reference, the intended/closest answer was **d**. Not worth studying the specific option — the formal-notation pattern is the same one covered for the 2024 exam (universally-quantified implication over two tuples).

d) "bid is all distinct, therefore all dependencies from it holds, including bid->age,size" — CORRECT. Same trivial-key argument, this time explicitly checked against the data (bid values 1-7 are indeed all distinct), so it still holds.

e) "c." — INCOMPLETE. This is a multi-select question ("multiple answers possible"), options were:
a. Given the data is high quality, it can be effectively used for business analytics.
b. There are a lot of missing values, but it always contains sufficient info for users' tasks, so quality is high.
c. Documentation is bad. This can be a reason for bad data quality.
d. New software released due to changed requirements → data is of higher quality as a consequence.
Based on the rubric's point split (a base total of 2pt implied by a 3+1+1+1=6pt table format) and the "fitness for use" principle central to this course, the correct selection is **a, b, c** (true) and **d** (false):
- a is true almost by definition (quality = fit for the intended use).
- b is the key insight the question is testing: DQ is not the same as completeness — if missing values don't stop users from doing their tasks, the data can still be considered high quality (fitness-for-use, not raw completeness).
- c is true (matches the documentation-as-data-quality-problem point from the 2024 exam too).
- d is false: releasing new software doesn't retroactively change data that's already sitting in the database; if anything, "changed requirements" could make old data *less* fit for the new purpose.
You only selected c, missing a and b (the bigger point value). See "Study notes -> fitness for use" below.

f) "d." — WRONG. Correct: **a** (the number of repairs can be infinite).
For a single FD violation between two tuples, an update-based repair can set the offending string attribute to *any* value that removes the violation — and since string domains are unbounded, there are infinitely many such values, hence infinitely many valid repairs. (This is the same point tested in the 2024 exam's "repair based on updates is not possible because there are infinitely many possible strings" option — here it's flipped into "the count of repairs can be infinite.")

g) "40,60,90,170" — CORRECT value, but INCOMPLETE explanation. The rubric awards 2pt for the correct value and a separate 2pt for explicitly stating *why*: the constraint "bid -> name,age,size" is never violated in this table (bid is unique), so under Consistent Query Answering no repair is ever needed, and the query just returns its normal, unrepaired result: the 4 distinct cost values {40,60,90,170}. Next time, say the "why," not just the answer — CQA questions are specifically graded on recognizing whether a repair is even necessary.

h) "study later" (unanswered) — Correct answer: **NO**, not all 5 rules are used. See "Study notes -> ASP rules 2023" below for the full derivation — rules 3 and 5 never fire (structurally, not just on this data), while rule 1 does fire (on two specific pairs of rows).

i) "study later" (unanswered) — Correct answer: **b** ("deleting one of the two records if a pair violates the constraint"). See "Study notes -> ASP rules 2023" below.


Exercise 2

a) "1A, 2C, 3D, 4B, 5C" — 4 out of 5 correct. Matching each DB→RW diagram to Proper(A) / Ambiguous(B) / Incomplete(C) / Duplicate(D):
- 1 -> A: CORRECT (clean, complete, unambiguous 1-1 correspondence).
- 2 -> you said C, key says something else (not C) — WRONG. My best reconstruction (the scan is genuinely unclear on this one letter) is **B**: a crossed-but-still-1-1 mapping is fully determined and non-duplicated, so it isn't "incomplete" — I lean toward "ambiguous" for a crossed pairing, but flag this one item as lower-confidence from the source scan.
- 3 -> D: CORRECT (two DB circles converging on one real-world circle = duplicate).
- 4 -> B: CORRECT (one DB circle fanning out to multiple real-world circles = ambiguous, you can't tell which one it really refers to).
- 5 -> C: CORRECT (a DB or RW node left unconnected = incomplete).
So you're solid on the core concept (4/5), just double check item 2 with a TA if it matters for your score.

b) P = {"Fl","lo","ow","we","er"} — CORRECT. This exam's 2-gram wording is (unlike the 2024 exam!) internally consistent: "a token is a string of 2 subsequent characters" and it really does mean overlapping 2-character substrings. "Flower" is 6 characters, giving 6-2+1=5 tokens. Nice work catching that this one wasn't contradictory.

c) |P∩Q| = 3 ({"Fl","we","er"}) — CORRECT.

d) |P∪Q| = 6 — CORRECT.

e) Jaccard(P,Q) = 3/6 = 0.5 — CORRECT.

f) Partitionings — CORRECT. Your classification (certain match: AD; certain non-matches: AB,AC,BD,BE,CD,CE; uncertain: AE,BC,DE) exactly matches the key, and so do your 4 final partitionings: {AD,B,C,E}, {AD,BC,E}, {ADE,B,C}, {ADE,BC}. (Minor: your reasoning prose says "BD is an independent cluster that can or cannot happen" — that should read "BC", since BD is a certain non-match, not an uncertain edge. Doesn't affect your correct final answer.)
Why exactly 4 and not more: once A and D are forced together (certain match), E's fate is a single joint decision — A-E and D-E can't be decided independently, because if E joined via A-E but not D-E (or vice versa) you'd have a partition that isn't transitively closed (A~D and A~E would force D~E too). So E either joins the AD cluster (both A-E and D-E "on") or stays out (both "off") — 2 choices, times B/C merging or not — 2 choices — 4 total.

g) Probability calculation — CORRECT method, just not carried to a final number. For {ADE,BC}: on-edges are A-D(0.9), A-E(0.7), D-E(0.75), B-C(0.6); off-edges are the remaining six pairs (0.1, 0.15, 0.2, 0.05, 0.1, 0.1). Your formula lists exactly these 10 factors correctly. Finishing the arithmetic: 0.9×0.7×0.75×0.6 = 0.2835, and 0.9×0.85×0.8×0.95×0.9×0.9 ≈ 0.4709, so P({ADE,BC}) ≈ 0.2835 × 0.4709 ≈ **0.1335**.


Exercise 3

a) "a., b., e., f." — Effectively CORRECT / thorough. Base correct answers are a and b (Z-score ±3 → 0.2% outliers; Z=+2.0 means 2 std devs above the mean), and f is a bonus-credit answer (Z-scores are undefined for nominal/categorical data, since there's no meaningful mean or std dev to compute). You caught all three. Your extra pick, e, says the same thing as b just using the word "average" instead of "mean" — literally the same statement, so it's a defensible, harmless inclusion even though the official key doesn't specifically credit it.

b) "b." — CORRECT. The reason 4-image mammography models don't work in practice: ~8% of real patients don't have all 4 images available, and the hospital doesn't want to exclude those patients from getting a prediction at all.

c) Your answer (IT lacks domain/usage-context knowledge → can only fix context-independent, application-independent problems like date parsing/name standardization; cannot fix user-dependent or context-dependent problems, e.g. "collected time" actually meaning entry time) — well-reasoned and directly uses the quadrant framework correctly. This covers both rubric criteria (what they *can* do: data cleaning, ~3pt; what they *cannot* do: lacking domain/usage knowledge, with two good concrete reasons, ~5pt). Strong answer, no correction needed.

d) Your answer gives one solid example (a DQ flaw in a medical training set leading to a wrong cancer-treatment decision — a literal life-or-death cost). The question asks for **two** examples of non-monetary cost, and only one was given, so this is likely worth about half credit. A second example to add, e.g.: loss of public/patient trust in the hospital or the AI system once an error surfaces (reputational cost); or wasted researcher/clinician time re-validating a flawed dataset before it can be used at all (opportunity cost); or in a different domain, a self-driving car misclassifying an object due to poor sensor-data quality causing physical harm.


---

Study notes

Fitness for use, Exercise 1e
A recurring theme in this course: data quality is not the same thing as literal completeness or literal accuracy — it's *fitness for the intended use*. A dataset riddled with missing values can still be "high quality" if none of those missing fields matter for what the users actually need to do with the data; conversely a perfectly complete, perfectly accurate dataset can be "low quality" if it's the wrong data for the job (irrelevant, hard to access, undocumented, etc. — the "user perspective" column from the quadrant you already studied for the 2024 exam). Exercise 1e and 1c/1d (the "IT department" question) are really testing the same underlying idea from two angles.

ASP rules, Exercise 1 h/i (2023 version)
The program (variables B=bid, N=name, A=age, L=level, S=size), rule 1 exactly as printed:
GB_(B1,N,A,L1,S,f) v GB_(B2,N,A,L2,S,f) <- GB_(B1,N,A,L1,S,t*) ^ GB_(B2,N,A,L2,S,t*) ^ B1≠B2
Read the variable positions carefully: N, A, and S are the *same* variable in both halves of the body (not subscripted), while B and L are subscripted (B1 vs B2, forced different). So rule 1 literally fires when two tuples share identical name, age, and size but have *different* bid — i.e. as written, it detects violations of "name,age,size -> bid", the reverse of the "bid -> name,age,size" constraint described in the question text. (This looks like an inconsistency in the exam's own rule vs. its prose description — worth a raised eyebrow, but it doesn't change how to answer the question: evaluate the rule exactly as given.)
Checking the actual data: rows 1 & 2 ("Tower of Babel", "Bronze", size "4x4") share identical name+age+size and differ only in bid/level/cost/bonus — rule 1's body is satisfied. Rows 5, 6, 7 ("Alcatraz", "Progressive", size "10x7" for all three) do too. So rule 1 *does* fire on this database.
Rules 3 and 5 both require a raw "t" (insertion) annotation as a precondition — but no rule in this 5-rule program ever *concludes* "t" anywhere (only "t*", "f", and "t**" are ever derived). Since nothing ever produces "t", rules 3 and 5's bodies can never be satisfied, so they never fire — structurally, regardless of what the data looks like. Rule 2 and rule 4 fire normally (rule 2 marks every original tuple t*; rule 4 collects every t* tuple not marked f into the final table).
So: NO, not all rules are used — specifically rules 3 and 5 never fire. That answers h). For i), since the only repair action this program can ever produce is rule 1's disjunctive head (propose deleting *one* of the two tuples in a violating pair), the only correct option is **b** — insertion-based, fill-in, and update-based repairs (a, c, d) aren't supported by this program at all, and "delete both" (e) isn't what a disjunction (OR) encodes — it only requires removing one side to satisfy the constraint, which is the minimal repair.
