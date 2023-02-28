import random
import simpy

# Parameters
RANDOM_SEED = 42
RAM_CAPACITY = 100
INTERVAL = 10
INSTRUCTIONS_PER_CYCLE = 3
IO_PROBABILITY = 1/21

# Initialize random number generator
random.seed(RANDOM_SEED)

class Process:
    def __init__(self, env, pid, ram, cpu):
        self.env = env
        self.pid = pid
        self.ram = ram
        self.cpu = cpu
        self.instructions = random.randint(1, 10)
        self.mem = random.randint(1, 10)
        self.wait_time = 0
        
    def run(self):
        # New process
        yield self.env.timeout(random.expovariate(1/INTERVAL))
        print(f"Process {self.pid}: new")
        if self.mem > RAM_CAPACITY:
            print(f"Process {self.pid}: not enough memory, terminating")
            return
        yield self.ram.get(self.mem)
        print(f"Process {self.pid}: memory allocated, {self.mem} units")
        
        # Ready process
        print(f"Process {self.pid}: ready, {self.instructions} instructions")
        while self.instructions > 0:
            with self.cpu.request() as req:
                yield req
                print(f"Process {self.pid}: running")
                for _ in range(INSTRUCTIONS_PER_CYCLE):
                    if self.instructions > 0:
                        self.instructions -= 1
                    else:
                        break
                if self.instructions == 0:
                    break
                if random.random() <= IO_PROBABILITY:
                    print(f"Process {self.pid}: waiting for I/O")
                    self.wait_time += 1
                    yield self.env.timeout(random.randint(1, 10))
                    print(f"Process {self.pid}: I/O completed, back to ready")
                else:
                    print(f"Process {self.pid}: back to ready")
        print(f"Process {self.pid}: terminated")
        self.ram.put(self.mem)

# Setup and start the simulation
print("Time sharing simulation")
env = simpy.Environment()
ram = simpy.Container(env, capacity=RAM_CAPACITY, init=RAM_CAPACITY)
cpu = simpy.Resource(env, capacity=1)

for i in range(5):
    num_processes = (i + 1) * 25
    print(f"\nSimulating {num_processes} processes")
    
    for j in range(num_processes):
        process = Process(env, j, ram, cpu)
        env.process(process.run())

    env.run()
