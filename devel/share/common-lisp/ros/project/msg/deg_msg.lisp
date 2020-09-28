; Auto-generated. Do not edit!


(cl:in-package project-msg)


;//! \htmlinclude deg_msg.msg.html

(cl:defclass <deg_msg> (roslisp-msg-protocol:ros-message)
  ((deg
    :reader deg
    :initarg :deg
    :type cl:float
    :initform 0.0))
)

(cl:defclass deg_msg (<deg_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <deg_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'deg_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name project-msg:<deg_msg> is deprecated: use project-msg:deg_msg instead.")))

(cl:ensure-generic-function 'deg-val :lambda-list '(m))
(cl:defmethod deg-val ((m <deg_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:deg-val is deprecated.  Use project-msg:deg instead.")
  (deg m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <deg_msg>) ostream)
  "Serializes a message object of type '<deg_msg>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'deg))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <deg_msg>) istream)
  "Deserializes a message object of type '<deg_msg>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'deg) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<deg_msg>)))
  "Returns string type for a message object of type '<deg_msg>"
  "project/deg_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'deg_msg)))
  "Returns string type for a message object of type 'deg_msg"
  "project/deg_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<deg_msg>)))
  "Returns md5sum for a message object of type '<deg_msg>"
  "75960300fe371de17649c522b949ca85")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'deg_msg)))
  "Returns md5sum for a message object of type 'deg_msg"
  "75960300fe371de17649c522b949ca85")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<deg_msg>)))
  "Returns full string definition for message of type '<deg_msg>"
  (cl:format cl:nil "float32 deg~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'deg_msg)))
  "Returns full string definition for message of type 'deg_msg"
  (cl:format cl:nil "float32 deg~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <deg_msg>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <deg_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'deg_msg
    (cl:cons ':deg (deg msg))
))
