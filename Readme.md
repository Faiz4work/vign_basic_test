# Vign Basic Application

Vign Provides you secure end-to-end encrypted file sharing, contact saving and
encryption/decryption system.

## 1) How to install

## Installing required dependencies:

## Ubuntu/Debian:
```bash
sudo apt install -y python3-pip python3-setuptools patchelf desktop-file-utils libgdk-pixbuf2.0-dev fakeroot strace fuse

# Install appimagetool AppImage
sudo wget https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage -O /usr/local/bin/appimagetool
sudo chmod +x /usr/local/bin/appimagetool
```

## Archlinux

```bash
sudo pacman -Sy python-pip python-setuptools binutils patchelf desktop-file-utils gdk-pixbuf2 wget fakeroot strace

# Install appimagetool AppImage
sudo wget https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage -O /usr/local/bin/appimagetool
sudo chmod +x /usr/local/bin/appimagetool
```

## Installing appimage-builder with Docker (Docker installation required)

```python
sudo pip3 install appimage-builder

# or Installing development version:
sudo pip3 install git+https://github.com/AppImageCrafters/appimage-builder.git

# There is a docker image with appimage-builder ready to be used at hub.docker.com.

docker pull appimagecrafters/appimage-builder:latest

# Installing appimage tool
sudo wget https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage -O /opt/appimagetool

```

## 2) Fetching Vign Source files from Github:

```bash
git clone https://github.com/username/repo_name.git
```

## 3) Building AppImage from source code:

we will use our "AppImageBuilder.yml" file
for creating our AppImage.

Run this on terminal:
```bash
# Open terminal under project folder or just "cd" into it.
cd project_folder

# Create app image from .yml file
appimage-builder --recipe AppImageBuilder.yml --skip-test
```

It will take some minutes depending on system requirements.

This will make "AppDir" where our application files 
will be installed. you can use "AppRun" under
"AppDir" to run our app.


Appdir will be only our main folder.
you can delete all other files.

