# Setting up C++ toolchain on the Mac

The official instructions are [here](https://datasheets.raspberrypi.org/pico/getting-started-with-pico.pdf) but.. well, they don't work. Sorry.
What follows doesn't work either. Worth a try though.
Another [source of help is here](https://blog.smittytone.net/2021/02/02/program-raspberry-pi-pico-c-mac/). it also doesn't work.

1. Download the pico-sdk and pico-examples

Create a folder on your Mac, and enter the following at terminal:

```
cd (enter the path to your new folder)
mkdir pico
cd pico
git clone -b master https://github.com/raspberrypi/pico-sdk.git
cd pico-sdk
git submodule update --init
cd ..
git clone -b master https://github.com/raspberrypi/pico-examples.git
```

2. Install the toolchain

2.1 Install [Homebrew](http://brew.sh) first if you haven't already got it on your Mac.

2.2 Install the tools

```
brew install cmake
brew tap ArmMbed/homebrew-formulae
brew install arm-none-eabi-gcc
```

If you don't have Xcode installed, you might see an error. If you do have Xcode installed you might see an error.
It's hard to know what to do other than make sure you have Xcode's tools installed and hope the error is in error.


3.0 Build the "Blink" example

This is where it all starts to go wrong.

```
cd pico-examples
mkdir build
cd build
export PICO_SDK_PATH=../../pico-sdk
```

Ok, so far so good. 

```
cmake ..
```

Errors. Lots of errors.

4.0 Try using Visual Studio Code instead

4.1 Install VS Code.
4.2 From the Extensions menu, include CMake Tools by Microsoft
4.3 In terminal, navigate to the pico-examples folder, and cd into blink
4.4 Launch code in this directory, and select blink.c

``code .``

Visual Studio Code will use the CMake extension to ask you select the right compiler. It will fail to find the right compiler. You are, once again, blocked.

# Using a Raspberry Pi as a development machine

At this point I gave up, and started setting up a Raspberry Pi 4 to work with the Pico instead. Those instructions are wrong too. When you're entering the ```cmake ..`` you must do this in the parent of the pico-examples, not in the specific Blink directory as the instructions say. More help [here](https://www.raspberrypi.org/forums/viewtopic.php?t=302082).

The C++ development process is a lot less fun than the MicroPython tools.

## Update

After moaning a bit, I found a readme file inside the pico SDK which gave the steps for creating and compiling a C++ program. There are several files you need to edit - the CMakeLists.txt file, and the pico_sdk_import.cmake file. The help file explains where to copy them  and/or create them. Then you run cmake, and then make and end up with an .elf and .uf2 file. Either of these can be copied to a Pico to execute on launch.