# Google Docs maintainer
Thanks to this code your Google Docs will be always up-to-date on your local drive saved as a PDF. Code is written in Python3 using PyDrive.


![Terminal output](https://github.com/tomas-dostal/google_docs_maintainer/blob/master/google_docs_maintainter_example.png)



You can choose between two versions of the code: 

| Version | 
| ------ |
| [automatic update](https://github.com/tomas-dostal/google_docs_maintainer/tree/master/auto_v1.1) | 
| [manual update](https://github.com/tomas-dostal/google_docs_maintainer/tree/master/manual_v1.1) | 


### Installation

This code requires:
* [Python 3](https://www.python.org/downloads/) (mostly preinstalled on *nix), 
* google-api-python-client (PyDrive), 
* httplib2

You can easily install it by typing: 
```sh
# pip3 install –upgrade google-api-python-client
# pip3 install httplib2
```

> Note: You will need a Google account to access the Google Docs. 
> Note_2: To download a Google docs file please ensure that you have a permission to download the file.


#### Installation (Automatic version)
Follow previous instruction. When finished continue here. 

To use automatically scheduled update you have to a command to "on start" folder. 
The most simple way is using the [Gnome tweak tool](https://launchpad.net/ubuntu/+source/gnome-tweak-tool): 


![Gnome tweak tool](https://github.com/tomas-dostal/google_docs_maintainer/blob/master/gnome-tweak-tool.png)


* Run the Gnome tweak tool (Alt+F2 and write gnome-tweak-tool) 
* -> Applications on startup 
* -> New
*  add the "python3 /path/automatic_maintain_execute.sh there to execute on startup"

## How to use Google Docs maintainer? 

First, you need to create some Google Docs file. By default, there are some of my notebooks' IDs. Just for testing purpose. 
When you create some, you have to extract its ID. 
![How to find ID](https://github.com/tomas-dostal/google_docs_maintainer/blob/master/how_to_get_google_docs_id.png)

Then you need to add this document's ID to proper script. In case you want to use automatic update, open and edit [automatic_maintain.py](https://github.com/tomas-dostal/google_docs_maintainer/blob/master/auto_v1.1/automatic_maintain.py), otherwise open and edit [manual_maintain.py](https://github.com/tomas-dostal/google_docs_maintainer/blob/master/manual_v1.1/manual_maintain.py).

Find where is an array with IDs and add your one. 
```
ids = { „1J_YafGKPBItGqJjxPBgJ-1sWDF2tmwIT0v2wClt2IB8", "Add e.g. here the Google Docs ID", "1BycZMbz8WCVArgHij1m02FmVt2iGv2KdJPtwglpyIXQ"}
```

And here we go. Try to run the .py script just to see if everything goes well. You'll be asked to log into your Google account. 
Later the code checks if your local version of your Google Docs is outdated (there is a newer version). If so, it starts a thread which downloads a PDF of your Google Docs. 


![Terminal output](https://github.com/tomas-dostal/google_docs_maintainer/blob/master/google_docs_maintainter_example.png)


The PDF file is saved in the same directory as the script. You can make a software link to another location using following command (*nix only).

```sh
$ ln -s /path/to/script/YOURFILE.PDF /your/desired/path/YOURFILE.PDF
$ ls -l
```
> Note: Filename of a downloaded file is the same as the name of your Google Docs document. 

> Note_2: To download a Google docs file please ensure that you have a permission to download the file.

> Note_3: You should generate your own settings.yaml file (which is included only for testing purposes at the moment) for your use. You can do it from [Google cloud platfrom](https://console.cloud.google.com/?hl=cs). 


License: MIT
-------
