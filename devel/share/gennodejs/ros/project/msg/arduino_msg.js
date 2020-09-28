// Auto-generated. Do not edit!

// (in-package project.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class arduino_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.voltage = null;
      this.gyroX = null;
      this.gyroY = null;
      this.gyroZ = null;
      this.accX = null;
      this.accY = null;
      this.accZ = null;
      this.roll = null;
      this.pitch = null;
      this.yaw = null;
    }
    else {
      if (initObj.hasOwnProperty('voltage')) {
        this.voltage = initObj.voltage
      }
      else {
        this.voltage = 0.0;
      }
      if (initObj.hasOwnProperty('gyroX')) {
        this.gyroX = initObj.gyroX
      }
      else {
        this.gyroX = 0.0;
      }
      if (initObj.hasOwnProperty('gyroY')) {
        this.gyroY = initObj.gyroY
      }
      else {
        this.gyroY = 0.0;
      }
      if (initObj.hasOwnProperty('gyroZ')) {
        this.gyroZ = initObj.gyroZ
      }
      else {
        this.gyroZ = 0.0;
      }
      if (initObj.hasOwnProperty('accX')) {
        this.accX = initObj.accX
      }
      else {
        this.accX = 0.0;
      }
      if (initObj.hasOwnProperty('accY')) {
        this.accY = initObj.accY
      }
      else {
        this.accY = 0.0;
      }
      if (initObj.hasOwnProperty('accZ')) {
        this.accZ = initObj.accZ
      }
      else {
        this.accZ = 0.0;
      }
      if (initObj.hasOwnProperty('roll')) {
        this.roll = initObj.roll
      }
      else {
        this.roll = 0.0;
      }
      if (initObj.hasOwnProperty('pitch')) {
        this.pitch = initObj.pitch
      }
      else {
        this.pitch = 0.0;
      }
      if (initObj.hasOwnProperty('yaw')) {
        this.yaw = initObj.yaw
      }
      else {
        this.yaw = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type arduino_msg
    // Serialize message field [voltage]
    bufferOffset = _serializer.float32(obj.voltage, buffer, bufferOffset);
    // Serialize message field [gyroX]
    bufferOffset = _serializer.float32(obj.gyroX, buffer, bufferOffset);
    // Serialize message field [gyroY]
    bufferOffset = _serializer.float32(obj.gyroY, buffer, bufferOffset);
    // Serialize message field [gyroZ]
    bufferOffset = _serializer.float32(obj.gyroZ, buffer, bufferOffset);
    // Serialize message field [accX]
    bufferOffset = _serializer.float32(obj.accX, buffer, bufferOffset);
    // Serialize message field [accY]
    bufferOffset = _serializer.float32(obj.accY, buffer, bufferOffset);
    // Serialize message field [accZ]
    bufferOffset = _serializer.float32(obj.accZ, buffer, bufferOffset);
    // Serialize message field [roll]
    bufferOffset = _serializer.float32(obj.roll, buffer, bufferOffset);
    // Serialize message field [pitch]
    bufferOffset = _serializer.float32(obj.pitch, buffer, bufferOffset);
    // Serialize message field [yaw]
    bufferOffset = _serializer.float32(obj.yaw, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type arduino_msg
    let len;
    let data = new arduino_msg(null);
    // Deserialize message field [voltage]
    data.voltage = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [gyroX]
    data.gyroX = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [gyroY]
    data.gyroY = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [gyroZ]
    data.gyroZ = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [accX]
    data.accX = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [accY]
    data.accY = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [accZ]
    data.accZ = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [roll]
    data.roll = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [pitch]
    data.pitch = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [yaw]
    data.yaw = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 40;
  }

  static datatype() {
    // Returns string type for a message object
    return 'project/arduino_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6147ba7bc1e9a27ffeb41686ce827cfa';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 voltage
    float32 gyroX
    float32 gyroY
    float32 gyroZ
    float32 accX
    float32 accY
    float32 accZ
    float32 roll
    float32 pitch
    float32 yaw
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new arduino_msg(null);
    if (msg.voltage !== undefined) {
      resolved.voltage = msg.voltage;
    }
    else {
      resolved.voltage = 0.0
    }

    if (msg.gyroX !== undefined) {
      resolved.gyroX = msg.gyroX;
    }
    else {
      resolved.gyroX = 0.0
    }

    if (msg.gyroY !== undefined) {
      resolved.gyroY = msg.gyroY;
    }
    else {
      resolved.gyroY = 0.0
    }

    if (msg.gyroZ !== undefined) {
      resolved.gyroZ = msg.gyroZ;
    }
    else {
      resolved.gyroZ = 0.0
    }

    if (msg.accX !== undefined) {
      resolved.accX = msg.accX;
    }
    else {
      resolved.accX = 0.0
    }

    if (msg.accY !== undefined) {
      resolved.accY = msg.accY;
    }
    else {
      resolved.accY = 0.0
    }

    if (msg.accZ !== undefined) {
      resolved.accZ = msg.accZ;
    }
    else {
      resolved.accZ = 0.0
    }

    if (msg.roll !== undefined) {
      resolved.roll = msg.roll;
    }
    else {
      resolved.roll = 0.0
    }

    if (msg.pitch !== undefined) {
      resolved.pitch = msg.pitch;
    }
    else {
      resolved.pitch = 0.0
    }

    if (msg.yaw !== undefined) {
      resolved.yaw = msg.yaw;
    }
    else {
      resolved.yaw = 0.0
    }

    return resolved;
    }
};

module.exports = arduino_msg;
