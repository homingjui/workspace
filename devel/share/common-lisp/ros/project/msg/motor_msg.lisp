; Auto-generated. Do not edit!


(cl:in-package project-msg)


;//! \htmlinclude motor_msg.msg.html

(cl:defclass <motor_msg> (roslisp-msg-protocol:ros-message)
  ((way
    :reader way
    :initarg :way
    :type cl:string
    :initform "")
   (speed
    :reader speed
    :initarg :speed
    :type cl:integer
    :initform 0)
   (persent
    :reader persent
    :initarg :persent
    :type cl:float
    :initform 0.0))
)

(cl:defclass motor_msg (<motor_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <motor_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'motor_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name project-msg:<motor_msg> is deprecated: use project-msg:motor_msg instead.")))

(cl:ensure-generic-function 'way-val :lambda-list '(m))
(cl:defmethod way-val ((m <motor_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:way-val is deprecated.  Use project-msg:way instead.")
  (way m))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <motor_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:speed-val is deprecated.  Use project-msg:speed instead.")
  (speed m))

(cl:ensure-generic-function 'persent-val :lambda-list '(m))
(cl:defmethod persent-val ((m <motor_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:persent-val is deprecated.  Use project-msg:persent instead.")
  (persent m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <motor_msg>) ostream)
  "Serializes a message object of type '<motor_msg>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'way))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'way))
  (cl:let* ((signed (cl:slot-value msg 'speed)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'persent))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <motor_msg>) istream)
  "Deserializes a message object of type '<motor_msg>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'way) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'way) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'speed) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'persent) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<motor_msg>)))
  "Returns string type for a message object of type '<motor_msg>"
  "project/motor_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'motor_msg)))
  "Returns string type for a message object of type 'motor_msg"
  "project/motor_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<motor_msg>)))
  "Returns md5sum for a message object of type '<motor_msg>"
  "3535bdf16ad57a8f3e9a1b542ed91b5d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'motor_msg)))
  "Returns md5sum for a message object of type 'motor_msg"
  "3535bdf16ad57a8f3e9a1b542ed91b5d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<motor_msg>)))
  "Returns full string definition for message of type '<motor_msg>"
  (cl:format cl:nil "string way~%int64 speed~%float64 persent~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'motor_msg)))
  "Returns full string definition for message of type 'motor_msg"
  (cl:format cl:nil "string way~%int64 speed~%float64 persent~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <motor_msg>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'way))
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <motor_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'motor_msg
    (cl:cons ':way (way msg))
    (cl:cons ':speed (speed msg))
    (cl:cons ':persent (persent msg))
))
