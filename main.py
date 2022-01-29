import spacy


def ner(string, lang):

    model = f'{lang}_core_web_sm'

    nlp = spacy.load(model)
    parsed = nlp(string)

    out_list = []
    for token in parsed:
        text = token.text
        word_type = token.ent_type_
        start_pos = token.idx
        end_pos = start_pos + len(text)

        out_dict = {'text': text,
                    'type': word_type,
                    'start_pos': start_pos,
                    'end_pos': end_pos}

        out_list.append(out_dict)

    return(out_list)


ner('I have $5 today', 'en')
'''
[{'text': 'I', 'type': '', 'start_pos': 0, 'end_pos': 1}, 
{'text': 'have', 'type': '', 'start_pos': 2, 'end_pos': 6}, 
{'text': '$', 'type': '', 'start_pos': 7, 'end_pos': 8}, 
{'text': '5', 'type': 'MONEY', 'start_pos': 8, 'end_pos': 9}, 
{'text': 'today', 'type': 'DATE', 'start_pos': 10, 'end_pos': 15}]
'''
