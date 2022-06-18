# ASCII-Art-generator
ASCII(American Standard Code for Information Interchange) is a common encoding format used for representing strings and text data in computers.

But..what if we use this for something other than text?

How about images? Images on your terminal!

The editor for ASCII-graphics, combining a graphical editor and an image to text converter. Decorate your text and surprise your readers with an original social media post or blog post using ASCII graphics. The tool does not require an internet connection and can work offline in a browser.
OpenCv, PIL,NumPy are some of the libraries I have used to write my code.
Prerequisites:
Basics of Image Processing and efficient in Python language

the demo video I have uploaded is in rar format because of size issue so extract it to run it.
##Internal Working of my code-
For running the code you should install opencv, numpy and pillow libraries in whichever IDE you are using. I have used VS code.
I have set the background colour to white because I have performed the image to sketch ascii art feature and for sketch a white bg is the most suitable.
Then I created a list of ascii characters which is placed in ascending order of their luminoscity(characters which covers less area are brighter and hence will be mapped to brighter pixels of the image. I have defined the function trim which will be used to remove the excessive borders from my output image later. I have used scale or scale factor =1.8 because height and width ratio of the characters generally is approximately equal to this ratio and I want square pixels that's why used scale factor to make both width and height of output image pixels in square format. For conversion of my image to sketch I first converted into grayscale format and then inverted my image to negate its effect and then blurred it to remove all the high frequency details from it and then again inverted it and then finally blended it with my original grayscale image to produce the sketched image and finally performed the mapping to convert it into ascii format.
NOTE- there are two methods I have found to convert the image into sketch both of the methods have been uploaded in sketch.py file

##Learnings from this project-
I have learnt image processing basics, python , how to form ascii images and how can I convert my images into sketches. It was a great experience and I have really learnt something interesting due to this project. Thanks to the ACM IITR team for providing such a great opportunity.

#Resources I have used
https://www.geeksforgeeks.org/python-pillow-blur-an-image/
https://towardsdatascience.com/generate-pencil-sketch-from-photo-in-python-7c56802d8acb
https://numpy.org/doc/stable/reference/generated/numpy.percentile.html
https://blog.waffles.space/2017/03/01/ascii-sketch/ 
https://pillow.readthedocs.io/en/stable/reference/ImageOps.html
and finally the workshops conducted by ACM IITR really helped me to write down the code of converting images into ascii arts.
