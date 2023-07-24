class Anagram: 
    def __init__(self, word):
        self.word = word

    def match(self, input_list):
        list = []
        word_string = [letter for letter in self.word]
        sorted_word = sorted(word_string)
        for word in input_list:
            compare = [letter for letter in word]
            sorted_compare = sorted(compare)
            if sorted_word == sorted_compare:
                list.append(word)
        return list