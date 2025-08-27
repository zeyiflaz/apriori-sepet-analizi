# Apriori Sepet Analizi

Bu depo, Apriori algoritmasını kullanarak market sepeti analizini öğrenmek isteyenler için hazırlanmıştır. Örnek Python kodları ve açıklamaları içerir.

## Kullanılan Kütüphaneler

- numpy
- pandas
- matplotlib
- apyori

## Kod Örneği

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori

# Veriyi yükleme
veriler = pd.read_csv('sepet.csv', header=None)  # Kolon başlığı yok

# Veri listesini hazırlama
t = []
for i in range(0, 7501):  # 7501 satır
    t.append([str(veriler.values[i,j]) for j in range(0, 20)])  # 20 sütun

# Apriori algoritmasını uygulama
kurallar = apriori(t, min_support=0.01, min_confidence=0.2, min_length=2)
print(list(kurallar))
"# apriori-sepet-analizi" 
