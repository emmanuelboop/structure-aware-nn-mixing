# Structure-Aware Nearest Neighbor Mixing (SANM)

We propose a data augmentation method that combines nearest neighbor selection with structure-aware region mixing.

## Key Idea
Instead of random mixing:
- Select similar images (nearest neighbors)
- Identify structure regions
- Mix only overlapping meaningful regions

## Motivation
- MixUp destroys structure
- CutMix uses random patches
- Our method preserves semantic consistency

## Status
Initial implementation and experiments in progress.
Paper draft available in 'draft_paper.md'
