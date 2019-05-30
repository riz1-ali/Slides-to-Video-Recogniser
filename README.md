# Slides-to-Video-Recogniser

The objective of building this tool was to match the snapshots of slides presented in videos to original slides. To achieve that, we used Scale Invariant Feature Transform (SIFT) and Normalized Cross Coorelation. The output is given as a file output.txt which can be obtained by exectuing the given code.

### Dependencies
Other than default linux modules, all dependencies are listed in requirements.txt and can be installed in the following way:- 
```console
user@linux:~/Slides-to-Video-Recogniser$ pip3 install -r requirements.txt
```
### To Run
```console
user@linux:~/Slides-to-Video-Recogniser$ python3 matcher.py <Path to Slides Folder> <Path to Frames Folder>
```
For testing purposes, you can use the folders in the Testing Set.

### Authors
- [Rizwan Ali](https://github.com/riz1-ali)
- [Pragun Saxena](https://github.com/pragun22)
- [Sankalp Agarwal](https://github.com/sankalp0210)
