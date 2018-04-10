#!/bin/bash

cd "$(dirname "$0")"

# in case you want to use notification, you need to download and install libnotify. 
#notify-send -t 100 "Aktualizace sešitů probíhá"

python3 manual_maintain.py
#notify-send -t 100 "Aktualizace sešitů dokončena! :) "
#echo 'message:Sešity jsou aktuální.' | zenity --notification --listen

