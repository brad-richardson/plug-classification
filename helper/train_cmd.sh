#!/bin/bash

python tensorflow/examples/image_retraining/retrain.py \
	--bottleneck_dir=/tf_files/bottlenecks \
	--model_dir=/tf_files/inception \
	--output_graph=/tf_files/retrained_graph.pb \
	--output_labels=/tf_files/retrained_labels.txt \
	--image_dir /tf_files/plug_photos

