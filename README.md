# MinecraftIpToGuiImage
Give it a valid, online, Minecraft server ip, and the program shall return an image of the server as if its a screenshot taken in Minecraft

# How does it work?
~~Basically, using the [Minecraft Server Status API](https://api.mcsrvstat.us), and its icon endpoint, the program gets the required information it needs to create an image, which looks as if it was a screenshot of the server menu taken inside Minecraft.~~
It uses the MCStatus to ping the server via sockets. This program then uses that info to convert into html that is then turned into a image that looks as if it was a screenshot of the server menu taken inside Minecraft.

# How to run it?
Prerequisites:
- Python 3+
- Three python libraries, `Pillow`, `BeautifulSoup`, and `mcstatus`.

To install the libraries, go to the command line and type

Pillow:
```shell
python3 -m pip install --upgrade Pillow
```

BeautifulSoup:
```shell
python3 -m pip install --upgrade BeautifulSoup4
```

MCStatus
```shell
python3 -m pip install --upgrade mcstatus
```

If an error occurs, use google or just common sense


To run it:
- Go to the command line and navigate it to the folder in which main.py is in
- Do 
```shell
python3 main.py
```
- Insert the server ip and the server name. Click enter after entering each one.
- Wait a few seconds. An image should pop up, showing the rendered image. It is also saved to a file called `output.png`.


# Example
Here is the output after running the file with the server ip as `mc.hypixel.net` and setting the server name as Hypixel
<img src="./output.png">


# Old Examples
Here I am putting the server ip as `hypixel.net`, and setting the server name as `Hypikle`
<img src="./resources/images/example/HypikleExample.png">

Here is the output after running the file

<img src="./resources/images/example/HypikleOutput.png">
