execute_process(COMMAND "/home/ivan/Desktop/ros_noetic_ws/build/srdfdom/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/ivan/Desktop/ros_noetic_ws/build/srdfdom/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
