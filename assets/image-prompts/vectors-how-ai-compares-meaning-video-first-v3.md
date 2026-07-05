# Vectors: How AI Compares Meaning - Video-First Prompt Pack v3

This v3 image set is the preferred visual direction for the vectors lesson. It keeps the warm student/tablet style from matrices and v2, but adds stronger technical teaching value in every frame.

## Style Bible

- warm modern Indian educational illustration
- Indian teenage learner with dark wavy hair and teal shirt
- wooden study desk, warm desk lamp, notebook, books, small plant
- tablet as the main technical surface
- readable technical elements where needed: vector chips, clusters, distance labels, angle labels, retrieval ranking
- sparse captions in the final video; the source frame itself should show the technical step

## Technical Sequence

```text
phrase pair -> embedding vector -> meaning-space points -> distance comparison -> angle comparison -> nearest search results -> recap pipeline
```

## Frame Teaching Table

| # | Frame | Learning job | Visible evidence | Motion role |
|---|---|---|---|---|
| 1 | `01-meaning-not-words-vector-compare.png` | Similar meaning can have similar vectors | two phrase cards become similar colored vector rows and a high similarity meter | vector chips glow in matching patterns |
| 2 | `02-sentence-to-embedding-vector.png` | A sentence becomes an embedding vector | input sentence -> embedding model -> numeric vector row and bars | pulse travels through the embedding model into number chips |
| 3 | `03-vectors-as-meaning-space-points.png` | Vectors can be plotted as points | query point sits near phone cluster and far from recipe/cricket clusters | points settle into clusters |
| 4 | `04-vector-distance-comparison.png` | Distance can measure similarity | short green distance to phone result, long red distance to recipe | short line glows, long line fades |
| 5 | `05-vector-direction-angle.png` | Direction/angle can measure similarity | two phone arrows have a small angle; recipe arrow points away | arrows draw from origin and angle arc pulses |
| 6 | `06-semantic-search-nearest-results.png` | Semantic search ranks nearest vectors | query vector connects to database cards sorted by distance | top two results highlight in order |
| 7 | `07-recap-vector-search-pipeline.png` | Full retrieval pipeline | text -> vector -> meaning space -> nearest result | pipeline nodes light up left to right |

## Source Image Prompts

### Frame 1 - Meaning, Not Exact Words

```text
Create a 9:16 vertical video-first source frame for an educational micro-lesson in the same warm modern Indian educational illustration style as prior matrices lesson: teenage Indian student with dark wavy hair, teal shirt, wooden study desk, warm desk lamp, notebook, books, small plant, cozy study room. Frame 1 technical learning job: AI compares meaning, not exact words. On a tablet, show two large phrase cards with readable text: "cheap phone" and "budget mobile". Each phrase card flows into a row of colored vector number chips below it. The two vector rows are visually similar in color pattern, and a large similarity meter on the tablet shows HIGH with a green glow. Keep the student looking curious, tablet large and clear, minimal extra text, no logos, no watermark, leave safe bottom area for caption overlay.
```

Runway prompt:

```text
The two phrase cards pulse softly into their vector number rows. Matching colored chips glow in both rows, then the HIGH similarity meter brightens. Student points gently at the tablet. Keep all text readable and unchanged. No new text. No crop.
```

### Frame 2 - Sentence To Embedding Vector

```text
Create a 9:16 vertical video-first source frame for an educational micro-lesson in the same warm modern Indian educational illustration style: teenage Indian student with dark wavy hair, teal shirt, wooden study desk, warm desk lamp, notebook, books, small plant, cozy study room. Frame 2 technical learning job: a sentence becomes an embedding vector. On a large tablet, show a readable input card: "affordable smartphone". The card enters a simple glowing box labeled "embedding model". From the box comes a clear vector row: [0.82, -0.14, 0.51, 0.07, -0.21]. Below the vector row, show colored vertical mini-bars aligned with the number chips, suggesting dimensions/features. Student points at the transformation path. Keep tablet large, numbers readable, minimal extra text, no logos, no watermark, safe bottom space for caption overlay.
```

Runway prompt:

```text
The input card sends a light pulse into the embedding model. The vector numbers appear left to right and the colored bars rise gently underneath. Student finger follows the transformation. Preserve text and numbers. No new text. No crop.
```

### Frame 3 - Meaning Space Points

```text
Create a 9:16 vertical video-first source frame for an educational micro-lesson in the same warm modern Indian educational illustration style: teenage Indian student with dark wavy hair, teal shirt, wooden study desk, warm desk lamp, notebook, books, small plant, cozy study room. Frame 3 technical learning job: vectors become points in meaning space. On the tablet, show a clean 2D coordinate plane titled "meaning space" with large colored points. A yellow point labeled "query" sits near a green cluster labeled "phone" with points "cheap phone" and "budget mobile". A red cluster labeled "recipe" is far away, and a purple cluster labeled "cricket" is elsewhere. Show faint coordinate grid lines and dotted circles around clusters. Student looks at the tablet with focused expression. Keep labels large and readable, no dense text, no watermark, safe bottom space.
```

Runway prompt:

```text
The yellow query point lands near the green phone cluster. Phone, recipe, and cricket clusters glow one by one while dotted cluster circles pulse. Keep labels readable and unchanged. No new text. No crop.
```

### Frame 4 - Distance Comparison

```text
Create a 9:16 vertical video-first source frame for an educational micro-lesson in the same warm modern Indian educational illustration style: teenage Indian student with dark wavy hair, teal shirt, wooden study desk, warm desk lamp, notebook, books, small plant, cozy study room. Frame 4 technical learning job: AI can compare vector distance. On the tablet, show the same meaning space plot. A yellow query point is connected by a short bright green line to "budget mobile" labeled "short distance". A long faded red line connects the query to "recipe" labeled "long distance". Add a small ruler icon or distance brackets on the two lines. The phone cluster is highlighted as nearest. Student points at the short line. Keep labels large and readable, no dense text, no logos, no watermark, safe bottom caption space.
```

Runway prompt:

```text
The short green distance line glows first, then the long red distance line appears faded. The nearest phone cluster pulses gently. Student points at the short line. Preserve labels. No new text. No crop.
```

### Frame 5 - Direction And Angle

```text
Create a 9:16 vertical video-first source frame for an educational micro-lesson in the same warm modern Indian educational illustration style: teenage Indian student with dark wavy hair, teal shirt, wooden study desk, warm desk lamp, notebook, books, small plant, cozy study room. Frame 5 technical learning job: AI can compare vector direction/angle. On the tablet, show a clean origin point with three large vector arrows. Two arrows labeled "cheap phone" and "budget mobile" point almost the same direction with a small glowing angle arc labeled "small angle". A third arrow labeled "cake recipe" points far away with a larger faded angle arc. Include a tiny note on tablet: "similar direction = similar meaning". Student watches the arrows closely. Make arrows large and readable, no dense text, no logos, no watermark, safe bottom caption space.
```

Runway prompt:

```text
The three vector arrows draw outward from the origin. The small angle arc between cheap phone and budget mobile glows, while the cake recipe arrow stays separate. Preserve labels. No new text. No crop.
```

### Frame 6 - Semantic Search Results

```text
Create a 9:16 vertical video-first source frame for an educational micro-lesson in the same warm modern Indian educational illustration style: teenage Indian student with dark wavy hair, teal shirt, wooden study desk, warm desk lamp, notebook, books, small plant, cozy study room. Frame 6 technical learning job: semantic search retrieves nearest vector results. On the tablet, show a query box: "affordable smartphone" turning into a yellow query vector dot. To the right, show a simple database column of document cards with distances: 0.08 cheap phone, 0.11 budget mobile, 0.64 laptop bag, 0.91 cake recipe. The first two cards are highlighted green as top matches, with arrows from query dot to those cards. Student has an aha expression. Keep text large and readable, no dense details, no logos, no watermark, safe bottom caption space.
```

Runway prompt:

```text
The query turns into a yellow vector dot. Arrows connect to the database cards, then the 0.08 and 0.11 results highlight green in order. Student reacts with a small aha expression. Preserve text and numbers. No new text. No crop.
```

### Frame 7 - Recap Pipeline

```text
Create a 9:16 vertical video-first source frame for an educational micro-lesson in the same warm modern Indian educational illustration style: teenage Indian student with dark wavy hair, teal shirt, wooden study desk, warm desk lamp, notebook, books, small plant, cozy study room. Frame 7 technical learning job: recap the full vector search pipeline. On the tablet, show a clear left-to-right visual chain with readable labels: "text" -> "vector" -> "meaning space" -> "nearest result". Under each label show the visual: phrase card, row of number chips, clustered points, highlighted search result card. Add the memory anchor in large readable text on the tablet: "Similar meaning = nearby vectors". Student smiles with aha expression and one finger raised. Keep layout clean, labels large, no logos, no watermark, safe bottom caption space.
```

Runway prompt:

```text
The pipeline nodes light up from left to right: text, vector, meaning space, nearest result. The memory anchor glows softly. Student smiles and raises one finger slightly. Preserve all text. No new text. No crop.
```
