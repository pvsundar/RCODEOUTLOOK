# Figure 7 — Redesign Brief (hand this to cowork)

**Figure:** Richness & evenness for pairs of years, across the eras.
**Problem:** One era-transition (the "jump") is so large that, on a single
linear y-axis, every other year-pair is squashed down near zero and becomes
unreadable.
**Goal:** Keep that big era-jump visible *in context* while making the other
year-pairs readable and comparable again.

## Preferred fix — broken / split Y-axis (Panel B in the handout PNG)

- Split the y-axis into two bands:
  - **lower band** = the normal range of values (zoom in here),
  - **upper band** = the spike (compressed),
  - draw small **diagonal break marks** where the axis is cut.
- Keep **richness** and **evenness** as the two grouped series.
- Keep the **year-pair labels** on the x-axis.

### R (ggplot2 + ggbreak)
```r
library(ggplot2)
library(ggbreak)   # install.packages("ggbreak")

# p = your existing Figure 7 ggplot (grouped bars: richness + evenness)
p_rescaled <- p +
  scale_y_break(c(TOP_OF_NORMAL, BOTTOM_OF_SPIKE), scales = 0.3) +
  labs(caption = "Y-axis has a break so the large era-jump does not compress the other values")

ggsave("figure7_axisbreak.svg", p_rescaled, width = 10, height = 6)
```
Set `TOP_OF_NORMAL` to just above the tallest "normal" bar and
`BOTTOM_OF_SPIKE` to just below the spike.

### Python (matplotlib, two stacked axes)
See `make_handout.py` in this folder — Panel B contains a working broken-axis
recipe (two stacked `Axes` sharing the x-axis, with diagonal break marks).
The `brokenaxes` package also works.

## Fallbacks
- **Log y-axis** (Panel C): one line — `scale_y_log10()` / `ax.set_yscale("log")`.
  Use if a clean break looks awkward.
- **Clip + label the spike** (Panel D): cap the axis at the normal range, let the
  spike run off the top, and print its true value as a text label. Simplest;
  keeps a linear feel.

## Must-dos
- **Save as a NEW file** (e.g. `figure7_axisbreak.svg`) — do **not** overwrite
  the original Figure 7.
- The numbers in the handout PNG are **placeholders** to show the layout —
  replace them with the real richness / evenness values.

## Files in this folder
- `figure7_redesign_handout.png` — the visual mockup (Panels A–D).
- `make_handout.py` — reproducible script that builds the mockup.
- `figure7_redesign_brief.md` — this brief.
