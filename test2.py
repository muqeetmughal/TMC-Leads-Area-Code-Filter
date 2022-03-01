# from tqdm import tqdm
# from time import sleep
# print([x for x in range(1000)])


# # for i in tqdm():
# #     # sleep(0.5)
# #     pass


from multiprocessing import Process
import os

def square_number():
     for i in range(1000):
         i + i


if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()

    for i in range(num_processes):
        process = Process(target=square_number)
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()