class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #declaring a stack 
        l = []
        for i in s:
            # if s[0] == ")" or s[0] == "]" or s[0] == "}":
            #     return False
            
            #Pushing items onto stack
            if i == "(" or i == "[" or i == "{":
                l.append(i)
            
            if i == ")":
                #check if the stack is empty
                if len(l) != 0:
                    #Check for closing parentheses and pop the respective parenthesis
                    if l[-1] == "(":
                        l.pop()
                        continue
                    else:
                        return False
                else:
                    return False
                
            if i == "]":
                if len(l) != 0:
                    if l[-1] == "[":
                        
                        l.pop()
                        continue
                    else:
                        return False
                else:
                    return False
                
            if i == "}":
                if len(l) != 0:
                    if l[-1] == "{":
                        l.pop()
                        continue
                    else:
                        return False
                else:
                    return False
        
        #check if the stack is empty
        if not l:
            return True
        else:
            return False
