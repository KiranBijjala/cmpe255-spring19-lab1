{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mean = 32.81818181818182\n",
      "median = 25\n"
     ]
    }
   ],
   "source": [
    "import statistics\n",
    "\n",
    "def mean_num_friends(x):\n",
    "    return statistics.mean(x)\n",
    "\n",
    "def median_num_friends(x):\n",
    "    return statistics.median(x)\n",
    "\n",
    "num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]\n",
    "\n",
    "print(\"mean = \"+ str(mean_num_friends(num_friends)))\n",
    "\n",
    "print(\"median = \"+ str(median_num_friends(num_friends)))\n"
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
