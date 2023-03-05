import json
import csv
import random
import subprocess

wordList = []
fileName = "documents.json"
snippetName = "corpora.json"

cols = (("oneWord", "String", True),
        ("name", "string", True),
         ("description", "string", True),
        )

def init_word():
    f = open('../wordList.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    reader = csv.reader(f,
                        delimiter = ",", quotechar = '"',
                        quoting = csv.QUOTE_ALL)
    for words in reader:
        for word in words:
            wordList.append(word)      
    f.close() 
    
    
def writeJson(rows):
    with open(fileName, 'w', encoding='utf-8') as f:
        for row in rows:
            json.dump(row,f, ensure_ascii=False)
            f.write("\n")
            

def writeSnippet():
    # Run the wc -l and stat -f %z commands and capture the output
    wc_output = subprocess.check_output(['wc', '-l', 'documents.json'])
    stat_output = subprocess.check_output(['stat', '-f', '%z', 'documents.json'])
  
    # Decode the output from bytes to a string
    wc_count = (wc_output.decode('utf-8'))
    file_size = (stat_output.decode('utf-8'))
    
    snippet = {
            "source-file": fileName,
            "document-count": int(wc_count.strip().split(" ")[0]),
            "uncompressed-bytes": int(file_size.strip())
    }
    
    with open(snippetName, 'w', encoding='utf-8') as f:
        json.dump(snippet, f)
    
       

def main():
    init_word()
    rows = []
    for i in range(0,1000000):
        record = {}
        for i in range(len(cols)):
              record["oneWord"] = random.choice(wordList)
              record["name"] =random.choice(wordList) + " " + random.choice(wordList)
              record["description"] = random.choice(wordList)+" " + random.choice(wordList)+" " + random.choice(wordList)+" " + random.choice(wordList)+" " + random.choice(wordList)
        rows.append(record)
    writeJson(rows)
    writeSnippet()


if __name__ == "__main__":
    main()
    
