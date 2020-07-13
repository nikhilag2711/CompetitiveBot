import datetime

def get_rank(rating):
    if rating < 1200:
        return (0xCCCCCC, 'Newbie')
    if rating >= 1200 and rating < 1400:
        return (0x77FF77, 'Pupil')
    if rating >= 1400 and rating < 1600:
        return (0x77DDBB, 'Specialist')
    if rating >= 1600 and rating < 1900:
        return (0xAAAAFF, 'Expert')
    if rating >= 1900 and rating < 2100:
        return (0xFF88FF, 'Candidate Master')
    if rating >= 2100 and rating < 2300:
        return (0xFFCC88, 'Master')
    if rating >= 2300 and rating < 2400:
        return (0xFFBB55, 'International Master')
    if rating >= 2400 and rating < 2600:
        return (0xFF7777, 'Grandmaster')
    if rating >= 2600 and rating < 3000:
        return (0xFF3333, 'International Grandmaster')
    if rating >= 3000:
        return (0xAA0000, 'Legendary Grandmaster')

def isValidInteger(s):
    try:
        int(s)
    except ValueError:
        return False
    num = int(s)
    return num

def isValidDate(s) :
    if len(s) == 4:
        try:
            datetime.datetime.strptime(s, '%Y')
        except ValueError:
            return False
        date = datetime.datetime.strptime(s, '%Y')
        return date
    elif len(s) == 6:
        try:
            datetime.datetime.strptime(s, '%m%Y')
        except ValueError:
            return False
        date = datetime.datetime.strptime(s, '%m%Y')
        return date
    elif len(s) == 8:
        try:
            datetime.datetime.strptime(s, '%d%m%Y')
        except ValueError:
            return False
        date = datetime.datetime.strptime(s, '%d%m%Y')
        return date
    else :
        return False

def tag_match(tags, latest_blog) :
    for tag in latest_blog['tags']:
        for chk in tags:
            if tag.find(chk) != -1:
                return latest_blog
    return False

def check_status(official, virtual, practice, unoff, part):
    if not official and not virtual and not practice and not unoff :
        return 1
    else:
        if part == 'CONTESTANT' and official :
            return 1
        if part == 'VIRTUAL' and virtual :
            return 1
        if part == 'PRACTICE' and practice :
            return 1
        if part == 'OUT_OF_COMPETITION' and unoff :
            return 1
        return 0

def contest_check(contest) :
    subs = []
    notSubs = []
    if contest == 'div1' :
        subs.append('Div. 1')
    elif contest == 'div2' :
        subs.append('Div. 2')
        notSubs.append('Div. 1')
        notSubs.append('Educational Codeforces')
    elif contest == 'div3' :
        subs.append('Div. 3')
    elif contest == 'div4' :
        subs.append('Div. 4')
    elif contest == 'edu' :
        subs.append('Educational Codeforces')
    elif contest == 'global' :
        subs.append('Codeforces Global Round')
    elif contest == 'beta' :
        subs.append('Codeforces Beta Round')
    elif contest == 'other' :
        notSubs.append('Div. 1')
        notSubs.append('Div. 2')
        notSubs.append('Div. 3')
        notSubs.append('Div. 4')
        notSubs.append('Educational Codeforces')
        notSubs.append('Codeforces Global Round')
        notSubs.append('Codeforces Beta Round')
    return subs, notSubs
