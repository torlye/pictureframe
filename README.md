# pictureframe
A collection of scripts and tools to set up a Raspberry Pi-driven digital photo frame or other wall-mounted display.

Runs on any Raspberry Pi; including Raspberry Pi Zero. Setup instructions are written for Raspberry Pi OS 
(previously called Raspbian), but can probably be adapted to many other embedded Linux distros and development boards
with minor changes.

Features:
* Automatic start on boot
* Automatic mounting of USB removable media on boot
* Photo slideshow
* Video playback
* Weather forecast (using yr.no)

## Removable media
Removable USB media can automatically mount file systems supported by the operating system. The setup instructions
provide suggestions for packages which add NTFS and exFAT support.

Up to four removable media with one partition each (sda1 ... sdd1) are automatically mounted, all in read-only.

They can be re-mounted as writable after login if needed.