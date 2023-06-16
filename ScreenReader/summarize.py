from transformers import AutoTokenizer, BartForConditionalGeneration


def generate_1000_character_string(input_string):
    try:
        # Split the input string into words
        words = input_string.split()

       
        # Select the words for the 1000-character string
        first_400_words = ' '.join(words[:400])
        middle_200_words = ' '.join(words[len(words) // 2 - 100: len(words) // 2 + 100])
        last_400_words = ' '.join(words[-400:])

        # Concatenate the selected words
        generated_string = first_400_words + middle_200_words + last_400_words

        return generated_string[:1000]  # Return the first 1000 characters of the generated string

    except Exception as e:
        print("An error occurred:", e)
        return 'Error'
    
    



def summarise(webpage_contents):
    model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
    tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")

    # with open('extracted.txt', 'r', encoding="utf8") as f:
    #     file_content = f.read()
    
    file_content = ''
    
    if len(webpage_contents) > 1000:
        file_content = generate_1000_character_string(webpage_contents)
    else:   
        file_content = webpage_contents
        
    
    ARTICLE_TO_SUMMARIZE = str(file_content)
    inputs = tokenizer([ARTICLE_TO_SUMMARIZE], max_length=1024, return_tensors="pt")

    # Generate Summary
    summary_ids = model.generate(inputs["input_ids"], num_beams=2, min_length=0, max_length=100)
    summary = tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    # Opens extracted.txt and returns summary
    
    print(summary)

content = '''
In the previous blog post, we learned about the retrieval-augmented approach to overcome the limitations of Large Language Models (LLMs), such as hallucinations and limited knowledge. The idea behind the retrieval-augmented approach is to reference external data at question time and feed it to an LLM to enhance its ability to generate accurate and relevant answers.
When a user asks a question, an intelligent search tool looks for relevant information in the provided Knowledge bases. For example, you might have encountered instances of searching for relevant information within PDFs or a company’s documentation. Most of those examples use vector similarity search to identify which chunks of text might contain relevant data to answer the user’s question accurately. The implementation is relatively straightforward.
'''
#summarise(content)