#import os
import random
import time
from PyDictionary import PyDictionary
from random_word import RandomWords
r = RandomWords()
# Return a single random word
#Extra sources and potential ones i may use: https://docs.google.com/document/d/1AyQOrNYSWcYHPr7uaxER_BTM5zV6M2EC3kqZJINS1PQ/edit
dictionary = PyDictionary()
#import logging
#eikonLogger = logging.getLogger('')
#eikonLogger.setLevel(logging.FATAL)
randWord = r.get_random_word()
randDef = dictionary.meaning(randWord, disable_errors=True)
while (randDef is None):
  randWord = r.get_random_word()
  randDef = dictionary.meaning(randWord, disable_errors=True)
print("\n\n\nWelcome to the Haas Hall Dictionary!\n\n")
print("~~~~~~~~~~~~~~~~~~~~ Your Random Word ~~~~~~~~~~~~~~~~~~~~\n")
#os.system('cls')
#printing the random word; a new word is provided each time the code is opened
print(randWord + "\n")
print ((str(randDef))[1:-1])
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#print(((dictionary.meaning("far")).get('Adverb'))[0])
while True:
  invalidType = 0
  print(
    "\n The Haas Hall Dictionary offers \nthree different applications:"
  )
  print('\n *Dictionary')
  print('\n *Vocab Building')
  print('\n *Translator')
  print('\n *Word Hunt')
 # print('\n *Synonyms')
  #print('\n *Antonyms')
  gamemode = str.capitalize(input("\nWhich would you like to use? "))
  print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#as long as the gamemode isn't changed (can be changed at the end), the gamemode will loop through Dictionary
  while (gamemode == ("Dictionary")):
    invalidType += 1
    dictword = input("\nPlease state the word \nthat you are seeking the definition of:\n ")
    print("\n")
   # definition = (dictionary.meaning(dictword))
    #print (definition)
    #print (dictionary.meaning(''))
    while (dictionary.meaning(dictword, disable_errors=True)) is None:
      print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      dictword = input("\nYour input is not recognized as a valid word by our dictionary. \n Please check that your spelling was correct and try again: ")
      print ('\n')
    fulldef = (dictionary.meaning(dictword))
    noun = fulldef.get('Noun')
    verb = fulldef.get('Verb')
    adj = fulldef.get('Adjective')
    adv = fulldef.get('Adverb')
    pos = ""
    while (pos == ""):
      availablepos = (str.capitalize(dictword) + " has definitions for the following: \n")
    #this checks through the code to see which parts of speech are available for the word
      if (noun is not None):
        availablepos += "\n*Noun\n"
        noun = (str(noun)[1:-1])
      if (adj is not None):
        availablepos += "\n*Adjective\n"
        adj = (str(adj)[1:-1])
      if (adv is not None):
        availablepos += "\n*Adverb\n"
        adv = (str(adv)[1:-1])
      if (verb is not None):
        availablepos += "\n*Verb\n"
        verb = (str(verb)[1:-1])
      print (availablepos)
      determinepos = str.lower(input("Please state which part(s) of speech would you like definitions for:\n "))
      if ('noun' in determinepos):
        if 'Noun' in availablepos:
          pos += ("\nNoun: \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" + noun + "\n\n")
          
        else:
          print ("\nNoun: not applicable\n\n")
      if ('adjective' in determinepos):
        if 'Adjective' in availablepos:
          pos += ("\nAdjective: \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" + adj + "\n\n")
        else:
          print ("\nAdjective: not applicable\n\n")
      if ('adverb' in determinepos):
        if 'Adverb' in availablepos:
          pos += ("\nAdverb: \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" + adv + "\n\n")
        else:
          print ("\nAdverb: not applicable")
        determinepos = determinepos.replace('adverb', '')
      if ('verb' in determinepos):
        if 'Verb' in availablepos:
          pos += ("\nVerb: \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" + verb + "\n\n")
        else:
          print ("\nVerb: not applicable\n\n")
      print (pos)
      if (pos == ""):
        print ("You did not provide one of the listed valid parts of speech. \n Please try again. \n")
    determinegm = input ("Would you like to do another word (yes or no)?")
    if determinegm == "no":
      break
  while (gamemode == ("Translator")):
    invalidType += 1
    if dictionary.translate('hi', 'es') is None:
##NOTE: sometimes the translator database stops functioning for no reason. When this happens, I made the code stop so that it doesn't cause further problems
      
      print("\n\nSorry, but the translation software is not currently working.\nPlease try again later.")
      break
    count = 0
    while (count == 0):
      language = str.capitalize(input("Would you like to translate to Spanish or Nepali? "))
    #I was planning on only doing Spanish, but I'm Nepali so
      if (language == "Nepali"):
        count+=1
        language = 'ne'
      elif (language == "Spanish"):
        count +=1
        language = 'es'
      else:
        print("Invalid translation language. Please try again.\n\n\n\n")     
    translated = ""
    translating = ""
    punctuation = ""
    fullPhrase = input("Please list the word, phrase, or sentence you would like to translate: ")
    for x in fullPhrase:
      if (x != " "):
        if x.isalpha():
          translating += x
        else:
          punctuation+=x
      else:
        translated += " "
       #the below code ensures that there are no nonwords given by the user. These nonwords would make the output incorrect. 
        if (dictionary.translate(translating, language) is None):
          print("One of the words wasnt real")
          break        
        translated += dictionary.translate(translating, language, )
        translated += punctuation
        translating = ""
        punctuation = ""
    translated += " "
    translated += dictionary.translate(translating, language)
    print(translated)
    determinegm = input("\n\nWould you like another translation (yes or no)?")
    if determinegm == ("no"):
      break
  while (gamemode == ("Vocab building")):
    invalidType += 1
    type = input("Welcome to vocab building!\nWe will provide a new word for you to learn based on\n a few criteria you can set. If you want a completely random word, \nthen just enter nothing.\nIf not, then please state the part of speech \n(if you want a specific one) and the length of the word (if you want a specific one):\n")
    type = (type.lower())
    valid = True
    thinking = 0
    nopos = 0
    while (valid == True):
      typecopy = type
      missingvalue = 0
      availablepos = ""
      pos = ""
      randWord = r.get_random_word()
      fulldef = dictionary.meaning(randWord, disable_errors=True)
      while (fulldef is None):
        randWord = r.get_random_word()
        fulldef = dictionary.meaning(randWord, disable_errors=True)
      noun = fulldef.get('Noun')
      verb = fulldef.get('Verb')
      adj = fulldef.get('Adjective')
      adv = fulldef.get('Adverb')
      if (noun is not None):
        availablepos += "noun"
        noun = (str(noun)[1:-1])
      if (adj is not None):
        availablepos += "adjective"
        adj = (str(adj)[1:-1])
      if (adv is not None):
        availablepos += "adverb"
        adv = (str(adv)[1:-1])
      if (verb is not None):
        availablepos += "verb"
        verb = (str(verb)[1:-1])
      if ('adverb' in typecopy):
        nopos += 1
        if ('adverb' in availablepos):
          pos += ("\nAdverb: \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" + (str(adv)) + "\n\n")
        else:
          missingvalue += 1
        typecopy = typecopy.replace('adverb','')
      if ('verb' in typecopy):
        nopos += 1
        if ('verb' in availablepos):
          pos += ("\nVerb:   \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" + (str(verb)) + "\n\n")
        else:
          missingvalue += 1
      if ('noun' in typecopy):
        nopos += 1
        if ('noun' in availablepos):
          pos += ("\nNoun: \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" + (str(noun)) + "\n\n")
        else:
          missingvalue += 1
      if ('adjective' in typecopy):
        nopos += 1
        if ('adjective' in availablepos):
          pos += ("\nAdjective: \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" + (str(adj)) + "\n\n")
        else:
          missingvalue += 1
      responses = ["Thinking. . .", "Thinking. . .", "Thinking. . .", "Thinking. . .", "Thinking. . .", "Thinking. . .", "Thinking. . .", "Thinking. . .", "This is a tricky one. . .", "Thinking hard. . . ", "Thinking very hard. . .", "The dictionary is using its full mental energy right now. . . ", "You're looking for quite an odd word", "Thinking. . .", "Thinking. . .", "Thinking. . .", "Thinking. . .", "Thinking. . .", "Thinking. . .", "Thinking. . .", "Thinking. . .", "Thinking. . .", "Thinking. . .", "Geeze louise this is tough. . ."]
      respNum = random.randint(0, len(responses)-1)
      thinking += 1
      if (thinking%3 == 0 or thinking ==1):
        print("\n\n" + responses[respNum])      
      if ((pos != "") and (missingvalue == 0)):
        print("\n\n" + randWord)
        print(pos)
        print("Wow! Your word took " + (str(thinking)) + " loops through the dictionary to find.")
        valid = False
      elif (nopos == 0):
        print("\n\n" + randWord)
        print((str(fulldef))[1:-1])
        valid = False
    determinegm = input("\n\nWould you like to use Vocab Builder again (yes or no)?")
    if determinegm == ("no"):
      break      
#  if (invalidType == 0):
  #  print("Invalid dictionary application.\n Please try again\n\n\n")
  while (gamemode == ("Word hunt")):
    print("\n\nWelcome to Word Hunt! In this game, you will have to find words fitting the criteria given to you. \nYour score is based on the amount of correct words you can find in the given time, with points being counted off for incorrect words. \nLet's begin!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    version = input("Pick Your Version: \nBlitz (15 Seconds)\nJog (30 Seconds)\nStandard(1 Minute)\n")
    prop = True
    while (prop == True):
      posq = input("Would you like to specify part of speech (Y or N)?")
      prop = False
      if (version == "Blitz"):
        vertime = 15
      elif (version == "Jog"):
        vertime = 30
      elif (version == "Standard"):
        vertime = 60
      else:
        print("Invalid type. Please try again.\n")
        prop = True
    print ("\nReady..")
    time.sleep(3)
    print ("\nSet...")
    time.sleep(6)
    print ("\nGo!")
    score = 0
    timer = (time.time() + vertime)
    number = random.randint(3,9)
    partsofspeech = ["Noun", "Verb", "Adjective", "Adverb"]
    partofspeech = partsofspeech[random.randint(0,3)]
    if (posq == "Y"):
      print ("Your part of speech is: " + partofspeech)  
    print ("Your word length is: " + (str(number)))
    while (timer > time.time()):
      submission = input("Your Word: ")
      if (len(submission) == number) and (dictionary.meaning(submission, disable_errors=True) is not None):
        if (posq == "Y"):
          if ((dictionary.meaning(submission)).get(partofspeech)) is not None:
            print("+10!\n")
            score +=10
          else:
            print("+0\nDoes not have " + partofspeech + " form.\n")
        else:
          print("+10!\n")
          score +=10
      else:
        print("+0\nIncorrect letter count.\n")
          
    print("Time's up! Your final score was " + (str(score)) + ".")
