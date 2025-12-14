import collections
def repeatedChars(word, partitions = 2):
    """
    :type word: str
    """
    w_size = len(word)
    if w_size == 1 or w_size % partitions != 0:
        return False

    word_substrs = []
    part_size = int(w_size/partitions)
    for part in range(0, partitions):
        word_substr = word[part * part_size : (part+1 % partitions) * part_size]
        word_substrs.append(word_substr)
    

    # print(word_substrs)
    rep_word = word_substrs[0]

    return all([word_substrs[i] == rep_word for i in range(0, partitions)])


if __name__ == '__main__':
    t_input = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'''
    d_input = '''194-253,81430782-81451118,7709443-7841298,28377-38007,6841236050-6841305978,2222204551-2222236166,2623-4197,318169-385942,9827-16119,580816-616131,646982-683917,147-181,90-120,3545483464-3545590623,4304-5747,246071-314284,8484833630-8484865127,743942-795868,42-53,1435-2086,50480-60875,16232012-16441905,94275676-94433683,61509567-61686956,3872051-4002614,6918792899-6918944930,77312-106847,282-387,829099-1016957,288251787-288311732,6271381-6313272,9877430-10095488,59-87,161112-224439,851833788-851871307,6638265-6688423,434-624,1-20,26-40,6700-9791,990-1307,73673424-73819233'''
    cases = d_input.split(',')
    # print(cases)
    # result = repeatedChars('123123123', 3)
    # print(result)
    totalSum = 0
    for case in cases:
        lower_interval = int(case.split('-')[0])
        uper_interval = int(case.split('-')[1]) + 1
        for word in range(lower_interval, uper_interval):
            for divs in range(2, len(str(word)) + 1):
                if repeatedChars(str(word), divs):
                    totalSum += word
                    break;

    # result = main(case_1)
    print(totalSum)