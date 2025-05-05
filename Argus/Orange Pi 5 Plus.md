- Memory: 16G
- Storage: 256GB eMMC Module 
- Processor: RK3588 8 Core 64 Bit Single Board Computer, 2.4GHz Frequency 
- SD Card, MMC, 
- 3 HDMI
- 2 ethernet
- GPIO

## OS: DietPi

- pretty minimal by default
- can't use sway (easily) because it still uses Xorg
	- but maybe that's a good thing? had driver issues with [[Khadas Edge 2]]
	- easiest way to get X might be to install LXDE?

Then setup i3:

- Edit/Create `~/.xinitrc`
-  Replace its contents with:

```
exec i3
```

Connect to HDMI I need to lower the resolution from 4K

```
xrandr --output HDMI-1 --mode 1920x1080 --rate 60
```

### Installation

I had to use an SD Card instead of USB boot to boot dietpi installer

#fixme I need to move the install to the eMMC module!
#fixme how to disable waiting for wifi/eth1 - adds over a minnute to boot


### Update SPI 

Recent discussions (as of May 2024) show that many Orange Pi 5 users need to update the SPI flash to boot from eMMC:

```
sudo orangepi-config
```

Then go to System > Install > "Install/Update the bootloader on SPI Flash"

Then reboot after it finishes (flashing takes a minute or two)
### Install on eMMC

First we need to finish the install, let's verify it is there.

```
dietpi@DietPi:~$ lsblk -o NAME,SIZE,MODEL
NAME          SIZE MODEL
mtdblock0      16M
mmcblk1      59.5G
└─mmcblk1p1  59.5G
mmcblk0       233G
mmcblk0boot0    4M
mmcblk0boot1    4M
```

Cool!  `mmcblk0` is the eMMC module.

```
# Make a new partition
fdisk /dev/mmcblk0  
mkfs.ext4 /dev/mmcblk0p1
mkdir /mnt/emmc
mount /dev/mmcblk0p1 /mnt/emmc
```
Now we can copy the system to it:

```
rsync -aAXv /* /mnt/emmc --exclude=/mnt --exclude=/proc --exclude=/tmp --exclude=/sys --exclude=/dev --exclude=/run --exclude=/media
mkdir /mnt/emmc/{dev,proc,sys,run,mnt,media,tmp}
chmod 1777 /mnt/emmc/tmp
```
#### Update `/mnt/emmc/etc/fstab`

Set the **root (`/`)** to the right UUID (`blkid /dev/mmcblk0p1`).

**Shutdown, Remove SD Card, and Boot**