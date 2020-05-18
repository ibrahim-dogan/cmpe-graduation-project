from gensim.models import LsiModel
from topic_modelling import preprocess, coherence, distributions


def LSA(corpus, n_topic):
    cleaned_data, data_tokens, id2word, corpus = preprocess.preprocess(corpus=corpus)
    doc_number = len(data_tokens)
    lsi_model = LsiModel(corpus=corpus, num_topics=n_topic, id2word=id2word)
    coherence_v = coherence.coherence_value(model=lsi_model, tokens=data_tokens, dictionary=id2word)
    word_distributions = distributions.word_distribution(model=lsi_model, n_topic=n_topic)
    topic_distributions = distributions.lsi_topic_distribution(doc_number=doc_number, model=lsi_model, corpus=corpus)
    doc_dist = distributions.lsi_doc_distribution(n_topic=n_topic, doc_number=doc_number, model=lsi_model, corpus=corpus)
    output = {"filecount": doc_number,
              "coherence_value": float(coherence_v),
              "word_distributions": word_distributions,
              "topic_distributions": topic_distributions,
              "doc_dist": doc_dist,
              }

    return output


    # def my_converter(o):
    #     return o.__str__()
    #
    # with open('output_first.txt', 'w', encoding='utf-8') as outfile:
    #     json.dump(output, outfile, indent=4, default=my_converter, ensure_ascii=False)
    #
    # with open('output_first.txt', 'r', encoding="utf8") as handle:
    #     parsed = json.load(handle)
