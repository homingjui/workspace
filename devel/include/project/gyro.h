// Generated by gencpp from file project/gyro.msg
// DO NOT EDIT!


#ifndef PROJECT_MESSAGE_GYRO_H
#define PROJECT_MESSAGE_GYRO_H


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
struct gyro_
{
  typedef gyro_<ContainerAllocator> Type;

  gyro_()
    : acc_x(0.0)
    , acc_y(0.0)
    , acc_z(0.0)
    , gyro_x(0.0)
    , gyro_y(0.0)
    , gyro_z(0.0)
    , angle_x(0.0)
    , angle_y(0.0)
    , angle_z(0.0)  {
    }
  gyro_(const ContainerAllocator& _alloc)
    : acc_x(0.0)
    , acc_y(0.0)
    , acc_z(0.0)
    , gyro_x(0.0)
    , gyro_y(0.0)
    , gyro_z(0.0)
    , angle_x(0.0)
    , angle_y(0.0)
    , angle_z(0.0)  {
  (void)_alloc;
    }



   typedef float _acc_x_type;
  _acc_x_type acc_x;

   typedef float _acc_y_type;
  _acc_y_type acc_y;

   typedef float _acc_z_type;
  _acc_z_type acc_z;

   typedef float _gyro_x_type;
  _gyro_x_type gyro_x;

   typedef float _gyro_y_type;
  _gyro_y_type gyro_y;

   typedef float _gyro_z_type;
  _gyro_z_type gyro_z;

   typedef float _angle_x_type;
  _angle_x_type angle_x;

   typedef float _angle_y_type;
  _angle_y_type angle_y;

   typedef float _angle_z_type;
  _angle_z_type angle_z;





  typedef boost::shared_ptr< ::project::gyro_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::project::gyro_<ContainerAllocator> const> ConstPtr;

}; // struct gyro_

typedef ::project::gyro_<std::allocator<void> > gyro;

typedef boost::shared_ptr< ::project::gyro > gyroPtr;
typedef boost::shared_ptr< ::project::gyro const> gyroConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::project::gyro_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::project::gyro_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::project::gyro_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::project::gyro_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::project::gyro_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::project::gyro_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::project::gyro_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::project::gyro_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::project::gyro_<ContainerAllocator> >
{
  static const char* value()
  {
    return "3826aa65725fd705677ace711a262484";
  }

  static const char* value(const ::project::gyro_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x3826aa65725fd705ULL;
  static const uint64_t static_value2 = 0x677ace711a262484ULL;
};

template<class ContainerAllocator>
struct DataType< ::project::gyro_<ContainerAllocator> >
{
  static const char* value()
  {
    return "project/gyro";
  }

  static const char* value(const ::project::gyro_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::project::gyro_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 acc_x\n"
"float32 acc_y\n"
"float32 acc_z\n"
"float32 gyro_x\n"
"float32 gyro_y\n"
"float32 gyro_z\n"
"float32 angle_x\n"
"float32 angle_y\n"
"float32 angle_z\n"
;
  }

  static const char* value(const ::project::gyro_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::project::gyro_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.acc_x);
      stream.next(m.acc_y);
      stream.next(m.acc_z);
      stream.next(m.gyro_x);
      stream.next(m.gyro_y);
      stream.next(m.gyro_z);
      stream.next(m.angle_x);
      stream.next(m.angle_y);
      stream.next(m.angle_z);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct gyro_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::project::gyro_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::project::gyro_<ContainerAllocator>& v)
  {
    s << indent << "acc_x: ";
    Printer<float>::stream(s, indent + "  ", v.acc_x);
    s << indent << "acc_y: ";
    Printer<float>::stream(s, indent + "  ", v.acc_y);
    s << indent << "acc_z: ";
    Printer<float>::stream(s, indent + "  ", v.acc_z);
    s << indent << "gyro_x: ";
    Printer<float>::stream(s, indent + "  ", v.gyro_x);
    s << indent << "gyro_y: ";
    Printer<float>::stream(s, indent + "  ", v.gyro_y);
    s << indent << "gyro_z: ";
    Printer<float>::stream(s, indent + "  ", v.gyro_z);
    s << indent << "angle_x: ";
    Printer<float>::stream(s, indent + "  ", v.angle_x);
    s << indent << "angle_y: ";
    Printer<float>::stream(s, indent + "  ", v.angle_y);
    s << indent << "angle_z: ";
    Printer<float>::stream(s, indent + "  ", v.angle_z);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PROJECT_MESSAGE_GYRO_H
