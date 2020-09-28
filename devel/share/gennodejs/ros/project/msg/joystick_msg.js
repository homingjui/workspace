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

class joystick_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.connect = null;
      this.leftX = null;
      this.leftY = null;
      this.rightX = null;
      this.rightY = null;
      this.leftTrg = null;
      this.rightTrg = null;
      this.A = null;
      this.B = null;
      this.X = null;
      this.Y = null;
      this.padUp = null;
      this.padDown = null;
      this.padLeft = null;
      this.padRight = null;
      this.bumperLeft = null;
      this.bumperRight = null;
      this.guide = null;
    }
    else {
      if (initObj.hasOwnProperty('connect')) {
        this.connect = initObj.connect
      }
      else {
        this.connect = false;
      }
      if (initObj.hasOwnProperty('leftX')) {
        this.leftX = initObj.leftX
      }
      else {
        this.leftX = 0.0;
      }
      if (initObj.hasOwnProperty('leftY')) {
        this.leftY = initObj.leftY
      }
      else {
        this.leftY = 0.0;
      }
      if (initObj.hasOwnProperty('rightX')) {
        this.rightX = initObj.rightX
      }
      else {
        this.rightX = 0.0;
      }
      if (initObj.hasOwnProperty('rightY')) {
        this.rightY = initObj.rightY
      }
      else {
        this.rightY = 0.0;
      }
      if (initObj.hasOwnProperty('leftTrg')) {
        this.leftTrg = initObj.leftTrg
      }
      else {
        this.leftTrg = 0.0;
      }
      if (initObj.hasOwnProperty('rightTrg')) {
        this.rightTrg = initObj.rightTrg
      }
      else {
        this.rightTrg = 0.0;
      }
      if (initObj.hasOwnProperty('A')) {
        this.A = initObj.A
      }
      else {
        this.A = false;
      }
      if (initObj.hasOwnProperty('B')) {
        this.B = initObj.B
      }
      else {
        this.B = false;
      }
      if (initObj.hasOwnProperty('X')) {
        this.X = initObj.X
      }
      else {
        this.X = false;
      }
      if (initObj.hasOwnProperty('Y')) {
        this.Y = initObj.Y
      }
      else {
        this.Y = false;
      }
      if (initObj.hasOwnProperty('padUp')) {
        this.padUp = initObj.padUp
      }
      else {
        this.padUp = false;
      }
      if (initObj.hasOwnProperty('padDown')) {
        this.padDown = initObj.padDown
      }
      else {
        this.padDown = false;
      }
      if (initObj.hasOwnProperty('padLeft')) {
        this.padLeft = initObj.padLeft
      }
      else {
        this.padLeft = false;
      }
      if (initObj.hasOwnProperty('padRight')) {
        this.padRight = initObj.padRight
      }
      else {
        this.padRight = false;
      }
      if (initObj.hasOwnProperty('bumperLeft')) {
        this.bumperLeft = initObj.bumperLeft
      }
      else {
        this.bumperLeft = false;
      }
      if (initObj.hasOwnProperty('bumperRight')) {
        this.bumperRight = initObj.bumperRight
      }
      else {
        this.bumperRight = false;
      }
      if (initObj.hasOwnProperty('guide')) {
        this.guide = initObj.guide
      }
      else {
        this.guide = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type joystick_msg
    // Serialize message field [connect]
    bufferOffset = _serializer.bool(obj.connect, buffer, bufferOffset);
    // Serialize message field [leftX]
    bufferOffset = _serializer.float32(obj.leftX, buffer, bufferOffset);
    // Serialize message field [leftY]
    bufferOffset = _serializer.float32(obj.leftY, buffer, bufferOffset);
    // Serialize message field [rightX]
    bufferOffset = _serializer.float32(obj.rightX, buffer, bufferOffset);
    // Serialize message field [rightY]
    bufferOffset = _serializer.float32(obj.rightY, buffer, bufferOffset);
    // Serialize message field [leftTrg]
    bufferOffset = _serializer.float32(obj.leftTrg, buffer, bufferOffset);
    // Serialize message field [rightTrg]
    bufferOffset = _serializer.float32(obj.rightTrg, buffer, bufferOffset);
    // Serialize message field [A]
    bufferOffset = _serializer.bool(obj.A, buffer, bufferOffset);
    // Serialize message field [B]
    bufferOffset = _serializer.bool(obj.B, buffer, bufferOffset);
    // Serialize message field [X]
    bufferOffset = _serializer.bool(obj.X, buffer, bufferOffset);
    // Serialize message field [Y]
    bufferOffset = _serializer.bool(obj.Y, buffer, bufferOffset);
    // Serialize message field [padUp]
    bufferOffset = _serializer.bool(obj.padUp, buffer, bufferOffset);
    // Serialize message field [padDown]
    bufferOffset = _serializer.bool(obj.padDown, buffer, bufferOffset);
    // Serialize message field [padLeft]
    bufferOffset = _serializer.bool(obj.padLeft, buffer, bufferOffset);
    // Serialize message field [padRight]
    bufferOffset = _serializer.bool(obj.padRight, buffer, bufferOffset);
    // Serialize message field [bumperLeft]
    bufferOffset = _serializer.bool(obj.bumperLeft, buffer, bufferOffset);
    // Serialize message field [bumperRight]
    bufferOffset = _serializer.bool(obj.bumperRight, buffer, bufferOffset);
    // Serialize message field [guide]
    bufferOffset = _serializer.bool(obj.guide, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type joystick_msg
    let len;
    let data = new joystick_msg(null);
    // Deserialize message field [connect]
    data.connect = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [leftX]
    data.leftX = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [leftY]
    data.leftY = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [rightX]
    data.rightX = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [rightY]
    data.rightY = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [leftTrg]
    data.leftTrg = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [rightTrg]
    data.rightTrg = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [A]
    data.A = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [B]
    data.B = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [X]
    data.X = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Y]
    data.Y = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [padUp]
    data.padUp = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [padDown]
    data.padDown = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [padLeft]
    data.padLeft = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [padRight]
    data.padRight = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [bumperLeft]
    data.bumperLeft = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [bumperRight]
    data.bumperRight = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [guide]
    data.guide = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 36;
  }

  static datatype() {
    // Returns string type for a message object
    return 'project/joystick_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'feedf0c4942de46502ada06975acd8c3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool connect
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new joystick_msg(null);
    if (msg.connect !== undefined) {
      resolved.connect = msg.connect;
    }
    else {
      resolved.connect = false
    }

    if (msg.leftX !== undefined) {
      resolved.leftX = msg.leftX;
    }
    else {
      resolved.leftX = 0.0
    }

    if (msg.leftY !== undefined) {
      resolved.leftY = msg.leftY;
    }
    else {
      resolved.leftY = 0.0
    }

    if (msg.rightX !== undefined) {
      resolved.rightX = msg.rightX;
    }
    else {
      resolved.rightX = 0.0
    }

    if (msg.rightY !== undefined) {
      resolved.rightY = msg.rightY;
    }
    else {
      resolved.rightY = 0.0
    }

    if (msg.leftTrg !== undefined) {
      resolved.leftTrg = msg.leftTrg;
    }
    else {
      resolved.leftTrg = 0.0
    }

    if (msg.rightTrg !== undefined) {
      resolved.rightTrg = msg.rightTrg;
    }
    else {
      resolved.rightTrg = 0.0
    }

    if (msg.A !== undefined) {
      resolved.A = msg.A;
    }
    else {
      resolved.A = false
    }

    if (msg.B !== undefined) {
      resolved.B = msg.B;
    }
    else {
      resolved.B = false
    }

    if (msg.X !== undefined) {
      resolved.X = msg.X;
    }
    else {
      resolved.X = false
    }

    if (msg.Y !== undefined) {
      resolved.Y = msg.Y;
    }
    else {
      resolved.Y = false
    }

    if (msg.padUp !== undefined) {
      resolved.padUp = msg.padUp;
    }
    else {
      resolved.padUp = false
    }

    if (msg.padDown !== undefined) {
      resolved.padDown = msg.padDown;
    }
    else {
      resolved.padDown = false
    }

    if (msg.padLeft !== undefined) {
      resolved.padLeft = msg.padLeft;
    }
    else {
      resolved.padLeft = false
    }

    if (msg.padRight !== undefined) {
      resolved.padRight = msg.padRight;
    }
    else {
      resolved.padRight = false
    }

    if (msg.bumperLeft !== undefined) {
      resolved.bumperLeft = msg.bumperLeft;
    }
    else {
      resolved.bumperLeft = false
    }

    if (msg.bumperRight !== undefined) {
      resolved.bumperRight = msg.bumperRight;
    }
    else {
      resolved.bumperRight = false
    }

    if (msg.guide !== undefined) {
      resolved.guide = msg.guide;
    }
    else {
      resolved.guide = false
    }

    return resolved;
    }
};

module.exports = joystick_msg;
