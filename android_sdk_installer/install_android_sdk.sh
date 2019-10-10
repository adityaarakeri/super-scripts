#!/bin/sh

echo ">>> Setting up the environment"

tmp_dir="/tmp/tmp.xQeqWI4DYD"
base_dir="$HOME/.local/opt"
profile_file="$HOME/.profile"

platform_version="29"
build_tools_version="29.0.2"

avd_name="Nexus"
avd_device="Nexus 5X"
avd_image="system-images;android-$platform_version;google_apis;x86_64"

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
# wget \
# https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip \
# -P $tmp_dir

echo ">>> Unpacking the tools"
unzip \
"$tmp_dir/sdk-tools-linux-4333796.zip" \
-d $ANDROID_SDK_ROOT

echo ">>> Installing the SDK"
yes | $ANDROID_SDK_ROOT/tools/bin/sdkmanager \
"platforms;android-$platform_version" \
"build-tools;$build_tools_version" \
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
