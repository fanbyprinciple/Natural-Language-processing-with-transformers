from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-bn-en")

model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-bn-en")

f1 =open('single_page.txt')

texts = f1.readlines()
#texts = "".join(f1.readlines())

# f2 = open('compiled.txt', 'w+', encoding='utf-8')
# f2.write(texts)


from transformers import pipeline
translation = pipeline(task="translation", model=model, tokenizer=tokenizer)

f3 = open('translated.txt', 'w+', encoding='utf-8')

for text in texts:
    print(translation(text))
    #f3.write((translation(t))

print('translated text in translated.txt')