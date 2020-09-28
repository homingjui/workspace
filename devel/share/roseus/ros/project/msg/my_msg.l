;; Auto-generated. Do not edit!


(when (boundp 'project::my_msg)
  (if (not (find-package "PROJECT"))
    (make-package "PROJECT"))
  (shadow 'my_msg (find-package "PROJECT")))
(unless (find-package "PROJECT::MY_MSG")
  (make-package "PROJECT::MY_MSG"))

(in-package "ROS")
;;//! \htmlinclude my_msg.msg.html


(defclass project::my_msg
  :super ros::object
  :slots (_connect _leftX _leftR _rightX _rightY _leftTrg _rightTrg _A _B _X _Y _padUp _padDown _padLeft _padRight _bumperLeft _bumperRight ))

(defmethod project::my_msg
  (:init
   (&key
    ((:connect __connect) nil)
    ((:leftX __leftX) 0.0)
    ((:leftR __leftR) 0.0)
    ((:rightX __rightX) 0.0)
    ((:rightY __rightY) 0.0)
    ((:leftTrg __leftTrg) 0.0)
    ((:rightTrg __rightTrg) 0.0)
    ((:A __A) nil)
    ((:B __B) nil)
    ((:X __X) nil)
    ((:Y __Y) nil)
    ((:padUp __padUp) nil)
    ((:padDown __padDown) nil)
    ((:padLeft __padLeft) nil)
    ((:padRight __padRight) nil)
    ((:bumperLeft __bumperLeft) nil)
    ((:bumperRight __bumperRight) nil)
    )
   (send-super :init)
   (setq _connect __connect)
   (setq _leftX (float __leftX))
   (setq _leftR (float __leftR))
   (setq _rightX (float __rightX))
   (setq _rightY (float __rightY))
   (setq _leftTrg (float __leftTrg))
   (setq _rightTrg (float __rightTrg))
   (setq _A __A)
   (setq _B __B)
   (setq _X __X)
   (setq _Y __Y)
   (setq _padUp __padUp)
   (setq _padDown __padDown)
   (setq _padLeft __padLeft)
   (setq _padRight __padRight)
   (setq _bumperLeft __bumperLeft)
   (setq _bumperRight __bumperRight)
   self)
  (:connect
   (&optional __connect)
   (if __connect (setq _connect __connect)) _connect)
  (:leftX
   (&optional __leftX)
   (if __leftX (setq _leftX __leftX)) _leftX)
  (:leftR
   (&optional __leftR)
   (if __leftR (setq _leftR __leftR)) _leftR)
  (:rightX
   (&optional __rightX)
   (if __rightX (setq _rightX __rightX)) _rightX)
  (:rightY
   (&optional __rightY)
   (if __rightY (setq _rightY __rightY)) _rightY)
  (:leftTrg
   (&optional __leftTrg)
   (if __leftTrg (setq _leftTrg __leftTrg)) _leftTrg)
  (:rightTrg
   (&optional __rightTrg)
   (if __rightTrg (setq _rightTrg __rightTrg)) _rightTrg)
  (:A
   (&optional __A)
   (if __A (setq _A __A)) _A)
  (:B
   (&optional __B)
   (if __B (setq _B __B)) _B)
  (:X
   (&optional __X)
   (if __X (setq _X __X)) _X)
  (:Y
   (&optional __Y)
   (if __Y (setq _Y __Y)) _Y)
  (:padUp
   (&optional __padUp)
   (if __padUp (setq _padUp __padUp)) _padUp)
  (:padDown
   (&optional __padDown)
   (if __padDown (setq _padDown __padDown)) _padDown)
  (:padLeft
   (&optional __padLeft)
   (if __padLeft (setq _padLeft __padLeft)) _padLeft)
  (:padRight
   (&optional __padRight)
   (if __padRight (setq _padRight __padRight)) _padRight)
  (:bumperLeft
   (&optional __bumperLeft)
   (if __bumperLeft (setq _bumperLeft __bumperLeft)) _bumperLeft)
  (:bumperRight
   (&optional __bumperRight)
   (if __bumperRight (setq _bumperRight __bumperRight)) _bumperRight)
  (:serialization-length
   ()
   (+
    ;; bool _connect
    1
    ;; float32 _leftX
    4
    ;; float32 _leftR
    4
    ;; float32 _rightX
    4
    ;; float32 _rightY
    4
    ;; float32 _leftTrg
    4
    ;; float32 _rightTrg
    4
    ;; bool _A
    1
    ;; bool _B
    1
    ;; bool _X
    1
    ;; bool _Y
    1
    ;; bool _padUp
    1
    ;; bool _padDown
    1
    ;; bool _padLeft
    1
    ;; bool _padRight
    1
    ;; bool _bumperLeft
    1
    ;; bool _bumperRight
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _connect
       (if _connect (write-byte -1 s) (write-byte 0 s))
     ;; float32 _leftX
       (sys::poke _leftX (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _leftR
       (sys::poke _leftR (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _rightX
       (sys::poke _rightX (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _rightY
       (sys::poke _rightY (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _leftTrg
       (sys::poke _leftTrg (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _rightTrg
       (sys::poke _rightTrg (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _A
       (if _A (write-byte -1 s) (write-byte 0 s))
     ;; bool _B
       (if _B (write-byte -1 s) (write-byte 0 s))
     ;; bool _X
       (if _X (write-byte -1 s) (write-byte 0 s))
     ;; bool _Y
       (if _Y (write-byte -1 s) (write-byte 0 s))
     ;; bool _padUp
       (if _padUp (write-byte -1 s) (write-byte 0 s))
     ;; bool _padDown
       (if _padDown (write-byte -1 s) (write-byte 0 s))
     ;; bool _padLeft
       (if _padLeft (write-byte -1 s) (write-byte 0 s))
     ;; bool _padRight
       (if _padRight (write-byte -1 s) (write-byte 0 s))
     ;; bool _bumperLeft
       (if _bumperLeft (write-byte -1 s) (write-byte 0 s))
     ;; bool _bumperRight
       (if _bumperRight (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _connect
     (setq _connect (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; float32 _leftX
     (setq _leftX (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _leftR
     (setq _leftR (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _rightX
     (setq _rightX (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _rightY
     (setq _rightY (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _leftTrg
     (setq _leftTrg (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _rightTrg
     (setq _rightTrg (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _A
     (setq _A (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _B
     (setq _B (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _X
     (setq _X (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _Y
     (setq _Y (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _padUp
     (setq _padUp (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _padDown
     (setq _padDown (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _padLeft
     (setq _padLeft (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _padRight
     (setq _padRight (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _bumperLeft
     (setq _bumperLeft (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _bumperRight
     (setq _bumperRight (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get project::my_msg :md5sum-) "666d003c179026e1a217a6c7a3916503")
(setf (get project::my_msg :datatype-) "project/my_msg")
(setf (get project::my_msg :definition-)
      "bool connect
float32 leftX
float32 leftR
float32 rightX
float32 rightY
float32 leftTrg
float32 rightTrg
bool A
bool B
bool X
bool Y
bool padUp
bool padDown
bool padLeft
bool padRight
bool bumperLeft
bool bumperRight

")



(provide :project/my_msg "666d003c179026e1a217a6c7a3916503")


