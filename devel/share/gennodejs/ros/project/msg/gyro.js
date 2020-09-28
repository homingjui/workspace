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

class gyro {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.acc_x = null;
      this.acc_y = null;
      this.acc_z = null;
      this.gyro_x = null;
      this.gyro_y = null;
      this.gyro_z = null;
      this.angle_x = null;
      this.angle_y = null;
      this.angle_z = null;
    }
    else {
      if (initObj.hasOwnProperty('acc_x')) {
        this.acc_x = initObj.acc_x
      }
      else {
        this.acc_x = 0.0;
      }
      if (initObj.hasOwnProperty('acc_y')) {
        this.acc_y = initObj.acc_y
      }
      else {
        this.acc_y = 0.0;
      }
      if (initObj.hasOwnProperty('acc_z')) {
        this.acc_z = initObj.acc_z
      }
      else {
        this.acc_z = 0.0;
      }
      if (initObj.hasOwnProperty('gyro_x')) {
        this.gyro_x = initObj.gyro_x
      }
      else {
        this.gyro_x = 0.0;
      }
      if (initObj.hasOwnProperty('gyro_y')) {
        this.gyro_y = initObj.gyro_y
      }
      else {
        this.gyro_y = 0.0;
      }
      if (initObj.hasOwnProperty('gyro_z')) {
        this.gyro_z = initObj.gyro_z
      }
      else {
        this.gyro_z = 0.0;
      }
      if (initObj.hasOwnProperty('angle_x')) {
        this.angle_x = initObj.angle_x
      }
      else {
        this.angle_x = 0.0;
      }
      if (initObj.hasOwnProperty('angle_y')) {
        this.angle_y = initObj.angle_y
      }
      else {
        this.angle_y = 0.0;
      }
      if (initObj.hasOwnProperty('angle_z')) {
        this.angle_z = initObj.angle_z
      }
      else {
        this.angle_z = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type gyro
    // Serialize message field [acc_x]
    bufferOffset = _serializer.float32(obj.acc_x, buffer, bufferOffset);
    // Serialize message field [acc_y]
    bufferOffset = _serializer.float32(obj.acc_y, buffer, bufferOffset);
    // Serialize message field [acc_z]
    bufferOffset = _serializer.float32(obj.acc_z, buffer, bufferOffset);
    // Serialize message field [gyro_x]
    bufferOffset = _serializer.float32(obj.gyro_x, buffer, bufferOffset);
    // Serialize message field [gyro_y]
    bufferOffset = _serializer.float32(obj.gyro_y, buffer, bufferOffset);
    // Serialize message field [gyro_z]
    bufferOffset = _serializer.float32(obj.gyro_z, buffer, bufferOffset);
    // Serialize message field [angle_x]
    bufferOffset = _serializer.float32(obj.angle_x, buffer, bufferOffset);
    // Serialize message field [angle_y]
    bufferOffset = _serializer.float32(obj.angle_y, buffer, bufferOffset);
    // Serialize message field [angle_z]
    bufferOffset = _serializer.float32(obj.angle_z, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type gyro
    let len;
    let data = new gyro(null);
    // Deserialize message field [acc_x]
    data.acc_x = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [acc_y]
    data.acc_y = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [acc_z]
    data.acc_z = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [gyro_x]
    data.gyro_x = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [gyro_y]
    data.gyro_y = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [gyro_z]
    data.gyro_z = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [angle_x]
    data.angle_x = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [angle_y]
    data.angle_y = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [angle_z]
    data.angle_z = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 36;
  }

  static datatype() {
    // Returns string type for a message object
    return 'project/gyro';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3826aa65725fd705677ace711a262484';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 acc_x
    float32 acc_y
    float32 acc_z
    float32 gyro_x
    float32 gyro_y
    float32 gyro_z
    float32 angle_x
    float32 angle_y
    float32 angle_z
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new gyro(null);
    if (msg.acc_x !== undefined) {
      resolved.acc_x = msg.acc_x;
    }
    else {
      resolved.acc_x = 0.0
    }

    if (msg.acc_y !== undefined) {
      resolved.acc_y = msg.acc_y;
    }
    else {
      resolved.acc_y = 0.0
    }

    if (msg.acc_z !== undefined) {
      resolved.acc_z = msg.acc_z;
    }
    else {
      resolved.acc_z = 0.0
    }

    if (msg.gyro_x !== undefined) {
      resolved.gyro_x = msg.gyro_x;
    }
    else {
      resolved.gyro_x = 0.0
    }

    if (msg.gyro_y !== undefined) {
      resolved.gyro_y = msg.gyro_y;
    }
    else {
      resolved.gyro_y = 0.0
    }

    if (msg.gyro_z !== undefined) {
      resolved.gyro_z = msg.gyro_z;
    }
    else {
      resolved.gyro_z = 0.0
    }

    if (msg.angle_x !== undefined) {
      resolved.angle_x = msg.angle_x;
    }
    else {
      resolved.angle_x = 0.0
    }

    if (msg.angle_y !== undefined) {
      resolved.angle_y = msg.angle_y;
    }
    else {
      resolved.angle_y = 0.0
    }

    if (msg.angle_z !== undefined) {
      resolved.angle_z = msg.angle_z;
    }
    else {
      resolved.angle_z = 0.0
    }

    return resolved;
    }
};

module.exports = gyro;
