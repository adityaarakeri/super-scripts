#!/bin/sh

echo ">>> Setting up the environment"

tmp_dir="/tmp/tmp.xQeqWI4DYD"
base_dir="$HOME/.local/opt"
profile_file="$HOME/.profile"

avd_name="Nexus"
avd_device="Nexus 5X"

ANDROID_SDK_ROOT=$base_dir/android_sdk
ANDROID_HOME=$ANDROID_SDK_ROOT
ANDROID_AVD_HOME=$base_dir/android_avd

echo "export ANDROID_SDK_ROOT=$base_dir/android_sdk" >> $profile_file
echo 'export ANDROID_HOME=$ANDROID_SDK_ROOT' >> $profile_file
echo "export ANDROID_AVD_HOME=$base_dir/android_avd" >> $profile_file

if [ ! -d "${base_dir}" ]
then
  mkdir ${base_dir}
fi

if [ ! -d "~/.android" ]
then
  mkdir ~/.android
  touch ~/.android/repositories.cfg
fi

echo ">>> Downloading the tools"
wget \
https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip \
-P $tmp_dir

echo ">>> Unpacking the tools"
unzip \
"$tmp_dir/sdk-tools-linux-4333796.zip" \
-d $ANDROID_SDK_ROOT

platform=$($ANDROID_SDK_ROOT/tools/bin/sdkmanager --list \
| grep platforms \
| awk '{ print $1 }' \
| LC_ALL=C sort -k 2 -t '-' -g \
| tail -n 1)
build_tools=$($ANDROID_SDK_ROOT/tools/bin/sdkmanager --list \
| grep build-tools \
| awk '{ print $1 }' \
| LC_ALL=C sort -k 2 -t '-' -g \
| tail -n 1)
avd_image="system-images;android-$(echo $platform | awk -F - '{ print $2 }');google_apis;x86_64"

echo ">>> Installing the SDK"
yes | $ANDROID_SDK_ROOT/tools/bin/sdkmanager \
"platforms;android-$platform_version" \
"$build_tools" \
"$avd_image" \
'platform-tools' \
'ndk-bundle'

echo ">>> Creating an AVD named $avd_name"
$ANDROID_SDK_ROOT/tools/bin/avdmanager create avd \
-n "$avd_name" \
-d "$avd_device" \
-k "$avd_image"

echo ">>> Adding the alias to boot up the emulator"
echo "alias avd='\$ANDROID_SDK_ROOT/tools/emulator @$avd_name -noaudio -nocache -nosnapstorage'" >> $profile_file

echo ">>> Applying changes"
source $profile_file
