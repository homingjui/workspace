;; Auto-generated. Do not edit!


(when (boundp 'project::arduino_msg)
  (if (not (find-package "PROJECT"))
    (make-package "PROJECT"))
  (shadow 'arduino_msg (find-package "PROJECT")))
(unless (find-package "PROJECT::ARDUINO_MSG")
  (make-package "PROJECT::ARDUINO_MSG"))

(in-package "ROS")
;;//! \htmlinclude arduino_msg.msg.html


(defclass project::arduino_msg
  :super ros::object
  :slots (_voltage _gyroX _gyroY _gyroZ _accX _accY _accZ _roll _pitch _yaw ))

(defmethod project::arduino_msg
  (:init
   (&key
    ((:voltage __voltage) 0.0)
    ((:gyroX __gyroX) 0.0)
    ((:gyroY __gyroY) 0.0)
    ((:gyroZ __gyroZ) 0.0)
    ((:accX __accX) 0.0)
    ((:accY __accY) 0.0)
    ((:accZ __accZ) 0.0)
    ((:roll __roll) 0.0)
    ((:pitch __pitch) 0.0)
    ((:yaw __yaw) 0.0)
    )
   (send-super :init)
   (setq _voltage (float __voltage))
   (setq _gyroX (float __gyroX))
   (setq _gyroY (float __gyroY))
   (setq _gyroZ (float __gyroZ))
   (setq _accX (float __accX))
   (setq _accY (float __accY))
   (setq _accZ (float __accZ))
   (setq _roll (float __roll))
   (setq _pitch (float __pitch))
   (setq _yaw (float __yaw))
   self)
  (:voltage
   (&optional __voltage)
   (if __voltage (setq _voltage __voltage)) _voltage)
  (:gyroX
   (&optional __gyroX)
   (if __gyroX (setq _gyroX __gyroX)) _gyroX)
  (:gyroY
   (&optional __gyroY)
   (if __gyroY (setq _gyroY __gyroY)) _gyroY)
  (:gyroZ
   (&optional __gyroZ)
   (if __gyroZ (setq _gyroZ __gyroZ)) _gyroZ)
  (:accX
   (&optional __accX)
   (if __accX (setq _accX __accX)) _accX)
  (:accY
   (&optional __accY)
   (if __accY (setq _accY __accY)) _accY)
  (:accZ
   (&optional __accZ)
   (if __accZ (setq _accZ __accZ)) _accZ)
  (:roll
   (&optional __roll)
   (if __roll (setq _roll __roll)) _roll)
  (:pitch
   (&optional __pitch)
   (if __pitch (setq _pitch __pitch)) _pitch)
  (:yaw
   (&optional __yaw)
   (if __yaw (setq _yaw __yaw)) _yaw)
  (:serialization-length
   ()
   (+
    ;; float32 _voltage
    4
    ;; float32 _gyroX
    4
    ;; float32 _gyroY
    4
    ;; float32 _gyroZ
    4
    ;; float32 _accX
    4
    ;; float32 _accY
    4
    ;; float32 _accZ
    4
    ;; float32 _roll
    4
    ;; float32 _pitch
    4
    ;; float32 _yaw
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _voltage
       (sys::poke _voltage (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _gyroX
       (sys::poke _gyroX (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _gyroY
       (sys::poke _gyroY (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _gyroZ
       (sys::poke _gyroZ (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _accX
       (sys::poke _accX (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _accY
       (sys::poke _accY (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _accZ
       (sys::poke _accZ (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _roll
       (sys::poke _roll (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _pitch
       (sys::poke _pitch (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _yaw
       (sys::poke _yaw (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _voltage
     (setq _voltage (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _gyroX
     (setq _gyroX (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _gyroY
     (setq _gyroY (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _gyroZ
     (setq _gyroZ (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _accX
     (setq _accX (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _accY
     (setq _accY (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _accZ
     (setq _accZ (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _roll
     (setq _roll (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _pitch
     (setq _pitch (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _yaw
     (setq _yaw (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get project::arduino_msg :md5sum-) "6147ba7bc1e9a27ffeb41686ce827cfa")
(setf (get project::arduino_msg :datatype-) "project/arduino_msg")
(setf (get project::arduino_msg :definition-)
      "float32 voltage
float32 gyroX
float32 gyroY
float32 gyroZ
float32 accX
float32 accY
float32 accZ
float32 roll
float32 pitch
float32 yaw

")



(provide :project/arduino_msg "6147ba7bc1e9a27ffeb41686ce827cfa")


