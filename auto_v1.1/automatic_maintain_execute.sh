#!/bin/bash

#commented lines are not needed anymore - all the stuff about update period is on automatic_maintain.py file. 
#while true
#do
	#echo "getting connection info"
	# Test for network conection
	#for interface in $(ls /sys/class/net/ | grep -v lo);
	#do
	#  if [[ $(cat /sys/class/net/$interface/carrier) = 1 ]]; 
	#then OnLine=1; 
	#fi
	#echo "Connected. Getting content!"
	cd "$(dirname "$0")"
	#notify-send -t 100 "Aktualizace sešitů probíhá"

	python3 automatic_maintain.py
	#notify-send -t 100 "Aktualizace sešitů dokončena! :) "
	#echo "Going to sleep now..." 
	#sleep 3600
	#done
	
#done


