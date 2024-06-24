from nltk import word_tokenize

def generate_n_grams(tokens,k):
    n_gram_list = []
    i = 0
    while(i < len(tokens)):
        n_gram_list.append(tokens[i:i+k])
    return n_gram_list
    

def generate_token_frequency(tokens):
    dict1 = {}
    for item in tokens:
        dict1[item] = 0
    for item in tokens:
        dict1[item] += 1
    return dict1

def tokenize_data(data):
    data = word_tokenize(data)
    return data
def pre_process(data):
    data = data.lower()
    data = "eos" + data
    data = data.replace(".","eos")
    return data




# MAIN CODE
data = input("Enter the corpus:")
data = pre_process(data)
tokens = tokenize_data(data)
distinctive_tokens = list(set(sorted(tokens)))

print("List of sorted and distinctive tokens are:", distinctive_tokens)

token_frequency = generate_token_frequency(tokens)
print("Frequency of each token is equal to :")
for i in token_frequency.items():
    print(i[0] +"\t"+i[1])

n_gram = generate_n_grams(tokens,2)

print("N-grams created using these tokens by taking n as 2:")
for i in n_gram:
    print(i)


