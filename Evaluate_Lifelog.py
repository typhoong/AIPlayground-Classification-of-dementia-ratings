
import sys
import pandas as pd
from sklearn.metrics import f1_score


def evaluation_metric(label, prediction):
    return f1_score(label, prediction, average='macro')


def evaluate(label, prediction):
    try:
        label = list(map(int, label))
        prediction = list(map(int, prediction))
    except:
        assert False, 'Data Type Error (should be int or convertible to int)'
    return evaluation_metric(label=label, prediction=prediction)


def load_result(path, pred=False):
    label_encoding = {'CN' : 0, 'MCI' : 1, 'Dem' : 2}
    result = pd.read_csv(path)
    for i, sample in enumerate(result['DIAG_NM']):
        assert sample in label_encoding.keys(), 'invalid answer ' + sample
        result['DIAG_NM'][i] = label_encoding[sample]
    if pred is False: # answer
        p_type_li = list(result['public'])
    else: # prediction
        p_type_li = None
    return list(result['ID']), list(result['DIAG_NM']), p_type_li

def F1Score(answer_path, pred_path):

    a_id, answer, p_type_li = load_result(answer_path)
    p_id, pred, _ = load_result(pred_path, pred=True)

    assert len(a_id) == len(p_id), 'The number of predictions and answers are not the same'
    assert set(p_id) == set(a_id), 'The prediction ids and answer ids are not the same'

    pub_a_id, pub_answer, prv_a_id, prv_answer = [], [], [], []
    pub_p_id, pub_pred, prv_p_id, prv_pred = [], [], [], []
    for idx, t in enumerate(p_type_li):
        if t == 'public':
            pub_a_id.append(a_id[idx])
            pub_answer.append(answer[idx])
            pub_p_id.append(p_id[idx])
            pub_pred.append(pred[idx])
        elif t == 'private':
            prv_a_id.append(a_id[idx])
            prv_answer.append(answer[idx])
            prv_p_id.append(p_id[idx])
            prv_pred.append(pred[idx])
        else:
            pass
    # sort
    pub_ans = pd.DataFrame({'ID': pub_a_id, 'answer': pub_answer}).sort_values('ID', ignore_index=True)
    prv_ans = pd.DataFrame({'ID': prv_a_id, 'answer': prv_answer}).sort_values('ID', ignore_index=True)
    pub_pred = pd.DataFrame({'ID': pub_p_id, 'answer': pub_pred}).sort_values('ID', ignore_index=True)
    prv_pred = pd.DataFrame({'ID': prv_p_id, 'answer': prv_pred}).sort_values('ID', ignore_index=True)

    # f1 score
    score = evaluate(label=pub_ans['answer'], prediction=pub_pred['answer'])
    pScore = evaluate(label=prv_ans['answer'], prediction=prv_pred['answer'])

    return score, pScore


if __name__ == '__main__':

    answer = sys.argv[1]
    pred = sys.argv[2]

    try:
        import time
        start = time.time()
        score, pScore = F1Score(answer, pred)
        score = 0.3*score + 0.7*pScore
        print(f'score={score},pScore={pScore}')
        print(f'Elapsed Time: {time.time() - start}')

    except Exception as e:
        print(f'evaluation exception error: {e}', file=sys.stderr)
        sys.exit()