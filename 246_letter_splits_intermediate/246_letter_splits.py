# https://www.reddit.com/r/dailyprogrammer/comments/3xye4g/20151223_challenge_246_intermediate_letter_splits/

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def find_combinations(nums, index=0):
    collection = []
    two_stepped = False
    while index != len(nums)-1:
        combinations = []
        for n in xrange(0, len(nums)):
            if n >= index and two_stepped is False:
                r = n+2
                if int(nums[n:r]) < len(alpha):
                    combinations.append(alpha[int(nums[n:r])-1])
                    two_stepped = True
                else:
                    combinations.append(alpha[int(nums[n:r-1])-1])
                    two_stepped = False
            else:
                two_stepped = False
                if n < index:
                    r = n+1
                    combinations.append(alpha[int(nums[n:r])-1])
        index += 1
        collection.append(combinations)
    return collection


for line in open('number_codes', 'r').readlines():
    combos = find_combinations(line.strip())
    print "Input: %s" % line.strip()
    for c in combos:
        print "".join(c)
