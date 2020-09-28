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

class deg_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.deg = null;
    }
    else {
      if (initObj.hasOwnProperty('deg')) {
        this.deg = initObj.deg
      }
      else {
        this.deg = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type deg_msg
    // Serialize message field [deg]
    bufferOffset = _serializer.float32(obj.deg, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type deg_msg
    let len;
    let data = new deg_msg(null);
    // Deserialize message field [deg]
    data.deg = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'project/deg_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '75960300fe371de17649c522b949ca85';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 deg
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new deg_msg(null);
    if (msg.deg !== undefined) {
      resolved.deg = msg.deg;
    }
    else {
      resolved.deg = 0.0
    }

    return resolved;
    }
};

module.exports = deg_msg;
