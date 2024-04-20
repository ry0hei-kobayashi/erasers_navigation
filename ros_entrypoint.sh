#!/bin/bash
set -e

# setup ros environment
source "/opt/ros/noetic/setup.bash"
source "/catkin_ws/devel/setup.bash" --extend
source "/cartographer_ws/install_isolated/setup.bash" --extend
exec "$@"
