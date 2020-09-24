import os
import random

import numpy as np
import tensorflow as tf

class MelDataset:
    def __init__(self,
                 root_dir,
                 random_seed):

        random.seed(random_seed)
        self.root_dir = root_dir
        self.file_list = sorted(os.listdir(root_dir))
        random.shuffle(self.file_list)

    def _generate(self):
        for mel_name in self.file_list:
            yield np.load(os.path.join(self.root_dir, mel_name))

    def create(self):
        return tf.data.Dataset.from_generator(self._generate, tf.float32)\
            .prefetch(tf.data.experimental.AUTOTUNE)
