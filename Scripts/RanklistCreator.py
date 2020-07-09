import requests,json

field_spaces = {'rank': 6, 'handle': 30, 'total_score': 7, 'prob':6, 'delta': 5}
def create_ranklist(data):
    data = data['result']
    cnt = data['contest']
    prbs = data['problems']
    rows = data['rows']
    prb_names = [prb['index'] for prb in prbs]
    procdata=[]
    for row in rows:
        temp=[]
        temp.append(row['rank'])
        temp.append(str(row['party']['members'][0]['handle']))
        temp.append(str(row['points']))
        res = row['problemResults']
        for r in res:
            temp.append(str(r['points']))
        procdata.append(temp)
    for proc in procdata:
        if(proc[0]==0):
            procdata.remove(proc)
    ans = '``' + str(cnt['name']) + '(' + str(cnt['id']) + ')' + '\n'
    table_header= 'rank  | handle                        | =      | '
    for prb in prb_names:
        table_header=table_header+str(prb)+str(' '*(field_spaces['prob']-len(prb)))+'| '
    ans += table_header + '\n'
    for p in procdata:
        temp=""
        temp += str(p[0])
        temp+= (' '*(field_spaces['rank']-len(str(p[0])))) + '| '
        temp+= p[1]
        temp+= (' '*(field_spaces['handle']-len(p[1]))) + '| '
        temp+= p[2]
        temp += (' '*(field_spaces['total_score']-len(p[2]))) + '| '
        for proc in p[3:]:
            if(proc==' '):
                proc='-'
            temp += proc
            temp+= (' '*(field_spaces['prob']-len(proc))) + '| '
        ans = ans + temp + '\n'
    ans += '``'
    return ans
    