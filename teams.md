# Team 1

## A) Matplotlib + NumPy Core

1. Create `x = np.linspace(-4, 4, 501)` and compute `[x, x², x³]`. Plot all three with labels and legend.
2. Given a vector `a` (length 5) and matrix `M` (shape 5×200 created with `np.linspace` then `np.sin`), plot `M + a[:,None]` as a heatmap. Write down the shapes of `a`, `M`, and `M + a[:,None]`.
3. Build `X,Y = np.meshgrid(np.linspace(-3,3,300), np.linspace(-3,3,300))`; compute `Z = np.sin(X)*np.cos(Y)`. Plot heatmap with colorbar.
4. Create `arr = np.arange(20).reshape(4,5)`. Take a view of the center 2×3 block and set it to −1. Print both arrays and plot the parent as an image.
5. Generate a random 100×5 matrix. Standardize each column: `(A - A.mean(axis=0)) / A.std(axis=0)`. Plot histograms before and after.
6. Create `B = np.arange(6).reshape(2,3)` and tile it to (10,15). Visualize with `imshow`.

## B) Images

1. Load an RGB image. Show its shape, dtype, min, and max values. Display it.
2. Crop a centered H/2×W/2 patch using slicing only (no copy). Display it.
3. Add 30 to all pixels (clip afterward). Then apply a per-channel scale `[1.0, 1.2, 1.0]`. Display results.
4. Rotate 90° using `img.transpose(1,0,2)[:, ::-1]`. Show before and after.

## C) Audio

1. Load a mono WAV. Convert to float in \[−1,1], show shape and dtype, and plot the first 0.05 s.
2. Reverse the signal with slicing. Plot the first 2000 samples of both signals.
3. Create a fade-in/out using `np.linspace` ramps and multiply with the signal.
4. Downsample by slicing with `sig[::2]`. Compare lengths and plot excerpts.

---

# Team 2

## A) Matplotlib + NumPy Core

1. Create `x` and compute `y = np.where(x<0, x**2, np.sqrt(x+1))`. Plot with axis labels and grid.
2. Create `u = np.linspace(-2,2,201)` and compute `U = u[:,None]`, `V = u[None,:]`. Plot `U*V` and `U+V` as heatmaps.
3. Simulate a random walk: `steps = np.random.choice([-1,1], size=2000)`, `pos = steps.cumsum()`. Plot and annotate the maximum excursion.
4. Make a 6×6 array. Set a checkerboard pattern to −1 using slicing. Plot before and after.
5. Reshape `np.arange(36)` to (6,6). Reshape it to (3,12), swap axes, and reshape back. Plot the result as an image.
6. Create a 100×5 random matrix and multiply each column by `[1,2,3,4,5]`. Show column means before and after.

## B) Images

1. Load and show an image. Compute per-channel means.
2. Convert to grayscale with `gray = img.mean(axis=2).astype(img.dtype)`. Display it.
3. Swap red and blue channels using indexing.
4. Multiply the image by a vertical gradient tint using `np.linspace(0.7, 1.3, H)[:,None,None]`.

## C) Audio

1. Load and normalize an audio file. Plot 0.05 s.
2. Concatenate the signal to itself with `np.concatenate`.
3. Slice out a middle 1-second clip using sample indices.
4. Apply different gains to the first half (0.8) and second half (1.2) using a mask.

---

# Team 3

## A) Matplotlib + NumPy Core

1. Draw 10,000 samples from `np.random.randn`. Plot histogram with 50 bins. Overlay the theoretical PDF.
2. Build a 20×20 block matrix from four tiles: zeros, ones, an arange pattern, and the identity. Plot with `imshow`.
3. Create a 200×200 grid of distances from the center. Mask a ring and plot it as an overlay.
4. For a random matrix, plot row means (line plot) and column standard deviations (bar plot).
5. Normalize each row independently to \[0,1]. Plot heatmaps before and after.
6. Select the diagonal and anti-diagonal of a square array and set them to constants. Plot before and after.

## B) Images

1. Load and show an image.
2. Crop a centered square using slicing. Show that modifying the crop changes the parent.
3. Tile the crop into a 3×3 mosaic with `np.tile`.
4. Add `[20, -10, 0]` to the channels using broadcasting. Clip afterward.

## C) Audio

1. Load and plot a small excerpt.
2. Reverse only the first half of the signal and compare to the original.
3. Multiply by a triangular envelope created with `np.linspace`.
4. Stack into a stereo array `(N,2)` with different scaling on each channel.

---

# Team 4

## A) Matplotlib + NumPy Core

1. Create a 1×3 subplot showing `sin(X)+cos(Y)`, `exp(-X²−Y²)`, and `sin(XY)` on a meshgrid. Add colorbars.
2. For vector `v`, plot the heatmap of absolute differences `|v[:,None]-v[None,:]|`.
3. Generate random walks for three rows of data. Plot their cumulative sums with a legend.
4. Create a 10×10 array and reorder columns using an index array. Plot before and after.
5. Center a random matrix by subtracting the overall mean. Show histogram before and after.
6. Start with data of shape (2,3,50). Permute axes into (3,2,50) and (50,3,2). Write down the new shapes.

## B) Images

1. Load and show an image.
2. Perform horizontal flip, vertical flip, and 180° rotation using slicing. Display all in a 2×2 grid.
3. Build a checkerboard mask with `np.indices` and darken alternating tiles by 40%.
4. Reorder channels: RGB→BGR and RGB→GBR. Compare visually.

## C) Audio

1. Load and normalize audio. Plot.
2. Keep two samples, drop one using reshaping and slicing. Plot result.
3. Apply different gains to samples before and after 0.5 s using a mask.
4. Pad 0.2 s of zeros at the end with `np.pad`. Verify new length.

---

# Team 5

## A) Matplotlib + NumPy Core

1. Generate a 2D lattice `Z = sin(2πkx)+sin(2πly)` over a meshgrid. Plot with colorbar.
2. Start with a zeros (50×50) array and add outer products of small vectors to draw stripes or shapes. Plot after each step.
3. Create `A = np.arange(64).reshape(8,8)`. Split into 2×2 quadrants and swap them around using slicing. Plot before and after.
4. For a random matrix, plot row medians as a line and column maxima as a bar plot.
5. Normalize rows to \[0,1] and apply a per-row threshold vector to make a binary heatmap.
6. Stack several 1D waves into a 2D image using `np.stack` and `np.tile`. Plot with `imshow`.

## B) Images

1. Load and show an image.
2. Downscale by taking every second row and column (`img[::2, ::2]`).
3. Multiply by a vertical fade using `np.linspace(1.0, 0.7, H)[:,None,None]`.
4. Clamp the red channel at its median value using a mask.

## C) Audio

1. Load and plot audio.
2. Repeat the signal 3 times using `np.tile`. Plot first and last 2000 samples.
3. Create a synthetic tone with `np.arange` and add it to the audio. Clip if needed.
4. Swap the first and second 0.5 s segments using slicing and `np.concatenate`.
