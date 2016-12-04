import tensorflow as tf
import sys
import os

# change this as you see fit
image_path =  "tf_files/test_data/" # sys.argv[1]

# # Read in the image_data
# image_data = tf.gfile.FastGFile(image_path, 'rb').read()

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line 
                   in tf.gfile.GFile("tf_files/models/plugs-separate/separate-retrained_labels.txt")]

# Unpersists graph from file
with tf.gfile.FastGFile("tf_files/models/plugs-separate/separate-retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:

    for image in os.listdir(image_path):
        if image == ".DS_Store":
            continue
        image_data = tf.gfile.FastGFile(image_path + image, 'rb').read()

        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        best_node = top_k[0]
        best_score = predictions[0][best_node]
        print(image)
        print('%s (score = %.5f)' % (label_lines[best_node], best_score))

        # for node_id in top_k:
        #     human_string = label_lines[node_id]
        #     score = predictions[0][node_id]
        #     print('%s (score = %.5f)' % (human_string, score))
        # for node_id in top_k:
        #     human_string = label_lines[node_id]
        #     score = predictions[0][node_id]
        #     print('%s (score = %.5f)' % (human_string, score))
