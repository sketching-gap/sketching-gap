# Codebook: `sketching_gap_coded_data.csv`

One row per analysed paper (2,087 rows). Yes/no features are `yes` or `no`. Purpose columns are filled only for papers eligible for that question (see below) and are otherwise empty.

## Bibliographic columns

| Column | Meaning |
|---|---|
| `paper_id` | Identifier used in the project (P00001 …) |
| `title`, `year`, `venue` | As recorded in the database export |
| `doi` | Digital Object Identifier, without the `https://doi.org/` prefix; empty for 66 papers without one |

## What the system does

| Column | Values |
|---|---|
| `task` | The paper's principal computational task: `GENERATION`, `RETRIEVAL`, `RECOGNITION_UNDERSTANDING`, `MODELLING_RECONSTRUCTION`, `INTERACTION_CONTROL`, `PROCESSING_ENHANCEMENT` |
| `sketch_role` | The role the sketch plays: `RETRIEVAL_QUERY` (a search query), `CONDITION_OR_PROMPT` (a prompt for a new image), `RECOGNITION_TARGET` (something to identify), `GENERATED_OUTPUT` (the output of the system), `INTERACTIVE_WORKSPACE` (an ongoing drawing to which person and system keep responding), `GEOMETRIC_CONSTRAINT`, `TRANSFORMED_OUTPUT`, `PARTIAL_SPECIFICATION`, `INTERMEDIATE_REPRESENTATION` |
| `sketch_input` | A person's sketch is an input to the system |
| `sketch_output` | The system's output is a new sketch |

## How people work with it

| Column | Meaning |
|---|---|
| `person_uses_system` | A person directly uses the system |
| `acts_on_result` | Repeated interaction: a person responds to a result and the system responds again |
| `unfinished_drawing` | The system responds while the person is drawing, or is designed to take an unfinished sketch |
| `earlier_material` | A person uses the system and can return to earlier versions of the work or reuse their own earlier sketches |
| `kept_across_sessions` | Sketch material is kept beyond a single session |
| `several_results` | Several alternative results are shown for one input, or separate branches are kept |
| `branches_kept` | Separate branches of work are kept and can be developed further |
| `several_people` | Two or more people take part in the same sketching workflow |
| `evaluated_with_people` | The paper reports an evaluation with people, and the supporting passage explicitly mentions human participation (for example participants, users, raters or a user study) |
| `claims_creative_support` | The paper explicitly claims to support creativity, ideation, exploration, design thinking or artistic practice |
| `artists_or_designers` | Artists, illustrators, animators, designers or architects are the intended users or study participants |

## What the capabilities are used for

Each purpose column is filled only for eligible papers, as in the article.

| Column | Eligible papers | Values |
|---|---|---|
| `search_purpose` | `task` is `RETRIEVAL` and `acts_on_result` or `several_results` is `yes` (400 papers) | `FIND_KNOWN_ITEM`, `EXPLORE_OR_COMPARE`, `UNCLEAR` |
| `loop_purpose` | `acts_on_result` is `yes` (739 coded) | `REFINE_TOWARDS_TARGET`, `EXPLORE_ALTERNATIVES`, `CORRECT_OR_CONFIRM`, `UNCLEAR` |
| `unfinished_treatment` | `unfinished_drawing` is `yes` (331 coded) | `OFFERS_EDITABLE_OR_REVERSIBLE`, `INTERPRETS_EARLY`, `RESOLVES_AUTOMATICALLY`, `UNCLEAR` |
| `earlier_material_use` | `earlier_material` is `yes` (152 coded) | `REUSE_IN_NEW_WORK`, `UNDO_OR_REVERT`, `COMPARE_OR_REVISIT`, `UNCLEAR` |
| `exchange_between_people` | `several_people` is `yes` (93 coded) | `CO_CREATION`, `COMMUNICATION_COORDINATION`, `FEEDBACK_REVIEW_APPROVAL`, `UNCLEAR` |
| `evaluation_focus` | `evaluated_with_people` is `yes` (806 coded) | `TASK_PERFORMANCE`, `OUTPUT_QUALITY`, `USABILITY_EXPERIENCE`, `PROCESS_OF_IDEAS_OR_DRAWING` |
