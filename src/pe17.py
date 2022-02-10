############################################################################################################################
#
# Problem 17
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
# in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 
# 20 letters. The use of "and" when writing out numbers is in compliance with 
# British usage.
############################################################################################################################

def countNums(n, nums):
    '''Count the total number of letters of every number from 1 to n'''
    
    count = 0
    
    for i in range(n+1):
        # Count all the keys
        if i in nums.keys():
            count += len(nums[i])

        elif i in range(21,100) and i not in nums.keys():
            # Get first and second digits
            w = nums[(i//10) * 10] + nums[i%10]
            count += len(w)

        elif i in range(101,1000):
            # Get first digit
            w = nums[(i//100) * 100] + 'and'

            # Numbers like 111, 112, ..., 119
            if i % 100 in nums.keys():
                w += nums[i % 100]
            else:
                # Get second and thrid digits
                w += nums[(i//10) % 10 * 10] +  nums[i%10]
            count += len(w)
            
    return count

if __name__ == "__main__":
    nums = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
        10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen',
        17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty',
        60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'onehundred', 200:'twohundred', 300:'threehundred',
        400:'fourhundred', 500:'fivehundred', 600:'sixhundred', 700:'sevenhundred', 800:'eighthundred',
        900:'ninehundred', 1000:'onethousand'}
    
    print(countNums(1000, nums))


    '''
    ############################################################################################################################
    #
    # Hideous Brute Force Approach
    #
    ############################################################################################################################
    ones = ['one','two','three','four','five','six','seven','eight','nine']
    tens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens2 = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    hundred = 'hundred'
    thousand = 'thousand'


    count = 0

    # Count 1-9
    for i in ones:
        count += len(i)

    # Count 10-19
    for i in tens:
        count += len(i)

    # Count 20-99
    for i in tens2:
        count += len(i)
        for j in ones:
            count += len(i+j)

    # Count 100-999 with the extra 'and'
    for h in ones:
        h += hundred
        count += len(h)

        # Count 1-9
        for i in ones:
            count += len(h+'and'+i)

        # Count 10-19
        for i in tens:
            count += len(h+'and'+i)

        # Count 20-99
        for i in tens2:
            count += len(h+'and'+i)
            for j in ones:
                count += len(h+'and'+i+j)

    # count to 1000
    count += len(ones[0]+ thousand)
    print(count)
    '''