;; Auto-generated. Do not edit!


(when (boundp 'project::position_msg)
  (if (not (find-package "PROJECT"))
    (make-package "PROJECT"))
  (shadow 'position_msg (find-package "PROJECT")))
(unless (find-package "PROJECT::POSITION_MSG")
  (make-package "PROJECT::POSITION_MSG"))

(in-package "ROS")
;;//! \htmlinclude position_msg.msg.html


(defclass project::position_msg
  :super ros::object
  :slots (_path _now_x _now_y _next_dot _next_p _passing ))

(defmethod project::position_msg
  (:init
   (&key
    ((:path __path) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:now_x __now_x) 0.0)
    ((:now_y __now_y) 0.0)
    ((:next_dot __next_dot) 0)
    ((:next_p __next_p) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:passing __passing) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _path __path)
   (setq _now_x (float __now_x))
   (setq _now_y (float __now_y))
   (setq _next_dot (round __next_dot))
   (setq _next_p __next_p)
   (setq _passing __passing)
   self)
  (:path
   (&optional __path)
   (if __path (setq _path __path)) _path)
  (:now_x
   (&optional __now_x)
   (if __now_x (setq _now_x __now_x)) _now_x)
  (:now_y
   (&optional __now_y)
   (if __now_y (setq _now_y __now_y)) _now_y)
  (:next_dot
   (&optional __next_dot)
   (if __next_dot (setq _next_dot __next_dot)) _next_dot)
  (:next_p
   (&optional __next_p)
   (if __next_p (setq _next_p __next_p)) _next_p)
  (:passing
   (&optional __passing)
   (if __passing (setq _passing __passing)) _passing)
  (:serialization-length
   ()
   (+
    ;; float64[] _path
    (* 8    (length _path)) 4
    ;; float64 _now_x
    8
    ;; float64 _now_y
    8
    ;; int64 _next_dot
    8
    ;; float64[] _next_p
    (* 8    (length _next_p)) 4
    ;; float64[] _passing
    (* 8    (length _passing)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[] _path
     (write-long (length _path) s)
     (dotimes (i (length _path))
       (sys::poke (elt _path i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64 _now_x
       (sys::poke _now_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _now_y
       (sys::poke _now_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; int64 _next_dot
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _next_dot (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _next_dot) (= (length (_next_dot . bv)) 2)) ;; bignum
              (write-long (ash (elt (_next_dot . bv) 0) 0) s)
              (write-long (ash (elt (_next_dot . bv) 1) -1) s))
             ((and (class _next_dot) (= (length (_next_dot . bv)) 1)) ;; big1
              (write-long (elt (_next_dot . bv) 0) s)
              (write-long (if (>= _next_dot 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _next_dot s)(write-long (if (>= _next_dot 0) 0 #xffffffff) s)))
     ;; float64[] _next_p
     (write-long (length _next_p) s)
     (dotimes (i (length _next_p))
       (sys::poke (elt _next_p i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _passing
     (write-long (length _passing) s)
     (dotimes (i (length _passing))
       (sys::poke (elt _passing i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[] _path
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _path (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _path i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64 _now_x
     (setq _now_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _now_y
     (setq _now_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; int64 _next_dot
#+(or :alpha :irix6 :x86_64)
      (setf _next_dot (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _next_dot (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; float64[] _next_p
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _next_p (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _next_p i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _passing
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _passing (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _passing i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(setf (get project::position_msg :md5sum-) "8c8333feeb19f29f3015ed8ba27f62fc")
(setf (get project::position_msg :datatype-) "project/position_msg")
(setf (get project::position_msg :definition-)
      "float64[] path
float64 now_x
float64 now_y
int64 next_dot
float64[] next_p
float64[] passing

")



(provide :project/position_msg "8c8333feeb19f29f3015ed8ba27f62fc")


