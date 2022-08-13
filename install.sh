#!/bin/bash
echo "Thanks for choosing pi-auto from https://fleet-rack.org"
# have installed and working os, you will not need a gui!
# pi zero w Raspberry Pi OS Lite (Legacy) or preferably 32bit os https://www.raspberrypi.com/software/operating-systems/
# curl -LJO https://raw.githubusercontent.com/LukeKeam/pi-auto/master/install.sh && sudo sh ./install.sh
# once have ssh connection to pi

# update
sudo apt-get update
sudo apt-get upgrade -y

# install
sudo apt-get install python3 python3-pip tmux minicom screen bluetooth busybox-syslogd wvdial libqmi-utils ntp git -y

# update host name
newhostname="pi-auto"
echo "$newhostname" | sudo tee /etc/hostname
# add hostname to /etc/hosts
echo "127.0.1.1   $newhostname" | sudo tee -a /etc/hosts

# update password?
# mypassword="password"
# echo "$mypassword" | passwd --stdin

# creat dir
cd /

# clone repository
git clone https://github.com/LukeKeam/pi-auto.git
sudo chown -R "$USER":"$USER" /pi-auto
cd /pi-auto

# pip install
sudo pip3 install -r requirements.txt



# add service
append_line='# sudo nano /lib/systemd/system/pi-auto.service
# sudo systemctl restart pi-auto.service
# sudo systemctl status pi-auto.service
# sudo systemctl enable pi-auto.service
# sudo systemctl daemon-reload
# User=pi?

[Unit]
Description=pi-auto
After=multi-user.target

[Service]
Type=idle
WorkingDirectory=/pi-auto
ExecStart=/bin/bash -c "mount -o remount,rw /pi-auto && python3 /pi-auto/main.py"

[Install]
WantedBy=multi-user.target'
echo "$append_line" | sudo tee /lib/systemd/system/pi-auto.service # need to make other lines ro
sudo systemctl enable pi-auto.service
# https://hallard.me/raspberry-pi-read-only/
# make os read only
append_line="/home/pi/pi-auto     /pi-auto        ext4    defaults,bind,rw     0       0
tmpfs        /tmp            tmpfs   nosuid,nodev         0       0
tmpfs        /var/log        tmpfs   nosuid,nodev         0       0
tmpfs        /var/tmp        tmpfs   nosuid,nodev         0       0"
echo "$append_line" | sudo tee -a /etc/fstab # need to make other lines ro
sudo apt-get remove --purge triggerhappy logrotate dphys-swapfile -y
sudo apt-get autoremove --purge -y
echo "fastboot noswap ro" | sudo tee -a /boot/cmdline.txt # not on the same line though
# sudo nano /boot/cmdline.txt # add fastboot noswap ro
sudo apt-get install busybox-syslogd -y
sudo rm /var/lib/systemd/random-seed &&
sudo ln -s /tmp/random-seed /var/lib/systemd/random-seed
sudo nano /lib/systemd/system/systemd-random-seed.service
ExecStartPre=/bin/echo "" >/tmp/random-seed


# add line to config enable uart # # raspi-config for serial???
append_line="enable_uart=1"
echo "$append_line" | sudo tee -a /boot/config.txt



# time cronjob
# /etc/cron.hourly/fake-hwclock

# add bluetooth device
# manual process


# finished & reboot
echo "Restarting in 5seconds"
sleep 5
sudo reboot