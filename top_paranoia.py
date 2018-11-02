"""
Paranoia

ByteCorp is a famous technological company in Byteania. The CEO of ByteCorp
doesn't trust anyone and thinks that his accountant managed to move huge
amounts of money to a competitor company, MegaCorp. He hires a computer crime
investigator, and asks him to find inconsistencies in the money transfers.

Here is a sample transaction log of the company:
Feb SLR 4 M
Feb ENT 800 K
Mar SLR 4000 K
Mar ENT 800 K
Apr SLR 4010 K
Apr ENT 810 K

There are four columns:
1. Month of the transaction
2. Reason of the expense
(SLR for "salary", ENT for "entertainment", OTR for "other")
3. Amount
4. M, K, or B (M for million, K for thousands, B for billion)

In the example above, April expenses show an inconsistency and should be
reported.

Another example:
Jul SLR 4 M
Jul ENR 800 K
Jul OTR 1200 K
Aug SLR 4000 K
Aug ENR 800 K
Aug OTR 1190 K
Sep SLR 4000 K
Sep ENR 800 K
Sep OTR 1190 K

Here, July expenses show an inconsistency and should be reported..

As the computer investigator, write a program, which reads the transaction
logs, detects inconsistent expenses and prints the exact month containing the
"unusual" activities.

The number of lines in the transaction log, as well as the reasons, are not
fixed and can contain other values.
"""

"""
INPUT INSTRUCTION FOR SOLOLEARN

Input logs line by line in such way:

Feb SLR 4 M
Feb ENT 800 K
Mar SLR 4000 K
Mar ENT 800 K
Apr SLR 4010 K
Apr ENT 810 K
end

(last laine must be 'end')
Or you may input only "test", for pre-install test input.
"""


class MonthTransactions():
    """
    This class contain month name and ammounts of different transactions.
    """
    def __init__(self, month):
        self.name = month
        self.reasons_ammount = {}

    def __str__(self):
        result = ''
        for reason in self.reasons_ammount:
            transaction = "\n{} {} {}".format(
                self.name, reason, str(self.reasons_ammount[reason]))
            result = result + transaction
        return result


def count_ammount(ammount_parts):
    """Count digital number of transaction from log cipher '400 K'"""
    amount_letter = {'K': 10**3, 'M': 10**6, 'B': 10**9}
    result = int(ammount_parts[0]) * amount_letter[ammount_parts[1]]
    return result


def add_log(log_list):
    """Add new log in log base"""
    reason = log_list[1]
    if reason not in REASONS_LIST:
        REASONS_LIST.append(reason)
    ammount = count_ammount(log_list[2:])
    month = log_list[0]
    if month not in LOG_BASE:
        temp = MonthTransactions(month)
    else:
        temp = LOG_BASE[month]
    temp.reasons_ammount[reason] = ammount
    LOG_BASE[month] = temp


def inconsistencies_search():
    """Search inconsistencies in transactions"""
    for reason in REASONS_LIST:
        # Create ammount list from same type transactions from all months.
        compare_ammoutn_list = []
        for month in LOG_BASE:
            reason_ammount = LOG_BASE[month].reasons_ammount[reason]
            compare_ammoutn_list.append(reason_ammount)
        # Check if transaction of current month is alone ammount in the list.
        for month in LOG_BASE:
            reason_ammount = LOG_BASE[month].reasons_ammount[reason]
            if compare_ammoutn_list.count(reason_ammount) == 1:
                print(f"\nAlarm! Find inconsistencies in {month} transfers!")


def lauch_test():
    """Test program input"""
    temp = MonthTransactions('Feb')
    temp.reasons_ammount = {
        'SLR': count_ammount(['4', 'M']),
        'ENT': count_ammount(['800', 'K']),
        'OTR': count_ammount(['1200', 'K'])}
    LOG_BASE['Feb'] = temp
    temp = MonthTransactions('Aug')
    temp.reasons_ammount = {
        'SLR': count_ammount(['4000', 'K']),
        'ENT': count_ammount(['800', 'K']),
        'OTR': count_ammount(['1190', 'K'])}
    LOG_BASE['Aug'] = temp
    temp = MonthTransactions('Sep')
    temp.reasons_ammount = {
        'SLR': count_ammount(['4000', 'K']),
        'ENT': count_ammount(['800', 'K']),
        'OTR': count_ammount(['1190', 'K'])}
    LOG_BASE['Sep'] = temp
    test_reason_list = ['SLR', 'ENT', 'OTR']
    for month in LOG_BASE:
        print(LOG_BASE[month])
    return test_reason_list


if __name__ == '__main__':
    # global LOG_BASE, REASONS_LIST
    LOG_BASE, REASONS_LIST = {}, []
    print("Input log, line by line. When you done input 'end'.\n\
You may input 'test' for pre-install test input.")
    while True:
        INPUT_LOG = input()
        if INPUT_LOG == 'end':
            break
        if INPUT_LOG == 'test':
            REASONS_LIST = lauch_test()
            break
        else:
            INPUT_LIST = list(INPUT_LOG.split(' '))
            add_log(INPUT_LIST)
    inconsistencies_search()
