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

class motor_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.way = null;
      this.speed = null;
      this.persent = null;
    }
    else {
      if (initObj.hasOwnProperty('way')) {
        this.way = initObj.way
      }
      else {
        this.way = '';
      }
      if (initObj.hasOwnProperty('speed')) {
        this.speed = initObj.speed
      }
      else {
        this.speed = 0;
      }
      if (initObj.hasOwnProperty('persent')) {
        this.persent = initObj.persent
      }
      else {
        this.persent = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type motor_msg
    // Serialize message field [way]
    bufferOffset = _serializer.string(obj.way, buffer, bufferOffset);
    // Serialize message field [speed]
    bufferOffset = _serializer.int64(obj.speed, buffer, bufferOffset);
    // Serialize message field [persent]
    bufferOffset = _serializer.float64(obj.persent, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type motor_msg
    let len;
    let data = new motor_msg(null);
    // Deserialize message field [way]
    data.way = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [speed]
    data.speed = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [persent]
    data.persent = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.way.length;
    return length + 20;
  }

  static datatype() {
    // Returns string type for a message object
    return 'project/motor_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3535bdf16ad57a8f3e9a1b542ed91b5d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string way
    int64 speed
    float64 persent
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new motor_msg(null);
    if (msg.way !== undefined) {
      resolved.way = msg.way;
    }
    else {
      resolved.way = ''
    }

    if (msg.speed !== undefined) {
      resolved.speed = msg.speed;
    }
    else {
      resolved.speed = 0
    }

    if (msg.persent !== undefined) {
      resolved.persent = msg.persent;
    }
    else {
      resolved.persent = 0.0
    }

    return resolved;
    }
};

module.exports = motor_msg;
