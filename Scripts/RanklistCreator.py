import requests,json
from constants import *
field_spaces = {'rank': 6, 'handle': 30, 'total_score': 7, 'prob':6, 'delta': 5}
def create_ranklist(data,dataoff):
    data = data['result']
    dataoff = dataoff['result']
    rows_off = dataoff['rows']
    cnt = data['contest']
    identity = cnt['id']
    RAT_URL = f'{CF_RAT_CHANGE}{identity}'
    obj = requests.get(RAT_URL)
    rating_changes = json.loads(obj.text)
    if(rating_changes['status']=='FAILED'):
        return f'{rating_changes["comment"]}'
    rating_changes = rating_changes['result']
    unrated=False
    if(len(rating_changes)==0):
        unrated=True
    prbs = data['problems']
    rows = data['rows']
    prb_names = [prb['index'] for prb in prbs]
    offRank = {'testHandle01213': 0}
    for row in rows_off:
        offRank[row['party']['members'][0]['handle']]=row['rank']
    
    procdata=[]
    for row in rows:
        temp=[]
        temp.append(row['rank'])
        temp.append(str(row['party']['members'][0]['handle']))
        temp.append(str(row['points']))
        res = row['problemResults']
        for r in res:
            temp.append(str(r['points']))
        
        isCont = False
        chng=0
        if(unrated==False):
            if(row['party']['participantType']=='CONTESTANT'):
                rat_chng = rating_changes[offRank[row['party']['members'][0]['handle']]-1]
                chng = rat_chng['newRating'] - rat_chng['oldRating']
                isCont = True
            if(isCont):
                if(chng>=0):
                    temp.append('+' + str(chng))
                else:
                    temp.append(str(chng))
            else:
                temp.append(' ??')
        else:
            temp.append(' ??')
        procdata.append(temp)
    
    for proc in procdata:
        if(proc[0]==0):
            procdata.remove(proc)
    ans = '``' + str(cnt['name']) + '(' + str(cnt['id']) + ')' + '\n'
    table_header= 'rank  | handle                        | =      | '
    for prb in prb_names:
        table_header=table_header+str(prb)+str(' '*(field_spaces['prob']-len(prb)))+'| '
    table_header += 'Delta | '
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
    