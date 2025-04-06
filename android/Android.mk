# ndk-build NDK_PROJECT_PATH=. APP_BUILD_SCRIPT=Android.mk APP_ABI=arm64-v8a
LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE    := sniffer
LOCAL_SRC_FILES := sniffer.c

include $(BUILD_EXECUTABLE)


# Build results:
# Android NDK: APP_PLATFORM not set. Defaulting to minimum supported version android-21.
# [arm64-v8a] Compile        : sniffer <= sniffer.c
# [arm64-v8a] Executable     : sniffer
# [arm64-v8a] Install        : sniffer => libs/arm64-v8a/sniffer