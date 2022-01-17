from curses import raw
import pickle

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


def process():
  for i in range(1, 6):
    raw_data = unpickle(f"data/cifar-10-batches-py/data_batch_{i}")
    print(f"Processing: {raw_data[b'batch_label'].decode()}")

    labels = raw_data[b"labels"]
    data = raw_data[b"data"]
    filenames = raw_data[b"filenames"]
    
  return None

if __name__ == '__main__':
  process()
