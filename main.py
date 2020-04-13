import cipher
import trainer
import file_work

text = file_work.get_file_text("text/text.txt")
trainer.train(file_work.get_file_text("text/sonnet.txt"))
encoded_text = cipher.caesar_encode(5, text)
file_work.write_res("text/encoded_text.txt", encoded_text)
decoded_text = trainer.caesar_hack(file_work.get_file_text("text/encoded_text.txt"))
print(decoded_text)
file_work.write_res("text/texted.txt", decoded_text)
