from tqdm import tqdm

with open('combinations.txt', 'w') as file:
    for i in tqdm(range(100000000), desc="Generating combinations"):
        file.write(f"{i:08d}\n")
