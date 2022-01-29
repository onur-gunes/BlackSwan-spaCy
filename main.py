import spacy


def ner(string, lang):

    model = f'{lang}_core_web_sm'

    nlp = spacy.load(model)
    parsed = nlp(string)

    out_list = []
    for token in parsed:

        text = token.text
        # Not sure what you mean by type, so including a few possiblities
        word_type = token.ent_type_, token.dep_, token.head.pos_
        start_pos = token.idx
        end_pos = start_pos + len(text)

        out_dict = {'text': text,
                    'type': word_type,
                    'start_pos': start_pos,
                    'end_pos': end_pos}

        out_list.append(out_dict)

    print(out_list)
    return(out_list)


ner('I have $5 today', 'en')
