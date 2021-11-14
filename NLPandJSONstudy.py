# created by McZazz, found at https://github.com/McZazz/NLPandJSONstudy
# import sys, os
# sys.path.append('/')
from .Weights import *
# import linecache
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet
import nltk
from nltk.stem import WordNetLemmatizer
from datetime import datetime
from datetime import timezone
# if stopwords is acting unpredictably, use the following in the command line:
# python -m nltk.downloader stopwords
# if spacy is being dumb:
# python -m spacy download en_core_web_lg
from nltk.corpus import stopwords
from secrets import randbelow
from hashlib import md5
from hashlib import sha256
from gensim import corpora

import json
import glob
import re

def tokenize_text(body):
    """ input is a string for sentence and word tokenization.
        This is tokenization which preserves some special characters
        for comprehensive nlp. takes only the message body as a string

        "^[a-zA-Z0-9]{1}$"
    """
    # print("0:",body)

    # temp1 = []
    # for char in body:
    #     temp1.append(char)
    #
    # for i, char in enumerate(temp1):
    #     if i>1:
    #         if temp1[i-2] == re.match("[a-zA-Z0-9!?,.@&$%()*-+=<>/]", char) and temp1[i-1] ==

    # body = re.sub("( ')", " ' ", body)
    # body = re.sub("([sS]' )", "s ' ", body)
    # body = re.sub(r'\"+', "'", body)
    # body = re.sub(r"\'+", "'", body)
    # body = re.sub("[\\\n\r\t\b\f]", "", body)
    body = re.sub("[']+", "'", body)
    body = re.sub('["]+', '\"', body)

    body = body.replace('{', '(')
    body = body.replace('[', '(')
    body = body.replace(']', ')')
    body = body.replace('}', ')')
    body = re.sub("[(]+", ",", body)
    body = re.sub('[)]+', ",", body)
    body = re.sub("[^a-zA-Z0-9!?,.@&$%()'\"*-+=<>/ ]", '', body)


    body = re.sub('[!]+', '!', body)
    body = re.sub('[?]+', '?', body)
    body = re.sub('[,]+', ',', body)
    body = re.sub('[.]+', '.', body)
    body = re.sub('[@]+', '@', body)
    body = re.sub('[&]+', '&', body)
    body = re.sub('[$]+', '$', body)
    body = re.sub('[%]+', '%', body)
    body = re.sub('[(]+', '(', body)
    body = re.sub('[)]+', ')', body)
    body = re.sub('[*]+', '*', body)
    body = re.sub('[-]+', '-', body)
    body = re.sub('[+]+', '+', body)
    body = re.sub('[=]+', '=', body)
    body = re.sub('[<]+', '<', body)
    body = re.sub('[>]+', '>', body)
    body = re.sub('[/]+', '/', body)

    # user error fix, preserve sinle quotes inside words
    # body = re.sub('[a-zA-Z](")[a-zA-Z]', "'", body)
    temp1 = []
    for char in body:
        temp1.append(char)
    for i, char in enumerate(temp1):
        if i>1:
            if re.match("[a-zA-Z0-9]", temp1[i-2]) and temp1[i-1] == '"' and re.match("[a-zA-Z0-9]", char):
                temp1[i-1] = "'"

    # put end quotes inside the period
    for i, char in enumerate(temp1):
        if i>0:
            if re.match('[!.?]', temp1[i-1]) and re.match("['\"]", char):
                period = temp1[i-1]
                temp1[i-1] = '"'
                temp1[i] = period
        elif i>1 and not re.match("[sS]", temp1[i-2]) and re.match("['\"]", temp1[i-1]) and re.match('[!.?]', char) :
            period = char
            temp1[i-1] = '"'
            temp1[i] = period

    # if not re.search("([sS]' )", body):
    for i, char in enumerate(temp1):
        if i>1:
            if re.match("[sS]", temp1[i-2]) and temp1[i-1] == "'" and char == ' ':
                pass
            # else:
            #     cntr = 0
            #     for char in temp1:
            #         if char == '"':
            #             cntr +=1
            #     if cntr == 1:
            #         for i, char in enumerate(temp1):
            #             if char == '"':
            #                 temp1.pop(i)

                    # if i>1 and re.match("[sS]", temp1[i-2]) and re.match("['\"]", temp1[i-1]) and char == ' ':
                    #     temp1[i-1] = "'"



    # get rid of error singles:
    # cntr = 0
    # for char in body:
    #     if char == "'":
    #         cntr +=1
    # if cntr == 1 and not re.search("[a-zA-Z](')[a-zA-Z]", body) and not re.search("([sS]' )", body):
    #     body = re.sub("'", "", body)

    body = ''.join(temp1)
    # print("0.1:",body)
    # body = re.sub('[a-zA-Z](\")[a-zA-Z]', "'", body)


    ################# need this one while in list format
    if not re.search("(s' )", body):
        body = re.sub("(' )", " ' ", body)
        body = re.sub("( ')", " ' ", body)
    # if not re.search("[a-zA-Z](')[a-zA-Z]", body):
    # body = re.sub("( ' )", ' " ', body)


    temp1 = []
    cntr = 0
    # get rid of error singles:



    # if these is a single (s' ) in the entire string, we dont get separated quotes
    # and must comprehensively check in the else block
    # if not re.search("(s' )", body):
    #     print("uhuh")
    #     body = re.sub("(' )", " ' ", body)
    #     body = re.sub("( ')", " ' ", body)
    #     if not re.search("[a-zA-Z](')[a-zA-Z]", body):
    #         body = re.sub("(')", '"', body)




    # if odd number of " exists, find the extra one and delete it
    # temp1 = []
    # for char in body:
    #     temp1.append(char)
    # dubcntr = 0
    # for char in temp1:
    #     if char == '"':
    #         dubcntr += 1
    # print(dubcntr)
    # if dubcntr % 2 != 0:
    #     print(dubcntr)

    # else:
        # temp1 = []
        # quotes = False
        # for char in body:
        #     temp1.append(char)
        # dubcntr = 0
        # for i, char in enumerate(char)
        #     if char == '"':
        #         dubcntr += 1





    # body = re.sub('(" )', " '' ", body)
    # body = re.sub('( ")', " '' ", body)

    # body = re.sub("(^')", " ' ", body)
    # body = re.sub('(^")', " ' ", body)
    # body = re.sub("('$)", " ' ", body)
    # body = re.sub('("$)', " ' ", body)


    # print("1:",body)
    # isolate special characters
    temp1 = []
    for i, char in enumerate(body):
        match = re.match("[^a-zA-Z0-9' ]", char)
        if match:
            char = ' ' + char + ' '
        temp1.append(char)


    # make double quotes from single quotes that need it
    for i, char in enumerate(temp1):
        if i>1 and temp1[i-2] == ' ' and temp1[i-1] == "'" and char == ' ':
            temp1[i-1] = '"'


    # if s' exists, make sure it isn't just a quoted area
    quotestart = False



    for i, char in enumerate(temp1):
        if (i-1 == 0 and len(temp1)>1) and re.match("['\"]", temp1[i-1]) and re.match("[a-zA-Z0-9]", char):
            temp1[i-1] = '" '
        if i>1:
            if re.match("[sS]", temp1[i-2]) and temp1[i-1] == "'" and char == ' ':
                cntr = 0
                for i, char in enumerate(temp1):
                    if i>1 and temp1[i-2] == ' ' and re.match("['\"]", temp1[i-1]) and re.match("[a-zA-Z0-9]", char):
                        quotestart = True
                    elif (i-1 == 0 and len(temp1)>1) and re.match("['\"]", temp1[i-1]) and re.match("[a-zA-Z0-9]", char):
                        quotestart = True
                for i, char in enumerate(temp1):
                    if i>1 and temp1[i-2] == ' ' and re.match("['\"]", temp1[i-1]) and re.match("[a-zA-Z0-9]", char):
                        temp1[i-1] = '" '
                    if i>1 and temp1[i-2] == "'" and re.match('"', temp1[i-1]) and char == ' ':
                        temp1[i-1] = ' "'

    # for char in temp1:
    #     cntr = 0
    #     if char == '"':
    #         cntr == 0
    # if cntr % 2 != 0:
    #     cntr = 0
    #
    #     for i, char in enumerate(temp1):
    #         if
    cntr = 0
    for i, char in enumerate(temp1):
        if re.search('"', char):
            cntr += 1
    # print("double counter:",cntr)
    if cntr % 2 != 0:
        instancecntr = 0
        for i, char in enumerate(temp1):
            if cntr == 1:
                if re.search('"', char):
                    temp1.pop(i)

            elif cntr > 1:

                if instancecntr == 0 and re.search('"', char):
                    instancecntr += 1
                elif instancecntr > 0 and re.search('"', char):
                    instancecntr += 1
                    if instancecntr < cntr:
                        temp1.pop(i)



    body = ''.join(temp1)
    # print("2:",body)
    # fix double spaces
    body = re.sub(r'\s+', ' ', body)




    # print("3:",body)

    # begin tokenization
    body = body.split()
    # arrange words and chars in sentence lists
    # and arrange sentence lists in body list
    sentences_list = []
    word_list = []
    for i, item in enumerate(body):
        match = re.match('[!.?]', item)
        if match:
            word_list.append(item)
            sentences_list.append(word_list)
            word_list = []
        else:
            word_list.append(item)
    sentences_list.append(word_list)

    # remove any wayward empty lists (especially at end)
    for i, sent in enumerate(sentences_list):
        if sent == []:
            sentences_list.pop(i)

    return sentences_list

def package_new_message(fromUserDb):
    """ takes loaded dict of 1 post from userdb. input is the dict from the userdb version. Tokens are arranged
        in lists in this format, splits based off spaces and removes extra spaces:
    ['Subject', [['This', 'is', 'a', 'sentence', '.'], ['Another', ',', 'sentence', '!']], 'tag tag', 'location', 'YYMMDD HHMMSS']
    """
    #####################################################
    # subject, body, tags, dtg, loc, sent, salt, id

    subj = fromUserDb['subject']
    body = fromUserDb['body']
    tags = fromUserDb['tags']
    dtg = fromUserDb['dtg']
    loc = fromUserDb['loc']
    sentiment = fromUserDb['sent']
    id = fromUserDb['id']
    # print(body)
    # tokenize body
    sentences_list = tokenize_text(body)

    # tokenize subject and tags
    subj = str_to_alphanumeric(subj, split=True)
    tags = str_to_alphanumeric(tags, split=True)

    # append everything to new list
    message = {}
    message['subject'] = subj
    message['body'] = sentences_list
    message['tags'] = tags
    message['dtg'] = dtg
    message['loc'] = loc
    message['sent'] = sentiment
    message['salt'] = 'none'
    message['id'] = id

    return message


def list_to_alphanumeric(message_list):
    """ Takes a list of strings, replaces @/& with at/and removes special
        chars (except . , ? ! $) and caps, preserves alphanumeric chars
        and spaces.
    Arguments:
        :message_list: List of strings for cleaning
    """
    # prepare for word only tokenization.
    # messages_joined = '. '.join(map(str, message_list))
    messages_cleaned = []
    for message in message_list:
        message = re.sub('[^a-zA-Z0-9 ]', '', message)
        message = re.sub(r'\s+', ' ', message).lower()
        messages_cleaned.append(message)
    return messages_cleaned

# def list_to_alphanum_preserve(message_list):
#     """ Takes a list of strings, replaces @/& with at/and preserves special chars
#         for punctuation, preserves alphanumeric chars and spaces.
#     Arguments:
#         :message_list: List of strings for cleaning
#     """
#     # prepare for word only tokenization.
#     # messages_joined = '. '.join(map(str, message_list))
#     messages_cleaned = []
#     for message in message_list:
#         message = re.sub('[^a-zA-Z0-9 ]', '', message)
#         message = re.sub(r'\s+', ' ', message).lower()
#         messages_cleaned.append(message)
#     return messages_cleaned

def str_to_alphanumeric(string, lower=False, split=False):
    """ Takes a string, removes special
        chars and caps, preserves alphanumeric chars
        and spaces.
    Arguments:
        :string: String for cleaning
    """
    string = re.sub('[^a-zA-Z0-9 ]', '', string)
    string = re.sub(r'\s+', ' ', string)

    if lower == True:
        string = string.lower()

    if string[0] == ' ':
        string = string[1:]

    if split == True:
        string = string.split()

    return string




def possent_withsubj(one_message):
    stopws = stopwords.words('english')
    prn_pre_pos = ['i', 'we', 'everyone', 'will', 'does', 'do']
    prn_pos_words = ['like', 'love', 'approve', 'vote', 'buy', 'purchase', 'do', 'does']

    tobe_pre_pos = ['is', 'are', 'am', 'the', 'a', 'an']
    tobe_pos_words = ['best', 'wonderful', 'awesome', 'great', 'good', 'spectacular', 'superior', 'favourable', 'favorable', 'commendable', 'tiptop', 'excellent', 'snazy', 'snazzy', 'superb', 'admirable', 'worthy', 'excellent', 'smart', 'intelligent', 'genius', 'magnificent']
    # cleaning
    body_cleaned = list_to_alphanumeric(one_message[1])
    subj_cleaned = str_to_alphanumeric(one_message[0])

    # get non-stop words for subject
    subj_tokens = []
    for word in word_tokenize(subj_cleaned):
        if word not in stopws:
            subj_tokens.append(word)

    ################################################################################
    # [['wer wer werrer', 'ertert ert ert', 'wer wer wer'], ['ertert ert ert', 'wer wer wer']]
    # get 1 list per sentence of body, in a list, words tokenized
    body_tokens = []

    # for word in word_tokenize()

    ###########################################################################################
    #body_cleaned = word_tokenize(body_cleaned)
    pos_count = 0
    # print("body_cleaned", body_cleaned)
    # this loop is for when any subject tokens are in the
    # same sentence as sentement words, only catches simple approvals
    # of the subject
    for sentence in body_cleaned:
        # temp tokenlist dumped for every new sentence
        tokenlist = []
        sent_has_subj = False
        for i, word in enumerate(word_tokenize(sentence)):
            # append words for this sentence
            tokenlist.append(word)

            if word in subj_tokens:
                sent_has_subj = True

            if i>0 and sent_has_subj and ((tokenlist[i-1] in prn_pre_pos and word in prn_pos_words) or (tokenlist[i-1] in tobe_pre_pos and word in tobe_pos_words)):
                # print(tokenlist[i-1], end=' ')
                # print(word)
                pos_count += 1

    # print("count:", pos_count)
    return 'nothing yet'

def split_sentences_tolist(body):
    """ Joins list sentences in a body list into one string for situations
        where split sentences is not needed (representative selection)
    """
    newlist = []
    for list in body:
        for word in list:
            newlist.append(word)

    return newlist




def hash_user_pass(userpass='password'):
    return sha256(userpass.encode('utf-8')).hexdigest()

def check_post_perms(messagedict, salt, passhash):
    """ checks for delete perms of a post, switches salt/id /none/none
        to recreate original hash condition when post was originally made

        postinuserdb['salt']
    """
    messagedict['salt'] = salt
    getid = messagedict['id']
    messagedict['id'] = 'none'

    dictstr = str(messagedict)

    verify_id = sha256((dictstr+passhash).encode('utf-8')).hexdigest()

    if getid == verify_id:
        result = "Match"
    else:
        result = "No Match"

    return result



# def newpost_to_userdb(subj, body, tags, dtg, loc, passhash):
#
#     id, salt = new_message_id(subj, body, tags, dtg, loc, passhash)
#
#     # tokenize and clean body
#     sentences_list = tokenize_text(body)
#     # tokenize and clean subject and tags
#     subj = str_to_alphanumeric(subj, split=True)
#     tags = str_to_alphanumeric(tags, split=True)
#
#
#     # prepare for id creation
#     dict = {
#         "subject": subj,
#         "body": body,
#         "tags": tags,
#         "dtg": dtg,
#         "loc": loc,
#         "sent": 0,
#         "salt": salt,
#     }
#
#     id, salt = new_message_id(subj, body, tags, dtg, loc, passhash)
#
#
#     return dict

def newpost_to_db2(subj, body, tags, dtg, loc, sent, passhash):
    """ Returns message dict with id (hashes id with user # id
        set to 'none'), salt
        returned dict is in the wild version, with salt set to
        none and id in place
    """

    salt = salt_maker()
    # tokenize and clean body
    sentences_list = tokenize_text(body)
    # tokenize and clean subject and tags
    subj = str_to_alphanumeric(subj, split=True)
    tags = str_to_alphanumeric(tags, split=True)


    # prepare for id creation
    dict = {
        "subject": subj,
        "body": sentences_list,
        "tags": tags,
        "dtg": dtg,
        "loc": loc,
        "sent": sent,
        "salt": salt,
        "id": 'none'
    }

    dictstr = str(dict)

    id = sha256((dictstr+passhash).encode('utf-8')).hexdigest()
    dict['salt'] = 'none'
    dict['id'] = id


    return dict, salt

def newPostToDb3(subj, alts, body, tags, loc, sent, passhash):
    """ Returns message dict with id (hashes id with user # id
        set to 'none'), salt
        returned dict is in the wild version, with salt set to
        none and id in place
    """

    salt = salt_maker()

    # tokenize and clean subject and tags
    subj = subjectWithPosTags(subj)
    alts = altsWithPosTags(alts)
    # tokenize and clean body
    sentences_list = tokenize_text(body)
    tags = tagsWithPosTags(tags)

    # timestamp is utc, no idea about daylight savings time
    timeStamp = datetime.now(tz=timezone.utc)
    timeStamp = str(timeStamp)
    ind = timeStamp.index(".")
    timeStamp = timeStamp[:ind]

    # prepare for id creation
    dicti = {
        "subject": subj,
        "alts": alts,
        "body": sentences_list,
        "tags": tags,
        "dtg": timeStamp,
        "loc": loc,
        "sent": sent,
        "salt": salt,
        "id": 'none'
    }

    # get double quotes instead of single, output is a str
    dictstr = json.dumps(dicti)
    # Hash our user id
    hashabledata = dictstr+passhash
    print(hashabledata)
    id = sha256((hashabledata).encode('utf-8')).hexdigest()
    dicti['salt'] = 'none'
    dicti['id'] = id

    return dicti, salt


def subjectWithPosTags(string, lower=False):
    """ Takes a string, removes special
        chars and caps, preserves alphanumeric chars
        and spaces. preserves the ~ pos tags from user entry
    Arguments:
        :string: String for cleaning
    """
    ## split by spaces here so the below can be sliced from ~
    prefix = string[:-3]
    suffix = string[-3:]
    # prefix = prefix.replace("-", "_")
    prefix = re.sub("[ ]+", " ", prefix)
    prefix = re.sub("[-]+", " ", prefix)
    prefix = re.sub("[_]+", " ", prefix)
    prefix = re.sub("[^a-zA-Z0-9' ]", '', prefix)
    string = prefix + suffix

    # string = re.sub(r'\s+', ' ', string)
    if lower == True:
        string = string.lower()

    if string[0] == ' ':
        string = string[1:]
    # string = string.replace(" ~", "~")

    string = string.split(" ")

    return string


def altsWithPosTags(stringslist, lower=False):
    """ Takes a list with strings, one string for each alt subject, same format as subject, removes special
        chars and caps, preserves alphanumeric chars
        and spaces. preserves the ~ pos tags from user entry
    Arguments:
        :string: String for cleaning
    """
    newstrlist = []
    for string in stringslist:

        ## split by spaces here so the below can be sliced from ~
        prefix = string[:-3]
        suffix = string[-3:]
        # prefix = prefix.replace("-", "_")
        prefix = re.sub("[ ]+", " ", prefix)
        prefix = re.sub("[-]+", " ", prefix)
        prefix = re.sub("[_]+", " ", prefix)
        prefix = re.sub("[^a-zA-Z0-9' ]", '', prefix)
        string = prefix + suffix
        if lower == True:
            string = string.lower()
        if string[0] == ' ':
            string = string[1:]
        # string = string.replace(" ~", "~")
        string = string.split(" ")
        newstrlist.append(string)

    return newstrlist


def tagsWithPosTags(string, lower=False):
    """ Takes a string, removes special
        chars and caps, preserves alphanumeric chars
        and spaces. preserves the ~ pos tags for every word
        outputs a list of tags
    Arguments:
        :string: String for cleaning
    """
    string = re.sub("[#]+", " ", string)
    string = re.sub("[ ]+", " ", string)
    string = re.sub("[-]+", " ", string)
    string = re.sub("[_]+", " ", string)
    splitString = string.split(" ")
    ## split by spaces here so the below can be sliced from ~
    newlist = []
    for word in splitString:
        prefix = word[:-3]
        suffix = word[-3:]
        # prefix = prefix.replace("-", "_")

        prefix = re.sub("[^a-zA-Z0-9']", '', prefix)
        if lower == True:
            prefix = prefix.lower()
        if prefix[0] == '_':
            prefix = prefix[1:]
        newWord = prefix + suffix
        newlist.append(newWord)
    # string = re.sub(r'\s+', ' ', string)
    # string = string.replace("_~", "~")
    return newlist

def subjPermutations(str):
    print("thing")
    pass

def json_to_file(json_listordict, folder='posts/'):
    """ input can be 1 dict, or a list of dicts,
        saves however many to file. if it's 1, filename
        is id name. if many, filneame is 'multi' followed
        by first post's id number. works with both post and message
        formats
    """
    if isinstance(json_listordict, dict):
        id = json_listordict['id']

        with open((folder + id + '.txt'), 'w') as outfile:
            json.dump(json_listordict, outfile)
    else:
        id = json_listordict[0]['id']
        with open((folder + 'multi_' + id + '.txt'), 'w') as outfile:
            for _ in json_listordict:
                # outfile.write(str(_) + '\n')
                json.dump(_, outfile)
                outfile.write('\n')

def salt_maker():
    dict = {0: ")", 1: "!", 2: "@", 3: "#", 4: "$", 5: "%", 6: "^", 7: "&", 8: "*", 9: "(", 10: "a", 11: "A", 12: "b", 13: "B", 14: "c", 15: "C", 16: "d", 17: "D", 18: "e", 19: "E", 20: "f", 21: "F", 22: "g", 23: "G", 24: "h", 25: "H", 26: "i", 27: "I", 28: "j", 29: "J", 30: "k", 31: "K", 32: "l", 33: "L", 34: "m", 35: "M", 36: "n", 37: "N", 38: "o", 39: "P", 40: "q", 41: "Q", 42: "r", 43: "R", 44: "s", 45: "S", 46: "t", 47: "T", 48: "u", 49: "U", 50: "v", 51: "V", 52: "w", 53: "W", 54: "x", 55: "X", 56: "y", 57: "Y", 58: "z", 59: "Z", 60: "O", 61: "p", 62: "?", 63: "/", 64: "<", 65: ">", 66: "{", 67: "}", 68: "[", 69: "]"}
    salt = ''

    while len(salt) < 64:
        # rand num or rand char?
        choice = randbelow(2)
        if choice == 0:
            randint = randbelow(10)
            salt += str(randint)
        else:
            randint = randbelow(70)
            salt += dict[randint]

    return salt

def new_message_id(subj, body, tags, dtg, loc, passhash):
    """ makes a unique message id, returns the message id and salt

        taking the following:
        subj = 'John Doe'
        body = 'John this is best sentence! lala falala.'
        tags = '$$spam $#ctuff%anythingatall'
        dtg = 'YYMMDD HHMMSS'
        loc = 'merica'
        sent = 0
        salt = '}1@J9mi036#s58Jq50ek49x@$139Y?67x061j5I5282}J0200Yv#6W47vj2EHL41'
    """
    salt = salt_maker()
    # make the id
    return sha256((salt+subj+body+tags+dtg+loc+passhash).encode('utf-8')).hexdigest(), salt


def new_message_id2(message, passhash):

    """ Takes the tokenized message dict and hashed user passwrod as input
        sets id to "none", puts the salt in the salt location, transfers
        the tokenized message returns the message id and salt

        input dict format:

        {"subject": = "John Doe"
        "body": = "John this is best sentence! lala falala."
        "tags": = "$$spam $#ctuff%anythingatall"
        "dtg": = "YYMMDD HHMMSS"
        "loc": = "merica"
        "sent": = 0
        "salt": = "}1@J9mi036#s58Jq50ek49x@$139Y?67x061j5I5282}J0200Yv#6W47vj2EHL41"
        "id": = "none"}
    """
    salt = salt_maker()
    # make the id
    return sha256((salt+subj+body+tags+dtg+loc+passhash).encode('utf-8')).hexdigest(), salt


def load_jsons_from_folder(filepath=''):
    """ load multiple json files in a folder into list, each line
        must be only a dict (dicts in a list in a file breaks it)
        format fro glob: filepath='posts/*.txt'
    """
    # 'posts/*.txt'
    all_files = glob.glob(filepath)
    # this will read a bunch of files into a list
    raw_lines = []
    for _ in all_files:
        # open it
        with open(_,'r') as json_file:
            # get the line count of each file
            # format for line counting
            cntr = 0
            splitfile = json_file.read()
            lineslist = splitfile.split('\n')
            # count the lines
            for i in lineslist:
                if i:
                    cntr += 1

            # get dicts from files with 1 dict
            if cntr == 1 and lineslist[0] != '':
                # append to the list
                for item in lineslist:
                    data = json.loads(item)
                    raw_lines.append(data)
            # get dicts from files with more than 1 dict
            elif cntr > 1:

                # remove empty lines
                for i, string in enumerate(lineslist):
                    if string == '':
                        lineslist.pop(i)

                # append to the list
                for item in lineslist:
                    data = json.loads(item)
                    raw_lines.append(data)

    return raw_lines


def json_from_file(filepath=''):
    """ loads one json from a file, any number of lines allowed
        each line, must be only a dict (dicts in a list in a file breaks it)
        if file len was 1, returns just that dict in dict type,
        if len was > 1, returns list with dicts inside
    """

    with open(filepath, 'r') as json_file:
        raw_lines = []
        cntr = 0
        splitfile = json_file.read()
        lineslist = splitfile.split('\n')
        # count the lines
        for i in lineslist:
            if i:
                cntr += 1

        if cntr == 1 and lineslist[0] != '':
            for item in lineslist:
                raw_lines = json.loads(item)

        elif cntr > 1:

            # remove empty lines
            for i, string in enumerate(lineslist):
                if string == '':
                    lineslist.pop(i)

            # append to the list
            for item in lineslist:
                data = json.loads(item)
                raw_lines.append(data)

    return raw_lines


def tokendict_to_list(input_dict):
    """ converts dict (loaded jason) in message format
        to lists in message format
    """
    # outs each sentence str in body in a temp list
    message_list = []
    body_list = []
    for item in input_dict['body']:
        body_list.append(input_dict['body'][item])
    # splits at ' ' each word in each sentence, keeping sentences
    # in their own lists, and puts it all in another list
    body_list2 = []
    for sent in body_list:
        sent = sent.split()
        body_list2.append(sent)
    # apends each string and the body list to the empty message_list
    for item in input_dict:
        if item != 'body':
            message_list.append(input_dict[item])
        else:
            message_list.append(body_list2)

    return message_list


def tokens_to_str(message, section='body'):
    """ Takes one section of a message as specified by key param and
        returns it in string format to be joined with other messages
        for summarization, printing, id creation (future).
    """

    body = message[section]
    new_mess = ''
    if isinstance(body[0], list):

        for sentence in body:
            for word in sentence:
                new_mess += (word + ' ')

        # put chars in list for easy processing
        interim_mess = []
        for char in new_mess:
            interim_mess.append(char)

        # push some chars to the left
        for i, char in enumerate(interim_mess):
            if i>0:
                match = re.match('[!.,?)]', char)
                if match and interim_mess[i-1] == ' ':
                    interim_mess.pop(i-1)

        # push some chars to the right
        for i, char in enumerate(interim_mess):
            if i>0:
                match = re.match('[$(]', interim_mess[i-1])
                if match and char == ' ':
                    interim_mess.pop(i)
    elif section == 'tags':
        interim_mess = ' #'.join(body)
        interim_mess = '#' + interim_mess
    else:
        # put chars in list for easy processing
        interim_mess = ' '.join(body)

    return ''.join(interim_mess)


def one_representative_message(message_list):
    """ Gets and returns message that is the most representative
        out of a list of messages. Cleaning occurs in this function.

        OLD VERSION*****************************

    Arguments:
        :message_list: List of strings for analysis
    """
    stopws = stopwords.words('english')
    messages_cleaned = list_to_alphanumeric(message_list)

    word_freqs = {}
    # gets unique words out of the entire group of messages
    # and puts them in a dict, starting with a count of 0 for each for now
    for message in messages_cleaned:
        # print(message)
        for word in word_tokenize(message):
            if word not in stopws:
                if word not in word_freqs.keys():
                    word_freqs[word] = 0


    # get the word counts, anti-ballot stuffing in place
    for message in messages_cleaned:
        # reset words used list at start of every new message
        words_used = []
        for word in word_tokenize(message):
            if word in word_freqs and word not in words_used:
                word_freqs[word] += 1
                words_used.append(word)
    # print(word_freqs)

    # find word with max freq
    max_freq = max(word_freqs.values())

    # remove emphasis coming from words with a count of 1 in statements that were popular
    for key in word_freqs:
        if word_freqs[key] == 1:
            word_freqs[key] = 0

    # this is called "weighted frequencies"
    for word in word_freqs.keys():
        # when we call the iterator inside a dict brackets, it references the value
        # mod all occurance counts to be the count/maxcount
        word_freqs[word] = (word_freqs[word]/max_freq)

    #prepare messages_list for final ranking
    messages_ranked = {}
    for message in message_list:
        # fyi, because this is a dict, messages taht are repeated verbatim are only
        # put in here as a key once. No problem, as the word counts were made
        # on the entire corpus, and thus verbatim repeated messages, earlier
        messages_ranked[message] = 0.0

    # get our ranking, e-democratic confederalism in action
    # for each message in the messages_ranked list (all messages start at 0):
    for message in messages_ranked:
        # for each word in each message (fyi, the .lower() propagates to all below levels):
        # use the words used thing again to anihilate single post ballot stuffing
        words_used = []
        for word in word_tokenize(message.lower()):
            # we take the messages_ranked word and iterate against every word in word_freqs
            for ranked_word in word_freqs:
                # if the words match, cumulatively add the rank to the message total
                if word == ranked_word and word not in words_used:
                    messages_ranked[message] += word_freqs[ranked_word]
                    words_used.append(word)

    # split the dict to lists to find the ones with the highest ranking
    keys = list(messages_ranked.keys())
    values = list(messages_ranked.values())

    final_max_freq = max(values)

    index_matches = []
    for i, match in enumerate(values):
        if match == final_max_freq:
            index_matches.append(i)

    # return the top matches (need them all to make sure an outlier didn't get lucky)
    result = []
    for i, value in enumerate(values):
        if value == final_max_freq:
            result.append(keys[i])

    # choose the most representative message that had the fewest chars
    minlen = len(result[0])
    min_index = 0
    for i, message in enumerate(result):
        newlen = len(message)
        if newlen < minlen:
            minlen = newlen
            min_index = i
        final_result = result[min_index]

    return final_result

def pack_for_nlp(section='body'):

    bunch = load_jsons_from_folder(filepath='posts/*.txt')
    bodylist = []
    for json in bunch:
        bodylist.append(json[section])
        # print(json[section])
        # print()
    return bodylist


def most_representative(message_list):
    """ Gets and returns message that is the most representative
        out of a list of messages. Cleaning occurs in this function.
    Arguments:
        :message_list: List of strings for analysis
    """
    stopws = stopwords.words('english')
    messages_cleaned = list_to_alphanumeric(message_list)

    word_freqs = {}
    # gets unique words out of the entire group of messages
    # and puts them in a dict, starting with a count of 0 for each for now
    for message in messages_cleaned:
        # print(message)
        for word in word_tokenize(message):
            if word not in stopws:
                if word not in word_freqs.keys():
                    word_freqs[word] = 0


    # get the word counts, anti-ballot stuffing in place
    for message in messages_cleaned:
        # reset words used list at start of every new message
        words_used = []
        for word in word_tokenize(message):
            if word in word_freqs and word not in words_used:
                word_freqs[word] += 1
                words_used.append(word)
    # print(word_freqs)

    # find word with max freq
    max_freq = max(word_freqs.values())

    # remove emphasis coming from words with a count of 1 in statements that were popular
    for key in word_freqs:
        if word_freqs[key] == 1:
            word_freqs[key] = 0

    # this is called "weighted frequencies"
    for word in word_freqs.keys():
        # when we call the iterator inside a dict brackets, it references the value
        # mod all occurance counts to be the count/maxcount
        word_freqs[word] = (word_freqs[word]/max_freq)

    #prepare messages_list for final ranking
    messages_ranked = {}
    for message in message_list:
        # fyi, because this is a dict, messages taht are repeated verbatim are only
        # put in here as a key once. No problem, as the word counts were made
        # on the entire corpus, and thus verbatim repeated messages, earlier
        messages_ranked[message] = 0.0

    # get our ranking, e-democratic confederalism in action
    # for each message in the messages_ranked list (all messages start at 0):
    for message in messages_ranked:
        # for each word in each message (fyi, the .lower() propagates to all below levels):
        # use the words used thing again to anihilate single post ballot stuffing
        words_used = []
        for word in word_tokenize(message.lower()):
            # we take the messages_ranked word and iterate against every word in word_freqs
            for ranked_word in word_freqs:
                # if the words match, cumulatively add the rank to the message total
                if word == ranked_word and word not in words_used:
                    messages_ranked[message] += word_freqs[ranked_word]
                    words_used.append(word)

    # split the dict to lists to find the ones with the highest ranking
    messages_ranked = orderdictoffvalues(messages_ranked)

    return messages_ranked

def basicstopwords():
    return ['a', 'an', 'the', 'of', 'from', 'at', 'in', 'he', 'she', 'they', 'them', 'her', 'him', 'his', 'hers', 'this', 'that', 'you', 'me', 'i', "im", 'is']

def charslist():
    return ['.', '!', '?', ',', '.', '@', '&', '$', '%', "'", '"', '*', '-', '+', '=', '<', '>', '/']

def bestrep_fromgroup_unigram(message_list, cutoffbelow=0, weights=True):
    """ Gets and returns message that is the most representative
        out of a list of messages. accepts sentences joined of tokens ( the
        tokens are still tokenized, just put multiple sentences in same list, one user's
        message per list, all tokenized)

        **** bodies with multiple sentences have to have sentences
        joined before being out into this function or it will not work***
        **** USE THIS ONE ********

    Arguments:
        :message_list: List of strings for analysis
    """
    stopws = basicstopwords()
    punct = charslist()
    # messages_cleaned = list_to_alphanumeric(message_list)
    word_freqs = {}
    # gets unique words out of the entire group of messages
    # and puts them in a dict, starting with a count of 0 for each for now
    for message in message_list:
        # print(message)
        for word in message:
            word = word.lower().replace("'", "")
            if word not in stopws and word not in punct:
                if word not in word_freqs.keys():
                    word_freqs[word] = 0
    # print(message_list)

    # get the word counts, anti-ballot stuffing in place
    # getting unique words per message
    for message in message_list:
        # reset words used list at start of every new message
        words_used = []
        for word in message:
            word = word.lower().replace("'", "")
            if word in word_freqs and word not in words_used:
                word_freqs[word] += 1
                words_used.append(word)


    # find word with max freq
    max_freq = max(word_freqs.values())

    # bind the word freqs into a range 0-1, needed until we can figure out how to weight
    # by math and not a dict, later. possible to modify the weight dict values on the fly via
    # range binding the keys/values to the dataset values...
    # for word in word_freqs.keys():
    #     # when we call the iterator inside a dict brackets, it references the value
    #     # mod all occurance counts to be the count/maxcount
    #     word_freqs[word] = (word_freqs[word]/max_freq)

    # range binding individual word freqs to 0.0 - 100.0, so it is compatible with weights,
    # which are 0.0 - 100.0 format
    for word in word_freqs:
        word_freqs[word] = round((word_freqs[word]/max_freq)*100, 1)

    # print("word freqs bound to 0 - 100:",word_freqs)
    ######
    # range bind our weights to our dataset to keep absolute values until the end
    # note, when tweaking this, make sure the original curve len and moddedcurve len match!
    # the rounding will cause erroneaus same values to self delete (dict probs)

    # print("orig curve len",len(curve.keys()))
    # moddedcurve = {}
    # # print(curve)
    # for key in curve:
    #     newkey = round((max_freq/100)*key, 4)
    #     val = curve[key]
    #     newval = round((max_freq/100)*val, 4)
    #
    #     moddedcurve[newkey] = newval

    # print("moddedcurve",moddedcurve)
    # print()
    # print(len(moddedcurve.keys()))
    # print()
    # print("word freqs 0-1 b4 cutoff:",word_freqs)
    if cutoffbelow > 0:
        for word in word_freqs:
            if word_freqs[word] <= cutoffbelow:
                word_freqs[word] = 0


    # print()
    # print("word freqs 0-1 after cutoff, after 0.0 - 100.0 binding, before weighting:",word_freqs)
    # print()
    # apply weights
    # apply curve weights, smooth in, smooth out (emphasize highsfreqs, de-emphasize lowfreqs)
    # if weights == True:
    #     # curve = smoothinout()
    #     for key in word_freqs:
    #         # keyold = round((word_freqs[key]*100),1)
    #         value = word_freqs[key]
    #         word_freqs[key] = moddedcurve[value]


    if weights == True:
        curve = smoothinout()
        for key in word_freqs:
            value = word_freqs[key]
            word_freqs[key] = curve[value]


    # print()
    # print("word freqs after weighting",word_freqs)
    # put the final weights in a range 0-1:
    # maxi = 0
    # for message in word_freqs:
    #     new = message[1]
    #     print(new)
    #     maxi = max(new, maxi)
    # for message in word_freqs:
    #     message[1] = message[1]/maxi


    #prepare messages_list for final ranking
    messages_ranked = []
    for message in message_list:
        # each index corresponds each message in original dict, but as list
        messages_ranked.append(0)
    # print("words ranked:",word_freqs)
    # get our ranking, e-democratic confederalism in action
    # for each message in the messages_list list (all messages start at 0):
    for i, message in enumerate(message_list):
        # for each word in each message (fyi, the .lower() propagates to all below levels):
        # use the words used thing again to anihilate single post ballot stuffing
        words_used = []
        for word in message:
            word = word.lower().replace("'", "")
            if word in word_freqs and word not in words_used:
                # we take the messages_ranked word and iterate against every word in word_freqs
                for ranked_word in word_freqs:
                    # if the words match, cumulatively add the rank to the message total
                    if word == ranked_word and word not in words_used:
                        messages_ranked[i] += word_freqs[ranked_word]
                        words_used.append(word)

    # putting them in a list
    rankedlist = []
    i = 0
    for i, rank in enumerate(messages_ranked):
        messageandrank = []
        # appends message, then rank in that order per messageandrank
        messageandrank.append(message_list[i])
        messageandrank.append(messages_ranked[i])
        rankedlist.append(messageandrank)


    # bind entire ranking to 0 - 1
    maxi = 0
    for message in rankedlist:
        new = message[1]
        maxi = max(new, maxi)
    # print("maxi:",maxi)
    for message in rankedlist:
        message[1] = round(message[1]/maxi, 4)
    # print()
    # print("ranked but not ordered",rankedlist)
    # print()
    # split the dict to lists to find the ones with the highest ranking

    finalthing = orderlistofranks(rankedlist)

    return finalthing

def orderlistofranks(listofranks):
    """ takes format: [[['word', 'stuff'], 0.75], [['thing', 'it'], 0.15], [['an', 'of'], 0.1]]
        orders them correctly by rank
    """
    sents = []
    ranks = []
    for sent in listofranks:
        sents.append(sent[0])
        ranks.append(sent[1])

    rankedlist = []

    for i in range(len(listofranks)):
        rankedmess = []
        maxi = max(ranks)
        indexofmax = ranks.index(maxi)
        rankedmess.append(sents[indexofmax])
        rankedmess.append(ranks[indexofmax])
        rankedlist.append(rankedmess)
        ranks.pop(indexofmax)
        sents.pop(indexofmax)

    return rankedlist


def orderdictoffvalues(dict):
    """ Assuming each key has a value that is a number,
        split keys from values, put in lists, reorder with that

    """
    keys = list(dict.keys())
    values = list(dict.values())
    # just in case the list is messeed up
    if len(keys) != len(values):
        newdict = "missing key or value"
    else:
        newdict = {}
        for i in range(len(values)):
            maxi = max(values)
            indexofmax = values.index(maxi)
            newdict[keys[indexofmax]] = values[indexofmax]
            values.pop(indexofmax)
            keys.pop(indexofmax)
    return newdict


# def one_lookslike_these(messagegroup, onemessage):
#     """ onemessage is compared to messagegroup, the group is ranked for similarity to onemessage
#     Arguments:
#         :message_list: List of strings for analysis
#     """
#     stopws = stopwords.words('english')
#     messages_cleaned = list_to_alphanumeric(message_list)
#
#     word_freqs = {}
#     # gets unique words out of the entire group of messages
#     # and puts them in a dict, starting with a count of 0 for each for now
#     for message in messages_cleaned:
#         # print(message)
#         for word in word_tokenize(message):
#             if word not in stopws:
#                 if word not in word_freqs.keys():
#                     word_freqs[word] = 0
#
#
#     # get the word counts, anti-ballot stuffing in place
#     for message in messages_cleaned:
#         # reset words used list at start of every new message
#         words_used = []
#         for word in word_tokenize(message):
#             if word in word_freqs and word not in words_used:
#                 word_freqs[word] += 1
#                 words_used.append(word)
#     # print(word_freqs)
#
#     # find word with max freq
#     max_freq = max(word_freqs.values())
#
#     # remove emphasis coming from words with a count of 1 in statements that were popular
#     for key in word_freqs:
#         if word_freqs[key] == 1:
#             word_freqs[key] = 0
#
#     # this is called "weighted frequencies"
#     for word in word_freqs.keys():
#         # when we call the iterator inside a dict brackets, it references the value
#         # mod all occurance counts to be the count/maxcount
#         word_freqs[word] = (word_freqs[word]/max_freq)
#
#     #prepare messages_list for final ranking
#     messages_ranked = {}
#     for message in message_list:
#         # fyi, because this is a dict, messages taht are repeated verbatim are only
#         # put in here as a key once. No problem, as the word counts were made
#         # on the entire corpus, and thus verbatim repeated messages, earlier
#         messages_ranked[message] = 0.0
#
#     # get our ranking, e-democratic confederalism in action
#     # for each message in the messages_ranked list (all messages start at 0):
#     for message in messages_ranked:
#         # for each word in each message (fyi, the .lower() propagates to all below levels):
#         # use the words used thing again to anihilate single post ballot stuffing
#         words_used = []
#         for word in word_tokenize(message.lower()):
#             # we take the messages_ranked word and iterate against every word in word_freqs
#             for ranked_word in word_freqs:
#                 # if the words match, cumulatively add the rank to the message total
#                 if word == ranked_word and word not in words_used:
#                     messages_ranked[message] += word_freqs[ranked_word]
#                     words_used.append(word)
#
#     # split the dict to lists to find the ones with the highest ranking
#     messages_ranked = orderdictoffvalues(messages_ranked)
#
#     return messages_ranked


def joinsentences(message, section='body'):
    """ For when we want to join multiple sentences of tokens
        into one list of sentences to consider the entire message/body in one loop
        takes a dict, section specifies which section to use
        also takes a list, function figures out which automatically.
        maintains tokenization
        float, int, str, list, dict, tuple
    """
    # for when the input is a dict
    if isinstance(message, dict):
        body = message[section]
    # for when message is a list
    elif isinstance(message, list):
        body = message

    # for when lists are inside
    newlist = []
    if isinstance(body[0], list):
        for list1 in body:
            for word in list1:
                newlist.append(word)
    # for when there is only 1 sentence inside
    elif isinstance(body[0], str):
        newlist = body

    return newlist


def joinsentenceslooped(message, section='body'):
    """ loops the join sentences so no matter how many lists there
        are, it gets rid of all the unecesary ones
    """
    thething = joinsentences(message=message, section=section)
    listinside = True
    while listinside:
        thething = joinsentences(thething, section=section)
        if isinstance(thething[0], str):
            listinside = False

    return thething



# def verbwork(findme, lemmatize=False):
#     """ input is one word, once a pos tag directs
#         flow to a verb, if we are lemmatizing, it gets the lemma str,
#         if we are searching, we get all verb forms and return a list.
#     """
#     # list1 = verbdict()
#
#     # file = open('functions/dictionaries/csv/verbdict2.txt')
#     cntr = 0
#     with open('functions/dictionaries/verbdict24.txt') as file:
#         for line in file:
#             print(line.rstrip().split(","))
#             cntr+=1
#             if cntr > 10:
#                 break
#                 # line = line.rstrip().split(',')
#         # print(line)

        # if findme in line:
        #     findmeindex = line.index(findme)
        #     if (findmeindex != 0 or findme == line[0]) and lemmatize == True:
        #         return line[0]
        #     else:
        #         return line
        # else:
        #     return findme


def getngrams(body, n=2, filterchars=True, filterstops=False):
    """ takes a list of lists, each interior list needs to have word tokens
        in it already.
    """

    newbody = filtertokens(body, filterstops=filterstops, filterchars=filterchars)
    # newbody = body
    # if n==2:
    ngrambody = []
    for j, sentence in enumerate(newbody):
        ngramsent = []
        for i, token in enumerate(sentence):
            if len(sentence) <= n:
                # string = ''
                # for u in range(len(sentence)-1):
                #     string += sentence[u] + ' '
                ngramsent.append(" ".join(sentence))
                break
            elif i > (len(sentence)-1) - n and i != len(sentence)-1:
                check = sentence[-1]
                checklen = len(check)
                if len(ngramsent)>0 and check != ngramsent[-1][-checklen:]:
                    string = ''
                    for u in range((len(sentence)-1) - i):
                        string += sentence[i+u] + ' '
                    ngramsent.append(string + sentence[i+u+1])
            elif i+(n-1) <= len(sentence)-(n-1):
                string = ''
                for u in range(n-1):
                    string += sentence[i+u] + ' '
                ngramsent.append(string + sentence[i+u+1])
            elif i==0:
                string = ''
                for u in range(n-1):
                    string += sentence[i+u] + ' '
                ngramsent.append(string + sentence[i+u+1])

            # elif i == len(sentence)-1:
            #     check = sentence[-1]
            #     checklen = len(check)
            #     if check != ngramsent[i-1][-checklen:]:
            #     #     for u in range(len(sentence)-1):

        ngrambody.append(ngramsent)
    return ngrambody

def postags(sentence):
    """ takes (sentence) list of word tokens
        unindexedreturn is list of sentence lists [sentence list][word/tag set][0=word, 1=pos]
    """
    newdoc = nltk.pos_tag(sentence)

    return newdoc


def lemmatize(message):
    """ insert only words in sentence lists, that have been run thru the postags(),
        it adds pos tags and outputs tuples in a list
    """
    lemmatizer = WordNetLemmatizer()
    # sentence = postags(message)

    emptysentence = []
    for wordset in sentence:
        if wordset[1][0] == 'N':
            pos = 'n'
        elif wordset[1][0] == 'J':
            pos = 'a'
        elif wordset[1][0] == 'R':
            pos = 'r'
        elif wordset[1][0] == 'V':
            pos = 'v'
        else:
            pos = ''
        if pos != '':
            # print("lemmad:",lemmatizer.lemmatize(wordset[0].lower(), pos=pos))
            newtuple = (wordset[0], wordset[1], lemmatizer.lemmatize(wordset[0], pos=pos))
        else:
            newtuple = (wordset[0], wordset[1], lemmatizer.lemmatize(wordset[0]))
        emptysentence.append(newtuple)

    return emptysentence

def charcount(string, char=' '):
    cntr = 0
    for item in string:
        if char == item:
            cntr +=1
    return cntr


def filtertokens(input, filterstops=True, filterchars=True):
    """ will combine tokenized lists inside a list. options for stop word and char filters
    """
    stoplist = stopwords.words('english')
    if filterstops:
        filtered = [[word.lower() for word in document if word not in stoplist] for document in input]
    if filterchars:
        filtered = [[word.lower() for word in document if re.search("[a-zA-Z0-9']", word)] for document in input]

    return filtered


def weightedwordfreqs(input):
    """ input must be entire group of bodies for comparison. aka, the function operates on the data in a
        [['string', 'string'], ['string', 'string'], ['string', 'string']] format. must be de-special charred
        and de-stopped if need be
        returns a dict of unique words as keys, with weighted counts as values
    """



    # store it in magical dictionary object
    dictionary = corpora.Dictionary(input)

    # function:
    wordsAndKeys = dictionary.token2id
    keysAndCounts = dictionary.cfs
    for key in wordsAndKeys:
        # print(key)
        # print(wordsAndKeys[key])
        if wordsAndKeys[key] in keysAndCounts:
            wordsAndKeys[key] = keysAndCounts[wordsAndKeys[key]]

    # now put them in order
    maxCnt = 0
    for key in wordsAndKeys:
        value = wordsAndKeys[key]
        maxCnt = max(value, maxCnt)
    wordCountsOrdered = {}

    # reverse the range with -1, and reverse and jack with the start and stop
    for cnt in range(maxCnt, 0, -1):
        for key in wordsAndKeys:
            if cnt == wordsAndKeys[key]:
                wordCountsOrdered[key] = cnt

    # get weighted average
    for key in wordCountsOrdered:
        wordCountsOrdered[key] = wordCountsOrdered[key]/maxCnt

    return wordCountsOrdered
