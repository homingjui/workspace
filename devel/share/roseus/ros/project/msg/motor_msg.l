;; Auto-generated. Do not edit!


(when (boundp 'project::motor_msg)
  (if (not (find-package "PROJECT"))
    (make-package "PROJECT"))
  (shadow 'motor_msg (find-package "PROJECT")))
(unless (find-package "PROJECT::MOTOR_MSG")
  (make-package "PROJECT::MOTOR_MSG"))

(in-package "ROS")
;;//! \htmlinclude motor_msg.msg.html


(defclass project::motor_msg
  :super ros::object
  :slots (_way _speed _persent ))

(defmethod project::motor_msg
  (:init
   (&key
    ((:way __way) "")
    ((:speed __speed) 0)
    ((:persent __persent) 0.0)
    )
   (send-super :init)
   (setq _way (string __way))
   (setq _speed (round __speed))
   (setq _persent (float __persent))
   self)
  (:way
   (&optional __way)
   (if __way (setq _way __way)) _way)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:persent
   (&optional __persent)
   (if __persent (setq _persent __persent)) _persent)
  (:serialization-length
   ()
   (+
    ;; string _way
    4 (length _way)
    ;; int64 _speed
    8
    ;; float64 _persent
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _way
       (write-long (length _way) s) (princ _way s)
     ;; int64 _speed
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _speed (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _speed) (= (length (_speed . bv)) 2)) ;; bignum
              (write-long (ash (elt (_speed . bv) 0) 0) s)
              (write-long (ash (elt (_speed . bv) 1) -1) s))
             ((and (class _speed) (= (length (_speed . bv)) 1)) ;; big1
              (write-long (elt (_speed . bv) 0) s)
              (write-long (if (>= _speed 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _speed s)(write-long (if (>= _speed 0) 0 #xffffffff) s)))
     ;; float64 _persent
       (sys::poke _persent (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _way
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _way (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int64 _speed
#+(or :alpha :irix6 :x86_64)
      (setf _speed (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _speed (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; float64 _persent
     (setq _persent (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get project::motor_msg :md5sum-) "3535bdf16ad57a8f3e9a1b542ed91b5d")
(setf (get project::motor_msg :datatype-) "project/motor_msg")
(setf (get project::motor_msg :definition-)
      "string way
int64 speed
float64 persent

")



(provide :project/motor_msg "3535bdf16ad57a8f3e9a1b542ed91b5d")


