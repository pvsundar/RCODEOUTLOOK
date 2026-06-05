"""
Figure 7 redesign handout — broken/split-axis mockup.

This is a DESIGN TEMPLATE, not the final figure. The numbers below are
illustrative placeholders chosen to reproduce the *shape* of the problem
(one era-transition that dwarfs every other year-pair). In cowork, swap in
the real richness / evenness values and the real year-pair labels.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

# ----------------------------------------------------------------------
# PLACEHOLDER DATA  (replace with real Figure 7 values in cowork)
# Pairs of consecutive years; one pair straddles an era boundary = "the jump"
# ----------------------------------------------------------------------
pairs = ["'90–'95", "'95–'00", "'00–'05", "'05–'10",
         "'10–'15", "'15–'20", "'20–'25"]
jump_idx = 3  # the era-boundary transition (the giant one)

# Two series shown in the real Figure 7
richness = np.array([12, 9, 14, 220, 11, 16, 13], dtype=float)   # the spike
evenness = np.array([8, 7, 10, 165, 9, 12, 10], dtype=float)

x = np.arange(len(pairs))
w = 0.38
c_rich, c_even = "#2c6fbb", "#e08a1e"

# break the y-axis: lower band holds the normal values, upper band the spike
lo_top = 30        # top of the lower (zoomed-in) band
hi_bot = 150       # bottom of the upper (spike) band
hi_top = 240

fig = plt.figure(figsize=(12.5, 13.5))
gs = fig.add_gridspec(4, 2, height_ratios=[0.55, 2.4, 2.4, 1.5], hspace=0.45, wspace=0.25)

# ===== Title banner =====
ax_t = fig.add_subplot(gs[0, :]); ax_t.axis("off")
ax_t.text(0.5, 0.72, "Figure 7 — Redesign Handout", ha="center", va="center",
          fontsize=24, fontweight="bold")
ax_t.text(0.5, 0.18,
          "Richness & evenness for pairs of years — rescaling the era-transition 'jump' with a broken Y-axis",
          ha="center", va="center", fontsize=12.5, color="#444")

# ===== Panel A: the PROBLEM (single linear axis) =====
axA = fig.add_subplot(gs[1, 0])
axA.bar(x - w/2, richness, w, color=c_rich, label="Richness")
axA.bar(x + w/2, evenness, w, color=c_even, label="Evenness")
axA.set_title("A.  Problem — one linear axis\n(the era jump flattens everything else)",
              fontsize=12, fontweight="bold")
axA.set_xticks(x); axA.set_xticklabels(pairs, rotation=0, fontsize=9)
axA.set_ylabel("Index value")
axA.legend(fontsize=9, frameon=False)
axA.annotate("everything here\nlooks ~0", xy=(1, 9), xytext=(0.2, 90),
             fontsize=9, color="#b00", ha="center",
             arrowprops=dict(arrowstyle="->", color="#b00"))
axA.annotate("era jump", xy=(jump_idx, 220), xytext=(jump_idx-1.4, 200),
             fontsize=9, color="#222",
             arrowprops=dict(arrowstyle="->", color="#222"))

# ===== Panel B: the FIX (broken / split axis) =====
gsB = gs[1, 1].subgridspec(2, 1, height_ratios=[1, 2.2], hspace=0.08)
axB_hi = fig.add_subplot(gsB[0])
axB_lo = fig.add_subplot(gsB[1])

for ax in (axB_hi, axB_lo):
    ax.bar(x - w/2, richness, w, color=c_rich)
    ax.bar(x + w/2, evenness, w, color=c_even)

axB_hi.set_ylim(hi_bot, hi_top)
axB_lo.set_ylim(0, lo_top)

# hide the spines at the break + add diagonal break marks
axB_hi.spines["bottom"].set_visible(False)
axB_lo.spines["top"].set_visible(False)
axB_hi.tick_params(labeltop=False, bottom=False)
axB_hi.set_xticks([])
axB_lo.set_xticks(x); axB_lo.set_xticklabels(pairs, fontsize=9)
d = 0.012
kw = dict(transform=axB_hi.transAxes, color="k", clip_on=False, lw=1)
axB_hi.plot((-d, +d), (-d*2.2, +d*2.2), **kw)
axB_hi.plot((1-d, 1+d), (-d*2.2, +d*2.2), **kw)
kw.update(transform=axB_lo.transAxes)
axB_lo.plot((-d, +d), (1-d, 1+d), **kw)
axB_lo.plot((1-d, 1+d), (1-d, 1+d), **kw)

axB_hi.set_title("B.  Fix — broken Y-axis\n(spike kept in context, small values readable)",
                 fontsize=12, fontweight="bold")
axB_lo.set_ylabel("Index value")
axB_lo.yaxis.set_label_coords(-0.11, 0.75)
axB_hi.annotate("era jump\n(compressed band)", xy=(jump_idx, 220),
                xytext=(jump_idx-2.0, 175), fontsize=8.5,
                arrowprops=dict(arrowstyle="->"))
axB_lo.annotate("now visible &\ncomparable", xy=(1, 9), xytext=(4.2, 22),
                fontsize=8.5, color="#127a12", ha="center",
                arrowprops=dict(arrowstyle="->", color="#127a12"))

# ===== Panel C: alternative — log axis (for reference) =====
axC = fig.add_subplot(gs[2, 0])
axC.bar(x - w/2, richness, w, color=c_rich)
axC.bar(x + w/2, evenness, w, color=c_even)
axC.set_yscale("log")
axC.set_title("C.  Alternative — log Y-axis\n(use if a clean break is awkward)",
              fontsize=12, fontweight="bold")
axC.set_xticks(x); axC.set_xticklabels(pairs, fontsize=9)
axC.set_ylabel("Index value (log)")

# ===== Panel D: small-multiples idea =====
axD = fig.add_subplot(gs[2, 1])
axD.bar(x - w/2, richness, w, color=c_rich)
axD.bar(x + w/2, evenness, w, color=c_even)
axD.set_ylim(0, lo_top)
axD.axhline(lo_top, ls="--", lw=1, color="#888")
axD.text(0.02, 0.92, "(spike clipped — annotate its true value as text)",
         transform=axD.transAxes, fontsize=8.5, color="#666")
axD.annotate("220", xy=(jump_idx, lo_top), xytext=(jump_idx, lo_top-6),
             ha="center", fontsize=9, fontweight="bold", color=c_rich)
axD.set_title("D.  Alternative — clip + label the spike\n(simplest; keeps a linear feel)",
              fontsize=12, fontweight="bold")
axD.set_xticks(x); axD.set_xticklabels(pairs, fontsize=9)
axD.set_ylabel("Index value")

# ===== Brief / instructions box =====
axN = fig.add_subplot(gs[3, :]); axN.axis("off")
brief = (
    "HOW TO REDO FIGURE 7 (hand this to cowork)\n"
    "• Goal: keep the big era-transition 'jump' in view without crushing the other year-pairs toward zero.\n"
    "• Preferred fix → Panel B: a BROKEN / SPLIT Y-axis. Lower band = normal range; upper band = the spike; diagonal\n"
    "   marks show the break. In R use ggbreak::scale_y_break(c(<top-of-normal>, <bottom-of-spike>)); in Python use\n"
    "   two stacked Axes sharing X (recipe in this script) or the 'brokenaxes' package.\n"
    "• Fallbacks: Panel C (log axis) or Panel D (clip the bar and print its true value as text).\n"
    "• Keep richness and evenness as the two grouped series; keep year-pair labels on X; SAVE AS A NEW FILE\n"
    "   (e.g. figure7_axisbreak.svg) — do NOT overwrite the original Figure 7.\n"
    "• NOTE: numbers here are PLACEHOLDERS to show the layout — replace with the real richness/evenness values."
)
box = FancyBboxPatch((0.01, 0.04), 0.98, 0.92, transform=axN.transAxes,
                     boxstyle="round,pad=0.012", fc="#f4f7fb", ec="#2c6fbb", lw=1.2)
axN.add_patch(box)
axN.text(0.025, 0.5, brief, transform=axN.transAxes, fontsize=10.2,
         va="center", ha="left", family="monospace")

fig.savefig("/home/user/RCODEOUTLOOK/handout/figure7_redesign_handout.png",
            dpi=170, bbox_inches="tight", facecolor="white")
print("saved PNG")
