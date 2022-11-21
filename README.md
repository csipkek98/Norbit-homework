# Author's notes

Hello dear Reader!<br>So I've tried to finish this project in time, unfortunately I had some problems with Vue js's data sending to other components and I ran out of time. Sadly, once I was able to send through the data to the Openlayers component I was not able to refresh the Openlayers VectorLayer to show new coordinates.<br>
As a conlusion: I had a blast with this project! I learned many new things like: Socket IO, OpenLayers, Vue and Express.js<br>
I'm really sad I was not been able to finish it in time, but it was fun!<br>

# Tech stack

- Coordinate Provider: Flask
- Backend: Express.js
- Frontend: Vue (+OpenLayers)

# Table of contents
 1. [How to Use?](#how-to-use)
 2. [Homework Status](#homework-status)
 3. [FAQ](#faq)

# How to Use?

1. Open the "init applications.bat" file in the main folder
2. Wait for the 3 cmd to close
3. Open the "run applications.bat" file in the main folder
4. If 3 cmd is showing up and stays (picture attached), you are Done!<br><br>
<img src="https://user-images.githubusercontent.com/90270578/203004724-2ce21ade-a488-4728-8d20-aa342bc5790a.png" width="700px"><br>

```
Bonus information:
You can change the config (like port) for every service in their folder's config.json file!
```


# Homework status

✅ Coordinate provider mock send one coordinate per sec<br>
✅ Express.js Backend get the current coordinate with Websockets<br>
✅ Backend send the current coordinate to frontend<br>
✅ Frontend has OpenLayers integration as a component<br>
✅ Record button emit signal of recording start<br>
❌ Visualization of current coordinate on OpenLayers<br>
❌ Save path to Data Base<br>
❌ Load path from Data Base<br>
❌ No boat icon with heading on the map



# FAQ

### The coordinate provider is not running, why?
If you get this error, there is many possible answers:

1. You have no python on you computer<br>
If you are using Linux, you can easily install it with: ```sudo apt-get install python3.10```<br>
If you are using Windows, there is a short guide for you to use here: [link](https://www.digitalocean.com/community/tutorials/install-python-windows-10)<br><br>

2. You have no virtualenv installed on you computer<br>
You can check this problem by looking in the "Coordinate provider" element to see if there is any venv folder.<br>
If there is not, you can solve this by run the following command in the cmd: ```pip install virtualenv```<br>
If it says: you have no pip installed, then return to problem 1.<br><br>

3. A module is missing<br>
In this case, try to delete the venv folder, and run the "init.bat" in the Coordinate provider folder and then try the "run.bat" to see if anything changed<br>
(the cmd should be open for a while. If not, in this case try problem 1. and 2.)<br><br>
