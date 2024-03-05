from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4-turbo-preview")

#grade function for post lab questions. Returns int - points awarded
def grade_plq(question, points, instruction, answer):
    
    opParser = StrOutputParser()

    #prompt specifically for post lab questions
    prompt_plq = ChatPromptTemplate.from_messages([
        
        ("system", 
        "You have to give points to a user-generated answer to a question.\n\
        This is the question the user tried to answer: {question}\n\
        Total possible points are: {points}\n\
        This is your instruction how to give points: {instruction}\n\
        Only return the number of points. If there is no answer, return 0 points."
        ),

        ("user", "{answer}")
    ])

    chain = prompt_plq | model | opParser

    res = chain.invoke({"question": question,
                  "points": points,
                  "instruction": instruction,
                  "answer": answer})    
    
    return int(res)


#-----EXAMPLE-----
#takes 434 tokens in total
question = "Explain how do you read and interpret syntax of any OS command."
points = 3
instruction = "The answer should contain a comprehensive explanation along with examples of 3 parts:\
    name of command, options of a command, arguments passed to a command. Each part carries 1 point,\
    Expected length of answer is between 100 to 400 words. Deduct a single point if this word limit is not respected. \
    Minimum possible points are 0. Give 1 point if the parts are mentioned without explanation"

answer = "Reading and interpreting the syntax of any operating system (OS) command involves\
understanding the command's structure, options, arguments, and any additional components\
that make up the command. Here's a general guide on how to do this:\
1. Command Name:\
• The first part of a command is the command name itself. This is the actual\
executable that you are running.\
• Example: In the command ls -l, \"ls\" is the command name.\
2. Options:\
• Options modify the behavior of a command. They are typically preceded by\
one or two hyphens (-) or sometimes a single hyphen.\
• Options are often used to enable or disable specific features or to provide\
additional information to the command.\
• Example: In the command ls -l, the \"-l\" is an option that tells the \"ls\"\
command to display a long listing of files.\
3. Arguments:\
• Arguments are the input values provided to a command. They can be files,\
directories, strings, or any data that the command operates on.\
• Some commands accept multiple arguments.\
• Example: In the command cp file1.txt file2.txt, \"file1.txt\" and \"file2.txt\" are\
arguments. The \"cp\" command copies \"file1.txt\" to \"file2.txt.\""

answer2="Reading and interpreting the syntax of any operating system (OS) command involves\
understanding the command's structure, options, arguments, and any additional components\
that make up the command."
#-----EXAMPLE-----


g = grade_plq(question, points, instruction, answer )
print(g)