#Write a program to fill in a letter template given below with name and date.
# letter = '''
#    Dear <|Name|>,
#    You are Selected!
#    <|Date|>


letter = ''' Dear <|Name|>,
            You are selected!
            <|Date|> '''
print(letter.replace("<|Name|>", "Yug").replace("<|Date|>", "24 September 2025")) 