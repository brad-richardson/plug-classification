from subprocess import call

TRAIN_CMD = "python tensorflow/examples/image_retraining/retrain.py \
--bottleneck_dir=/tf_files/bottlenecks \
--train_batch_size=20 \
--test_batch_size=20 \
--learning_rate={} \
--how_many_training_steps={} \
--model_dir=/tf_files/inception \
--output_graph=/tf_files/models/{}retrained_graph.pb \
--output_labels=/tf_files/models/retrained_labels.txt \
--image_dir /tf_files/plugs/plugs-separate" 

def model_prefix(rate, steps):
    return "{}_{}_".format(str(rate).replace("0.", ""), str(steps))


def main():
    learning_rates = [.05, .01, .001, .0001]
    train_steps = [500, 2000, 10000, 15000]

    for rate in learning_rates:
        for steps in train_steps:
            prefix = model_prefix(rate, steps)
            # call("rm -r bottlenecks/*", shell=True)
            call(TRAIN_CMD.format(rate, steps, prefix), shell=True)
            # call("mkdir bottlenecks/{}".format(prefix), shell=True)
            # call("touch bottlenecks/{}/{}.txt".format(prefix, prefix), shell=True)


if __name__ == '__main__':
    main()
