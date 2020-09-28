; Auto-generated. Do not edit!


(cl:in-package project-msg)


;//! \htmlinclude joystick.msg.html

(cl:defclass <joystick> (roslisp-msg-protocol:ros-message)
  ((connect
    :reader connect
    :initarg :connect
    :type cl:boolean
    :initform cl:nil)
   (leftX
    :reader leftX
    :initarg :leftX
    :type cl:float
    :initform 0.0)
   (leftR
    :reader leftR
    :initarg :leftR
    :type cl:float
    :initform 0.0)
   (rightX
    :reader rightX
    :initarg :rightX
    :type cl:float
    :initform 0.0)
   (rightY
    :reader rightY
    :initarg :rightY
    :type cl:float
    :initform 0.0)
   (leftTrg
    :reader leftTrg
    :initarg :leftTrg
    :type cl:float
    :initform 0.0)
   (rightTrg
    :reader rightTrg
    :initarg :rightTrg
    :type cl:float
    :initform 0.0)
   (A
    :reader A
    :initarg :A
    :type cl:boolean
    :initform cl:nil)
   (B
    :reader B
    :initarg :B
    :type cl:boolean
    :initform cl:nil)
   (X
    :reader X
    :initarg :X
    :type cl:boolean
    :initform cl:nil)
   (Y
    :reader Y
    :initarg :Y
    :type cl:boolean
    :initform cl:nil)
   (padUp
    :reader padUp
    :initarg :padUp
    :type cl:boolean
    :initform cl:nil)
   (padDown
    :reader padDown
    :initarg :padDown
    :type cl:boolean
    :initform cl:nil)
   (padLeft
    :reader padLeft
    :initarg :padLeft
    :type cl:boolean
    :initform cl:nil)
   (padRight
    :reader padRight
    :initarg :padRight
    :type cl:boolean
    :initform cl:nil)
   (bumperLeft
    :reader bumperLeft
    :initarg :bumperLeft
    :type cl:boolean
    :initform cl:nil)
   (bumperRight
    :reader bumperRight
    :initarg :bumperRight
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass joystick (<joystick>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <joystick>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'joystick)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name project-msg:<joystick> is deprecated: use project-msg:joystick instead.")))

(cl:ensure-generic-function 'connect-val :lambda-list '(m))
(cl:defmethod connect-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:connect-val is deprecated.  Use project-msg:connect instead.")
  (connect m))

(cl:ensure-generic-function 'leftX-val :lambda-list '(m))
(cl:defmethod leftX-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:leftX-val is deprecated.  Use project-msg:leftX instead.")
  (leftX m))

(cl:ensure-generic-function 'leftR-val :lambda-list '(m))
(cl:defmethod leftR-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:leftR-val is deprecated.  Use project-msg:leftR instead.")
  (leftR m))

(cl:ensure-generic-function 'rightX-val :lambda-list '(m))
(cl:defmethod rightX-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:rightX-val is deprecated.  Use project-msg:rightX instead.")
  (rightX m))

(cl:ensure-generic-function 'rightY-val :lambda-list '(m))
(cl:defmethod rightY-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:rightY-val is deprecated.  Use project-msg:rightY instead.")
  (rightY m))

(cl:ensure-generic-function 'leftTrg-val :lambda-list '(m))
(cl:defmethod leftTrg-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:leftTrg-val is deprecated.  Use project-msg:leftTrg instead.")
  (leftTrg m))

(cl:ensure-generic-function 'rightTrg-val :lambda-list '(m))
(cl:defmethod rightTrg-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:rightTrg-val is deprecated.  Use project-msg:rightTrg instead.")
  (rightTrg m))

(cl:ensure-generic-function 'A-val :lambda-list '(m))
(cl:defmethod A-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:A-val is deprecated.  Use project-msg:A instead.")
  (A m))

(cl:ensure-generic-function 'B-val :lambda-list '(m))
(cl:defmethod B-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:B-val is deprecated.  Use project-msg:B instead.")
  (B m))

(cl:ensure-generic-function 'X-val :lambda-list '(m))
(cl:defmethod X-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:X-val is deprecated.  Use project-msg:X instead.")
  (X m))

(cl:ensure-generic-function 'Y-val :lambda-list '(m))
(cl:defmethod Y-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:Y-val is deprecated.  Use project-msg:Y instead.")
  (Y m))

(cl:ensure-generic-function 'padUp-val :lambda-list '(m))
(cl:defmethod padUp-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:padUp-val is deprecated.  Use project-msg:padUp instead.")
  (padUp m))

(cl:ensure-generic-function 'padDown-val :lambda-list '(m))
(cl:defmethod padDown-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:padDown-val is deprecated.  Use project-msg:padDown instead.")
  (padDown m))

(cl:ensure-generic-function 'padLeft-val :lambda-list '(m))
(cl:defmethod padLeft-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:padLeft-val is deprecated.  Use project-msg:padLeft instead.")
  (padLeft m))

(cl:ensure-generic-function 'padRight-val :lambda-list '(m))
(cl:defmethod padRight-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:padRight-val is deprecated.  Use project-msg:padRight instead.")
  (padRight m))

(cl:ensure-generic-function 'bumperLeft-val :lambda-list '(m))
(cl:defmethod bumperLeft-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:bumperLeft-val is deprecated.  Use project-msg:bumperLeft instead.")
  (bumperLeft m))

(cl:ensure-generic-function 'bumperRight-val :lambda-list '(m))
(cl:defmethod bumperRight-val ((m <joystick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project-msg:bumperRight-val is deprecated.  Use project-msg:bumperRight instead.")
  (bumperRight m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <joystick>) ostream)
  "Serializes a message object of type '<joystick>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'connect) 1 0)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'leftX))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'leftR))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'rightX))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'rightY))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'leftTrg))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'rightTrg))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'A) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'B) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'X) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Y) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'padUp) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'padDown) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'padLeft) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'padRight) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'bumperLeft) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'bumperRight) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <joystick>) istream)
  "Deserializes a message object of type '<joystick>"
    (cl:setf (cl:slot-value msg 'connect) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'leftX) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'leftR) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'rightX) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'rightY) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'leftTrg) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'rightTrg) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'A) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'B) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'X) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Y) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'padUp) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'padDown) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'padLeft) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'padRight) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'bumperLeft) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'bumperRight) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<joystick>)))
  "Returns string type for a message object of type '<joystick>"
  "project/joystick")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'joystick)))
  "Returns string type for a message object of type 'joystick"
  "project/joystick")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<joystick>)))
  "Returns md5sum for a message object of type '<joystick>"
  "666d003c179026e1a217a6c7a3916503")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'joystick)))
  "Returns md5sum for a message object of type 'joystick"
  "666d003c179026e1a217a6c7a3916503")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<joystick>)))
  "Returns full string definition for message of type '<joystick>"
  (cl:format cl:nil "bool connect~%float32 leftX~%float32 leftR~%float32 rightX~%float32 rightY~%float32 leftTrg~%float32 rightTrg~%bool A~%bool B~%bool X~%bool Y~%bool padUp~%bool padDown~%bool padLeft~%bool padRight~%bool bumperLeft~%bool bumperRight~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'joystick)))
  "Returns full string definition for message of type 'joystick"
  (cl:format cl:nil "bool connect~%float32 leftX~%float32 leftR~%float32 rightX~%float32 rightY~%float32 leftTrg~%float32 rightTrg~%bool A~%bool B~%bool X~%bool Y~%bool padUp~%bool padDown~%bool padLeft~%bool padRight~%bool bumperLeft~%bool bumperRight~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <joystick>))
  (cl:+ 0
     1
     4
     4
     4
     4
     4
     4
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <joystick>))
  "Converts a ROS message object to a list"
  (cl:list 'joystick
    (cl:cons ':connect (connect msg))
    (cl:cons ':leftX (leftX msg))
    (cl:cons ':leftR (leftR msg))
    (cl:cons ':rightX (rightX msg))
    (cl:cons ':rightY (rightY msg))
    (cl:cons ':leftTrg (leftTrg msg))
    (cl:cons ':rightTrg (rightTrg msg))
    (cl:cons ':A (A msg))
    (cl:cons ':B (B msg))
    (cl:cons ':X (X msg))
    (cl:cons ':Y (Y msg))
    (cl:cons ':padUp (padUp msg))
    (cl:cons ':padDown (padDown msg))
    (cl:cons ':padLeft (padLeft msg))
    (cl:cons ':padRight (padRight msg))
    (cl:cons ':bumperLeft (bumperLeft msg))
    (cl:cons ':bumperRight (bumperRight msg))
))
