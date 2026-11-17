# The Sketching Gap: Rethinking Sketch AI Through Illustration Practice

Companion repository for the article **The Sketching Gap: Rethinking Sketch AI Through Illustration Practice** by Zeynep Begüm Kara and T. Metin Sezgin (Koç University). The article is currently under review.

Project website: https://sketching-gap.github.io (also at https://zbegum.github.io/sketching-gap.html)

## What is here

| Path | Contents |
|---|---|
| `data/sketching_gap_coded_data.csv` | The 2,087 analysed papers: title, year, venue, DOI and their coded features |
| `data/codebook.md` | What every column and value means |
| `prompts/` | The shared system prompt and the three coding prompts (Tasks A, B and C) |
| `analysis/reproduce_results.py` | Recomputes the main results reported in the article from the CSV |

## How the data were produced

### Corpus

We searched Scopus, the ACM Digital Library and IEEE Xplore on 19 July 2026 for work published between 2011 and 2026. Of 6,497 records, 4,964 remained after removing duplicates; screening left 2,273 papers, and the 2,087 with an English full text available were analysed.

### Coding

- **Model.** Each paper was coded by Qwen3-4B-Instruct-2507, an openly available language model, served with vLLM on two NVIDIA T4 GPUs.
- **Full text.** Each PDF was converted to text page by page with PyMuPDF4LLM (without OCR), and the reference list was removed. All 2,087 papers were sent to the model in full, with a context window of 65,536 tokens (49,152 for 394 papers when GPU memory required it). The median paper was 10,821 tokens long, and the longest 53,912.
- **Three passes.** The model answered short yes/no or short-list questions in three passes, using the prompts in `prompts/`:
  - **Task A**, what the system does with a sketch: its inputs and outputs, the principal task and the role of the sketch;
  - **Task B**, how people work with it: 15 questions on repeated interaction and its purpose, unfinished drawings, several results and branches, earlier material, several people, evaluation with people and its focus, claims of creative support, and intended users;
  - **Task C**, what the capabilities are used for: one follow-up question per capability, asked only of papers that have that capability.

  The paper text comes first and the instructions last, with the same system prompt for every pass. Each later pass is shown the answers to the earlier ones.
- **Evidence first.** For every question, the model first quotes a short passage and gives its page, then answers. Each quote was checked automatically against the PDF text and marked as exact, approximate or not found.
- **Majority of three.** Each request asked for three completions at a temperature of 0.6, and the most frequent answer to each question was kept.
- **Derived features.** Some columns combine several answers, for example `unfinished_drawing` (the system responds while drawing, or is designed for unfinished sketches). The rules are given in `data/codebook.md`.

See the article for the full method and its checks.

## Reproducing the results

```
python3 analysis/reproduce_results.py
```

The script needs only Python 3.8 or later and prints the task and role distributions, their change between periods, the capabilities, their coded purposes, and the evaluation results.

## Citation

```
@misc{sketchinggap2026,
  title        = {The Sketching Gap: Rethinking Sketch AI Through Illustration Practice},
  author       = {Kara, Zeynep Begüm and Sezgin, T. Metin},
  year         = {2026},
  howpublished = {https://sketching-gap.github.io},
  note         = {Manuscript under review}
}
```

## Licence

The data (`data/`) and prompts (`prompts/`) are released under the [Creative Commons Attribution 4.0 International licence (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). The code (`analysis/`) is released under the MIT licence; see `LICENSE`.
