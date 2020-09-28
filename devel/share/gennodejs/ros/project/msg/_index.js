
"use strict";

let position_msg = require('./position_msg.js');
let gps_msg = require('./gps_msg.js');
let joystick_msg = require('./joystick_msg.js');
let arduino_msg = require('./arduino_msg.js');
let deg_msg = require('./deg_msg.js');
let motor_msg = require('./motor_msg.js');
let gyro_msg = require('./gyro_msg.js');

module.exports = {
  position_msg: position_msg,
  gps_msg: gps_msg,
  joystick_msg: joystick_msg,
  arduino_msg: arduino_msg,
  deg_msg: deg_msg,
  motor_msg: motor_msg,
  gyro_msg: gyro_msg,
};
