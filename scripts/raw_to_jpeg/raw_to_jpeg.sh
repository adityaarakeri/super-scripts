#!/bin/bash

if [ ! -d ./processed_images ]; then mkdir ./processed_images; fi;

# read all raw files from folder
# .CR2 can be replaced with other raw formats as long as they are supported by ufraw

for f in *.CR2; 
do
	echo "Processing $f"
	ufraw-batch \
		--wb=camera \
		--exposure=auto \
		--out-type=jpeg \
		--compression=96 \
		--out-path=./processed_images \
		$f
done

cd ./processed_images

# change the image names
for i in *.jpg;
do
	mv "$i" "${i/.jpg}"_r.jpg;
done
for i in *.jpg;
do
	mv "$i" "${i/imgp/_igp}";
done