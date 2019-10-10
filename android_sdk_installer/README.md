# Android SDK Installer

Shell script that  
- Installs Android SDK
- Sets up an AVD  
- Adds a function that powers on that AVD  

on Linux based systems following the instructions on [My blog post](https://glacion.com/2019/04/06/AVD.html)

## Dependencies

- Java 8 with $JAVA_HOME environment variable set.
- wget
- unzip 

## Usage

Run `sh install_android_sdk` without sudo.

## Notes

- Script assumes that you have read the Dependencies and Usage section, so if an error occurs you may end up with an unstable state.
- Environment variables will be saved on `~/.profile` so if you have an environment that does not source that file, you'll have to handle it yourself. 