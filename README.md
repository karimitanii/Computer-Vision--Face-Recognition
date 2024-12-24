<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Multiple Face Recognition</title>
    <style>
      body {
        font-family: "Arial", sans-serif;
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        color: #e8e8e8;
        margin: 0;
        padding: 0;
      }
      header {
        background: #0f3460;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
      }
      header h1 {
        font-size: 2.5em;
        color: #e94560;
        margin: 0;
      }
      section {
        padding: 20px;
        max-width: 1200px;
        margin: auto;
      }
      h2 {
        color: #0fbcf9;
      }
      a {
        color: #34e89e;
        text-decoration: none;
      }
      a:hover {
        text-decoration: underline;
      }
      ul {
        list-style-type: disc;
        padding-left: 20px;
      }
      footer {
        text-align: center;
        padding: 10px;
        background: #0f3460;
        color: #e8e8e8;
        position: fixed;
        width: 100%;
        bottom: 0;
      }
    </style>
  </head>
  <body>
    <header>
      <h1>Multiple Face Recognition</h1>
    </header>

    <section>
      <h2>Overview</h2>
      <p>
        My first thought with doing this project is to solve a real-life problem
        with a modern solution which translated into addressing a common issue
        faced by students and instructors in universities: taking attendance.
        Manually marking attendance for a large class is time-consuming and can
        disrupt the flow of a lecture. By leveraging modern technology, this
        solution aims to automate attendance marking, saving time and effort for
        both instructors and students.
      </p>

      <h2>Open-Source Libraries Used</h2>
      <ul>
        <li><b>dlib</b></li>
        <li><b>face_recognition</b></li>
        <li><b>OpenCV</b></li>
      </ul>
      <p>
        These libraries made it feasible to recognize faces and mark attendance
        efficiently.
      </p>

      <h2>How It Works</h2>
      <ul>
        <li>The system encodes the faces of students from their images.</li>
        <li>
          Using a live camera feed, the system detects and recognizes the faces
          of students present in the classroom.
        </li>
        <li>
          Recognized students are automatically marked as present in the
          attendance record.
        </li>
      </ul>

      <h2>For More Technical Details</h2>
      <ul>
        <li>
          <a
            href="https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78"
            >Machine Learning is Fun: Modern Face Recognition</a
          >
        </li>
        <li>
          <a href="https://pypi.org/project/face-recognition/"
            >Face Recognition PyPI Documentation</a
          >
        </li>
        <li><a href="http://dlib.net/">dlib Documentation</a></li>
        <li>
          <a href="https://docs.opencv.org/3.4/"
            >Open Source Computer Vision Documentation</a
          >
        </li>
      </ul>

      <h2>Future Enhancements</h2>
      <ul>
        <li>
          <b>Higher-Resolution Cameras and Parallelization</b> Using better
          cameras with higher resolution will capture more pixels, improving
          accuracy and performance.In addition we can apply linear
          transformations on the pixels caught by the camera , and apply
          parallel processing which enables us to recogize students in extremely
          large classrooms.
        </li>
      </ul>

      <h2>How to Use</h2>
      <h3>Prerequisites</h3>
      <ul>
        <li>Install C++ on your machine.</li>
        <li>Install the required Python libraries:</li>
      </ul>
      <pre>
            pip install dlib
            pip install face_recognition
            pip install opencv-python
        </pre
      >

      <h3>Setup</h3>
      <ul>
        <li>
          Create a folder named <b>images</b> and place the images of the
          students you want to recognize in it.
        </li>
        <li>Prepare a <b>students.csv</b> file with the following columns:</li>
        <ul>
          <li><b>id:</b> Unique identifier for each student.</li>
          <li><b>name:</b> Name of the student.</li>
          <li>
            <b>image_path:</b> Path to the corresponding image in the images
            folder.
          </li>
        </ul>
        <li>
          Ensure the <b>students.csv</b> file and the <b>main.py</b> script are
          in the same directory.
        </li>
      </ul>

      <h3>Running the Project</h3>
      <ul>
        <li>Run the <b>main.py</b> script:</li>
      </ul>
      <pre>
            python main.py
        </pre
      >
      <ul>
        <li>The system will open a live camera feed.</li>
        <li>
          Recognized students will be marked as "present" in the
          <b>attendance.csv</b> file along with the date.
        </li>
      </ul>
    </section>

    <footer>&copy; 2024 Student-Face-Recognition Project</footer>

  </body>
</html>
