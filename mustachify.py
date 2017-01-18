#!/usr/bin/env python3
import sys
import argparse
import dlib
from skimage import io

def main(face_file):
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    img = io.imread(face_file)

    dets = detector(img, 1)

    for k, d in enumerate(dets):
      print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
          k, d.left(), d.top(), d.right(), d.bottom()))
      # Get the landmarks/parts for the face in box d.
      shape = predictor(img, d)
      print("Part 0: {}, Part 1: {} ...".format(shape.part(0), shape.part(1)))

if __name__ == "__main__":
    # execute only if run as a script
    parser = argparse.ArgumentParser(description='This is a demo script by nixCraft.')
    parser.add_argument('-i','--input', help='Input file name',required=True)
    args = parser.parse_args()
    main(args.input)
