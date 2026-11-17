"""Recompute the main results of The Sketching Gap from the coded data.

usage: python3 analysis/reproduce_results.py [data/sketching_gap_coded_data.csv]
Requires Python 3.8+ only (standard library).
"""
import csv, sys
from collections import Counter

path = sys.argv[1] if len(sys.argv) > 1 else "data/sketching_gap_coded_data.csv"
rows = list(csv.DictReader(open(path, encoding="utf-8")))
N = len(rows)
yes = lambda r, k: r[k] == "yes"
pct = lambda a, b: f"{100 * a / b:.1f}%" if b else "–"
PERIODS = [("2011–14", 2011, 2014), ("2015–18", 2015, 2018), ("2019–22", 2019, 2022), ("2023–26", 2023, 2026)]
period = lambda lo, hi: [r for r in rows if lo <= int(r["year"]) <= hi]

def section(t): print(f"\n== {t}")

print(f"Papers analysed: {N}")

section("Principal task")
for k, n in Counter(r["task"] for r in rows).most_common(): print(f"  {k:28s} {n:5d}  {pct(n, N)}")

section("Role of the sketch")
for k, n in Counter(r["sketch_role"] for r in rows).most_common(): print(f"  {k:28s} {n:5d}  {pct(n, N)}")

section("Change between periods (share of papers)")
print("  papers per period:", ", ".join(f"{l} {len(period(a, b))}" for l, a, b in PERIODS))
for label, f in [("generation", lambda r: r["task"] == "GENERATION"),
                 ("sketch as prompt", lambda r: r["sketch_role"] == "CONDITION_OR_PROMPT"),
                 ("sketch as interactive workspace", lambda r: r["sketch_role"] == "INTERACTIVE_WORKSPACE")]:
    print(f"  {label:32s}", " → ".join(pct(sum(f(r) for r in period(a, b)), len(period(a, b))) for _, a, b in PERIODS))

section("Working with a sketch over time (all papers; by period)")
for k in ["acts_on_result", "unfinished_drawing", "earlier_material", "several_people", "several_results", "branches_kept"]:
    n = sum(yes(r, k) for r in rows)
    trend = " → ".join(pct(sum(yes(r, k) for r in period(a, b)), len(period(a, b))) for _, a, b in PERIODS)
    print(f"  {k:24s} {n:5d}  {pct(n, N):>6s}   {trend}")

section("What the capabilities are used for (eligible papers only)")
for k in ["search_purpose", "loop_purpose", "unfinished_treatment", "earlier_material_use", "exchange_between_people"]:
    vals = [r[k] for r in rows if r[k]]
    print(f"  {k} (n = {len(vals)}): " + ", ".join(f"{v} {pct(c, len(vals))}" for v, c in Counter(vals).most_common()))

section("Practitioner-oriented papers")
A = [r for r in rows if yes(r, "artists_or_designers")]; O = [r for r in rows if not yes(r, "artists_or_designers")]
print(f"  share of corpus: {len(A)} ({pct(len(A), N)});  by period:",
      " / ".join(pct(sum(yes(r, "artists_or_designers") for r in period(a, b)), len(period(a, b))) for _, a, b in PERIODS))
for k in ["acts_on_result", "unfinished_drawing", "earlier_material", "several_people"]:
    print(f"  {k:24s} practitioner {pct(sum(yes(r, k) for r in A), len(A))}  vs other {pct(sum(yes(r, k) for r in O), len(O))}")

section("Evaluation with people")
E = [r for r in rows if yes(r, "evaluated_with_people")]
foc = [r["evaluation_focus"] for r in E if r["evaluation_focus"]]
print(f"  evaluated with people: {len(E)} ({pct(len(E), N)})")
print("  main focus: " + ", ".join(f"{v} {pct(c, len(foc))}" for v, c in Counter(foc).most_common()))
C = [r for r in rows if yes(r, "claims_creative_support")]; CE = [r for r in C if yes(r, "evaluated_with_people")]
proc = sum(r["evaluation_focus"] == "PROCESS_OF_IDEAS_OR_DRAWING" for r in CE)
print(f"  claims creative support: {len(C)} ({pct(len(C), N)}); no study with people {pct(len(C) - len(CE), len(C))}; "
      f"study of how ideas or drawings develop {pct(proc, len(C))}; from practitioner-oriented papers {pct(sum(yes(r, 'artists_or_designers') for r in C), len(C))}")
