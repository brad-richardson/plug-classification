#!/bin/bash

brew install automake

git clone https://github.com/tensorflow/tensorflow ~/tensorflow

cd ~/tensorflow
tensorflow/contrib/makefile/build_all_ios.sh
cp ~/tf_files/mmapped_graph.pb \
	tensorflow/contrib/ios_examples/camera/data/
cp ~/tf_files/retrained_labels.txt \
	tensorflow/contrib/ios_examples/camera/data/
open tensorflow/contrib/ios_examples/camera/camera_example.xcodeproj

