def helper(s, slate, result):
    if len(slate) == len(s):
        result.append(slate)
        return result

    else:
        print(len(s))
        print(len(slate))
        i = len(slate)
        if s[i].isalpha():
            helper(s, s[i].lower() + slate, result)
            helper(s, s[i].upper() + slate, result)
        else:
            helper(s, s[i] + slate, result)

def combination(s):
    result = []
    slate = ""
    helper(s, slate, result)
    print(result)


s = "a1b2"
combination(s)