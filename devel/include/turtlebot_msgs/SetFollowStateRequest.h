// Generated by gencpp from file turtlebot_msgs/SetFollowStateRequest.msg
// DO NOT EDIT!


#ifndef TURTLEBOT_MSGS_MESSAGE_SETFOLLOWSTATEREQUEST_H
#define TURTLEBOT_MSGS_MESSAGE_SETFOLLOWSTATEREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace turtlebot_msgs
{
template <class ContainerAllocator>
struct SetFollowStateRequest_
{
  typedef SetFollowStateRequest_<ContainerAllocator> Type;

  SetFollowStateRequest_()
    : state(0)  {
    }
  SetFollowStateRequest_(const ContainerAllocator& _alloc)
    : state(0)  {
  (void)_alloc;
    }



   typedef uint8_t _state_type;
  _state_type state;



  enum {
    STOPPED = 0u,
    FOLLOW = 1u,
  };


  typedef boost::shared_ptr< ::turtlebot_msgs::SetFollowStateRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::turtlebot_msgs::SetFollowStateRequest_<ContainerAllocator> const> ConstPtr;

}; // struct SetFollowStateRequest_

typedef ::turtlebot_msgs::SetFollowStateRequest_<std::allocator<void> > SetFollowStateRequest;

typedef boost::shared_ptr< ::turtlebot_msgs::SetFollowStateRequest > SetFollowStateRequestPtr;
typedef boost::shared_ptr< ::turtlebot_msgs::SetFollowStateRequest const> SetFollowStateRequestConstPtr;

// constants requiring out of line definition

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::turtlebot_msgs::SetFollowStateRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::turtlebot_msgs::SetFollowStateRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace turtlebot_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'turtlebot_msgs': ['/home/isp/Desktop/workspace/src/turtlebot_msgs/msg'], 'sensor_msgs': ['/opt/ros/melodic/share/sensor_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/melodic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::turtlebot_msgs::SetFollowStateRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::turtlebot_msgs::SetFollowStateRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::turtlebot_msgs::SetFollowStateRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::turtlebot_msgs::SetFollowStateRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::turtlebot_msgs::SetFollowStateRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::turtlebot_msgs::SetFollowStateRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::turtlebot_msgs::SetFollowStateRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "92b912c48c68248015bb32deb0bf7713";
  }

  static const char* value(const ::turtlebot_msgs::SetFollowStateRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x92b912c48c682480ULL;
  static const uint64_t static_value2 = 0x15bb32deb0bf7713ULL;
};

template<class ContainerAllocator>
struct DataType< ::turtlebot_msgs::SetFollowStateRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "turtlebot_msgs/SetFollowStateRequest";
  }

  static const char* value(const ::turtlebot_msgs::SetFollowStateRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::turtlebot_msgs::SetFollowStateRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint8 STOPPED = 0\n"
"uint8 FOLLOW  = 1\n"
"\n"
"\n"
"uint8 state\n"
"\n"
;
  }

  static const char* value(const ::turtlebot_msgs::SetFollowStateRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::turtlebot_msgs::SetFollowStateRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.state);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SetFollowStateRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::turtlebot_msgs::SetFollowStateRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::turtlebot_msgs::SetFollowStateRequest_<ContainerAllocator>& v)
  {
    s << indent << "state: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.state);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TURTLEBOT_MSGS_MESSAGE_SETFOLLOWSTATEREQUEST_H
