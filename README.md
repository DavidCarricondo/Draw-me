# **Draw-me!**
  <head>
    <style>
      .img-container {
        text-align: center;
        display: block;
      }
    </style>
  </head>
  <body>
    <span class="img-container"> <!-- Inline parent element -->
      <img src='./INPUT/Eye_logo.png' alt="Draw me!" width="150" height="100">
    </span>
  </body>


Draw me! is several things at the same time. It is a quick drawing classifier. It is a face features recognition and tracking engine. It is a features swapping application.

## How does it work?

The app provides a drawing canvas where the user can use the mouse to quick sketch a feature (eye, nose, mouth, eyeglasses or hat). The user can then save the image that will be fed to a trained neural network that will guess the feature.

Then, the user can launch the webcam through the app (feature swapping button). This will trigger some haar cascade classifiers that will recognice the features from the video and substitute them with the drawn features.

Quick start guide:
  <head>
    <style>
      .img-container {
        text-align: center;
        display: block;
      }
    </style>
  </head>
  <body>
    <span class="img-container"> <!-- Inline parent element -->
      <img src='./INPUT/App_guide.jpg' alt="Draw me!" width="600" height="400">
    </span>
  </body>

## Under the hood: main modules used
+   Keras==2.3.1
+   matplotlib==3.2.1
+   numpy==1.18.2
+   opencv-python==4.2.0.34
+   pandas==1.0.3
+   scikit-learn==0.22.2
+   tensorflow==2.2.0
+   Tkinter==8.6

### **Click the image for a demo video:**

[![Draw me! Demo video]('./INPUT/Video_snapshot.png')](https://www.youtube.com/watch?v=VjCKxSiYEgo)