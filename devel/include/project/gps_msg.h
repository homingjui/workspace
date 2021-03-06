// Generated by gencpp from file project/gps_msg.msg
// DO NOT EDIT!


#ifndef PROJECT_MESSAGE_GPS_MSG_H
#define PROJECT_MESSAGE_GPS_MSG_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace project
{
template <class ContainerAllocator>
struct gps_msg_
{
  typedef gps_msg_<ContainerAllocator> Type;

  gps_msg_()
    : latitude(0.0)
    , longitude(0.0)
    , fix_code(0)  {
    }
  gps_msg_(const ContainerAllocator& _alloc)
    : latitude(0.0)
    , longitude(0.0)
    , fix_code(0)  {
  (void)_alloc;
    }



   typedef double _latitude_type;
  _latitude_type latitude;

   typedef double _longitude_type;
  _longitude_type longitude;

   typedef int64_t _fix_code_type;
  _fix_code_type fix_code;





  typedef boost::shared_ptr< ::project::gps_msg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::project::gps_msg_<ContainerAllocator> const> ConstPtr;

}; // struct gps_msg_

typedef ::project::gps_msg_<std::allocator<void> > gps_msg;

typedef boost::shared_ptr< ::project::gps_msg > gps_msgPtr;
typedef boost::shared_ptr< ::project::gps_msg const> gps_msgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::project::gps_msg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::project::gps_msg_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace project

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'project': ['/home/isp/Desktop/workspace/src/project/msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::project::gps_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::project::gps_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::project::gps_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::project::gps_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::project::gps_msg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::project::gps_msg_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::project::gps_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "7ed9f98eb48746167a823b93c6cfb5ff";
  }

  static const char* value(const ::project::gps_msg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x7ed9f98eb4874616ULL;
  static const uint64_t static_value2 = 0x7a823b93c6cfb5ffULL;
};

template<class ContainerAllocator>
struct DataType< ::project::gps_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "project/gps_msg";
  }

  static const char* value(const ::project::gps_msg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::project::gps_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 latitude\n"
"float64 longitude\n"
"int64 fix_code\n"
;
  }

  static const char* value(const ::project::gps_msg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::project::gps_msg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.latitude);
      stream.next(m.longitude);
      stream.next(m.fix_code);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct gps_msg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::project::gps_msg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::project::gps_msg_<ContainerAllocator>& v)
  {
    s << indent << "latitude: ";
    Printer<double>::stream(s, indent + "  ", v.latitude);
    s << indent << "longitude: ";
    Printer<double>::stream(s, indent + "  ", v.longitude);
    s << indent << "fix_code: ";
    Printer<int64_t>::stream(s, indent + "  ", v.fix_code);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PROJECT_MESSAGE_GPS_MSG_H
