{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "a7469107",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import xlsxwriter as xl\n",
    "import itertools as it"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "6ccef6a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "dat = pd.read_excel(r\"F:\\CMP\\SThota work\\Dielectric data\\HI-T BTO\\BTO 500-605 Temp graph.xlsx\", sheet_name = None)\n",
    "ind = list(dat.keys())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "995760f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cleaner(i):\n",
    "    df = pd.DataFrame.from_dict(dat[ind[i]])\n",
    "    df = df.drop(columns = ['Unnamed: 0'])\n",
    "    df = df[(df.iloc[:, 1] != 9.90E+37)]\n",
    "    df = df[(df.iloc[:, 3] != 9.90E+37)]\n",
    "    return df\n",
    "    #df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "410a4e0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "tempset = [cleaner(i) for i in range(len(ind))]\n",
    "\n",
    "for j in range(len(ind)):\n",
    "    tempset[j].columns = ['Temp', dat[ind[0]].columns[2], dat[ind[0]].columns[3], dat[ind[0]].columns[4], dat[ind[0]].columns[5]]\n",
    "    \n",
    "with pd.ExcelWriter(r\"F:\\CMP\\SThota work\\Dielectric data\\HI-T BTO\\BTO 500-605 Temp graph clean.xlsx\",engine='xlsxwriter') as writer:\n",
    "    \n",
    "    for k in range(len(ind)):\n",
    "        tempset[k].to_excel(writer, sheet_name = ind[k])"
   ]
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
