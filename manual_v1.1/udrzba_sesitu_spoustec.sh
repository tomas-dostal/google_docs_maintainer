#!/bin/bash

cd "$(dirname "$0")"

notify-send -t 100 "Aktualizace sešitů probíhá"

python3 udrzba_sesitu.py
notify-send -t 100 "Aktualizace sešitů dokončena! :) "
#echo 'message:Sešity jsou aktuální.' | zenity --notification --listen

