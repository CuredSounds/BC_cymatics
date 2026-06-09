# BC_cymatics

Resonant frequencies and cymatics-modal vibrational phenomena.

This repository includes a small Python script for generating cymatic-like
visuals with a square Chladni plate model:

```bash
python chladni_pattern.py --output output/chladni.png
```

The command above saves an image without opening a window. For an interactive
preview instead:

```bash
python chladni_pattern.py --show
```

Install the required libraries first if needed:

```bash
pip install numpy matplotlib
```

Pass `--show` to open an interactive window, or use `--output` to save an image.
