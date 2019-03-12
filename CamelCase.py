from math import log
from Dictionary import Dictionary
import re, gzip, os

class CamelCase:
    '''
    Inspired by this post: https://stackoverflow.com/questions/8870261/how-to-split-text-without-spaces-into-list-of-words/11642687#11642687
    Convert string to CamelCase by using Zipf's law. 
    Zipf's law states that given a large sample of words used, the frequency of any word is inversely proportional to its rank in the frequency table. 
    So word number n has a frequency proportional to 1/n. So, mathematically, cost = -log(probability)
    Not using Oxford dictionary API for scalability reasons.
    Instead using words collected from /usr/share/dict/american-english after installing wamerican and compressing into gz.
    '''
    def __init__(self,path=os.path.join(os.path.dirname(__file__),"files","words.txt.gz")):
        self.path = path
    
    def initialize_camel_case(self):
        ''' Creating cost dictionary using Zipf's law '''
        with gzip.open(self.path) as wf:
            words = wf.read().decode().split()
        self.word_cost = {k:log((i+1)*log(len(words))) for i,k in enumerate(words)}
        self.max_word_length = max(len(word) for word in words)
        self.regex_split = re.compile("[^a-zA-Z0-9']+")

    def initialize_camel_case_api(self,api_url,app_id="",app_key=""):
        self.cache = {}
        self.camel_dict = Dictionary(api_url,app_id=app_id,app_key=app_key)
    
    def convert_camel_case(self,string):
        ''' Check and if string can be converted to integers '''
        try:
            string_int = int(string)
            return string
        except:
            dpTable = [self._split(x) for x in self.regex_split.split(string)]
            return "".join([substr.capitalize() for sublist in dpTable for substr in sublist])

    def _split(self,substr):
        
        def best_match(first_i):
            # best match for first i characters assuming cost is available for i-1
            candidates = enumerate(reversed(cost[max(0, first_i-self.max_word_length):first_i]))
            print(candidates)
            return min((c + self.word_cost.get(substr[first_i-k-1:first_i].lower(), 9e999), k+1) for k,c in candidates)
        
        cost=[0]
        for i in range(1,len(substr)+1):
            c,k = best_match(i)
            cost.append(c)

        # Backtrack to recover the minimal-cost string.
        out = []
        i = len(substr)
        while i>0:
            c,k = best_match(i)
            print(c,k,cost[i])
            assert c == cost[i]
            # Apostrophe and digit handling
            newToken = True
            print(substr[i-k:i])
            if not substr[i-k:i] == "'": # ignore a lone apostrophe
                if len(out) > 0:
                    # re-attach split 's and split digits
                    if out[-1] == "'s" \
                    or (substr[i-1].isdigit() and out[-1][0].isdigit()): # digit followed by digit
                        out[-1] = substr[i-k:i] + out[-1] # combine current token with previous token
                        newToken = False

            if newToken:
                out.append(substr[i-k:i])

            i -= k
        print(out)
        return reversed(out)

    def convert_camelcase_dp(self,string,min_length=1):
        def convert_camelcase_dp_util(string,min_length=1):
            if string in self.cache:
                return self.cache[string]
            if string == "":
                return []
            for i in range(min_length,len(string)+1):
                if self.camel_dict.is_word(string[:i]):
                    remaining = convert_camelcase_dp_util(string[i:])
                    if remaining is not None:
                        result = [string[:i]] + remaining
                        self.cache[string] = result
                        return result
            self.cache[string] = None
            return None
        result_list = convert_camelcase_dp_util(string)
        return result_list[0]+"".join([string.capitalize() for string in result_list[1:]])