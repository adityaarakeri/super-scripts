# Join Images with the Terminal

Recently I needed to do a work that required joining two images together from  an album of 200 images. Surely it would take too much time to do it manually with a photo editing tool, so I made a script. :D

### Install dependencies

This script requires python3 and depends on imagemagick which is a console based image manipulation tool for Linux. It comes preinstalled with most distributions. In case it is not in the system, install with

```
    sudo apt install imagemagick
```

### Run

Run using

```
    python3 img_append.py [+/-] img1 img2 output_file_name
    + for horizontal append
    - for vertical append
```
