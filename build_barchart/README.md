## build_barchart
Utility for building bar chart from data stored in file. This utility can be useful in scientific work for experimental data analysis.

### Prerequisities
The script requires matplotlib installed. To install it use pip:

```
pip install matplotlib
```

### Usage
Create a file with data in the following format
```
1: 0
2: 1
3: 0
4: 2
...
```
First number specifies the values along the x axis i.e. bins in the histogram. Second number if the value for each bin i.e. the height of the bin.

Using: python build_histogram.py -f \<file> -m \<y_max> -x \<x_label> -y \<y_label>

where y_max - maximum value for y axis.

The script outputs
```
Barchart was saved in file  <file>.png
```
Sctipt creates a barchart in the file <file>.png.

