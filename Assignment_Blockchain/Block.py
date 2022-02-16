import json
import os
import hashlib


BLOCKCHAIN_DIR = 'blockchain/'

def get_hash(prev_block):
    with open(BLOCKCHAIN_DIR + prev_block) as f:
        block = json.load(f)
    
    prev_hash = block.get('prev_block').get('hash')
    prev_blockIndex = block.get('prev_block').get('blockIndex')
    T1 = block.get('T1')
    T2 = block.get('T2')
   
    About =  block.get('About')
    data = (f"T1 : {T1} T2 : {T2} About : {About} \n Previous hash : {prev_hash} blockIndex : {prev_blockIndex}")
    return hashlib.sha256(data.encode()).hexdigest()

def check_integrity():
    files = sorted(os.listdir(BLOCKCHAIN_DIR), key=lambda x: int(x))
    
    results = []
    
    for file in files[1:]:
        with open(BLOCKCHAIN_DIR + file) as f:
            block = json.load(f)
        
        prev_hash = block.get('prev_block').get('hash')
        prev_blockIndex = block.get('prev_block').get('blockIndex')
        
        actual_hash = get_hash(prev_blockIndex)
        if prev_hash == actual_hash:
            res = 'OK'
        else:
            res = 'Was Changed'

        print(f'Block { prev_blockIndex} : {res}')
        results.append({'block' :  prev_blockIndex, 'results' : res})
    return results


def write_block(T1, T2, About):
    blocks_count = len(os.listdir(BLOCKCHAIN_DIR))
    prev_block = str(blocks_count)
    print(prev_block)
    prev_hash = get_hash(prev_block)
    data_block_hash = (f"T1 : {T1} T2 : {T2} About : {About} \n Previous hash : {prev_hash} blockIndex : {prev_block}")
    block_hash = hashlib.sha256(data_block_hash.encode()).hexdigest()

    data = {
        "T1": T1,
        "T2": T2,
        "About": About,
        "block_hash" :  block_hash,
        "prev_block": {
            "hash": prev_hash,
            "blockIndex": prev_block
        }
    }

    current_block = BLOCKCHAIN_DIR + str(blocks_count + 1)

    with open(current_block, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.write('\n')


def show_data():
    files = sorted(os.listdir(BLOCKCHAIN_DIR), key=lambda x: int(x))
    data = []
    for file in files[1:]:
        with open(BLOCKCHAIN_DIR + file) as f:
            block = json.load(f)
        
        prev_blockIndex = block.get('prev_block').get('blockIndex')
        T1 = block.get('T1')
        T2 = block.get('T2')
        About =  block.get('About')
        actual_hash = get_hash( prev_blockIndex)

        data.append({'block' :  prev_blockIndex, 'T1' : T1, 'T2' : T2, 'About' : About})
    return data

def main():
    write_block(T1 = 'Buriram United Esports', T2 = 'Dewa United',About = '2021-06-19T15:00 ')
    write_block(T1 = 'VGaming', T2 = 'ONE Team Esports',About = '2021-06-19T19:30 ')
    write_block(T1 = 'Overclock Esports', T2 = 'dtac Talon Esports',About = '2021-06-20T18:00 ')
    write_block(T1 = 'Bacon Time', T2 = 'Saigon Phantom',About = '2021-06-20T19:30 ')
    write_block(T1 = 'ArchAngel', T2 = 'UndeRank',About = '2021-06-22T15:00 ')
    write_block(T1 = 'Z9 Gaming', T2 = 'ONE Team Esports',About = '2021-06-24T12:00 ')
    write_block(T1 = 'VGaming', T2 = 'Team CIV',About = '2021-06-24T18:00 ')
    write_block(T1 = 'dtac Talon Esports', T2 = 'Overclock Esports',About = '2021-06-25T13:30 ')
    write_block(T1 = 'UndeRank', T2 = 'MAD Team',About = '2021-06-25T16:30 ')
    write_block(T1 = 'Bacon Time', T2 = 'Buriram United Esports',About = '2021-06-26T09:00 ')
    check_integrity()
    

if __name__ == '__main__':
    main()