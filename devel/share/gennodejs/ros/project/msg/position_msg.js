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

class position_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.path = null;
      this.now_x = null;
      this.now_y = null;
      this.next_dot = null;
      this.next_p = null;
      this.passing = null;
    }
    else {
      if (initObj.hasOwnProperty('path')) {
        this.path = initObj.path
      }
      else {
        this.path = [];
      }
      if (initObj.hasOwnProperty('now_x')) {
        this.now_x = initObj.now_x
      }
      else {
        this.now_x = 0.0;
      }
      if (initObj.hasOwnProperty('now_y')) {
        this.now_y = initObj.now_y
      }
      else {
        this.now_y = 0.0;
      }
      if (initObj.hasOwnProperty('next_dot')) {
        this.next_dot = initObj.next_dot
      }
      else {
        this.next_dot = 0;
      }
      if (initObj.hasOwnProperty('next_p')) {
        this.next_p = initObj.next_p
      }
      else {
        this.next_p = [];
      }
      if (initObj.hasOwnProperty('passing')) {
        this.passing = initObj.passing
      }
      else {
        this.passing = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type position_msg
    // Serialize message field [path]
    bufferOffset = _arraySerializer.float64(obj.path, buffer, bufferOffset, null);
    // Serialize message field [now_x]
    bufferOffset = _serializer.float64(obj.now_x, buffer, bufferOffset);
    // Serialize message field [now_y]
    bufferOffset = _serializer.float64(obj.now_y, buffer, bufferOffset);
    // Serialize message field [next_dot]
    bufferOffset = _serializer.int64(obj.next_dot, buffer, bufferOffset);
    // Serialize message field [next_p]
    bufferOffset = _arraySerializer.float64(obj.next_p, buffer, bufferOffset, null);
    // Serialize message field [passing]
    bufferOffset = _arraySerializer.float64(obj.passing, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type position_msg
    let len;
    let data = new position_msg(null);
    // Deserialize message field [path]
    data.path = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [now_x]
    data.now_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [now_y]
    data.now_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [next_dot]
    data.next_dot = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [next_p]
    data.next_p = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [passing]
    data.passing = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 8 * object.path.length;
    length += 8 * object.next_p.length;
    length += 8 * object.passing.length;
    return length + 36;
  }

  static datatype() {
    // Returns string type for a message object
    return 'project/position_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8c8333feeb19f29f3015ed8ba27f62fc';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[] path
    float64 now_x
    float64 now_y
    int64 next_dot
    float64[] next_p
    float64[] passing
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new position_msg(null);
    if (msg.path !== undefined) {
      resolved.path = msg.path;
    }
    else {
      resolved.path = []
    }

    if (msg.now_x !== undefined) {
      resolved.now_x = msg.now_x;
    }
    else {
      resolved.now_x = 0.0
    }

    if (msg.now_y !== undefined) {
      resolved.now_y = msg.now_y;
    }
    else {
      resolved.now_y = 0.0
    }

    if (msg.next_dot !== undefined) {
      resolved.next_dot = msg.next_dot;
    }
    else {
      resolved.next_dot = 0
    }

    if (msg.next_p !== undefined) {
      resolved.next_p = msg.next_p;
    }
    else {
      resolved.next_p = []
    }

    if (msg.passing !== undefined) {
      resolved.passing = msg.passing;
    }
    else {
      resolved.passing = []
    }

    return resolved;
    }
};

module.exports = position_msg;
