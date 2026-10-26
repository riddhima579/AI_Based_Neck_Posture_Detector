# --- Import necessary libraries ---
import cv2                     # For webcam and image processing
import mediapipe as mp          # For detecting human body posture
import numpy as np              # For mathematical calculations
import pyttsx3                  # For text-to-speech alert

# --- Initialize MediaPipe and speech engine ---
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
engine = pyttsx3.init()

# --- Function to make the computer speak alert messages ---
def speak_alert(msg):
    engine.say(msg)
    engine.runAndWait()

# --- Function to calculate angle between three body points (ear-shoulder-hip) ---
def calculate_angle(a, b, c):
    a, b, c = np.array(a), np.array(b), np.array(c)
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    if angle > 180:
        angle = 360 - angle
    return angle

# --- Access the webcam (0 = default camera) ---
cap = cv2.VideoCapture(0)

# --- Start MediaPipe Pose detection ---
with mp_pose.Pose(min_detection_confidence=0.5,
                  min_tracking_confidence=0.5) as pose:

    alert_given = False  # To avoid repeating the voice alert

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert image color from BGR to RGB (required by MediaPipe)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)

        # Convert color back to BGR for OpenCV display
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        try:
            # --- Get the required landmarks (ear, shoulder, hip) ---
            landmarks = results.pose_landmarks.landmark
            left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                             landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            left_ear = [landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].y]
            left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

            # --- Calculate posture angle ---
            angle = calculate_angle(left_ear, left_shoulder, left_hip)

            # Display angle on the screen
            cv2.putText(image, f'Angle: {int(angle)} deg',
                        (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)

            # --- Check posture condition ---
            if angle < 150:  # Threshold for bad posture
                cv2.putText(image, "BAD POSTURE!", (30,100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 3, cv2.LINE_AA)
                if not alert_given:
                    speak_alert("Bad posture detected. Please sit straight.")
                    alert_given = True
            else:
                cv2.putText(image, "Good posture", (30,100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 3, cv2.LINE_AA)
                alert_given = False

        except:
            pass

        # --- Draw body landmarks and connections on the image ---
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # --- Show the output video window ---
        cv2.imshow('Posture Detector', image)

        # Exit loop when 'ESC' key is pressed
        if cv2.waitKey(5) & 0xFF == 27:
            break

# --- Release camera and close all windows ---
cap.release()
cv2.destroyAllWindows()