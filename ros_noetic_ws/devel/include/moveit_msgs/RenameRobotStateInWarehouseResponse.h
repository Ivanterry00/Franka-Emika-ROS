// Generated by gencpp from file moveit_msgs/RenameRobotStateInWarehouseResponse.msg
// DO NOT EDIT!


#ifndef MOVEIT_MSGS_MESSAGE_RENAMEROBOTSTATEINWAREHOUSERESPONSE_H
#define MOVEIT_MSGS_MESSAGE_RENAMEROBOTSTATEINWAREHOUSERESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace moveit_msgs
{
template <class ContainerAllocator>
struct RenameRobotStateInWarehouseResponse_
{
  typedef RenameRobotStateInWarehouseResponse_<ContainerAllocator> Type;

  RenameRobotStateInWarehouseResponse_()
    {
    }
  RenameRobotStateInWarehouseResponse_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::moveit_msgs::RenameRobotStateInWarehouseResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::moveit_msgs::RenameRobotStateInWarehouseResponse_<ContainerAllocator> const> ConstPtr;

}; // struct RenameRobotStateInWarehouseResponse_

typedef ::moveit_msgs::RenameRobotStateInWarehouseResponse_<std::allocator<void> > RenameRobotStateInWarehouseResponse;

typedef boost::shared_ptr< ::moveit_msgs::RenameRobotStateInWarehouseResponse > RenameRobotStateInWarehouseResponsePtr;
typedef boost::shared_ptr< ::moveit_msgs::RenameRobotStateInWarehouseResponse const> RenameRobotStateInWarehouseResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::moveit_msgs::RenameRobotStateInWarehouseResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::moveit_msgs::RenameRobotStateInWarehouseResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace moveit_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::moveit_msgs::RenameRobotStateInWarehouseResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::moveit_msgs::RenameRobotStateInWarehouseResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::moveit_msgs::RenameRobotStateInWarehouseResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::moveit_msgs::RenameRobotStateInWarehouseResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::moveit_msgs::RenameRobotStateInWarehouseResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::moveit_msgs::RenameRobotStateInWarehouseResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::moveit_msgs::RenameRobotStateInWarehouseResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::moveit_msgs::RenameRobotStateInWarehouseResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::moveit_msgs::RenameRobotStateInWarehouseResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "moveit_msgs/RenameRobotStateInWarehouseResponse";
  }

  static const char* value(const ::moveit_msgs::RenameRobotStateInWarehouseResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::moveit_msgs::RenameRobotStateInWarehouseResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
;
  }

  static const char* value(const ::moveit_msgs::RenameRobotStateInWarehouseResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::moveit_msgs::RenameRobotStateInWarehouseResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RenameRobotStateInWarehouseResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::moveit_msgs::RenameRobotStateInWarehouseResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::moveit_msgs::RenameRobotStateInWarehouseResponse_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // MOVEIT_MSGS_MESSAGE_RENAMEROBOTSTATEINWAREHOUSERESPONSE_H
