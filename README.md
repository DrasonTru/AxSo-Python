# AxSo-Python

Originally, I had tried to construct an Object Character Recognition (OCR) engine in order to read numbers and text present in the image. However the quality of the test images proved to be unusable.
Had the images been better quality, and there had been many more instances, I would have looked into a Machine Learning algorithm to get better at reading serial numbers through OCR.
The OCR program would put images in a more "machine-readable" format, and attempt to crop the image to only contain the product label.
Given my knowledge at the time and my limited time with this organization, I decided into finding an alternate solution to getting serial numbers.

I used these programs to get serial numbers from barcodes in images taken in the field:

1. read barcodes using pyzbar, write results to .txt file
Works for about 40-50% of photos, depending on how well the pics were taken. I suppose it could be the limitations of the pyzbar library.
   
2. sort image files into numbered order to iterate through each image
   
3. Selenium web driver automation - used to upload images to online bar code scanner with superior image recognition capabilities. (note: does not work on 100% of images)
