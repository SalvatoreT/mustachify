#!/usr/bin/env python3
import sys
import dlib
from skimage import io

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

img = io.imread('sal-face.jpg')

dets = detector(img, 1)

for k, d in enumerate(dets):
  print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
      k, d.left(), d.top(), d.right(), d.bottom()))
  # Get the landmarks/parts for the face in box d.
  shape = predictor(img, d)
  print("Part 0: {}, Part 1: {} ...".format(shape.part(0), shape.part(1)))
