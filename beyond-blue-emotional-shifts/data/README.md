# Data

The data files for this project are not published. The forum files contain usernames and the full text of people's posts about their mental health, so they stay on my machine. This page describes each file so the pipeline can be rebuilt from a fresh scrape.

All notebooks read and write this folder as `../data/`.

## Forum files

### `beyondblue_data.csv`

Written by notebook 01 and read by notebook 02. One row per thread.

| Column | Meaning |
|---|---|
| `post_id` | Sequential thread number assigned by the scraper |
| `title` | Thread title |
| `author` | Username of the original poster |
| `date` | Date of the opening post (YYYY-MM-DD) |
| `category` | Board: Anxiety, Depression, PTSD and trauma, Suicidal thoughts and self-harm |
| `preview` | Short preview text from the board listing |
| `post_text` | Full text of the opening post |
| `num_comments` | Number of replies collected (up to 40) |
| `comments_combined` | JSON list of replies, each with `comment_id`, `author`, `timestamp` and `comment` |
| `url` | Thread URL |

### `beyondblue_data_unflattened.csv`

Written by notebook 02. The same threads after cleaning: title and body merged into `post_text`, emojis converted to words, and `preview` and `url` removed.

### `beyondblue_data_flattened.csv`

Written by notebook 02 and read by notebooks 04 and 05. One row per message (42,961 rows).

| Column | Meaning |
|---|---|
| `parent_post_id` | Thread the message belongs to |
| `user_id` | Username of the writer |
| `role` | `original` (opening post), `op_reply` (original poster replying) or `commenter` |
| `text` | Message text |
| `date` | Message date |
| `category` | Board, inherited from the thread |

### `beyondblue_data_flattened_lexicon_enriched.csv`

Written by notebook 04. The flattened file plus `valence_vader`, `subjectivity_tb`, `intensity_scaled` and `arousal_simple`.

### `beyondblue_data_flattened_transformers_twitter_english_enriched.csv`

Written by notebook 05 and read by notebooks 06, 07 and 08. The flattened file plus:

| Column | Meaning |
|---|---|
| `sentiment_dist` | Probabilities for negative, neutral and positive |
| `valence_s` | Positive minus negative probability (−1 to 1) |
| `sentiment_top`, `sentiment_conf` | Most likely sentiment and its probability |
| `emotion_dist` | Probabilities for the 7 emotions |
| `valence_e`, `arousal_e` | Valence and arousal from the emotion probabilities and NRC-VAD (0 to 1) |
| `emotion_top`, `emotion_conf` | Most likely emotion and its probability |

### `validation_sample_for_labeling.csv` and `validation_sample_labeled.csv`

Notebook 05 writes 50 random messages to the first file (`random_state=42`). I added my own labels in `valence_human` (negative, neutral or positive) and `emotion_human` (one of the 7 emotions) and saved the result as the second file.

## Disaster files

### `natural_disaster_data.csv`

Read by notebook 03. Australian Government disaster declarations, 350 rows.

| Column | Meaning |
|---|---|
| `AGRN` | Australian Government Reference Number of the declaration |
| `Start date`, `End date` | Event dates (DD/MM/YYYY), sometimes missing |
| `Duration` | Length in days, often missing |
| `State` | State or territory |
| `Disaster Types` | Comma-separated hazards, for example "Flood, Storm" |

### `natural_disaster_data_cleaned.csv`

Written by notebook 03 and read by notebook 08. 76 bushfire, flood and cyclone events with `agrn`, `state`, `start_date`, `end_date`, `duration_days` and `disaster_types`.

### `beyondblue_x_natural_disaster_data_aligned.csv`

Written by notebook 08. One row for each message and each disaster within 30 days of it (105,713 rows), with `bb_id`, `user_id`, `bb_date`, `disaster_type`, `disaster_state`, `phase` (pre, during, post or empty), `valence`, `arousal`, `emotion_top` and `duration_days`.
