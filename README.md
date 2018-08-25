Getting Started
-------
First, you need some things installed!
- Python 2.x
- pip (to make all of this easier)
- OpenCV2
- numpPy
- Git

Let's get all of that by copying this code into your terminal.
##### Mac OSX & Ubuntu
```
sudo easy_install pip
sudo pip install opencv-python
sudo pip install numpy
git --version
git clone https://github.com/myumi/face-recognition 
```

You will also need
- A webcam attached to the computer running the code

Instructions
------
In order for the recognizer to, well, recognize you, you need to provide it with many images of you.
You can do this yourself if you somehow have 300+ pictures of only your face (no judgement here), or you can run the provided ```face-scan.py``` file.

```face-scan.py``` will take 300 photos of you using the webcam on your system. It will save all of these photos in ```data/temp``` (this is important for later).

```
python face-scan.py
```

When you run this, you will see what your webcam sees. Make sure your full face (straight on only) can be seen by the webcame and *no other faces are in the frame*.
It may help to make some common expressions as well as neutral faces so that the program can indentify you better.

After it is finished, you will want to go into that ```data/temp``` directory, CTRL+A and CTRL+X to select all of the images and cut them.
Go back to the ```people``` directory you may have also seen in ```data``` CTRL+V to paste all of the images into the ```p1``` folder inside people.
If you already have images of someone you can paste the images into ```p2``` or make another directory (p3, p4, p5, etc as long as they are sequential) for any new people you want to add.

Next, open up ```face-recognition.py``` in any text editor. Find the line that says: 
```
PEOPLE = ["", "Emma Watson", "Cardi B"]
```

And edit it to contain the name of the person you just added. 
```
PEOPLE = ["", "Jane Doe"]
```

Like so. If you want to add a second person, and the photos of their face are in p2, you would do it like so:
```
PEOPLE = ["", "Jane Doe", "Joshua Buck"]
```

And so on.

Go ahead and open up ```application.py``` now. Read the instructions about commenting out two lines and follow it according to the cases it provides.
- You need to train the recognizer with new faces when you add a new person (like the first time you run it)
- But this takes a lot of time, and you don't need to do this if you haven't added a new person, so be sure to comment out (add a # in front) the lines where it is *trained*, and un-comment out the lines where the trained model is *loaded*

If you don't want to touch the code at all, that is also fine. You'll just have to wait a long time every time you want to run it.

When this is ready, go ahead and run ```application.py```
```
python application.py
```

You should see a green box appear around the faces of the people you showed it, with their name on top. Yay!
