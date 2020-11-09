# First-time setup; assuming stock Raspberry Pi OS Lite
## Install apt packages
```
sudo apt install omxplayer exfat-fuse exfat-utils ntfs-3g fim git wiringpi rpi.gpio
```

If you want to mount SMB file shares; also install `smbclient`

## Clone the git repo
You can clone it into e.g. the default `pi` user's home folder.
```
git clone https://github.com/torlye/pictureframe.git
```

To later update the scripts; cd into the repo path and run `git pull`.


## Autostart
### Automatically log in on boot
Run `sudo raspi-config` and make the following selections:
* 3: Boot options
* B1: Desktop/CLI
* B2: Console autologin

### Automount
To automatically mount up to four USB removable media on boot; first create mountpoints:
```
sudo mkdir /mnt/sda1
sudo mkdir /mnt/sdb1
sudo mkdir /mnt/sdc1
sudo mkdir /mnt/sdd1
```
If you have a separate data partition on the memory cart; you can also create a mount point for that:
`sudo mkdir /media/mmcblk0p3`

Run the script automount.sh on startup to mount these devices.

Edit `/etc/rc.local`. Add a line to execute the automount script; e.g. `/home/pi/pictureframe/automount.sh`

### Start script on boot
Edit a login script; e.g. `~/.profile`. Add a line to call your script.

E.g. to start the menu on boot; add:
```
pictureframe/menu.py
```

If you want to start a specific function instead of showing the menu; simply specify another script; e.g. photo.py

## Minimize SD writes
Minimizing writes may extend the life of the SD card.

### Use tmpfs for /tmp
Edit `/etc/fstab`. Insert the following line:
```
tmpfs /tmp tmpfs defaults,size=10M 0 0
```

### Disable swap
```
sudo swapoff --all
```
Add this to `/etc/rc.local`.


## Screen brightness adjustment
Brightness adjustment is specific to the model of LCD panel and controller board.

If you have a script that sets brightness for your LCD panel; simply add a line in e.g. `~/.profile`
to run it at login.

E.g.
```
pictureframe/lcd-brightness-waveshare_7inch_c.sh 490
```

