import matplotlib.pyplot as plt

class Entry:
    def __init__(self, loss, global_step, accuracy, time, batch_size, steps, epochs):
        self.loss = loss
        self.global_step = global_step
        self.accuracy = accuracy
        self.time = time
        self.batch_size = batch_size
        self.steps = steps
        self.epochs = epochs

with open("res.txt", "r") as fh:
    lines = fh.readlines()

entries = []

for line in lines:
    loss = float(line.split("'loss': ")[1].split(",")[0])
    global_step = float(line.split("'global_step': ")[1].split(",")[0])
    accuracy = float(line.split("'accuracy': ")[1].split("}")[0])
    batch_size = float(line.split("'batch_size': ")[1].split(",")[0])
    steps = float(line.split("'steps': ")[1].split(",")[0])
    epochs = float(line.split("'epochs': ")[1].split("}")[0])
    time = float(line.split("took ")[1].split(" ")[0])
    entry = Entry(loss, global_step, accuracy, time, batch_size, steps, epochs)
    entries.append(entry)

print(len(entries))