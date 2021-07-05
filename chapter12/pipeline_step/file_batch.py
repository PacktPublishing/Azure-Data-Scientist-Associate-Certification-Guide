def init():
    print("Load model here")


def run(mini_batch):
    output = []
    for file_path in mini_batch:
        output.append([file_path, 0])
    return output
