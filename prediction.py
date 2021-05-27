{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import *\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "#List of the symptoms is listed here in list l1.\n",
    "\n",
    "l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',\n",
    "'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',\n",
    "'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',\n",
    "'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',\n",
    "'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',\n",
    "'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',\n",
    "'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',\n",
    "'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',\n",
    "'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',\n",
    "'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',\n",
    "'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',\n",
    "'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',\n",
    "'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',\n",
    "'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',\n",
    "'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',\n",
    "'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',\n",
    "'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',\n",
    "'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',\n",
    "'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',\n",
    "'yellow_crust_ooze']\n",
    "\n",
    "#List of Diseases is listed in list disease.\n",
    "\n",
    "disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',\n",
    "'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',\n",
    "' Migraine','Cervical spondylosis',\n",
    "'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',\n",
    "'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',\n",
    "'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',\n",
    "'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',\n",
    "'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',\n",
    "'Impetigo']\n",
    "\n",
    "l2=[]\n",
    "\n",
    "for i in range(0,len(l1)):\n",
    "    l2.append(0)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0,\n",
       " 0]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      prognosis\n",
      "0             0\n",
      "1             0\n",
      "2             0\n",
      "3             0\n",
      "4             0\n",
      "...         ...\n",
      "4915         36\n",
      "4916         37\n",
      "4917         38\n",
      "4918         39\n",
      "4919         40\n",
      "\n",
      "[4920 rows x 1 columns]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,\n",
       "       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,\n",
       "       34, 35, 36, 37, 38, 39, 40])"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=pd.read_csv(\"/Users/ayush/Downloads/Prototype.csv\")\n",
    "#Replace the values in the imported file by pandas by the inbuilt function replace in pandas.\n",
    "\n",
    "df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,\n",
    "'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,\n",
    "'Migraine':11,'Cervical spondylosis':12,\n",
    "'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,\n",
    "'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,\n",
    "'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,\n",
    "'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,\n",
    "'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,\n",
    "'Impetigo':40}},inplace=True)\n",
    "\n",
    "#check the df \n",
    "#print(df.head())\n",
    "\n",
    "X= df[l1]\n",
    "\n",
    "# print(X)\n",
    "\n",
    "y = df[[\"prognosis\"]]\n",
    "np.ravel(y)\n",
    "\n",
    "# print(y)\n",
    "\n",
    "#Read a csv named Testing.csv\n",
    "\n",
    "tr=pd.read_csv(\"/Users/ayush/Downloads/Prototype-1.csv\")\n",
    "\n",
    "#Use replace method in pandas.\n",
    "\n",
    "tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,\n",
    "'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,\n",
    "'Migraine':11,'Cervical spondylosis':12,\n",
    "'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,\n",
    "'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,\n",
    "'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,\n",
    "'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,\n",
    "'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,\n",
    "'Impetigo':40}},inplace=True)\n",
    "\n",
    "X_test= tr[l1]\n",
    "y_test = tr[[\"prognosis\"]]\n",
    "\n",
    "#print(y_test)\n",
    "\n",
    "np.ravel(y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "def DecisionTree():\n",
    "\n",
    "    from sklearn import tree\n",
    "\n",
    "    clf3 = tree.DecisionTreeClassifier() \n",
    "    clf3 = clf3.fit(X,y)\n",
    "\n",
    "    from sklearn.metrics import accuracy_score\n",
    "    y_pred=clf3.predict(X_test)\n",
    "    print(accuracy_score(y_test, y_pred))\n",
    "    print(accuracy_score(y_test, y_pred,normalize=False))\n",
    "\n",
    "    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]\n",
    "\n",
    "    for k in range(0,len(l1)):\n",
    "        for z in psymptoms:\n",
    "            if(z==l1[k]):\n",
    "                l2[k]=1\n",
    "\n",
    "    inputtest = [l2]\n",
    "    predict = clf3.predict(inputtest)\n",
    "    predicted=predict[0]\n",
    "\n",
    "    h='no'\n",
    "    for a in range(0,len(disease)):\n",
    "        if(predicted == a):\n",
    "            h='yes'\n",
    "            break\n",
    "\n",
    "\n",
    "    if (h=='yes'):\n",
    "        t1.delete(\"1.0\", END)\n",
    "        t1.insert(END, disease[a])\n",
    "    else:\n",
    "        t1.delete(\"1.0\", END)\n",
    "        t1.insert(END, \"Not Found\")\n",
    "\n",
    "\n",
    "def randomforest():\n",
    "    from sklearn.ensemble import RandomForestClassifier\n",
    "    clf4 = RandomForestClassifier()\n",
    "    clf4 = clf4.fit(X,np.ravel(y))\n",
    "\n",
    "    # calculating accuracy \n",
    "    from sklearn.metrics import accuracy_score\n",
    "    y_pred=clf4.predict(X_test)\n",
    "    print(accuracy_score(y_test, y_pred))\n",
    "    print(accuracy_score(y_test, y_pred,normalize=False))\n",
    "    \n",
    "    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]\n",
    "\n",
    "    for k in range(0,len(l1)):\n",
    "        for z in psymptoms:\n",
    "            if(z==l1[k]):\n",
    "                l2[k]=1\n",
    "\n",
    "    inputtest = [l2]\n",
    "    predict = clf4.predict(inputtest)\n",
    "    predicted=predict[0]\n",
    "\n",
    "    h='no'\n",
    "    for a in range(0,len(disease)):\n",
    "        if(predicted == a):\n",
    "            h='yes'\n",
    "            break\n",
    "\n",
    "    if (h=='yes'):\n",
    "        t2.delete(\"1.0\", END)\n",
    "        t2.insert(END, disease[a])\n",
    "    else:\n",
    "        t2.delete(\"1.0\", END)\n",
    "        t2.insert(END, \"Not Found\")\n",
    "\n",
    "\n",
    "def NaiveBayes():\n",
    "    from sklearn.naive_bayes import GaussianNB\n",
    "    gnb = GaussianNB()\n",
    "    gnb=gnb.fit(X,np.ravel(y))\n",
    "\n",
    "    from sklearn.metrics import accuracy_score\n",
    "    y_pred=gnb.predict(X_test)\n",
    "    print(accuracy_score(y_test, y_pred))\n",
    "    print(accuracy_score(y_test, y_pred,normalize=False))\n",
    "\n",
    "    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]\n",
    "    for k in range(0,len(l1)):\n",
    "        for z in psymptoms:\n",
    "            if(z==l1[k]):\n",
    "                l2[k]=1\n",
    "\n",
    "    inputtest = [l2]\n",
    "    predict = gnb.predict(inputtest)\n",
    "    predicted=predict[0]\n",
    "\n",
    "    h='no'\n",
    "    for a in range(0,len(disease)):\n",
    "        if(predicted == a):\n",
    "            h='yes'\n",
    "            break\n",
    "\n",
    "    if (h=='yes'):\n",
    "        t3.delete(\"1.0\", END)\n",
    "        t3.insert(END, disease[a])\n",
    "    else:\n",
    "        t3.delete(\"1.0\", END)\n",
    "        t3.insert(END, \"Not Found\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9512195121951219\n",
      "39\n",
      "0.9512195121951219\n",
      "39\n",
      "0.9512195121951219\n",
      "39\n",
      "0.9512195121951219\n",
      "39\n",
      "0.9512195121951219\n",
      "39\n"
     ]
    }
   ],
   "source": [
    "from tkinter import *\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "#List of the symptoms is listed here in list l1.\n",
    "\n",
    "l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',\n",
    "'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',\n",
    "'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',\n",
    "'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',\n",
    "'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',\n",
    "'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',\n",
    "'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',\n",
    "'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',\n",
    "'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',\n",
    "'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',\n",
    "'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',\n",
    "'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',\n",
    "'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',\n",
    "'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',\n",
    "'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',\n",
    "'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',\n",
    "'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',\n",
    "'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',\n",
    "'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',\n",
    "'yellow_crust_ooze']\n",
    "\n",
    "#List of Diseases is listed in list disease.\n",
    "\n",
    "disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',\n",
    "'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',\n",
    "' Migraine','Cervical spondylosis',\n",
    "'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',\n",
    "'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',\n",
    "'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',\n",
    "'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',\n",
    "'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',\n",
    "'Impetigo']\n",
    "\n",
    "l2=[]\n",
    "\n",
    "for i in range(0,len(l1)):\n",
    "    l2.append(0)\n",
    "df=pd.read_csv(\"/Users/ayush/Downloads/Prototype.csv\")\n",
    "#Replace the values in the imported file by pandas by the inbuilt function replace in pandas.\n",
    "\n",
    "df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,\n",
    "'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,\n",
    "'Migraine':11,'Cervical spondylosis':12,\n",
    "'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,\n",
    "'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,\n",
    "'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,\n",
    "'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,\n",
    "'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,\n",
    "'Impetigo':40}},inplace=True)\n",
    "\n",
    "#check the df \n",
    "#print(df.head())\n",
    "\n",
    "X= df[l1]\n",
    "\n",
    "# print(X)\n",
    "\n",
    "y = df[[\"prognosis\"]]\n",
    "np.ravel(y)\n",
    "\n",
    "# print(y)\n",
    "\n",
    "#Read a csv named Testing.csv\n",
    "\n",
    "tr=pd.read_csv(\"/Users/ayush/Downloads/Prototype-1.csv\")\n",
    "\n",
    "#Use replace method in pandas.\n",
    "\n",
    "tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,\n",
    "'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,\n",
    "'Migraine':11,'Cervical spondylosis':12,\n",
    "'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,\n",
    "'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,\n",
    "'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,\n",
    "'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,\n",
    "'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,\n",
    "'Impetigo':40}},inplace=True)\n",
    "\n",
    "X_test= tr[l1]\n",
    "y_test = tr[[\"prognosis\"]]\n",
    "\n",
    "#print(y_test)\n",
    "\n",
    "np.ravel(y_test)\n",
    "\n",
    "def DecisionTree():\n",
    "\n",
    "    from sklearn import tree\n",
    "\n",
    "    clf3 = tree.DecisionTreeClassifier() \n",
    "    clf3 = clf3.fit(X,y)\n",
    "\n",
    "    from sklearn.metrics import accuracy_score\n",
    "    y_pred=clf3.predict(X_test)\n",
    "    print(accuracy_score(y_test, y_pred))\n",
    "    print(accuracy_score(y_test, y_pred,normalize=False))\n",
    "\n",
    "    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]\n",
    "\n",
    "    for k in range(0,len(l1)):\n",
    "        for z in psymptoms:\n",
    "            if(z==l1[k]):\n",
    "                l2[k]=1\n",
    "\n",
    "    inputtest = [l2]\n",
    "    predict = clf3.predict(inputtest)\n",
    "    predicted=predict[0]\n",
    "\n",
    "    h='no'\n",
    "    for a in range(0,len(disease)):\n",
    "        if(predicted == a):\n",
    "            h='yes'\n",
    "            break\n",
    "\n",
    "\n",
    "    if (h=='yes'):\n",
    "        t1.delete(\"1.0\", END)\n",
    "        t1.insert(END, disease[a])\n",
    "    else:\n",
    "        t1.delete(\"1.0\", END)\n",
    "        t1.insert(END, \"Not Found\")\n",
    "\n",
    "\n",
    "def randomforest():\n",
    "    from sklearn.ensemble import RandomForestClassifier\n",
    "    clf4 = RandomForestClassifier()\n",
    "    clf4 = clf4.fit(X,np.ravel(y))\n",
    "\n",
    "    # calculating accuracy \n",
    "    from sklearn.metrics import accuracy_score\n",
    "    y_pred=clf4.predict(X_test)\n",
    "    print(accuracy_score(y_test, y_pred))\n",
    "    print(accuracy_score(y_test, y_pred,normalize=False))\n",
    "    \n",
    "    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]\n",
    "\n",
    "    for k in range(0,len(l1)):\n",
    "        for z in psymptoms:\n",
    "            if(z==l1[k]):\n",
    "                l2[k]=1\n",
    "\n",
    "    inputtest = [l2]\n",
    "    predict = clf4.predict(inputtest)\n",
    "    predicted=predict[0]\n",
    "\n",
    "    h='no'\n",
    "    for a in range(0,len(disease)):\n",
    "        if(predicted == a):\n",
    "            h='yes'\n",
    "            break\n",
    "\n",
    "    if (h=='yes'):\n",
    "        t2.delete(\"1.0\", END)\n",
    "        t2.insert(END, disease[a])\n",
    "    else:\n",
    "        t2.delete(\"1.0\", END)\n",
    "        t2.insert(END, \"Not Found\")\n",
    "\n",
    "\n",
    "def NaiveBayes():\n",
    "    from sklearn.naive_bayes import GaussianNB\n",
    "    gnb = GaussianNB()\n",
    "    gnb=gnb.fit(X,np.ravel(y))\n",
    "\n",
    "    from sklearn.metrics import accuracy_score\n",
    "    y_pred=gnb.predict(X_test)\n",
    "    print(accuracy_score(y_test, y_pred))\n",
    "    print(accuracy_score(y_test, y_pred,normalize=False))\n",
    "\n",
    "    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]\n",
    "    for k in range(0,len(l1)):\n",
    "        for z in psymptoms:\n",
    "            if(z==l1[k]):\n",
    "                l2[k]=1\n",
    "\n",
    "    inputtest = [l2]\n",
    "    predict = gnb.predict(inputtest)\n",
    "    predicted=predict[0]\n",
    "\n",
    "    h='no'\n",
    "    for a in range(0,len(disease)):\n",
    "        if(predicted == a):\n",
    "            h='yes'\n",
    "            break\n",
    "\n",
    "    if (h=='yes'):\n",
    "        t3.delete(\"1.0\", END)\n",
    "        t3.insert(END, disease[a])\n",
    "    else:\n",
    "        t3.delete(\"1.0\", END)\n",
    "        t3.insert(END, \"Not Found\")\n",
    "        \n",
    "# GUI stuff..............................................................................\n",
    "        \n",
    "root = Tk()\n",
    "root.configure(background='black')\n",
    "\n",
    "Symptom1 = StringVar()\n",
    "Symptom1.set(\"Select Here\")\n",
    "\n",
    "Symptom2 = StringVar()\n",
    "Symptom2.set(\"Select Here\")\n",
    "\n",
    "Symptom3 = StringVar()\n",
    "Symptom3.set(\"Select Here\")\n",
    "\n",
    "Symptom4 = StringVar()\n",
    "Symptom4.set(\"Select Here\")\n",
    "\n",
    "Symptom5 = StringVar()\n",
    "Symptom5.set(\"Select Here\")\n",
    "\n",
    "Name = StringVar()\n",
    "\n",
    "w2 = Label(root, justify=LEFT, text=\"Disease Predictor using Machine Learning\", fg=\"Red\", bg=\"White\")\n",
    "w2.config(font=(\"Times\",30,\"bold italic\"))\n",
    "w2.grid(row=1, column=0, columnspan=2, padx=100)\n",
    "w2 = Label(root, justify=LEFT, text=\"A Project by Shrimad Mishra\", fg=\"Pink\", bg=\"Blue\")\n",
    "w2.config(font=(\"Times\",30,\"bold italic\"))\n",
    "w2.grid(row=2, column=0, columnspan=2, padx=100)\n",
    "\n",
    "NameLb = Label(root, text=\"Name of the Patient\", fg=\"Red\", bg=\"Sky Blue\")\n",
    "NameLb.config(font=(\"Times\",15,\"bold italic\"))\n",
    "NameLb.grid(row=6, column=0, pady=15, sticky=W)\n",
    "\n",
    "S1Lb = Label(root, text=\"Symptom 1\", fg=\"Blue\", bg=\"Pink\")\n",
    "S1Lb.config(font=(\"Times\",15,\"bold italic\"))\n",
    "S1Lb.grid(row=7, column=0, pady=10, sticky=W)\n",
    "\n",
    "S2Lb = Label(root, text=\"Symptom 2\", fg=\"White\", bg=\"Purple\")\n",
    "S2Lb.config(font=(\"Times\",15,\"bold italic\"))\n",
    "S2Lb.grid(row=8, column=0, pady=10, sticky=W)\n",
    "\n",
    "S3Lb = Label(root, text=\"Symptom 3\", fg=\"Green\",bg=\"white\")\n",
    "S3Lb.config(font=(\"Times\",15,\"bold italic\"))\n",
    "S3Lb.grid(row=9, column=0, pady=10, sticky=W)\n",
    "\n",
    "S4Lb = Label(root, text=\"Symptom 4\", fg=\"blue\", bg=\"Yellow\")\n",
    "S4Lb.config(font=(\"Times\",15,\"bold italic\"))\n",
    "S4Lb.grid(row=10, column=0, pady=10, sticky=W)\n",
    "\n",
    "S5Lb = Label(root, text=\"Symptom 5\", fg=\"purple\", bg=\"light green\")\n",
    "S5Lb.config(font=(\"Times\",15,\"bold italic\"))\n",
    "S5Lb.grid(row=11, column=0, pady=10, sticky=W)\n",
    "\n",
    "\n",
    "lrLb = Label(root, text=\"DecisionTree\", fg=\"white\", bg=\"red\")\n",
    "lrLb.config(font=(\"Times\",15,\"bold italic\"))\n",
    "lrLb.grid(row=15, column=0, pady=10,sticky=W)\n",
    "\n",
    "destreeLb = Label(root, text=\"RandomForest\", fg=\"Red\", bg=\"Orange\")\n",
    "destreeLb.config(font=(\"Times\",15,\"bold italic\"))\n",
    "destreeLb.grid(row=17, column=0, pady=10, sticky=W)\n",
    "\n",
    "ranfLb = Label(root, text=\"NaiveBayes\", fg=\"White\", bg=\"green\")\n",
    "ranfLb.config(font=(\"Times\",15,\"bold italic\"))\n",
    "ranfLb.grid(row=19, column=0, pady=10, sticky=W)\n",
    "\n",
    "OPTIONS = sorted(l1)\n",
    "\n",
    "NameEn = Entry(root, textvariable=Name)\n",
    "NameEn.grid(row=6, column=1)\n",
    "\n",
    "S1 = OptionMenu(root, Symptom1,*OPTIONS)\n",
    "S1.grid(row=7, column=1)\n",
    "\n",
    "S2 = OptionMenu(root, Symptom2,*OPTIONS)\n",
    "S2.grid(row=8, column=1)\n",
    "\n",
    "S3 = OptionMenu(root, Symptom3,*OPTIONS)\n",
    "S3.grid(row=9, column=1)\n",
    "\n",
    "S4 = OptionMenu(root, Symptom4,*OPTIONS)\n",
    "S4.grid(row=10, column=1)\n",
    "\n",
    "S5 = OptionMenu(root, Symptom5,*OPTIONS)\n",
    "S5.grid(row=11, column=1)\n",
    "\n",
    "\n",
    "dst = Button(root, text=\"Prediction 1\", command=DecisionTree,bg=\"Red\",fg=\"yellow\")\n",
    "dst.config(font=(\"Times\",15,\"bold italic\"))\n",
    "dst.grid(row=8, column=3,padx=10)\n",
    "\n",
    "rnf = Button(root, text=\"Prediction 2\", command=randomforest,bg=\"White\",fg=\"green\")\n",
    "rnf.config(font=(\"Times\",15,\"bold italic\"))\n",
    "rnf.grid(row=9, column=3,padx=10)\n",
    "\n",
    "lr = Button(root, text=\"Prediction 3\", command=NaiveBayes,bg=\"Blue\",fg=\"white\")\n",
    "lr.config(font=(\"Times\",15,\"bold italic\"))\n",
    "lr.grid(row=10, column=3,padx=10)\n",
    "\n",
    "\n",
    "t1 = Text(root, height=1, width=40,bg=\"Light green\",fg=\"red\")\n",
    "t1.config(font=(\"Times\",15,\"bold italic\"))\n",
    "t1.grid(row=15, column=1, padx=10)\n",
    "\n",
    "t2 = Text(root, height=1, width=40,bg=\"White\",fg=\"Blue\")\n",
    "t2.config(font=(\"Times\",15,\"bold italic\"))\n",
    "t2.grid(row=17, column=1 , padx=10)\n",
    "\n",
    "t3 = Text(root, height=1, width=40,bg=\"red\",fg=\"white\")\n",
    "t3.config(font=(\"Times\",15,\"bold italic\"))\n",
    "t3.grid(row=19, column=1 , padx=10)\n",
    "\n",
    "root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
