;; Auto-generated. Do not edit!


(when (boundp 'project::deg_msg)
  (if (not (find-package "PROJECT"))
    (make-package "PROJECT"))
  (shadow 'deg_msg (find-package "PROJECT")))
(unless (find-package "PROJECT::DEG_MSG")
  (make-package "PROJECT::DEG_MSG"))

(in-package "ROS")
;;//! \htmlinclude deg_msg.msg.html


(defclass project::deg_msg
  :super ros::object
  :slots (_deg ))

(defmethod project::deg_msg
  (:init
   (&key
    ((:deg __deg) 0.0)
    )
   (send-super :init)
   (setq _deg (float __deg))
   self)
  (:deg
   (&optional __deg)
   (if __deg (setq _deg __deg)) _deg)
  (:serialization-length
   ()
   (+
    ;; float32 _deg
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _deg
       (sys::poke _deg (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _deg
     (setq _deg (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get project::deg_msg :md5sum-) "75960300fe371de17649c522b949ca85")
(setf (get project::deg_msg :datatype-) "project/deg_msg")
(setf (get project::deg_msg :definition-)
      "float32 deg

")



(provide :project/deg_msg "75960300fe371de17649c522b949ca85")


