# Face Mask Detection

 This project on face mask detection detects if a person is wearing a mask primarily in public places or not. Since in a pandemic time like this, this project can become one of many solutions in order to maintain safety among people. 

## Technologies used:
(This assignment has been carried out on a Windows machine)
1)	Python == 3.6.8
2)	OpenCV == 4.4.0
3)	Tensorflow == 2.3.0
4)	Numpy == 1.18.5
5)	imutils == 0.5.3

## Executable files:
1) image_mask_detections.py – Takes an image as input.
2) video_mask_detections.py – Takes a video as input.
3) realtime_mask_detections.py – Takes no input instead starts a video 

## How to run the files?
(Make sure all the above mentioned modules are installed)
1) First, open command prompt and **cd** into the project directory.
2) Now paste the following code inside command prompt,<br>
```python image_mask_detections.py -i people.jpg -c 0.13```
3) Now let’s run another file, paste the following code in command prompt,<br>
```python video_mask_detections.py -v trial_video.mp4 -c 0.3```
