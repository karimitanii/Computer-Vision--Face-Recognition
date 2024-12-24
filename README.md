# Multiple Face Recognition

## Overview

My first thought with doing this project is to solve a real-life problem with a modern solution which translated into addressing a common issue faced by students and instructors in universities: taking attendance. Manually marking attendance for a large class is time-consuming and can disrupt the flow of a lecture. By leveraging modern technology, this solution aims to automate attendance marking, saving time and effort for both instructors and students.

## Open-Source Libraries Used

- **dlib**
- **face_recognition**
- **OpenCV**

These libraries made it feasible to recognize faces and mark attendance efficiently.

## How It Works

1. The system encodes the faces of students from their images.
2. Using a live camera feed, the system detects and recognizes the faces of students present in the classroom.
3. Recognized students are automatically marked as present in the attendance record.

## For More Technical Details

- [Machine Learning is Fun: Modern Face Recognition](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78)
- [Face Recognition PyPI Documentation](https://pypi.org/project/face-recognition/)
- [dlib Documentation](http://dlib.net/)

## Future Enhancements

- **Higher-Resolution Cameras**: Using better cameras with higher resolution will capture more pixels, improving accuracy and performance.
- **Parallelization**: Applying linear transformations and parallel processing can enable the system to efficiently recognize students in larger classrooms.
- **Scalability**: Enhancements to support real-time recognition in large-scale environments with minimal latency.

## How to Use

### Prerequisites

1. Install C++ on your machine.
2. Install the required Python libraries:
   ```bash
   pip install dlib
   pip install face_recognition
   pip install opencv-python
   ```

### Setup

1. Create a folder named `images` and place the images of the students you want to recognize in it.
2. Prepare a `students.csv` file with the following columns:
   - `id`: Unique identifier for each student.
   - `name`: Name of the student.
   - `image_path`: Path to the corresponding image in the `images` folder.
3. Ensure the `students.csv` file and the `main.py` script are in the same directory.

### Running the Project

1. Run the `main.py` script:
   ```bash
   python main.py
   ```
2. The system will open a live camera feed.
3. Recognized students will be marked as "present" in the `attendance.csv` file along with the date.

---


