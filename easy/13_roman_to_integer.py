class Solution:
    def romanToInt(self, s: str) -> int:
        integer=0
        for i in range(len(s)-1):
            if s[i]=='I':
                if s[i+1]=='V' or s[i+1]=='X':
                    integer-=1
                else:
                    integer+=1
            
            if s[i]=='V':
                integer+=5

            if s[i]=='X':
                if s[i+1]=='L' or s[i+1]=='C':
                    integer-=10
                else:
                    integer+=10

            if s[i]=='L':
                integer+=50

            if s[i]=='C':
                if s[i+1]=='D' or s[i+1]=='M':
                    integer-=100
                else:
                    integer+=100

            if s[i]=='D':
                integer+=500

            if s[i]=='M':
                integer+=1000

        if s[len(s)-1]=='I':
            integer+=1
        elif s[len(s)-1]=='X':
            integer+=10
        elif s[len(s)-1]=='C':
            integer+=100
        elif s[len(s)-1]=='M':
            integer+=1000
        elif s[len(s)-1]=='V':
            integer+=5
        elif s[len(s)-1]=='L':
            integer+=50
        else:
            integer+=500

        return integer
        

        

       





