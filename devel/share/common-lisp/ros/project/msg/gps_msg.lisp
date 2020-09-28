; Auto-generated. Do not edit!


(cl:in-package project-msg)


;//! \htmlinclude gps_msg.msg.html

(cl:defclass <gps_msg> (roslisp-msg-protocol:ros-message)
  ((latitude
    :reader latitude
    :initarg :latitude
    :type cl:float
    :initform 0.0)
   (longitude
    :reader longitude
    :initarg :longitude
    :type cl:float
    :initform 0.0)
   (fix_code
    :reader fix_code
    :initarg :fix_code
    :type cl:integer
    :initform 0))
)

(cl:defclass gps_msg (<gps_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <gps_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'gps_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name project-msg:<gps_msg> is deprecated: use project-msg:gps_msg instead.")))

(cl:ensure-generic-function 'latitude-val :lambda-list '(m))
(cl:defmethod latitude-val ((m <gps_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:latitude-val is deprecated.  Use project-msg:latitude instead.")
  (latitude m))

(cl:ensure-generic-function 'longitude-val :lambda-list '(m))
(cl:defmethod longitude-val ((m <gps_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:longitude-val is deprecated.  Use project-msg:longitude instead.")
  (longitude m))

(cl:ensure-generic-function 'fix_code-val :lambda-list '(m))
(cl:defmethod fix_code-val ((m <gps_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:fix_code-val is deprecated.  Use project-msg:fix_code instead.")
  (fix_code m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <gps_msg>) ostream)
  "Serializes a message object of type '<gps_msg>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'latitude))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'longitude))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'fix_code)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <gps_msg>) istream)
  "Deserializes a message object of type '<gps_msg>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'latitude) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'longitude) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'fix_code) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<gps_msg>)))
  "Returns string type for a message object of type '<gps_msg>"
  "project/gps_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'gps_msg)))
  "Returns string type for a message object of type 'gps_msg"
  "project/gps_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<gps_msg>)))
  "Returns md5sum for a message object of type '<gps_msg>"
  "7ed9f98eb48746167a823b93c6cfb5ff")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'gps_msg)))
  "Returns md5sum for a message object of type 'gps_msg"
  "7ed9f98eb48746167a823b93c6cfb5ff")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<gps_msg>)))
  "Returns full string definition for message of type '<gps_msg>"
  (cl:format cl:nil "float64 latitude~%float64 longitude~%int64 fix_code~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'gps_msg)))
  "Returns full string definition for message of type 'gps_msg"
  (cl:format cl:nil "float64 latitude~%float64 longitude~%int64 fix_code~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <gps_msg>))
  (cl:+ 0
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <gps_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'gps_msg
    (cl:cons ':latitude (latitude msg))
    (cl:cons ':longitude (longitude msg))
    (cl:cons ':fix_code (fix_code msg))
))
