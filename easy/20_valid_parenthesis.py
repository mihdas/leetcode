class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        for char in s:
            if char=='(' or char=='[' or char=='{':
                stk.append(char)
            if char==')':
                try:
                    bl=stk.pop()
                except:
                    return False
                if bl!='(':
                    return False

            if char==']':
                try:
                    bl=stk.pop()
                except:
                    return False
                if bl!='[':
                    return False
            
            if char=='}':
                try:
                    bl=stk.pop()
                except:
                    return False
                if bl!='{':
                    return False
        if len(stk)>0:
            return False

        return True
            