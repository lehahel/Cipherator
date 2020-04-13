import argparse
import cipher
import file_work
import trainer

func_map = ['encode', 'decode', 'train', 'hack']
cipher_types = ['caesar', 'vigenere']

parser = argparse.ArgumentParser()

parser.add_argument("func", choices=func_map, help="encode/decode/train/hack")
parser.add_argument("--cipher", choices=cipher_types, dest='cipher', help="type of cipher you use")
parser.add_argument("--key", dest='key', help="key of cipher: number for Caesar, string for Vigenere")
parser.add_argument("--input-file", dest='input_file', help="text file to encode/decode")
parser.add_argument("--output-file", dest='output_file', help="output file to encode/decode into")
parser.add_argument("--text-file", dest='text_file', help="text file to train")
parser.add_argument("--model-file", dest='model_file', help="file with statistic to hack Caesar cipher")

args = parser.parse_args()

if args.func == 'encode':
    if args.input_file:
        with open(args.input_file, 'r') as f:
            text = f.read()
    else:
        text = input()
    if args.cipher == 'caesar':
        result = cipher.caesar_encode(int(args.key), text)
    elif args.cipher == 'vigenere':
        result = cipher.vigenere_encode(args.key, text)
    else:
        raise NameError('Wrong cipher type!')
    if args.output_file:
        with open(args.output_file, 'w') as f:
            f.write(result)
    else:
        print(result)
elif args.func == 'decode':
    if args.input_file:
        with open(args.input_file, 'r') as f:
            text = f.read()
    else:
        text = input()
    if args.cipher == 'caesar':
        result = cipher.caesar_decode(int(args.key), text)
    elif args.cipher == 'vigenere':
        result = cipher.vigenere_decode(args.key, text)
    else:
        raise NameError('Wrong cipher type!')
    if args.output_file:
        with open(args.output_file, 'w') as f:
            f.write(result)
    else:
        print(result)
elif args.func == 'train':
    if args.text_file:
        with open(args.text_file, 'r') as f:
            text = f.read
    else:
        text = input()
    trainer.train(text, args.model_file)
else:
    if args.input_file:
        with open(args.input_file, 'r') as f:
            text = f.read()
    else:
        text = input()
    result = trainer.hack(text, args.model_file)
    if args.output_file:
        with open(args.output_file, 'w') as f:
            f.write(result)
    else:
        print(result)
