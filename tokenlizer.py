from queue import Queue
import unittest

special = [';', ' ', '\n', '(', ')', '[', ']', '{', '}']

def tokenlize(code: str, ans):

    if not code:
        return ans
    
    if code[0] in special:
        ans.append(code[0])
        return tokenlize(code[1:], ans)

    token_len = 0

    while token_len < len(code) and code[token_len] not in special:
        token_len += 1
    
    token = code[:token_len]

    ans.append(token)
    return tokenlize(code[token_len:], ans)
    

class TokenlizerTest(unittest.TestCase):

    def test_simple_sql(self):
        ans = []
        tokenlize('select * from abc;', ans)
        self.assertEquals(ans, ['select', ' ', '*', ' ', 'from', ' ', 'abc', ';'])

    def test_simple_func(self):
        ans = []
        tokenlize('function foo(){return 1;}', ans)
        self.assertEquals(ans, ['function', ' ', 'foo', '(', ')', '{', 'return', ' ', '1', ';', '}'])


if __name__ == '__main__':

    unittest.main()