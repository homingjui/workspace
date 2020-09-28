;; Auto-generated. Do not edit!


(when (boundp 'project::gyro_msg)
  (if (not (find-package "PROJECT"))
    (make-package "PROJECT"))
  (shadow 'gyro_msg (find-package "PROJECT")))
(unless (find-package "PROJECT::GYRO_MSG")
  (make-package "PROJECT::GYRO_MSG"))

(in-package "ROS")
;;//! \htmlinclude gyro_msg.msg.html


(defclass project::gyro_msg
  :super ros::object
  :slots (_acc_x _acc_y _acc_z _gyro_x _gyro_y _gyro_z _angle_x _angle_y _angle_z ))

(defmethod project::gyro_msg
  (:init
   (&key
    ((:acc_x __acc_x) 0.0)
    ((:acc_y __acc_y) 0.0)
    ((:acc_z __acc_z) 0.0)
    ((:gyro_x __gyro_x) 0.0)
    ((:gyro_y __gyro_y) 0.0)
    ((:gyro_z __gyro_z) 0.0)
    ((:angle_x __angle_x) 0.0)
    ((:angle_y __angle_y) 0.0)
    ((:angle_z __angle_z) 0.0)
    )
   (send-super :init)
   (setq _acc_x (float __acc_x))
   (setq _acc_y (float __acc_y))
   (setq _acc_z (float __acc_z))
   (setq _gyro_x (float __gyro_x))
   (setq _gyro_y (float __gyro_y))
   (setq _gyro_z (float __gyro_z))
   (setq _angle_x (float __angle_x))
   (setq _angle_y (float __angle_y))
   (setq _angle_z (float __angle_z))
   self)
  (:acc_x
   (&optional __acc_x)
   (if __acc_x (setq _acc_x __acc_x)) _acc_x)
  (:acc_y
   (&optional __acc_y)
   (if __acc_y (setq _acc_y __acc_y)) _acc_y)
  (:acc_z
   (&optional __acc_z)
   (if __acc_z (setq _acc_z __acc_z)) _acc_z)
  (:gyro_x
   (&optional __gyro_x)
   (if __gyro_x (setq _gyro_x __gyro_x)) _gyro_x)
  (:gyro_y
   (&optional __gyro_y)
   (if __gyro_y (setq _gyro_y __gyro_y)) _gyro_y)
  (:gyro_z
   (&optional __gyro_z)
   (if __gyro_z (setq _gyro_z __gyro_z)) _gyro_z)
  (:angle_x
   (&optional __angle_x)
   (if __angle_x (setq _angle_x __angle_x)) _angle_x)
  (:angle_y
   (&optional __angle_y)
   (if __angle_y (setq _angle_y __angle_y)) _angle_y)
  (:angle_z
   (&optional __angle_z)
   (if __angle_z (setq _angle_z __angle_z)) _angle_z)
  (:serialization-length
   ()
   (+
    ;; float32 _acc_x
    4
    ;; float32 _acc_y
    4
    ;; float32 _acc_z
    4
    ;; float32 _gyro_x
    4
    ;; float32 _gyro_y
    4
    ;; float32 _gyro_z
    4
    ;; float32 _angle_x
    4
    ;; float32 _angle_y
    4
    ;; float32 _angle_z
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _acc_x
       (sys::poke _acc_x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _acc_y
       (sys::poke _acc_y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _acc_z
       (sys::poke _acc_z (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _gyro_x
       (sys::poke _gyro_x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _gyro_y
       (sys::poke _gyro_y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _gyro_z
       (sys::poke _gyro_z (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _angle_x
       (sys::poke _angle_x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _angle_y
       (sys::poke _angle_y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _angle_z
       (sys::poke _angle_z (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _acc_x
     (setq _acc_x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _acc_y
     (setq _acc_y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _acc_z
     (setq _acc_z (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _gyro_x
     (setq _gyro_x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _gyro_y
     (setq _gyro_y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _gyro_z
     (setq _gyro_z (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _angle_x
     (setq _angle_x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _angle_y
     (setq _angle_y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _angle_z
     (setq _angle_z (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get project::gyro_msg :md5sum-) "3826aa65725fd705677ace711a262484")
(setf (get project::gyro_msg :datatype-) "project/gyro_msg")
(setf (get project::gyro_msg :definition-)
      "float32 acc_x
float32 acc_y
float32 acc_z
float32 gyro_x
float32 gyro_y
float32 gyro_z
float32 angle_x
float32 angle_y
float32 angle_z

")



(provide :project/gyro_msg "3826aa65725fd705677ace711a262484")


