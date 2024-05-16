#!/bin/bash

# Install system dependencies
sudo apt-get update
sudo apt-get install -y \
    sudo \
    ffmpeg \
    libsdl2-2.0-0 \
    adb \
    wget \
    gcc \
    git \
    pkg-config \
    meson \
    ninja-build \
    libsdl2-dev \
    libavcodec-dev \
    libavdevice-dev \
    libavformat-dev \
    libavutil-dev \
    libswresample-dev \
    libusb-1.0-0 \
    libusb-1.0-0-dev \
    libimobiledevice-utils \
    ewf-tools \
    openssh-server \
    nmap \
    autopsy \
    g++ \
    libc-dev \
    libffi-dev \
    libssl-dev \
    python3-dev \
    swig \
    xvfb \
    libbfio1 \
    libc6 \
    libvhdi1 \
    libvmdk1 \
    libewf-dev \
    libafflib-dev \
    libsqlite3-dev \
    libc3p0-java \
    libvmdk-dev \
    libvhdi-dev \
    pip \
    build-essential \
    checkinstall \
    autoconf \
    automake \
    libtool-bin \
    libplist-dev \
    libimobiledevice-dev \
    libfuse-dev \
    usbmuxd 
 
# Download ifuse 
git clone https://github.com/libimobiledevice/ifuse.git
cd ifuse


# Install ifuse   
./autogen.sh
make
sudo make install


# Change directory back to the working directory
cd ..

# Remove installation file once complete
sudo rm -r ifuse
    

# Download scrcpy 
git clone https://github.com/Genymobile/scrcpy
cd scrcpy

# Install scrcpy
./install_release.sh

# Change directory back to the working directory
cd ..

# Remove installation file once complete
sudo rm -r scrcpy

# Install Python dependencies
pip install -r requirements.txt --break-system-packages


# Start adb server
adb start-server

echo "Installation completed successfully."
