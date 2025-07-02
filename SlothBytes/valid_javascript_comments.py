###############################
## Valid JavaScript Comments ##
###############################
#
# In JavaScript, there are two types of comments. 
#
# 1. Single-line comments start with //
# 2. Multi-line or inline comments start with /* and end with */
#
# The input will be a sequence of //, /* and */. Every /* must have a */ that immediately follows it. To add, there can be no single-line comments in between multi-line comments in between the /* and */.
#
# Create a function that returns True if comments are properly formatted, and False otherwise. 

# comments_correct("//////") 
# output = True
# # 3 single-line comments: ["//", "//", "//"]

# comments_correct("/**//**////**/")
# output = True
# # 3 multi-line comments + 1 single-line comment:
# # ["/*", "*/", "/*", "*/", "//", "/*", "*/"]

# comments_correct("///*/**/")
# output = False
# # The first /* is missing a */

# comments_correct("/////")
# output = False
# # The 5th / is single, not a double //

def comments_correct(comments:str):
    # We can already say that if the comments is not an even length, then it cannot contain a correnct sequence of comments. 
    if len(comments) % 2 != 0:
        return f'{False} - A "/" or "*" is missing'
    
    # Otherwise check if there is a correct sequence of comments. 
    i = 0
    opened_multi_line = False
    final_comments_sequence = []
    single_line_comments = 0
    multi_line_comments = 0
    while i < len(comments):    
        start_idx = i
        end_idx = i + 2
        curr_sequence = comments[start_idx : end_idx]
        final_comments_sequence.append(curr_sequence)
        
        # Counter for the single line comment.        
        if curr_sequence == "//" : single_line_comments += 1
        
        # Check if there is a multi_line_opened. Cause in that case we can only close, no other comments (// or /*) are accepted
        if opened_multi_line and curr_sequence != "*/":
            return f'{False} - A closing multiline comment "*/" is missing'
        else:
            # Check if there is a closing multi-line comments, without an opening one. 
            if curr_sequence == "*/" and not opened_multi_line:
                return f'{False} - A closing multiline commen "*/" occurs before an opening one "/*"'            
            opened_multi_line = False
            # Check if the current sequence of two char is /*
            if curr_sequence == "/*":
                opened_multi_line = True
                # Counter for the multi line comment. 
                multi_line_comments += 1
        i += 2
        
    return f'True - {final_comments_sequence} - {f"There are {single_line_comments} single line comments" if single_line_comments != 0 else ""} {f"+ {multi_line_comments} multi-line comments" if multi_line_comments != 0 else ""}'
    
    
    
print(comments_correct("//////"))

# print(comments_correct("/**//**////**/"))

# print(comments_correct("////*///"))

# print(comments_correct("///*/**/"))

# print(comments_correct("/////"))