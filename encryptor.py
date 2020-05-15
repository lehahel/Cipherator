import cipher
import file_work
import trainer
import argparser


args = argparser.parse_arguments()

if args.func != 'train':
    text = file_work.read_text(args.input_file)
    if args.func != 'hack':
        result = cipher.act(args.func, args.cipher, args.key, text)
    else:
        result = trainer.caesar_hack(text, args.model_file)
    file_work.write_text(result, args.output_file)

else:
    text = file_work.read_text(args.text_file)
    trainer.train(text, args.model_file)
