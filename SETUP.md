# First-time setup; assuming stock Raspberry Pi OS Lite
## Install apt packages
```
sudo apt install omxplayer exfat-fuse exfat-utils ntfs-3g fim
```

If you want to mount SMB file shares; also install `smbclient`

## Autostart
### Automatically log in on boot
Run `sudo raspi-config` and make the following selections:
* 3: Boot options
* B1: Desktop/CLI
* B2: Console autologin

## Minimize SD writes
Minimizing writes may extend the life of the SD card.

### Use tmpfs for 
Edit `/etc/fstab`. Insert the following line:
```
tmpfs /tmp tmpfs defaults,size=10M 0 0
```

### Disable swap
```
sudo swapoff --all
```
Add this to `/etc/rc.local`.

## Automount
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
