import re

keywordFileName = "./keywords.txt"
keywords = []
textFileName = "./searchText.txt"
searchText = ""

totalFileName = "./totals.txt"
totalsList = []

def main():
  f = open(keywordFileName, 'r+')
  keywords = [line for line in f.readlines()]
  f.close()

  with open(textFileName, 'r') as file:
    searchText = file.read().replace('\n', '')

  for word in keywords:
    pattern = re.compile(r'\b%s\b' % word.replace("\n", ''), re.I)
    n = re.findall(pattern, searchText)

    totalsList.append(word.replace("\n", '') + ": " + str(len(n)) + "\n")

  totalFile = open(totalFileName, 'w')
  totalFile.writelines(totalsList)

if __name__ == "__main__":
	main()