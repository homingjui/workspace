#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/isp/Desktop/workspace/src/ROS-TCP-Endpoint"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/isp/Desktop/workspace/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/isp/Desktop/workspace/install/lib/python2.7/dist-packages:/home/isp/Desktop/workspace/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/isp/Desktop/workspace/build" \
    "/usr/bin/python2" \
    "/home/isp/Desktop/workspace/src/ROS-TCP-Endpoint/setup.py" \
    egg_info --egg-base /home/isp/Desktop/workspace/build/ROS-TCP-Endpoint \
    build --build-base "/home/isp/Desktop/workspace/build/ROS-TCP-Endpoint" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/isp/Desktop/workspace/install" --install-scripts="/home/isp/Desktop/workspace/install/bin"
