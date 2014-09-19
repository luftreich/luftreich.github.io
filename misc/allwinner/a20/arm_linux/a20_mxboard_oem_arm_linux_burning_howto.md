
## Install Debian 
#### In this tutorial you will learn how to install Debian to MXBboard on both micro-SD card and NAND.

* Download Debian Nand/Sdcard IMAGEs/TOOLs

    <http://pan.baidu.com/s/1gdj7K11> 
    `password: vbf5`


## STEP 1 -- Install to Micro-SD card

#### Windows users
* Use Image writer. < sdcard/imageWriter.exe.7z >, 
* Unzip the IMG
* If it ends with `.7z`, Please use 7-zip to unzip the IMG file
* Rename the .img file with a .raw extension
* Write the IMG to your device

#### Linux users
* Unzip the img < sdcard/cubieez_1.0.0_A20_repack`*`.img.gz >
```bash
    # If it ends with 7z
    apt-get install p7zip-full
    7z x PATH_TO_DEBIAN.7z
    # Write to your device
    dd if=PATH/TO/DEBIAN of=/dev/YOUR_DEVICE bs=4096; sync
```


## STEP 2 -- Install to NAND
  
####    Windows users
Use PhoenixSuit  < nand/PhoenixSuit1.0.6.rar >
         
* 1. Extract DEBIAN image
* 2. Start PhoenixSuit. Select "Firmware".  Select DEBIAN image
* 3. Enter FEL mode:
* 4. Power off MXBboard
* 5. Connect the board to you PC using USB OTG wire
* 6. Hold down the FEL key when powering on
* 7. Release FEL key
* 8. PhoenixSuit will auto-start the flash.

####    Linux users
        ...
        TODO

## STEP 3 -- 相关修改，目前该步骤必需!
* a. 请确认前面两个步骤已经完成
* b. 连接HDMI显示器、键盘、鼠标，插入SD卡，启动设备
* c. login to board

     user:     root
     password: cubieboard

* d. Run `LXTerminal`, Start command-line
* e. 输入命令: `mmc2nand_sync_oem_v0830.sh`, 请耐心等待，耗时比较久, 成功后会显示:`All is OK`
* f. 拔掉SD卡，连接VGA显示器, 重启设备
* g. THE END

### How to switch display mode 

* double click "Switch_display" desktop icon

* connect the board to you TV using an HDMI/VGA cable, it can display 720P

