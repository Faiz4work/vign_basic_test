# This script will convert flask Vign app
# to appimage.

### making "AppDir" folder and copying files in dir.

from os import system
# Remove any previous build
system("rm -rf AppDir  | true")
# Make usr and src dirs
system("mkdir -p AppDir/usr/src")
# Copy the python application code into the AppDir
print("Copying files")
system("cp Gui.py  AppDir/usr/src -r")
system("cp -R myapp  AppDir/usr/src")
# system("sudo -p mkdir /usr/share/icons/360x289/")
# system("sudo cp logo.png /usr/share/icons/360x289/")
# Install application dependencies
print("Installing libraries...")
system("python3 -m pip install --ignore-installed --prefix=/usr --root=AppDir -r ./requirements.txt")

def make_app_image_recipe(recipe_filename):
    f = open(recipe_filename, 'w')
    recipe_str = """ 
version: 1
AppDir:
  path: ./AppDir

  app_info:
    id: app_dsk
    name: Vign Basic
    icon: utilities-icon
    version: 0.1.0
    # Set the python executable as entry point
    exec: usr/bin/python3
    # Set the application main script path as argument. Use '$@' to forward CLI parameters
    exec_args: "$APPDIR/usr/src/Gui.py $@"

  apt:
    arch: amd64
    sources:
      - sourceline: 'deb [arch=amd64] http://archive.ubuntu.com/ubuntu/ focal main restricted universe multiverse'
        key_url: 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3b4fe6acc0b21f32'

    include:
        - python3
        - python3-pkg-resources
        - python3-pyqt5
        - libfreetype6
        - libfontconfig1
    exclude: []

  runtime:
    version: "continuous"
    env:
      PATH: '${APPDIR}/usr/bin:${PATH}'
      # Set python home
      # See https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHOME
      PYTHONHOME: '${APPDIR}/usr'
      # Path to the site-packages dir or other modules dirs
      # See https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH
      PYTHONPATH: '${APPDIR}/usr/lib/python3.8/site-packages'

  test:
    fedora:
      image: appimagecrafters/tests-env:fedora-30
      command: ./AppRun
      use_host_x: true
    debian:
      image: appimagecrafters/tests-env:debian-stable
      command: ./AppRun
      use_host_x: true
    arch:
      image: appimagecrafters/tests-env:archlinux-latest
      command: ./AppRun
      use_host_x: true
    centos:
      image: appimagecrafters/tests-env:centos-7
      command: ./AppRun
      use_host_x: true
    ubuntu:
      image: appimagecrafters/tests-env:ubuntu-xenial
      command: ./AppRun
      use_host_x: true

AppImage:
  update-information: 'gh-releases-zsync|AppImageCrafters|python-appimage-example|latest|python-appimage-*x86_64.AppImage.zsync'
  sign-key: None
  arch: x86_64
"""

    f.write(recipe_str)
    f.close()

    print("Yml file created.")


# Making appimage recipe file
recipe_filename = "AppImageBuilder.yml"
make_app_image_recipe(recipe_filename)


system(f"appimage-builder --recipe {recipe_filename} --skip-test")

import os
# Removing Recipe file
if os.path.exists(recipe_filename):
  os.remove(recipe_filename)

import glob2
img = glob2.glob("*.AppImage")
os.remove(img[-1])

zsync = glob2.glob("*.zsync")
os.remove(zsync[-1])

# Getting all file names
all_files = glob2.glob('*')















# End of script

