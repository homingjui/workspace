# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from project/joystick_msg.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class joystick_msg(genpy.Message):
  _md5sum = "feedf0c4942de46502ada06975acd8c3"
  _type = "project/joystick_msg"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool connect
float32 leftX
float32 leftY
float32 rightX
float32 rightY
float32 leftTrg
float32 rightTrg
bool A
bool B
bool X
bool Y
bool padUp
bool padDown
bool padLeft
bool padRight
bool bumperLeft
bool bumperRight
bool guide
"""
  __slots__ = ['connect','leftX','leftY','rightX','rightY','leftTrg','rightTrg','A','B','X','Y','padUp','padDown','padLeft','padRight','bumperLeft','bumperRight','guide']
  _slot_types = ['bool','float32','float32','float32','float32','float32','float32','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       connect,leftX,leftY,rightX,rightY,leftTrg,rightTrg,A,B,X,Y,padUp,padDown,padLeft,padRight,bumperLeft,bumperRight,guide

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(joystick_msg, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.connect is None:
        self.connect = False
      if self.leftX is None:
        self.leftX = 0.
      if self.leftY is None:
        self.leftY = 0.
      if self.rightX is None:
        self.rightX = 0.
      if self.rightY is None:
        self.rightY = 0.
      if self.leftTrg is None:
        self.leftTrg = 0.
      if self.rightTrg is None:
        self.rightTrg = 0.
      if self.A is None:
        self.A = False
      if self.B is None:
        self.B = False
      if self.X is None:
        self.X = False
      if self.Y is None:
        self.Y = False
      if self.padUp is None:
        self.padUp = False
      if self.padDown is None:
        self.padDown = False
      if self.padLeft is None:
        self.padLeft = False
      if self.padRight is None:
        self.padRight = False
      if self.bumperLeft is None:
        self.bumperLeft = False
      if self.bumperRight is None:
        self.bumperRight = False
      if self.guide is None:
        self.guide = False
    else:
      self.connect = False
      self.leftX = 0.
      self.leftY = 0.
      self.rightX = 0.
      self.rightY = 0.
      self.leftTrg = 0.
      self.rightTrg = 0.
      self.A = False
      self.B = False
      self.X = False
      self.Y = False
      self.padUp = False
      self.padDown = False
      self.padLeft = False
      self.padRight = False
      self.bumperLeft = False
      self.bumperRight = False
      self.guide = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_B6f11B().pack(_x.connect, _x.leftX, _x.leftY, _x.rightX, _x.rightY, _x.leftTrg, _x.rightTrg, _x.A, _x.B, _x.X, _x.Y, _x.padUp, _x.padDown, _x.padLeft, _x.padRight, _x.bumperLeft, _x.bumperRight, _x.guide))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 36
      (_x.connect, _x.leftX, _x.leftY, _x.rightX, _x.rightY, _x.leftTrg, _x.rightTrg, _x.A, _x.B, _x.X, _x.Y, _x.padUp, _x.padDown, _x.padLeft, _x.padRight, _x.bumperLeft, _x.bumperRight, _x.guide,) = _get_struct_B6f11B().unpack(str[start:end])
      self.connect = bool(self.connect)
      self.A = bool(self.A)
      self.B = bool(self.B)
      self.X = bool(self.X)
      self.Y = bool(self.Y)
      self.padUp = bool(self.padUp)
      self.padDown = bool(self.padDown)
      self.padLeft = bool(self.padLeft)
      self.padRight = bool(self.padRight)
      self.bumperLeft = bool(self.bumperLeft)
      self.bumperRight = bool(self.bumperRight)
      self.guide = bool(self.guide)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_B6f11B().pack(_x.connect, _x.leftX, _x.leftY, _x.rightX, _x.rightY, _x.leftTrg, _x.rightTrg, _x.A, _x.B, _x.X, _x.Y, _x.padUp, _x.padDown, _x.padLeft, _x.padRight, _x.bumperLeft, _x.bumperRight, _x.guide))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 36
      (_x.connect, _x.leftX, _x.leftY, _x.rightX, _x.rightY, _x.leftTrg, _x.rightTrg, _x.A, _x.B, _x.X, _x.Y, _x.padUp, _x.padDown, _x.padLeft, _x.padRight, _x.bumperLeft, _x.bumperRight, _x.guide,) = _get_struct_B6f11B().unpack(str[start:end])
      self.connect = bool(self.connect)
      self.A = bool(self.A)
      self.B = bool(self.B)
      self.X = bool(self.X)
      self.Y = bool(self.Y)
      self.padUp = bool(self.padUp)
      self.padDown = bool(self.padDown)
      self.padLeft = bool(self.padLeft)
      self.padRight = bool(self.padRight)
      self.bumperLeft = bool(self.bumperLeft)
      self.bumperRight = bool(self.bumperRight)
      self.guide = bool(self.guide)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B6f11B = None
def _get_struct_B6f11B():
    global _struct_B6f11B
    if _struct_B6f11B is None:
        _struct_B6f11B = struct.Struct("<B6f11B")
    return _struct_B6f11B
