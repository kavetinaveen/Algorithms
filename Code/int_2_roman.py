class Solution(object):
    def get_roman(self, pos, digit, symbol_val):
        if digit == 5:
            return symbol_val[digit*pos]
        elif digit == 4 or digit == 9:
            return symbol_val[pos] + symbol_val[(digit+1)*pos]
        elif digit > 5:
            return symbol_val[pos*5]+(digit - 5)*symbol_val[pos]
        elif digit < 4:
            return symbol_val[pos]*digit
        
    def intToRoman(self, num):
        symbol_val = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        split_num = []
        r = []
        m = []
        k = 0
        while num > 0:
            r.append(num % 10)
            m.append(k)
            k += 1
            num = int(num/10)
        r = r[::-1]
        pos = [10**x for x in m][::-1]
        result = ''
        for i in range(len(r)):
            result = result+self.get_roman(pos[i], r[i], symbol_val)
        return result