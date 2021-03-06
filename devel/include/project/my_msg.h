// Generated by gencpp from file project/my_msg.msg
// DO NOT EDIT!


#ifndef PROJECT_MESSAGE_MY_MSG_H
#define PROJECT_MESSAGE_MY_MSG_H


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
struct my_msg_
{
  typedef my_msg_<ContainerAllocator> Type;

  my_msg_()
    : connect(false)
    , leftX(0.0)
    , leftR(0.0)
    , rightX(0.0)
    , rightY(0.0)
    , leftTrg(0.0)
    , rightTrg(0.0)
    , A(false)
    , B(false)
    , X(false)
    , Y(false)
    , padUp(false)
    , padDown(false)
    , padLeft(false)
    , padRight(false)
    , bumperLeft(false)
    , bumperRight(false)  {
    }
  my_msg_(const ContainerAllocator& _alloc)
    : connect(false)
    , leftX(0.0)
    , leftR(0.0)
    , rightX(0.0)
    , rightY(0.0)
    , leftTrg(0.0)
    , rightTrg(0.0)
    , A(false)
    , B(false)
    , X(false)
    , Y(false)
    , padUp(false)
    , padDown(false)
    , padLeft(false)
    , padRight(false)
    , bumperLeft(false)
    , bumperRight(false)  {
  (void)_alloc;
    }



   typedef uint8_t _connect_type;
  _connect_type connect;

   typedef float _leftX_type;
  _leftX_type leftX;

   typedef float _leftR_type;
  _leftR_type leftR;

   typedef float _rightX_type;
  _rightX_type rightX;

   typedef float _rightY_type;
  _rightY_type rightY;

   typedef float _leftTrg_type;
  _leftTrg_type leftTrg;

   typedef float _rightTrg_type;
  _rightTrg_type rightTrg;

   typedef uint8_t _A_type;
  _A_type A;

   typedef uint8_t _B_type;
  _B_type B;

   typedef uint8_t _X_type;
  _X_type X;

   typedef uint8_t _Y_type;
  _Y_type Y;

   typedef uint8_t _padUp_type;
  _padUp_type padUp;

   typedef uint8_t _padDown_type;
  _padDown_type padDown;

   typedef uint8_t _padLeft_type;
  _padLeft_type padLeft;

   typedef uint8_t _padRight_type;
  _padRight_type padRight;

   typedef uint8_t _bumperLeft_type;
  _bumperLeft_type bumperLeft;

   typedef uint8_t _bumperRight_type;
  _bumperRight_type bumperRight;





  typedef boost::shared_ptr< ::project::my_msg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::project::my_msg_<ContainerAllocator> const> ConstPtr;

}; // struct my_msg_

typedef ::project::my_msg_<std::allocator<void> > my_msg;

typedef boost::shared_ptr< ::project::my_msg > my_msgPtr;
typedef boost::shared_ptr< ::project::my_msg const> my_msgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::project::my_msg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::project::my_msg_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::project::my_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::project::my_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::project::my_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::project::my_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::project::my_msg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::project::my_msg_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::project::my_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "666d003c179026e1a217a6c7a3916503";
  }

  static const char* value(const ::project::my_msg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x666d003c179026e1ULL;
  static const uint64_t static_value2 = 0xa217a6c7a3916503ULL;
};

template<class ContainerAllocator>
struct DataType< ::project::my_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "project/my_msg";
  }

  static const char* value(const ::project::my_msg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::project::my_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool connect\n"
"float32 leftX\n"
"float32 leftR\n"
"float32 rightX\n"
"float32 rightY\n"
"float32 leftTrg\n"
"float32 rightTrg\n"
"bool A\n"
"bool B\n"
"bool X\n"
"bool Y\n"
"bool padUp\n"
"bool padDown\n"
"bool padLeft\n"
"bool padRight\n"
"bool bumperLeft\n"
"bool bumperRight\n"
;
  }

  static const char* value(const ::project::my_msg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::project::my_msg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.connect);
      stream.next(m.leftX);
      stream.next(m.leftR);
      stream.next(m.rightX);
      stream.next(m.rightY);
      stream.next(m.leftTrg);
      stream.next(m.rightTrg);
      stream.next(m.A);
      stream.next(m.B);
      stream.next(m.X);
      stream.next(m.Y);
      stream.next(m.padUp);
      stream.next(m.padDown);
      stream.next(m.padLeft);
      stream.next(m.padRight);
      stream.next(m.bumperLeft);
      stream.next(m.bumperRight);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct my_msg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::project::my_msg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::project::my_msg_<ContainerAllocator>& v)
  {
    s << indent << "connect: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.connect);
    s << indent << "leftX: ";
    Printer<float>::stream(s, indent + "  ", v.leftX);
    s << indent << "leftR: ";
    Printer<float>::stream(s, indent + "  ", v.leftR);
    s << indent << "rightX: ";
    Printer<float>::stream(s, indent + "  ", v.rightX);
    s << indent << "rightY: ";
    Printer<float>::stream(s, indent + "  ", v.rightY);
    s << indent << "leftTrg: ";
    Printer<float>::stream(s, indent + "  ", v.leftTrg);
    s << indent << "rightTrg: ";
    Printer<float>::stream(s, indent + "  ", v.rightTrg);
    s << indent << "A: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.A);
    s << indent << "B: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.B);
    s << indent << "X: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.X);
    s << indent << "Y: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Y);
    s << indent << "padUp: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.padUp);
    s << indent << "padDown: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.padDown);
    s << indent << "padLeft: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.padLeft);
    s << indent << "padRight: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.padRight);
    s << indent << "bumperLeft: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.bumperLeft);
    s << indent << "bumperRight: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.bumperRight);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PROJECT_MESSAGE_MY_MSG_H
