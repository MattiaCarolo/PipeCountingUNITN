# PipeCountingUNITN

To launch the main algorithm write 

``` bash
python3 main.py -i <path to image>
```

The main files correlated are `utils.py` and `homography.py`. The remaining files are obsolete or used to test specific functions.


## How to use

This algorithm permits two type of usages basing on the photos provided. At the start after loading the image the program will output an image. If no homography is needed by pressing any key it will go directly to the evaluation part while if the pipes are not directly in front of the camera we can select 4 corners and than press any key in order to get a better representation for the evaluation part

As output we will get in the terminal the count of circular and rectangular pipe inside the image plus a json list that encodes shape type and centroid location. 
In the resulting image the countour of the different shapes will be highlighted together with the relative centroid