# Structure-Aware Nearest Neighbor Mixing (SANM)

## Abstract
We propose a data augmentation method that combines nearest neighbor selection with structure-aware region mixing. Unlike existing approaches such as MixUp and CutMix that rely on random pairing and region selection, our method identifies semantically similar samples and selectively merges overlapping structural regions. This preserves meaningful features while introducing diversity.

## Method

Given an image x_i, we:

1. Select a nearest neighbor x_j based on feature similarity
2. Define a structure mask S(x) such that:
   S(x) = 1 if b1 <= x <= b2, else 0
3. Compute overlap:
   O = S(x_i) ∩ S(x_j)
4. Compute structural differences:
   d_i = |O - S(x_i)|
   d_j = |O - S(x_j)|
5. Construct output image:
   - Use x_i if d_i <= d_j, else x_j
   - Replace overlapping regions with the corresponding values from the other image

## Key Properties

- Structure-aware mixing
- Nearest neighbor-based pairing
- Preservation of semantic consistency
- Avoidance of random patch artifacts

## Notes

Initial implementation completed. Experiments in progress (CIFAR-10 planned).
