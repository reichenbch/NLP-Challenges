from sklearn.feature_extraction.text import TfidfVectorizer,HashingVectorizer
import numpy as np
from sklearn.linear_model import SGDClassifier

f = open("C:\\Users\\RISHAV\\Documents\\NLP_Work\\training.txt", "r")
allData = f.read().split("\n")
T = int(allData[0])
allData = allData[1:-1]

corpus = [f.split("\t")[0] for f in allData]
target = [f.split("\t")[1] for f in allData]

corpus += ['Data Structures and Algorithms with Object- Oriented Design Patterns in C++ 1 Edition (Paperback)','God Moments: Stories That Inspire, Moments to Remember (Paperback)','The Ultimate C: Concepts, Programs and Interview Questions (Paperback)','Canon EOS 1100D SLR (Black, with Kit (EF S18-55 III))','A Textbook of Organic Chemistry for JEE Main & Advanced and Other Engineering Entrance Examinations (Paperback)','Test your C ++ Skills 1 Edition (Paperback)','IIM Ahmedabad Business Books: Day to Day Economics (Paperback)','Calvin Klein One Eau de Toilette  -  200 ml',"A Practical Guide to Spoken English: Improve Your Communication Skills and Be On Top in Today's Competitve World (Paperback)",
 'Olympiad Champs Science, Mathematics and English Class 5 - Set of 3 Books : 18 Mock Olympiad CD with Insta Reports 1st Edition (Paperback)','Chapterwise Topicwise Questions-Solutions Mathematics for Engineering Entrances 1st Edition (Paperback)','Atomic Physics: 8th Edition 8th  Edition (Paperback)','Head First C (Paperback)','Mathematics for Physicists New edition Edition (Paperback)','The C Programming Language : Ansi C Version 2 Edition (Paperback)','Axe Musk Deodorant Spray  -  150 ml (For Men)','Question Bank - Physics, Chemistry and Biology for Class 12th (Set of 3 Books) 1st Edition (Paperback)','Timex Analog Watch  - For Men (Silver)','Sony CyberShot DSC-WX300 Point & Shoot (Brown)','Essential Physical Chemistry for JEE Main & Advanced (Paperback)','Introduction To Financial Accounting','Essential Organic Chemistry: The Perfect Book for JEE Main & Advanced (Paperback)','Problems Plus In IIT Mathematics (Paperback)','Sony CyberShot DSC-WX50 Point & Shoot (Pink)','Read It Yourself: Books Box Level 4 (Set Of 6 Titles) (Paperback)','Principles Of Physics 9th Edition (Paperback)','Sony HDR-AS30V Full HD Action Camcorder','Programming in ANSI C 6th  Edition (Paperback)','Canon EOS 60D SLR (Black, with Kit EF-S18-55mm Lens)','Axe Denim Deodorant Spray with Offer - 150 ml (For Men)','Case Logic DCB-301 Camera Case (Black)','Titan Raga Analog Watch  - For Women (Gold)','Comprehensive Chemistry - JEE Advanced 2014 1st Edition (Paperback)','Sony Cybershot DSC-WX7 Point & Shoot (Black)','GENERAL CHEMISTRY? 3rd  Edition (Paperback)','Laptops: AMD Mobile Platform, AMD Vision, Barebook, Cen...','Calvin Klein One Eau de Toilette  -  200 ml (Unisex)','Calvin Klein One Eau de Toilette  -  50 ml (Unisex)','Study Package For IBPS Institute of Banking Personnel Selection: Common Written Examination Clerical Cadre Recruitment 1st Edition (Paperback)','Sony CyberShot DSC-WX300 Point & Shoot (Red)','Question Bank - Physics, Chemistry and Mathematics for Class 12th (Set of 3 Books) 1st Edition (Paperback)','3 more combos','Dell Vostro 2520 Laptop (2nd Gen PDC/ 2GB/ 320GB/ Linux...','Advanced Engineering Mathematics 9 Edition (Paperback)','Comprehensive Mathematics - JEE Advanced 2014 1st Edition (Paperback)','Dell Inspiron 15R 5521 Laptop (3rd Gen Ci7/ 8GB/ 1TB/ W...','2 more combos','Concise Inorganic Chemistry 5 Edition (Paperback)','Nike Up or Down Deodorant Spray  -  200 ml (For Men)','10 more combos','Calvin Klein Eternity Eau de Parfum  -  50 ml (For Women)','Titan Karishma Analog Watch  - For Women (Silver, Gold)','Titan Karishma Analog Watch  - For Men (Gold, Silver)','Axe Marine Deodorant Spray  -  150 ml (For Men)','Concepts Of Physics (Volume - 2) 2nd Edition (Paperback)','Sony DCR-SX22E Camcorder (Black)','Sony Cybershot DSC-S5000 Point & Shoot (Silver)','Calvin Klein Euphoria Eau de Toilette  -  100 ml (For Men)','Spoken English: A Manual of Speech and Phonetics (With CD) 4 Edition (Paperback)','Spoken English (With CD) (Paperback)']
target += ['data structures algorithms', 'written english', 'c programming', 'dslr canon', 'chemistry', 'c programming', 'best-seller books', 'calvin klein', 'spoken english', 'mathematics', 'mathematics', 'physics', 'c programming', 'physics', 'c programming', 'axe deo', 'chemistry', 'timex watch', 'sony cybershot', 'chemistry', 'c programming', 'chemistry', 'mathematics', 'sony cybershot', 'best-seller books', 'physics', 'camcorder', 'c programming', 'dslr canon', 'axe deo', 'camera', 'titan watch', 'chemistry', 'sony cybershot', 'chemistry', 'chromebook', 'calvin klein', 'calvin klein', 'written english', 'sony cybershot', 'physics', 'axe deo', 'dell laptops', 'mathematics', 'mathematics', 'dell laptops', 'axe deo', 'chemistry', 'nike-deodrant', 'dell laptops', 'calvin klein', 'titan watch', 'titan watch', 'axe deo', 'physics', 'camcorder', 'sony cybershot', 'calvin klein', 'spoken english', 'spoken english']

# vectorizer
vectorizer = TfidfVectorizer(min_df=0, ngram_range=(1, 3), max_df=1.0)
tranSize = len(corpus)
X_train = vectorizer.fit_transform(corpus)
feature_names = np.asarray(vectorizer.get_feature_names())
categories = list(set(target))

clf = SGDClassifier(alpha=.0001, n_iter=50, penalty="elasticnet")
clf.fit(X_train, target)

T = int(raw_input())
for i in range(T):
    print clf.predict(vectorizer.transform([raw_input()]))[0]
