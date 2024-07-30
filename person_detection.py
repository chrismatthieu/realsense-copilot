import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
import pyrealsense2 as rs2

class PersonDetectionNode(Node):
    def __init__(self):
        super().__init__('person_detection_node')
        self.bridge = CvBridge()
        self.rgb_subscriber = self.create_subscription(
            Image,
            '/camera/color/image_raw',
            self.rgb_callback,
            10)
        self.depth_subscriber = self.create_subscription(
            Image,
            '/camera/depth/image_raw',
            self.depth_callback,
            10)
        self.rgb_image = None
        self.depth_image = None

    def rgb_callback(self, msg):
        self.rgb_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        self.detect_person()

    def depth_callback(self, msg):
        self.depth_image = self.bridge.imgmsg_to_cv2(msg, "16UC1")

    def detect_person(self):
        if self.rgb_image is None or self.depth_image is None:
            return

        # Load a pre-trained person detection model (e.g., MobileNet SSD)
        net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'mobilenet_iter_73000.caffemodel')
        blob = cv2.dnn.blobFromImage(self.rgb_image, 0.007843, (300, 300), 127.5)
        net.setInput(blob)
        detections = net.forward()

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:
                idx = int(detections[0, 0, i, 1])
                if idx == 15:  # Class ID for person
                    box = detections[0, 0, i, 3:7] * np.array([self.rgb_image.shape[1], self.rgb_image.shape[0], self.rgb_image.shape[1], self.rgb_image.shape[0]])
                    (startX, startY, endX, endY) = box.astype("int")
                    cv2.rectangle(self.rgb_image, (startX, startY), (endX, endY), (0, 255, 0), 2)

                    # Calculate the distance to the person
                    person_depth = self.depth_image[startY:endY, startX:endX]
                    distance = np.mean(person_depth[person_depth > 0])
                    self.get_logger().info(f"Person detected at distance: {distance} mm")

        cv2.imshow("Person Detection", self.rgb_image)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = PersonDetectionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
