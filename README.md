
# What's the song

## Project Description
Have you heard a song somewhere, and you really want to find it out? I have run into the same situation many times. And as beginner programmer I liked the idea of building things on my own so i built this website in which you can just upload a video or an audio file which contains the song and it will automatically give you the song name and it's spotify link.

## How to Install and Run the Project
To be able to run the project on your machine you need to follow these steps:

**Step 1:**
Run this command on your terminal:

    $ git clone https://github.com/mjiid/What-s_the_song

**Step 2:**
You now have the project on your local machine, You need to install the required libraries:

    $ pip install -r requirements.txt

After doing all of that you still need one thing to go; which is the API I used to able to detect the songs which is in this case **AUDD MUSIC RECOGNITION API**

You can get your API token [here](https://dashboard.audd.io/)

After getting your API token, you would have to go to **found** folder then **song_recognition.py** and insert your API token in data dictionary as shown below:
![image](https://imgtr.ee/images/2023/06/18/Z7rFD.png)


And now you can easily use the project by just running it :

    python run.py

and there you go!
