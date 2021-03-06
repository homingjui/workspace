// Generated by gencpp from file project/arduino_msg.msg
// DO NOT EDIT!


#ifndef PROJECT_MESSAGE_ARDUINO_MSG_H
#define PROJECT_MESSAGE_ARDUINO_MSG_H


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
struct arduino_msg_
{
  typedef arduino_msg_<ContainerAllocator> Type;

  arduino_msg_()
    : voltage(0.0)
    , gyroX(0.0)
    , gyroY(0.0)
    , gyroZ(0.0)
    , accX(0.0)
    , accY(0.0)
    , accZ(0.0)
    , roll(0.0)
    , pitch(0.0)
    , yaw(0.0)  {
    }
  arduino_msg_(const ContainerAllocator& _alloc)
    : voltage(0.0)
    , gyroX(0.0)
    , gyroY(0.0)
    , gyroZ(0.0)
    , accX(0.0)
    , accY(0.0)
    , accZ(0.0)
    , roll(0.0)
    , pitch(0.0)
    , yaw(0.0)  {
  (void)_alloc;
    }



   typedef float _voltage_type;
  _voltage_type voltage;

   typedef float _gyroX_type;
  _gyroX_type gyroX;

   typedef float _gyroY_type;
  _gyroY_type gyroY;

   typedef float _gyroZ_type;
  _gyroZ_type gyroZ;

   typedef float _accX_type;
  _accX_type accX;

   typedef float _accY_type;
  _accY_type accY;

   typedef float _accZ_type;
  _accZ_type accZ;

   typedef float _roll_type;
  _roll_type roll;

   typedef float _pitch_type;
  _pitch_type pitch;

   typedef float _yaw_type;
  _yaw_type yaw;





  typedef boost::shared_ptr< ::project::arduino_msg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::project::arduino_msg_<ContainerAllocator> const> ConstPtr;

}; // struct arduino_msg_

typedef ::project::arduino_msg_<std::allocator<void> > arduino_msg;

typedef boost::shared_ptr< ::project::arduino_msg > arduino_msgPtr;
typedef boost::shared_ptr< ::project::arduino_msg const> arduino_msgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::project::arduino_msg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::project::arduino_msg_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::project::arduino_msg_<ContainerAllocator1> & lhs, const ::project::arduino_msg_<ContainerAllocator2> & rhs)
{
  return lhs.voltage == rhs.voltage &&
    lhs.gyroX == rhs.gyroX &&
    lhs.gyroY == rhs.gyroY &&
    lhs.gyroZ == rhs.gyroZ &&
    lhs.accX == rhs.accX &&
    lhs.accY == rhs.accY &&
    lhs.accZ == rhs.accZ &&
    lhs.roll == rhs.roll &&
    lhs.pitch == rhs.pitch &&
    lhs.yaw == rhs.yaw;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::project::arduino_msg_<ContainerAllocator1> & lhs, const ::project::arduino_msg_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace project

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::project::arduino_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::project::arduino_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::project::arduino_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::project::arduino_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::project::arduino_msg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::project::arduino_msg_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::project::arduino_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6147ba7bc1e9a27ffeb41686ce827cfa";
  }

  static const char* value(const ::project::arduino_msg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6147ba7bc1e9a27fULL;
  static const uint64_t static_value2 = 0xfeb41686ce827cfaULL;
};

template<class ContainerAllocator>
struct DataType< ::project::arduino_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "project/arduino_msg";
  }

  static const char* value(const ::project::arduino_msg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::project::arduino_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 voltage\n"
"float32 gyroX\n"
"float32 gyroY\n"
"float32 gyroZ\n"
"float32 accX\n"
"float32 accY\n"
"float32 accZ\n"
"float32 roll\n"
"float32 pitch\n"
"float32 yaw\n"
;
  }

  static const char* value(const ::project::arduino_msg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::project::arduino_msg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.voltage);
      stream.next(m.gyroX);
      stream.next(m.gyroY);
      stream.next(m.gyroZ);
      stream.next(m.accX);
      stream.next(m.accY);
      stream.next(m.accZ);
      stream.next(m.roll);
      stream.next(m.pitch);
      stream.next(m.yaw);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct arduino_msg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::project::arduino_msg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::project::arduino_msg_<ContainerAllocator>& v)
  {
    s << indent << "voltage: ";
    Printer<float>::stream(s, indent + "  ", v.voltage);
    s << indent << "gyroX: ";
    Printer<float>::stream(s, indent + "  ", v.gyroX);
    s << indent << "gyroY: ";
    Printer<float>::stream(s, indent + "  ", v.gyroY);
    s << indent << "gyroZ: ";
    Printer<float>::stream(s, indent + "  ", v.gyroZ);
    s << indent << "accX: ";
    Printer<float>::stream(s, indent + "  ", v.accX);
    s << indent << "accY: ";
    Printer<float>::stream(s, indent + "  ", v.accY);
    s << indent << "accZ: ";
    Printer<float>::stream(s, indent + "  ", v.accZ);
    s << indent << "roll: ";
    Printer<float>::stream(s, indent + "  ", v.roll);
    s << indent << "pitch: ";
    Printer<float>::stream(s, indent + "  ", v.pitch);
    s << indent << "yaw: ";
    Printer<float>::stream(s, indent + "  ", v.yaw);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PROJECT_MESSAGE_ARDUINO_MSG_H
