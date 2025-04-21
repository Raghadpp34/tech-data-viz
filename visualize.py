import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Tech': ['AI', 'IoT', 'Blockchain', 'Cloud', 'Cybersecurity'],
    'Usage': [80, 65, 45, 90, 70]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
sns.barplot(x='Tech', y='Usage', data=df, palette='coolwarm')
plt.title('Technology Usage')
plt.xlabel('Technology')
plt.ylabel('Usage (%)')
plt.tight_layout()
plt.savefig("tech_usage.png")
plt.show()
