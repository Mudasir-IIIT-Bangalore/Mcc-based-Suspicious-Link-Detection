from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from fuzzywuzzy import fuzz
from difflib import SequenceMatcher
import nltk
from nltk.corpus import wordnet
import sys
import string
import xlrd

# Normalization Function
def norml(str):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(str)
    nor_str = "";
    punctuations = list(string.punctuation);
    for w in words:
        if w not in stop_words and w not in punctuations:
            nor_str = nor_str + " " + w;
    nor_str = nor_str.lower();
    for w in phd_synonyms:
        nor_str = nor_str.replace(w, "phd")
    for x in jmi_synonyms:
        nor_str = nor_str.replace(x, "jamia millia islamia");
    return (nor_str);


#Loading Attribute file

file_location="C:/Python27/attrib.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(0)

#Loading frien_network file
edgefile_loc="C:/Python27/friend_network.xlsx";
workbook2=xlrd.open_workbook(edgefile_loc);
sheet2=workbook2.sheet_by_index(0);
count = 1;
f = open("C:/Python27/work_sim(new).csv", 'w');
f.write("Node1,Node2, Work (fuzzy_token_set_ratio), Education(fuzz.token_sort_ratio), Home_town (fuzzy_token_set_ratio), Current_city (fuzzy_token_set_ratio),\n");
for i in range(1,sheet2.nrows):
      for j in range(i,sheet2.ncols):
          if(sheet2.cell_value(i,j)==1):
              f.write(`i`+","+`j`+" ");
              e1=sheet.cell_value(i,1);
              e2=sheet.cell_value(j,1);
              phd_synonyms = ['research scholar', 'scholar', 'ph.d. scholar', 'junior research scholar',
                              'senior research scholar', 'ph.d', 'phd'];
              jmi_synonyms = ['jamia millia islamia', 'jamia millia', 'jmi', 'jamia'];

              n_e1 = norml(e1);
              n_e2 = norml(e2);
              print("\n");
              print("User 1-> "+ sheet.cell_value(i, 0) + "  :" + n_e1);
              print("User 2-> "+sheet.cell_value(j, 0) + "  :" + n_e2);

              m = fuzz.ratio(n_e1, n_e2);
              print("fuzz.ratio-> " + `m`);

              m1 = SequenceMatcher(None, n_e1, n_e2);
              m1 = m1.ratio();
              print("SequenceMatcher-> " + `m1`);

              m2 = fuzz.partial_ratio(n_e1, n_e2);
              print("fuzz.partial_ratio-> " + `m2`);

              m3 = fuzz.token_sort_ratio(n_e1, n_e2);
              print("fuzz.token_sort_ratio-> " + `m3`);

              m4 = fuzz.token_set_ratio(n_e1, n_e2);
              print("fuzz.token_set_ratio-> " + `m4`);
              count = count + 1;

              w_sim = fuzz.token_set_ratio(norml(sheet.cell_value(i, 1)), norml(sheet.cell_value(j, 1)));
              e_sim = fuzz.token_set_ratio(norml(sheet.cell_value(i, 2)), norml(sheet.cell_value(j, 2)));
              h_sim = fuzz.token_set_ratio(norml(sheet.cell_value(i, 3)), norml(sheet.cell_value(j, 3)));
              c_sim = fuzz.token_set_ratio(norml(sheet.cell_value(i, 4)), norml(sheet.cell_value(j, 4)));
              f.write(","+str(w_sim)+","+str(e_sim)+","+str(h_sim)+","+str(c_sim)+"\n");



print(count);


