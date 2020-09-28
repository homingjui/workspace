; Auto-generated. Do not edit!


(cl:in-package project-msg)


;//! \htmlinclude arduino_msg.msg.html

(cl:defclass <arduino_msg> (roslisp-msg-protocol:ros-message)
  ((voltage
    :reader voltage
    :initarg :voltage
    :type cl:float
    :initform 0.0)
   (gyroX
    :reader gyroX
    :initarg :gyroX
    :type cl:float
    :initform 0.0)
   (gyroY
    :reader gyroY
    :initarg :gyroY
    :type cl:float
    :initform 0.0)
   (gyroZ
    :reader gyroZ
    :initarg :gyroZ
    :type cl:float
    :initform 0.0)
   (accX
    :reader accX
    :initarg :accX
    :type cl:float
    :initform 0.0)
   (accY
    :reader accY
    :initarg :accY
    :type cl:float
    :initform 0.0)
   (accZ
    :reader accZ
    :initarg :accZ
    :type cl:float
    :initform 0.0)
   (roll
    :reader roll
    :initarg :roll
    :type cl:float
    :initform 0.0)
   (pitch
    :reader pitch
    :initarg :pitch
    :type cl:float
    :initform 0.0)
   (yaw
    :reader yaw
    :initarg :yaw
    :type cl:float
    :initform 0.0))
)

(cl:defclass arduino_msg (<arduino_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <arduino_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'arduino_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name project-msg:<arduino_msg> is deprecated: use project-msg:arduino_msg instead.")))

(cl:ensure-generic-function 'voltage-val :lambda-list '(m))
(cl:defmethod voltage-val ((m <arduino_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:voltage-val is deprecated.  Use project-msg:voltage instead.")
  (voltage m))

(cl:ensure-generic-function 'gyroX-val :lambda-list '(m))
(cl:defmethod gyroX-val ((m <arduino_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:gyroX-val is deprecated.  Use project-msg:gyroX instead.")
  (gyroX m))

(cl:ensure-generic-function 'gyroY-val :lambda-list '(m))
(cl:defmethod gyroY-val ((m <arduino_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:gyroY-val is deprecated.  Use project-msg:gyroY instead.")
  (gyroY m))

(cl:ensure-generic-function 'gyroZ-val :lambda-list '(m))
(cl:defmethod gyroZ-val ((m <arduino_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:gyroZ-val is deprecated.  Use project-msg:gyroZ instead.")
  (gyroZ m))

(cl:ensure-generic-function 'accX-val :lambda-list '(m))
(cl:defmethod accX-val ((m <arduino_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:accX-val is deprecated.  Use project-msg:accX instead.")
  (accX m))

(cl:ensure-generic-function 'accY-val :lambda-list '(m))
(cl:defmethod accY-val ((m <arduino_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:accY-val is deprecated.  Use project-msg:accY instead.")
  (accY m))

(cl:ensure-generic-function 'accZ-val :lambda-list '(m))
(cl:defmethod accZ-val ((m <arduino_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:accZ-val is deprecated.  Use project-msg:accZ instead.")
  (accZ m))

(cl:ensure-generic-function 'roll-val :lambda-list '(m))
(cl:defmethod roll-val ((m <arduino_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:roll-val is deprecated.  Use project-msg:roll instead.")
  (roll m))

(cl:ensure-generic-function 'pitch-val :lambda-list '(m))
(cl:defmethod pitch-val ((m <arduino_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:pitch-val is deprecated.  Use project-msg:pitch instead.")
  (pitch m))

(cl:ensure-generic-function 'yaw-val :lambda-list '(m))
(cl:defmethod yaw-val ((m <arduino_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:yaw-val is deprecated.  Use project-msg:yaw instead.")
  (yaw m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <arduino_msg>) ostream)
  "Serializes a message object of type '<arduino_msg>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'voltage))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'gyroX))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'gyroY))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'gyroZ))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'accX))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'accY))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'accZ))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'roll))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'pitch))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'yaw))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <arduino_msg>) istream)
  "Deserializes a message object of type '<arduino_msg>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'voltage) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'gyroX) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'gyroY) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'gyroZ) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'accX) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'accY) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'accZ) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'roll) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pitch) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'yaw) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<arduino_msg>)))
  "Returns string type for a message object of type '<arduino_msg>"
  "project/arduino_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'arduino_msg)))
  "Returns string type for a message object of type 'arduino_msg"
  "project/arduino_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<arduino_msg>)))
  "Returns md5sum for a message object of type '<arduino_msg>"
  "6147ba7bc1e9a27ffeb41686ce827cfa")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'arduino_msg)))
  "Returns md5sum for a message object of type 'arduino_msg"
  "6147ba7bc1e9a27ffeb41686ce827cfa")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<arduino_msg>)))
  "Returns full string definition for message of type '<arduino_msg>"
  (cl:format cl:nil "float32 voltage~%float32 gyroX~%float32 gyroY~%float32 gyroZ~%float32 accX~%float32 accY~%float32 accZ~%float32 roll~%float32 pitch~%float32 yaw~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'arduino_msg)))
  "Returns full string definition for message of type 'arduino_msg"
  (cl:format cl:nil "float32 voltage~%float32 gyroX~%float32 gyroY~%float32 gyroZ~%float32 accX~%float32 accY~%float32 accZ~%float32 roll~%float32 pitch~%float32 yaw~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <arduino_msg>))
  (cl:+ 0
     4
     4
     4
     4
     4
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <arduino_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'arduino_msg
    (cl:cons ':voltage (voltage msg))
    (cl:cons ':gyroX (gyroX msg))
    (cl:cons ':gyroY (gyroY msg))
    (cl:cons ':gyroZ (gyroZ msg))
    (cl:cons ':accX (accX msg))
    (cl:cons ':accY (accY msg))
    (cl:cons ':accZ (accZ msg))
    (cl:cons ':roll (roll msg))
    (cl:cons ':pitch (pitch msg))
    (cl:cons ':yaw (yaw msg))
))
