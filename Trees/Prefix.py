class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        trie = self.make_trie(*A)
        #print trie
        prefix_list = self.traverse_trie(trie)
        new_pre = []
        for word in A:
            for pre in prefix_list:
                if word.startswith(pre):
                    new_pre.append(pre)
                    
        return new_pre
    
    
    def traverse_trie(self, root):
        prefix_list = []
        
        if root[1] == 1:
            return root[0].keys()
        
        for node in root[0]:
            #prefix_list = []
            #print "node is : ", node
            if root[0][node][1] <= 1:
                prefix_list.append(node[0])
                
            else:
                for pre in self.traverse_trie(root[0][node]):
                    prefix_list.append(node[0]+ pre)
                    
            
        return prefix_list
                
        

    
    def make_trie(self, *words):
        _end = '_end_'
        root = [dict(), 0]
        #print words
        for word in words:
            #print word
            current_dict = root
            for letter in word:
                current_dict[1] += 1
                current_dict = current_dict[0]
                current_dict = current_dict.setdefault(letter, [{}, 0])
                #current_dict = current_dict[0]
            current_dict[0][_end] = (_end,0)
            #print current_dict, word
    
        return root

