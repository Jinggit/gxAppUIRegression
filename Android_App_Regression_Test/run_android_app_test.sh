#!/bin/sh
pybot --outputdir ./logs --variable REMOTE_URL:$REMOTE_URL --variable PLATFORM_NAME:$PLATFORM_NAME --variable PLATFORM_VERSION:$PLATFORM_VERSION --variable DEVICE_NAME:$DEVICE_NAME --variable APP:$APP --variable PACKAGE:$PACKAGE --variable APPACTIVITY:$APPACTIVITY --exclude $EXCLUDE1 ./Android_App_Regression_Test
exit 0
