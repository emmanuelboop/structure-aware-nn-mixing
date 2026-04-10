import torch

def sanm(dataset, bs=64, b1=-0.4, b2=0.7):
    device = dataset.device
    N = dataset.shape[0]

    ci = torch.randint(0, N, (bs,), device=device)
    img1 = dataset[ci]

    img1_flat = img1.view(bs, -1)
    dataset_flat = dataset.view(N, -1)

    dists = torch.cdist(img1_flat, dataset_flat)
    dists[torch.arange(bs), ci] = float('inf')

    nn_idx = dists.argmin(dim=1)
    img2 = dataset[nn_idx]

    s1 = ((img1 >= b1) & (img1 <= b2)).float()
    s2 = ((img2 >= b1) & (img2 <= b2)).float()

    overlap = (s1 + s2 == 2)

    d1 = (overlap.float() - s1).abs().view(bs, -1).sum(dim=1)
    d2 = (overlap.float() - s2).abs().view(bs, -1).sum(dim=1)

    use_img1 = d1 <= d2

    new = img1.clone()
    new[~use_img1] = img2[~use_img1]

    replacement = torch.where(
        use_img1.view(-1, *([1] * (len(dataset.shape) - 1))),
        img2,
        img1
    )

    new[overlap] = replacement[overlap]

    return new
