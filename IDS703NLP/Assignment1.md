PomeloWu

##########Q1#########

1. Regular Expression:
    pattern = r"\b([A-Z][a-z]+)[\s.]* (([A-Z|a-z][a-z]+)([-, ]+))*([A-Z][a-z]+)[\s.]*"
    
2. DiscussionS on Assumptions & Failing Tests

    a. Names are presented in a consistent form, i.e., first name + space + (middle name) + space + last name, and in the form of capital letter followed by lower-case letter. 

    b.  Names must be western roman languages or be able to convert to that (meaning names have to be represented by western characters), for instance, East Asian languages could not be identify in its original spelling such as mā, mǎ.

    c. In order to match the case of Ken Griey, Jr., I did not put '\b' this expression. Therefore, the expression might fail when the name is followed by a puntuction. For instance, "I invited Dr. Wilson." might end up with an additional period. 

    d. If it's a random pair of letters/characters, as long as it suits the pattern of capital letter with lower-case letters, even if the name itself is not meaningful, the test will pass, for instance, Jiadc Wmd will be seen as a correct name.
    e. The expression technically could match any word combo, for example, Ice Cream, Hot Summer, not necessarily names. Therefore, the phrase might be semantically meaningless.


##########Q2:Fail Cases of My Gerund Test#########

1. 
If the prefix of a gerund is morphologically meaningful, i.e., correct combination of consonants and vowel, but are not semantically meaningful, then my test would fail. For instance, zighing, beuwing.

2. 
If the prefix of a gerund is both morphologically and semantically meaningful, but the prefix is not a verb, my test will fail. For instance, somehthing, everything, nothing, notwithstanding. 

3. 
long words, such as counterchecking, procrastinating, overestimating, and so on; in fact, my expression could match words with 9 characters max. I could change it to include longer words, but I think most gerunds are within that length. 

4. 
Gerunds at the start of the sentence, for example, "Hurting her is not what he wants." Because my expression doesn't capture capital letter, the test would fail. 