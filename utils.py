import pandas as pd
import face_recognition
from datetime import datetime
import os
import cv2

# Load student data from CSV
def load_student_data(csv_path):
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces
    return df

# Initialize attendance CSV
def initialize_attendance(csv_path):
    if not os.path.exists(csv_path):
        df = pd.DataFrame(columns=["date", "student_name", "status"])
        df.to_csv(csv_path, index=False)
    return pd.read_csv(csv_path)

# Create encodings for known students
def create_database_encodings(student_df):
    print("Creating face encodings for students...")
    encodings = {}
    for _, row in student_df.iterrows():
        image_path = row["image_path"]
        if not os.path.exists(image_path):
            print(f"Warning: Image file {image_path} not found. Skipping...")
            continue
        # Load and encode the student's face
        image = face_recognition.load_image_file(image_path)
        face_encodings = face_recognition.face_encodings(image)
        if len(face_encodings) > 0:
            encodings[row["name"]] = face_encodings[0]
        else:
            print(f"Warning: No face found in image {image_path}. Skipping...")
    return encodings

# Recognize a face by comparing encodings and save the matching image
def recognize_face(encodings, input_frame):
    # Detect and encode faces in the input frame
    face_locations = face_recognition.face_locations(input_frame)
    face_encodings = face_recognition.face_encodings(input_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        for name, known_encoding in encodings.items():
            match = face_recognition.compare_faces([known_encoding], face_encoding, tolerance=0.6)
            if match[0]:  # If a match is found
                # Expand the bounding box for a larger image
                top, right, bottom, left = face_location
                padding = 50  # Increase this value for a larger bounding box
                top = max(0, top - padding)
                right = min(input_frame.shape[1], right + padding)
                bottom = min(input_frame.shape[0], bottom + padding)
                left = max(0, left - padding)

                # Crop and save the expanded face region
                matched_face = input_frame[top:bottom, left:right]
                save_path = "temp.jpg"                
                if not os.path.exists("matched_faces"):
                    os.makedirs("matched_faces")
                cv2.imwrite(save_path, matched_face)
                print(f"Saved matched image for {name} at {save_path}")
                return name
    return None


# Mark attendance in CSV
def mark_attendance(student_name, attendance_path):
    df = pd.read_csv(attendance_path)
    date = datetime.now().strftime("%Y-%m-%d")
    if not ((df["date"] == date) & (df["student_name"] == student_name)).any():
        new_entry = {"date": date, "student_name": student_name, "status": "present"}
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_csv(attendance_path, index=False)
        print(f"Marked {student_name} as present.")
    else:
        print(f"{student_name} is already marked as present today.")
