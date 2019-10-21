# Rename Images with Date in Exif Metadata
## Overview:

This is a script to remane JPGs images with the creation date that is in the
Exif Metadata.
The output format is:

```
IMG_%Y%m%d_%H%M%S.jpg
Example:
IMG_20190129_140034.jpg
```

The script will automatically rename all files ending in .jpg in the current directory.

## Why would you find that useful?

This way of naming the images help to keep your images order by date.

## Requirement:

The only requirement is *jhead*

```
apt-get install jhead
```

## How do you run the script?

1. Move the script inside the folder where you have the images to rename.
2. In a console type:

```
./rename_images_exif_date.sh
```
