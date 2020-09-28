;; Auto-generated. Do not edit!


(when (boundp 'project::gps_msg)
  (if (not (find-package "PROJECT"))
    (make-package "PROJECT"))
  (shadow 'gps_msg (find-package "PROJECT")))
(unless (find-package "PROJECT::GPS_MSG")
  (make-package "PROJECT::GPS_MSG"))

(in-package "ROS")
;;//! \htmlinclude gps_msg.msg.html


(defclass project::gps_msg
  :super ros::object
  :slots (_latitude _longitude _fix_code ))

(defmethod project::gps_msg
  (:init
   (&key
    ((:latitude __latitude) 0.0)
    ((:longitude __longitude) 0.0)
    ((:fix_code __fix_code) 0)
    )
   (send-super :init)
   (setq _latitude (float __latitude))
   (setq _longitude (float __longitude))
   (setq _fix_code (round __fix_code))
   self)
  (:latitude
   (&optional __latitude)
   (if __latitude (setq _latitude __latitude)) _latitude)
  (:longitude
   (&optional __longitude)
   (if __longitude (setq _longitude __longitude)) _longitude)
  (:fix_code
   (&optional __fix_code)
   (if __fix_code (setq _fix_code __fix_code)) _fix_code)
  (:serialization-length
   ()
   (+
    ;; float64 _latitude
    8
    ;; float64 _longitude
    8
    ;; int64 _fix_code
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _latitude
       (sys::poke _latitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _longitude
       (sys::poke _longitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; int64 _fix_code
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _fix_code (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _fix_code) (= (length (_fix_code . bv)) 2)) ;; bignum
              (write-long (ash (elt (_fix_code . bv) 0) 0) s)
              (write-long (ash (elt (_fix_code . bv) 1) -1) s))
             ((and (class _fix_code) (= (length (_fix_code . bv)) 1)) ;; big1
              (write-long (elt (_fix_code . bv) 0) s)
              (write-long (if (>= _fix_code 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _fix_code s)(write-long (if (>= _fix_code 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _latitude
     (setq _latitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _longitude
     (setq _longitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; int64 _fix_code
#+(or :alpha :irix6 :x86_64)
      (setf _fix_code (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _fix_code (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(setf (get project::gps_msg :md5sum-) "7ed9f98eb48746167a823b93c6cfb5ff")
(setf (get project::gps_msg :datatype-) "project/gps_msg")
(setf (get project::gps_msg :definition-)
      "float64 latitude
float64 longitude
int64 fix_code

")



(provide :project/gps_msg "7ed9f98eb48746167a823b93c6cfb5ff")


