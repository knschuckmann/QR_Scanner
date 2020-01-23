# QR_Scanner

## How to create executable
After searching the Internet for the best solution on how to create an executable file from my python script, I finally figured it out and want to share the knowledge with everyone. 

**Speciality:**

Since I am using a Mac OS and want to distribute the executable on Windows I had to create a Virtual Box that runs a Windows OS.

### Virtual Box on host (Mac OS) 
you will need 
1) Virtual Box [official website](https://www.virtualbox.org/wiki/Downloads)
2) Windows iso file [chip download](https://www.chip.de/downloads/Windows-ISO-Downloader_95133731.html)

After installing the Virtual Box on your host machine, in my case Mac OS, you will need to start it for the first time and give it the iso file. Here is a website unfortunatelly in german on how to create a virtual machine and give it the Windows iso [Website](https://www.pcwelt.de/ratgeber/Windows-10-mit-Virtualbox-in-Mac-OS-X-einrichten-9839076.html).

### In Virtual Box guest (Windows)
you will need 
1) shared folder 
2) python [official webite](https://www.python.org/downloads/windows/)
3) pyinstaller

A very big issue was to create a **Shared Folder in Virtual Box**. This is a good [Link](https://helpdeskgeek.com/virtualization/virtualbox-share-folder-host-guest/) on how to create the shared folder.

After doing so you should start the guest OS (Windows) on the Virtual Box and download Python executable. Start the executable from Downloads folder and make sure you click on **add Python to PATH**
Python automatically downloads pip. 

Now you should **restart the guest OS (Windows)** 
and make sure that python and pip are properly installed by typing those comans in comandline on Windows
```console
python --version
```
and 
```console
pip --version
```
If both command do not throw exeptions you are good to go.

After you have done so, run the following command in cmd
```console
pip install pyinstaller
```

### Creating the executable 

1) open Comandline in guest OS (Windows) 
2) navigate to your python file that you probably shared through the shared folders 
3) take a look on your file and **pip install** all libraries that are marked with **import** e.g. import pandas as pd as followed
```console
pip install pandas
```
4) after all important files are downloaded in giuest OS (Windows) and this is very important to understand because it took me a while. Only after you installed all dependencies you can run the following code for a console app.
```console
pyinstaller --onefile --console yourfile.py
```
or if you want a window based app runn following code
```console
pyinstaller --onefile --windowed yourfile.py
```
The final app will be created in a folder named dist in your directory.

Finisch!!!!
