class Solution:
    def calculate(self, s: str) -> int:
        
                
        
        s = s.replace(" ", "")
        s = list(reversed(s))
        
        
        
        stack = []
        i = 0
        temp = ""
        sign = 1
        for i in range(len(s)):
            
            
            
            if s[i]=='(': #need to pop from stack until we reach )
                
                
                
                if temp!='':
                    temp = "".join(list(reversed(temp)))
                    stack.append(int(temp))
                    temp = ""
                    
                
                curr = 0
                sign = 1
                ## empty stack until the correpsonding )
                while len(stack)>0 and stack[-1]!=')':
                    
                    
                    
                    if stack[-1]=='+':
                        
                        stack.pop()
                        sign = 1
                        
                    elif stack[-1]=='-':
                        
                        stack.pop()
                        sign = -1
                        
                    else:
                        curr+=sign*stack.pop()
                        
                    
                        
                        
                        
                stack.pop()        
                stack.append(curr)
                continue
                
                
            elif s[i]==")" or s[i]=='+' or s[i]=='-': ## push +- and ( to the stack
                
                if temp:
                    temp = "".join(list(reversed(temp)))
                    stack.append(int(temp))
                    temp = ""
                stack.append(s[i]) 
                
                
            else:
                
                temp += s[i]
            
            
                
                
        if temp:        
            temp = "".join(list(reversed(temp)))    
            stack.append(int(temp))    
        
        
        
        if stack[-1]=="-":
            stack.append(0)
        
        try:
            curr = int(stack.pop())
        except:
            curr = 0
            
        
        while len(stack)>0:
            
            
            if stack[-1]=='+':
                    
                    stack.pop()
                    curr+=stack.pop()
                    
            elif stack[-1]=='-':
                    stack.pop()
                    curr-=stack.pop()
        
            
            
        return curr       
        
                

                
        
