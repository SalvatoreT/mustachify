# Mustachify

    Download and unzip shape_predictor_68_face_landmarks.dat from:
    http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

I used `bzip2` to unzip the file, but you do whatever works for you.

    bzip2 -d shape_predictor_68_face_landmarks.dat.bz2

Install the Python requirements.

    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt

Once the libraries are all installed, you can run the program on the picture of a face.

    ./mustachify.py -i PICTURE_OF_FACE
